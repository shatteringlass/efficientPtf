import math
import numpy as np
import os

try:
    dim = int(input('How many risky assets are present in the market?\n'))
except ValueError:
    raise SystemExit("This is not a whole number.")

mean_path = input('Provide the path to the mean return vector (csv format only) for the risky assets: ')
if mean_path != "":
    mu = np.loadtxt(open(mean_path, 'rb'), delimiter=',')
    assert len(mu) == dim
else:
    raise SystemExit("No input file provided. Exiting...")

cov_path = input('Provide the path to the covariance matrix (csv format only) for the risky assets: ')
if mean_path != "":
    V = np.loadtxt(open(cov_path, 'rb'), delimiter=',')
    assert len(V[0]) == dim
else:
    raise SystemExit("No input file provided. Exiting...")

try:
    rf_rate = float(input('State the riskfree rate on the market (in p.p.): '))
except ValueError:
    raise SystemExit()
try:
    req_vol = float(input('State the required max volatility for the portfolio to be built: '))
except ValueError:
    raise SystemExit()

excess_ret = mu - rf_rate
sharpe_ptf = np.linalg.solve(V, excess_ret)
sharpe_ptf = sharpe_ptf / sum(sharpe_ptf)
nom = np.dot(sharpe_ptf, mu) - rf_rate
denom = 100 * (math.sqrt(np.dot(sharpe_ptf, np.matmul(V, sharpe_ptf))))
beta = (nom) / (denom)
rate = rf_rate + beta * req_vol

print('The Sharpe ptf has weights: \n % \n and its rate of return amounts to \n %f' % (np.array_str(sharpe_ptf), rate))
