###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##


# ----------------------------
# IMPORTS (with fail messages)
# ----------------------------

try:
    import numpy as np
except ImportError as e:
    raise ImportError("Error: NumPy is required for this module but is not installed.") from e

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None   # Allow stats functions to work even without matplotlib


# ----------------------------
# INPUT CHECKING
# ----------------------------

def _ensure_array(data):
    """Ensure data is a numpy array (convert list → array)."""
    if isinstance(data, list):
        return np.array(data, dtype=float)
    elif isinstance(data, np.ndarray):
        return data.astype(float)
    else:
        raise TypeError("Input must be a list or a numpy array.")


# ----------------------------
# STATS FUNCTIONS
# ----------------------------

def compute_stats(data):
    """Return mean, median, std of the input data."""
    data = _ensure_array(data)

    mean_val = np.mean(data)
    median_val = np.median(data)
    std_val = np.std(data)

    return mean_val, median_val, std_val


def pretty_print_stats(data):
    """Display statistics nicely formatted."""
    mean_val, median_val, std_val = compute_stats(data)

    print("\n======= STATISTICS =======")
    print(f"Mean:        {mean_val:.4f}")
    print(f"Median:      {median_val:.4f}")
    print(f"Std Dev:     {std_val:.4f}")
    print("==========================\n")


