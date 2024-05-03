from scipy.io import loadmat
import pandas as pd

# Load the MATLAB data file
data = loadmat("influenza_outbreak_dataset.mat")
print(data)
# Extract the individual arrays from the loaded data
flu_X_tr = data['flu_X_tr'].flatten()
flu_Y_tr = data['flu_Y_tr'].flatten()
flu_X_te = data['flu_X_te'].flatten()
flu_Y_te = data['flu_Y_te'].flatten()
flu_locs = data['flu_locs'].flatten()
flu_keywords = data['flu_keywords'].flatten()

# Check if all arrays have the same length
array_lengths = [len(arr) for arr in [flu_X_tr, flu_Y_tr, flu_X_te, flu_Y_te, flu_locs, flu_keywords]]
if len(set(array_lengths)) != 1:
    raise ValueError("All arrays must be of the same length")

# Create a DataFrame using pandas
df = pd.DataFrame({
    'flu_X_tr': flu_X_tr,
    'flu_Y_tr': flu_Y_tr,
    'flu_X_te': flu_X_te,
    'flu_Y_te': flu_Y_te,
    'flu_locs': flu_locs,
    'flu_keywords': flu_keywords
})


print(df)
