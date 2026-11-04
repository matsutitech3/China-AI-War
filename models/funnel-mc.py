#!/usr/bin/env python3
"""
Monte Carlo behind the AI4S value funnel (Chapter 24).

Model
-----
For each task class j:  dU_j = w_j * a_j * (s_j - 1) * v_j * d_j * l_j
                        U     = sum_j dU_j

Marginals: triangular over each parameter's (pessimistic, central, optimistic)
triple, taken verbatim from funnel-model.csv.

Dependence: the three conversion terms (v, d, l) are coupled within and across
classes by a single latent "conversion-quality" factor, implemented as a
Gaussian copula with loading sqrt(rho), rho = 0.5.  This gives every pair of
conversion terms a rank correlation near 0.5 while leaving each marginal
exactly triangular.  a and s are drawn independently.

Reproducibility: fixed seed; numpy PCG64.  Re-running this file reproduces the
numbers printed in the chapter.
"""
import numpy as np, csv, sys, os

SEED     = 20260923
N        = 200_000
RHO      = 0.5          # conversion-quality loading (v, d, l)
CSV      = os.path.join(os.path.dirname(__file__), "..", "funnel-model.csv")

def tri_ppf(u, lo, mode, hi):
    """Inverse CDF of the triangular distribution, vectorised."""
    lo, mode, hi = np.asarray(lo,float), np.asarray(mode,float), np.asarray(hi,float)
    span = hi - lo
    flat = span <= 0
    span = np.where(flat, 1.0, span)
    c    = np.where(flat, 0.5, (mode - lo) / span)
    left = u < c
    out  = np.where(left,
                    lo + np.sqrt(np.clip(u * span * (mode - lo), 0, None)),
                    hi - np.sqrt(np.clip((1 - u) * span * (hi - mode), 0, None)))
    return np.where(flat, mode, out)

def load(path):
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(l for l in f if not l.startswith("#")):
            rows.append(r)
    return rows

def main():
    rows = load(CSV)
    rng  = np.random.default_rng(SEED)
    K    = len(rows)

    w  = np.array([float(r["w"]) for r in rows])
    tri = {p: np.array([[float(r[f"{p}_pess"]), float(r[f"{p}_cen"]), float(r[f"{p}_opt"])]
                        for r in rows]) for p in ("a","s","v","d","l")}

    # independent draws for a, s
    U = {}
    for p in ("a","s"):
        u = rng.random((N, K))
        U[p] = tri_ppf(u, tri[p][:,0], tri[p][:,1], tri[p][:,2])

    # Gaussian copula for v, d, l: one latent factor shared by all of them
    z0 = rng.standard_normal((N,1))
    from math import sqrt
    for p in ("v","d","l"):
        zi = rng.standard_normal((N,K))
        z  = sqrt(RHO)*z0 + sqrt(1-RHO)*zi
        u  = 0.5*(1.0+np.vectorize(lambda x: np.math.erf(x/np.sqrt(2)))(z)) if False else _phi(z)
        U[p] = tri_ppf(u, tri[p][:,0], tri[p][:,1], tri[p][:,2])

    dU = w * U["a"] * (U["s"]-1.0) * U["v"] * U["d"] * U["l"]
    tot = dU.sum(axis=1)

    cen = np.array([float(r["dU_central"]) for r in rows])
    print(f"seed={SEED}  draws={N}  rho={RHO}")
    print(f"central (printed tuples)      : {cen.sum()*100:.4f}%")
    print(f"median                        : {np.median(tot)*100:.2f}%")
    print(f"mean                          : {tot.mean()*100:.2f}%")
    print(f"P10 - P90                     : {np.percentile(tot,10)*100:.2f}% - {np.percentile(tot,90)*100:.2f}%")
    print(f"P05 - P95                     : {np.percentile(tot,5)*100:.2f}% - {np.percentile(tot,95)*100:.2f}%")

    # deterministic corners (all classes at their worst / best simultaneously)
    def corner(idx):
        a=tri["a"][:,idx]; s=tri["s"][:,idx]; v=tri["v"][:,idx]; d=tri["d"][:,idx]; l=tri["l"][:,idx]
        return (w*a*(s-1)*v*d*l).sum()
    print(f"all-pessimistic corner        : {corner(0)*100:.2f}%")
    print(f"all-optimistic corner         : {corner(2)*100:.2f}%")

    # one-at-a-time sensitivity: swing each class across its own corners
    print("\none-at-a-time class sensitivity (total with class j at its corner, others central):")
    base = cen.sum()
    for j,r in enumerate(rows):
        lo = base - cen[j] + (w[j]*tri["a"][j,0]*(tri["s"][j,0]-1)*tri["v"][j,0]*tri["d"][j,0]*tri["l"][j,0])
        hi = base - cen[j] + (w[j]*tri["a"][j,2]*(tri["s"][j,2]-1)*tri["v"][j,2]*tri["d"][j,2]*tri["l"][j,2])
        print(f"  {r['class']:24s} {lo*100:6.2f}%  ..  {hi*100:6.2f}%")

def _phi(z):
    from scipy.special import ndtr
    return ndtr(z)

if __name__ == "__main__":
    main()
