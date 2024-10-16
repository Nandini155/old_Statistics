import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import boxcox
import warnings

# Ignore warnings for cleaner output
warnings.filterwarnings('ignore')

# 1. Generate synthetic non-normal data using a beta distribution
np.random.seed(42)  # For reproducibility
data = np.random.beta(1, 3, 5000)  # Beta distributed data (skewed)

# Plot the original data distribution
plt.figure(figsize=(6, 4))
sns.histplot(data, kde=True, bins=30)
plt.title("Original Data Distribution (Beta)")
plt.show()

# 2. Apply the Box-Cox transformation
data_shifted = data + 1e-8  # Add a small constant to ensure positive values
data_transformed, lambda_ = boxcox(data_shifted)

# Print the lambda value
print(f"Lambda that maximizes the log-likelihood: {lambda_}")

# 3. Plot the transformed data distribution
plt.figure(figsize=(6, 4))
sns.histplot(data_transformed, kde=True, bins=30)
plt.title("Transformed Data Distribution (Box-Cox)")
plt.show()

# 4. Manual Box-Cox transformation for verification
manually_transformed = [(i ** lambda_ - 1) / lambda_ for i in data_shifted]

# Plot manually transformed data
plt.figure(figsize=(6, 4))
sns.histplot(manually_transformed, kde=True, bins=30)
plt.title("Manually Transformed Data Distribution")
plt.show()

# 5. Experiment with multiple lambda values
lambdas = [-4, -2, -1, 0.5, 1, 2, 4]
x = np.linspace(data.min(), data.max(), 5000)

for l in lambdas:
    transformed = [(i ** l - 1) / l if l != 0 else np.log(i) for i in data_shifted]
    
    plt.figure(figsize=(6, 4))
    plt.hist(data, bins=20, density=True, alpha=0.5, label='Original Data')
    plt.hist(transformed, bins=30, density=True, alpha=0.7, label=f'Lambda: {l}')
    plt.title(f'Distribution with Lambda = {l}')
    plt.legend()
    plt.show()
