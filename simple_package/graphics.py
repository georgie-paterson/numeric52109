###
## Graphics to plot a histogram of the data, with the mean and median marked on the plot.
###

# ----------------------------
# GRAPHICS FUNCTION
# ----------------------------
try:
    import numpy as np
except ImportError as e:
    raise ImportError("Error: NumPy is required for this module but is not installed.") from e

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None   # Allow stats functions to work even without matplotlib

from simple_package.statistics import *


def plot_histogram(data):
    """Plot a histogram of the data with mean and median marked."""

    if plt is None:
        raise ImportError("Matplotlib is required for plotting but is not installed.")

    data = _ensure_array(data)
    mean_val, median_val, _ = compute_stats(data)

    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=20, alpha=0.7, edgecolor='black')

    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2,
                label=f"Mean = {mean_val:.2f}")
    plt.axvline(median_val, color='green', linestyle='-', linewidth=2,
                label=f"Median = {median_val:.2f}")

    plt.title("Histogram with Mean and Median")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.show()