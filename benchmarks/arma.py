"""
Filename: time_arma.py
Author: Matt McKay

Benchmarks for arma.py
"""

import numpy as np
from quantecon.arma import ARMA

# Intial Values
phi = np.array([.95, -.4, -.4])
theta = np.zeros(3)
sigma = .15

def arma_setup():
	global lp
	lp = ARMA(phi, theta, sigma)

def time_simulation():
	sim = lp.simulation(ts_length=250)
time_simulation.setup = arma_setup

def time_impulse_response():
	imp_resp = lp.impulse_response(impulse_length=75)
time_impulse_response.setup = arma_setup