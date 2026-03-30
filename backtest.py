import numpy as np

returns = np.random.normal(0, 0.02, 1000)
var_95 = np.percentile(returns, 5)

violations = returns < var_95
print("Violations:", violations.sum())
