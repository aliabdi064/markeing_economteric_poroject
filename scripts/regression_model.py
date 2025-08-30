import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.optimize import minimize # For budget optimization, though we'll use direct calculation

# Load the dataset
data = pd.read_csv('data/advertising.csv') # Updated path

# Prepare the data for multiple linear regression
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Add a constant to the independent variables for the intercept
X_const = sm.add_constant(X)

# Fit the OLS model
model = sm.OLS(y, X_const).fit()

# Print the model summary
print("--- Regression Model Summary ---")
print(model.summary())

# Calculate VIF for multicollinearity check
print("\n--- Variance Inflation Factors (VIF) ---")
vif_data = pd.DataFrame()
vif_data["feature"] = X_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_const.values, i) for i in range(X_const.shape[1])]
print(vif_data)

# Budget Optimization - Proportional Allocation
print("\n--- Budget Optimization (Proportional Allocation) ---")

# Get coefficients for TV, Radio, Newspaper
tv_coef = model.params[1]
radio_coef = model.params[2]
newspaper_coef = model.params[3]

# Only consider positive coefficients for allocation
positive_coefs = {
    'TV': tv_coef,
    'Radio': radio_coef,
    'Newspaper': newspaper_coef
}

total_positive_coef_sum = 0
for coef in positive_coefs.values():
    if coef > 0:
        total_positive_coef_sum += coef

if total_positive_coef_sum == 0:
    print("Cannot allocate proportionally: sum of positive coefficients is zero.")
else:
    budget = 1000.0

    tv_percent = tv_coef / total_positive_coef_sum if tv_coef > 0 else 0
    radio_percent = radio_coef / total_positive_coef_sum if radio_coef > 0 else 0
    newspaper_percent = newspaper_coef / total_positive_positive_coef_sum if newspaper_coef > 0 else 0

    tv_spend = budget * tv_percent
    radio_spend = budget * radio_percent
    newspaper_spend = budget * newspaper_percent

    # Calculate estimated sales with this allocation
    estimated_sales = model.params[0] +
                      model.params[1] * tv_spend +
                      model.params[2] * radio_spend +
                      model.params[3] * newspaper_spend

    print(f"Total Budget: £{budget:.2f}")
    print(f"TV Coefficient: {tv_coef:.4f} ({tv_percent:.2%})")
    print(f"Radio Coefficient: {radio_coef:.4f} ({radio_percent:.2%})\n")
    print(f"Newspaper Coefficient: {newspaper_coef:.4f} ({newspaper_percent:.2%})")
    print(f"Allocated TV Spend: £{tv_spend:.2f}")
    print(f"Allocated Radio Spend: £{radio_spend:.2f}")
    print(f"Allocated Newspaper Spend: £{newspaper_spend:.2f}")
    print(f"Estimated Sales with Proportional Allocation: {estimated_sales:.2f}")