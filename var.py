import numpy as np

epsilon = 1e-4

try:
    dim = int(input('How many risky assets are present in the market?\n'))
except ValueError:
    raise SystemExit("This is not a whole number.")

hist_ret = input('Provide the path to the historical returns (csv format only) for the risky assets: ')
if hist_ret != "":
    hmu = np.loadtxt(open(hist_ret, 'rb'), delimiter=',').reshape(-1, dim)
    print('\n %s \n' % hmu)
    assert len(hmu[0]) == dim
else:
    raise SystemExit("No input file provided. Exiting...")

ptf_weights = np.array(eval(input('Provide the portfolio weighting (leave blank for a uniform portfolio):')) or np.zeros(dim) + 1 / dim)
assert len(ptf_weights) == dim and 1-int(sum(ptf_weights)) <= epsilon

print('\nSelected portfolio has weights %s\n' % np.array_str(ptf_weights))

# Evaluate daily return for selected ptf

daily_return = hmu.dot(ptf_weights.T).reshape(-1, 1) * -1
hist_days = len(daily_return)

print('Daily losses are as follows:\n %s \n' % daily_return)

# Require confidence level in order to proceed with VaR estimation

conf = input('Provide the required confidence level for the VaR estimation in p.p. (leave blank for 90%):') or 90

# Calculate i-th percentile based on conf value

var = np.percentile(daily_return, q=conf, interpolation='higher')

print('\nValue at Risk estimated is equal to: %s' % var)

cvar = daily_return[daily_return >= var].sum() / (hist_days * (1 - conf / 100))
assert cvar >= var

print('\nConditional Value at Risk (cVaR or expected shortfall) estimated is equal to: %s' % cvar)
