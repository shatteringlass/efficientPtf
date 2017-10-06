import math
import numpy as np
import os

try:
    dim = int(input('How many risky assets are present in the market?\n'))
except ValueError:
    raise SystemExit("This is not a whole number.")

hist_ret = input('Provide the path to the historical returns (csv format only) for the risky assets: ')
if hist_ret != "":
    hmu = np.loadtxt(open(hist_ret, 'rb'), delimiter=',')
    assert len(hmu[0]) == dim
else:
    raise SystemExit("No input file provided. Exiting...")

ptf_weights = np.array(input('Provide the portfolio weighting (leave blank for a uniform portfolio):') or np.zeros(dim)+1/dim)
assert len(ptf_weights) == dim and int(sum(ptf_weights)) == 1

print('\nSelected portfolio has weights %s\n' % np.array_str(ptf_weights))