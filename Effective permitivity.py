import numpy as np
import pandas as pd

def effective_permittivity(eps_r, h_subs, w_line):
    return (eps_r + 1) / 2 + (eps_r - 1) / 2 * (1 / np.sqrt(1 + 12 * h_subs / w_line))

# Constants
c = 3e8
eps_r = 12
f = 9.4e9  # Hz

h_subs = np.array((0.050, 0.100, 0.200, 0.500)) * 1e-3
w_line = np.array((0.030, 0.050, 0.200)) * 1e-3

rows = []

for h in h_subs:
    # f_c depends only on h_subs
    f_c = c / (4 * h * np.sqrt(eps_r - 1))
    
    for w in w_line:
        eps_eff = effective_permittivity(eps_r, h, w)
        lambda_g = c / f / np.sqrt(eps_eff)
        
        rows.append({
            "h_subs (mm)": h * 1e3,
            "w_line (mm)": w * 1e3,
            "eps_eff": eps_eff,
            "f_c (GHz)": f_c * 1e-9,
            "lambda_g (mm)": lambda_g * 1e3,
        })

df = pd.DataFrame(rows)

# Optional: prettier formatting for terminal display
df = df.round({
    "h_subs (mm)": 3,
    "w_line (mm)": 3,
    "eps_eff": 3,
    "f_c (GHz)": 3,
    "lambda_g (mm)": 3
})

print(df.to_string(index=False))

# df.columns = [
#     r"$h_{\mathrm{subs}}$ (mm)",
#     r"$w_{\mathrm{line}}$ (mm)",
#     r"$\varepsilon_{\mathrm{eff}}$",
#     r"$f_c$ (GHz)",
#     r"$\lambda_g$ (mm)"
# ]
# print(df.to_latex(index=False, escape=False, float_format="%.3f"))