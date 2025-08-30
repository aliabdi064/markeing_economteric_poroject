import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load the dataset
data = pd.read_csv('advertising.csv')

# --- Data Inspection ---
print("--- Data Info ---")
data.info()
print("\n--- Missing Values ---")
print(data.isnull().sum())

# --- Descriptive Statistics ---
print("\n--- Descriptive Statistics ---")
print(data.describe())

# --- Univariate Analysis ---
# Histograms
data.hist(bins=20, figsize=(14,10))
plt.suptitle('Histograms of all variables')
plt.savefig('histograms.png')
plt.show()

# Box plots
plt.figure(figsize=(14,10))
sns.boxplot(data=data)
plt.title('Box plots of all variables')
plt.savefig('boxplots.png')
plt.show()

# --- Bivariate Analysis ---
# Scatter plots
sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.suptitle('Scatter plots of Sales vs. Advertising Channels', y=1.02)
plt.savefig('scatter_plots.png')
plt.show()

# Correlation matrix and heatmap
corr_matrix = data.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of all variables')
plt.savefig('correlation_heatmap.png')
plt.show()

# --- Statistical Tests ---
print("\n--- Correlation Tests ---")
for col in ['TV', 'Radio', 'Newspaper']:
    corr, p_value = pearsonr(data[col], data['Sales'])
    print(f'Correlation between {col} and Sales: {corr:.3f}, p-value: {p_value:.3f}')