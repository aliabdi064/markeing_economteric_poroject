import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data for the table
data = {
    'Feature': ['const', 'TV', 'Radio', 'Newspaper'],
    'Coefficient (coef)': [4.6251, 0.0544, 0.1070, 0.0003],
    'Std Error': [0.308, 0.001, 0.008, 0.006],
    't-value': [15.041, 39.592, 12.604, 0.058],
    'P>|t|': [0.000, 0.000, 0.000, 0.954],
    '[0.025': [4.019, 0.052, 0.090, -0.011],
    '0.975]': [5.232, 0.057, 0.124, 0.012]
}
df = pd.DataFrame(data)

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(10, 2)) # Adjust figure size as needed
ax.axis('off') # Hide axes

# Create the table
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center',
                 colColours=['#f2f2f2']*len(df.columns)) # Light grey background for headers

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2) # Scale table size

# Save the table as an image
plt.savefig('plots/regression_table.png', bbox_inches='tight', dpi=300)
plt.close(fig) # Close the figure to free memory

print("Table image 'plots/regression_table.png' generated successfully.")