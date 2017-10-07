import math
import numpy as np

epsilon = 1e-4

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
if cov_path != "":
    V = np.loadtxt(open(cov_path, 'rb'), delimiter=',')
    assert len(V[0]) == dim
else:
    raise SystemExit("No input file provided. Exiting...")

try:
    rf_rate = float(input('State the riskfree rate on the market (in p.p.): '))
except ValueError:
    raise SystemExit()

try:
    req_vol = float(input('State the required max volatility for the portfolio to be built (in p.p.): '))
except ValueError:
    raise SystemExit()

ptf_weights = input('Provide the path to the portfolio weights (csv format only - leave blank for a uniformly distributed portfolio): ')
if ptf_weights != "":
    ptf = np.loadtxt(open(ptf_weights, 'rb'), delimiter=',')
else:
    ptf = np.ones((dim,1))/dim
assert len(ptf) == dim and 1-sum(ptf)<epsilon

print('\nAbout to compute returns for selected portfolio with weights %s\n' % ptf)

excess_ret = mu - rf_rate
nom = np.dot(ptf, mu) - rf_rate
denom = 100 * (math.sqrt(np.dot(ptf, np.matmul(V, ptf))))
beta = (nom) / denom
rate = rf_rate + beta * req_vol

print('\nThe selected portfolio has rate of return:\n\n\t%f\n' % rate)
