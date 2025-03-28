# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hzoGICr-RwnC04vgBdn1oNex5pkf23aD
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def percent_var(r, confidence):
    """
    Calculates the Value at Risk (VaR) using the percentile method.

    Parameters:
    - r: array-like, stock returns
    - confidence: float, confidence level (e.g., 0.95 for 95%)

    Returns:
    - Absolute VaR at the given confidence level
    """
    out = np.percentile(r, (1 - confidence) * 100)  # Calculate percentile
    return abs(out)  # Ensure the return value is positive

# Simulate stock returns using a normal distribution
returns = np.random.normal(0, 1, 10000)  # Mean=0, Std=1, 10,000 samples

# Example: Calculate 97.72 percentile of returns
print("97.72 percentile of returns:", np.percentile(returns, 97.72))

# Unit test for VaR calculation
r = np.random.normal(0.05, 0.03, 100000)  # Simulated stock returns
probability_2SD = norm.cdf(2)  # Probability under normal curve within 2 standard deviations

my_confidence = probability_2SD  # Confidence level
my_percent_var = percent_var(r, my_confidence)  # Calculate VaR

print("VaR at confidence level {:.2f}: {:.4f}".format(my_confidence, my_percent_var))

# Plot histogram of stock returns
plt.hist(r, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.axvline(-my_percent_var, color='red', linestyle='dashed', linewidth=2)
plt.title("Histogram of Stock Returns with Value at Risk (VaR)")
plt.xlabel("Returns")
plt.ylabel("Frequency")
plt.show()