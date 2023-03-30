import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme("paper")
# Load in as multi-index
os.chdir("/Users/jonthanwarkentin/Desktop")

df = pd.read_csv("rho-P_solar_model.csv", header=[0, 1])
fig, ax = plt.subplots(figsize=(7, 5))

# Split into groups by 
for name, df_group in df.groupby(level = 0, axis=1):
    # Get the specific group's data and drop all na
    # pandas is a bit weird here with groupby
    df_group = df_group[name].dropna()
    # Plot individually
    ax.plot(df_group["logRho"], df_group["logP"], label=name)
    # Get the dPdrho and plot the fit. Could use scipy.stats linregress
    avg_run = df_group["logRho"].diff().mean()
    avg_rise = df_group["logP"].diff().mean()
    dPdrho = avg_rise/avg_run
    ax.plot(df_group["logRho"], df_group["logRho"]*dPdrho,
            label=f"{name} $\\frac{{dP}}{{d\\rho}}$ = {dPdrho:.3f}")

# more plotting
ax.set_xlabel("")
ax.set_ylabel("")
ax.set_title("")
ax.legend()
fig.tight_layout()
# fig.show()
plt.show()
print('l')
#plt.close("all")
