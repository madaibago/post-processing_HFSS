from math import *
import numpy as np
import pandas as pd

def effective_permittivity(eps_r, h_subs, w_line):
    return (eps_r + 1) / 2 + (eps_r - 1) / 2 * (1 / np.sqrt(1 + 12 * h_subs / w_line))

# Constants
c = 3e8
eps_r = 12

h_subs = np.array((0.050, 0.1, 0.25)) * 1e-3
w_line = np.array((0.030, 0.050, 0.200)) * 1e-3

# Create grid of combinations
H, W = np.meshgrid(h_subs, w_line, indexing='ij')

eps_eff = effective_permittivity(eps_r, H, W)

# Frequency
f = 9.4e9
lambda_g = c / f * (1 / np.sqrt(eps_eff))

# Convert to tables
eps_table = pd.DataFrame(
    eps_eff,
    index=[f"h={h*1e3:.3f} mm" for h in h_subs],
    columns=[f"w={w*1e3:.3f} mm" for w in w_line]
)

lambda_table = pd.DataFrame(
    lambda_g * 1e3,
    index=[f"h={h*1e3:.3f} mm" for h in h_subs],
    columns=[f"w={w*1e3:.3f} mm" for w in w_line]
)

print("\nEffective permittivity")
print(eps_table.round(3))

print("\nGuided wavelength (mm)")
print(lambda_table.round(3))