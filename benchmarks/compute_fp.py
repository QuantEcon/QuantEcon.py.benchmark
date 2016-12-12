"""
Filename: time_arma.py
Author: Matt McKay

Benchmarks for arma.py

"""

from __future__ import division
import unittest
from quantecon import compute_fixed_point


def compute_fp_setup():
    global mu 
    mu = 0.2      # 0 is unique fixed point forall x_0 \in [0, 1]
                  # (4mu - 1)/(4mu) is a fixed point forall x_0 \in [0, 1]

    # arguments for compute_fixed_point
    global kwargs
    kwargs = {"error_tol": 1e-5, "max_iter": 200, "verbose": 0}

def T(self, x, mu):
    return 4.0 * mu * x * (1.0 - x)

def time_compute_fixed_point():
    "compute_fp: convergence inside interval of convergence"
    f = lambda x: T(x, mu)
    compute_fixed_point(f, i, **kwargs)

