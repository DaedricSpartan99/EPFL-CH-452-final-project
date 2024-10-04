import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

enable_pgf = True

if enable_pgf:
    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "pdflatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
        "figure.figsize": (4.6,1.8), # ratio 6/5, default 4.5, 3.7
        "pgf.preamble": "\n".join([ # plots will use this preamble
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage{siunitx}",
        ])
    })

# load DataFrames

cutwfc_df = pd.read_csv("conv-cutwfc/result.dat", sep=" ", index_col=False)

cutrho_df = pd.read_csv("conv-cutrho/result.dat", sep=" ", index_col=False)

k_df = pd.read_csv("conv-k/result.dat", sep=" ", index_col=False)

# define reference value for total energy
ref_energy = -370.75198828

# plot energy for cutwfc
fig = plt.figure()

ax = fig.add_subplot(111)

hand1, = ax.plot(cutwfc_df.ecutwfc, cutwfc_df.etot, color='orange', label="Total energy")
handline = ax.axhline(ref_energy, 0, 1, linestyle='--', color='black', label=r'Reference energy', zorder=0)
ax.set_ylabel("Total energy")
ax.set_xlabel("Cutoff energy on the wave function")

ax2 = ax.twinx()
hand2, = ax2.plot(cutwfc_df.ecutwfc, cutwfc_df.time, label="Compute time")
ax2.set_ylabel("Compute time")

ax.legend(handles=[hand1, hand2, handline], loc='upper center', prop={'size': 8})

if enable_pgf:
    plt.savefig('conv-cutwfc/conv-cutwfc.pgf')
else:
    fig.suptitle('Wave function', fontsize=16)
    plt.show()


# plot energy for cutrho
fig = plt.figure()

ax = fig.add_subplot(111)

hand1, = ax.plot(cutrho_df.ecutrho, cutrho_df.etot, color='orange', label="Total energy")
handline = ax.axhline(ref_energy, 0, 1, linestyle='--', color='black', label=r'Reference energy', zorder=0)
ax.set_ylabel("Total energy")
ax.set_xlabel("Cutoff energy on the density")

ax2 = ax.twinx()
hand2, = ax2.plot(cutrho_df.ecutrho, cutrho_df.time, label="Compute time")
ax2.set_ylabel("Compute time")

ax.legend(handles=[hand1, hand2, handline], loc='center right')

if enable_pgf:
    plt.savefig('conv-cutrho/conv-cutrho.pgf')
else:
    fig.suptitle('Density', fontsize=16)
    plt.show()


# plot energy for XY K-points
fig = plt.figure()

ax = fig.add_subplot(111)

hand1, = ax.plot(k_df.k, k_df.etot, color='orange', label="Total energy")
handline = ax.axhline(ref_energy, 0, 1, linestyle='--', color='black', label=r'Reference energy', zorder=0)
ax.set_ylabel("Total energy")
ax.set_xlabel("Cutoff energy on the density")

ax2 = ax.twinx()
hand2, = ax2.plot(k_df.k, k_df.time, label="Compute time")
ax2.set_ylabel("Compute time")

ax.legend(handles=[hand1, hand2, handline], loc='lower right', prop={'size': 9})

if enable_pgf:
    plt.savefig('conv-k/conv-k.pgf')
else:
    fig.suptitle('XY K-points', fontsize=16)
    plt.show()


