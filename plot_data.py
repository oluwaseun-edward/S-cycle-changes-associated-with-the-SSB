#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:05:23 2022

@author: charline

Plot data of sulfur cycle box-model outputs.
For one simulation, there is two outputs files (one for each equation integration):
	- *S.npy  for the first one
	- *SdeltaS.npy for the second one
To access delta_S, divide SdeltaS/S (as done l. 41-44 directly when plotting)
"""


import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np


# %% GENERAL PARAMETERS FIGURES

# Make global settings for the figures.
mpl.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["mathtext.default"] = "regular"
mpl.rcParams["pdf.fonttype"] = 42
# This is for using seaborn
# sns.set_theme(style="white")
# sns.set_style('ticks')


save_path = "/media/charline/ElementsSE/sulfur_cycle_box_model/figures_sims/"

data_path = "/media/charline/ElementsSE/sulfur_cycle_box_model/sims_reduced/"


# %% OMAN BURIAL PYRITHE INCEASE 211 KYR

fig, ax = plt.subplots(figsize=(12, 6), ncols=3, nrows=2, sharey=False)

fig.subplots_adjust(wspace=0.35, hspace=0.4)
# fig.subplots_adjust(wspace=0.3, hspace = 0.2)


# SUBPLOT 1: S steady 1.6 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_211000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_211000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_211000_SdeltaS.npy"
)

ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 0].set_ylim(13.5, 22)
ax[0, 0].set_xlim(-2.5, 10)
# ax[0,0].set_xlabel('Time [kyrs]')
ax[0, 0].set_ylabel("$\delta^{34}$S$_{seawater}$")
ax[0, 0].set_title("S$_{steady} = 1.6~mM$")
ax[0, 0].legend(["1.5", "2", "3", "4", "5"])

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 2: S steady 2.5 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_211000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_211000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_211000_SdeltaS.npy"
)


ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')
# ax[0,0].axhline(x=13.8+6, linewidth=1, color='black', linestyle='--')

# 25 000 to 40 000
ax[0, 1].set_ylim(13.5, 22)
ax[0, 1].set_xlim(-2.5, 10)
ax[0, 1].set_title("S$_{steady} = 2.5~mM$")

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 3: S steady 5 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_211000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_211000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_211000_SdeltaS.npy"
)


ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 2].set_ylim(13.5, 22)
ax[0, 2].set_xlim(-2.5, 10)
ax[0, 2].set_title("S$_{steady} = 5~mM$")
# ax[0,2].grid(True, linestyle=':', color='gray')

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 4: S steady 1.6 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_211000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_211000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_211000_SdeltaS.npy"
)

ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 0].set_ylim(21, 35)
ax[1, 0].set_xlim(-2.5, 10)
# ax[0,0].set_xlabel('Time [kyrs]')
ax[1, 0].set_ylabel("$\delta^{34}$S$_{seawater}$")
# ax[1,0].set_title('S$_{steady} = 1.6~mM$')
ax[1, 0].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 5: S steady 2.5 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_211000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_211000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_211000_SdeltaS.npy"
)


ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 1].set_ylim(21, 35)
ax[1, 1].set_xlim(-2.5, 10)
# ax[1,1].set_title('S$_{steady} = 2.5~mM$')
ax[1, 1].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 6: S steady 5 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_211000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_211000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_211000_SdeltaS.npy"
)


ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 2].set_ylim(21, 35)
ax[1, 2].set_xlim(-2.5, 10)
# ax[1,2].set_title('S$_{steady} = 5~mM$')
# ax[0,2].grid(True, linestyle=':', color='gray')
ax[1, 2].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5

fig.savefig(
    "/media/charline/ElementsSE/sulfur_cycle_box_model/figures_sims/oman_211kyr_burial_increase.pdf",
    bbox_inches="tight",
)


# %% NEXT FIGURE


# %% QIAKONG BURIAL PYRITHE INCREASE 397 KYR

fig, ax = plt.subplots(figsize=(12, 6), ncols=3, nrows=2, sharey=False)

fig.subplots_adjust(wspace=0.35, hspace=0.4)
# fig.subplots_adjust(wspace=0.3, hspace = 0.2)


# SUBPLOT 1: S steady 1.6 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_397000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_397000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_397000_SdeltaS.npy"
)

ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 0].set_ylim(13.5, 30)
ax[0, 0].set_xlim(-2.5, 10)
# ax[0,0].set_xlabel('Time [kyrs]')
ax[0, 0].set_ylabel("$\delta^{34}$S$_{seawater}$")
ax[0, 0].set_title("S$_{steady} = 1.6~mM$")
ax[0, 0].legend(["1.5", "2", "3", "4", "5"])

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 2: S steady 2.5 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_397000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_397000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_397000_SdeltaS.npy"
)


ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 1].set_ylim(13.5, 30)
ax[0, 1].set_xlim(-2.5, 10)
ax[0, 1].set_title("S$_{steady} = 2.5~mM$")

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 3: S steady 5 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__1.5_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__2.0_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__3.0_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__4.0_perturbDuration_397000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_397000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_b_pyr__5.0_perturbDuration_397000_SdeltaS.npy"
)


ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 2].set_ylim(13.5, 30)
ax[0, 2].set_xlim(-2.5, 10)
ax[0, 2].set_title("S$_{steady} = 5~mM$")
# ax[0,2].grid(True, linestyle=':', color='gray')

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 4: S steady 1.6 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_397000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_397000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_397000_SdeltaS.npy"
)

ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 0].set_ylim(21, 50)
ax[1, 0].set_xlim(-2.5, 10)
# ax[0,0].set_xlabel('Time [kyrs]')
ax[1, 0].set_ylabel("$\delta^{34}$S$_{seawater}$")
# ax[1,0].set_title('S$_{steady} = 1.6~mM$')
ax[1, 0].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 5: S steady 2.5 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_397000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_397000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_397000_SdeltaS.npy"
)


ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 1].set_ylim(21, 50)
ax[1, 1].set_xlim(-2.5, 10)
# ax[1,1].set_title('S$_{steady} = 2.5~mM$')
ax[1, 1].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5


# SUBPLOT 6: S steady 5 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__1.5_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__2.0_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__3.0_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__4.0_perturbDuration_397000_SdeltaS.npy"
)

s5 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_397000_S.npy"
)
sd5 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_b_pyr__5.0_perturbDuration_397000_SdeltaS.npy"
)


ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd5 / s5,
    color=[0, 0, 0],
    linestyle="--",
    linewidth=1.5,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 2].set_ylim(21, 50)
ax[1, 2].set_xlim(-2.5, 10)
# ax[1,2].set_title('S$_{steady} = 5~mM$')
# ax[0,2].grid(True, linestyle=':', color='gray')
ax[1, 2].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, s5, sd1, sd2, sd3, sd4, sd5

fig.savefig(
    "/media/charline/ElementsSE/sulfur_cycle_box_model/figures_sims/qiakong_397kyr_burial_increase.pdf",
    bbox_inches="tight",
)


# %% NEXT FIGURE


# %% OMAN BURIAL WEATHERING DECREASE 211 KYR

fig, ax = plt.subplots(figsize=(12, 6), ncols=3, nrows=2, sharey=False)

fig.subplots_adjust(wspace=0.35, hspace=0.4)
# fig.subplots_adjust(wspace=0.3, hspace = 0.2)


# SUBPLOT 1: S steady 1.6 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_211000_SdeltaS.npy"
)


ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 0].set_ylim(13.5, 16)
ax[0, 0].set_xlim(-2.5, 10)
# ax[0,0].set_xlabel('Time [kyrs]')
ax[0, 0].set_ylabel("$\delta^{34}$S$_{seawater}$")
ax[0, 0].set_title("S$_{steady} = 1.6~mM$")
ax[0, 0].legend(["0.2", "0.25", "0.3", "0.5"])

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 2: S steady 2.5 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_211000_SdeltaS.npy"
)


ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 1].set_ylim(13.5, 16)
ax[0, 1].set_xlim(-2.5, 10)
ax[0, 1].set_title("S$_{steady} = 2.5~mM$")

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 3: S steady 5 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_211000_SdeltaS.npy"
)


ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 2].set_ylim(13.5, 16)
ax[0, 2].set_xlim(-2.5, 10)
ax[0, 2].set_title("S$_{steady} = 5~mM$")
# ax[0,2].grid(True, linestyle=':', color='gray')

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 4: S steady 1.6 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_211000_SdeltaS.npy"
)


ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 0].set_ylim(21.5, 24.5)
ax[1, 0].set_xlim(-2.5, 10)
# ax[0,0].set_xlabel('Time [kyrs]')
ax[1, 0].set_ylabel("$\delta^{34}$S$_{seawater}$")
# ax[1,0].set_title('S$_{steady} = 1.6~mM$')
ax[1, 0].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 5: S steady 2.5 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_211000_SdeltaS.npy"
)


ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 1].set_ylim(21.5, 24.5)
ax[1, 1].set_xlim(-2.5, 10)
# ax[1,1].set_title('S$_{steady} = 2.5~mM$')
ax[1, 1].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 6: S steady 5 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_211000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_211000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_211000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_211000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_211000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_211000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_211000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_211000_SdeltaS.npy"
)


ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 2].set_ylim(21.5, 24.5)
ax[1, 2].set_xlim(-2.5, 10)
# ax[1,2].set_title('S$_{steady} = 5~mM$')
# ax[0,2].grid(True, linestyle=':', color='gray')
ax[1, 2].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, sd1, sd2, sd3, sd4

fig.savefig(
    "/media/charline/ElementsSE/sulfur_cycle_box_model/figures_sims/oman_211kyr_weath_decrease.pdf",
    bbox_inches="tight",
)


# %% NEXT FIGURE


# %% QIAKONG BURIAL WEATHERING DECREASE 397 KYR

fig, ax = plt.subplots(figsize=(12, 6), ncols=3, nrows=2, sharey=False)

fig.subplots_adjust(wspace=0.35, hspace=0.4)
# fig.subplots_adjust(wspace=0.3, hspace = 0.2)


# SUBPLOT 1: S steady 1.6 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_397000_SdeltaS.npy"
)


ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 0].set_ylim(13.5, 30)
ax[0, 0].set_xlim(-2.5, 10)
# ax[0,0].set_xlabel('Time [kyrs]')
ax[0, 0].set_ylabel("$\delta^{34}$S$_{seawater}$")
ax[0, 0].set_title("S$_{steady} = 1.6~mM$")
ax[0, 0].legend(["0.2", "0.25", "0.3", "0.5"])

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 2: S steady 2.5 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_397000_SdeltaS.npy"
)


ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 1].set_ylim(13.5, 30)
ax[0, 1].set_xlim(-2.5, 10)
ax[0, 1].set_title("S$_{steady} = 2.5~mM$")

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 3: S steady 5 / Delta S 25 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.2_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.25_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.3_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS25_perturb_w_pyr__0.5_perturbDuration_397000_SdeltaS.npy"
)


ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[0, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[0, 2].set_ylim(13.5, 30)
ax[0, 2].set_xlim(-2.5, 10)
ax[0, 2].set_title("S$_{steady} = 5~mM$")
# ax[0,2].grid(True, linestyle=':', color='gray')

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 4: S steady 1.6 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini1.6mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_397000_SdeltaS.npy"
)


ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 0].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 0].set_ylim(21, 50)
ax[1, 0].set_xlim(-2.5, 10)
# ax[0,0].set_xlabel('Time [kyrs]')
ax[1, 0].set_ylabel("$\delta^{34}$S$_{seawater}$")
# ax[1,0].set_title('S$_{steady} = 1.6~mM$')
ax[1, 0].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 5: S steady 2.5 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini2.5mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_397000_SdeltaS.npy"
)


ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 1].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 1].set_ylim(21, 50)
ax[1, 1].set_xlim(-2.5, 10)
# ax[1,1].set_title('S$_{steady} = 2.5~mM$')
ax[1, 1].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, sd1, sd2, sd3, sd4


# SUBPLOT 6: S steady 5 / Delta S 44 ---------------------------------------

s1 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_397000_S.npy"
)
sd1 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.2_perturbDuration_397000_SdeltaS.npy"
)

s2 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_397000_S.npy"
)
sd2 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.25_perturbDuration_397000_SdeltaS.npy"
)

s3 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_397000_S.npy"
)
sd3 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.3_perturbDuration_397000_SdeltaS.npy"
)

s4 = np.load(
    data_path + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_397000_S.npy"
)
sd4 = np.load(
    data_path
    + "SO4ini5.0mM_deltaS44_perturb_w_pyr__0.5_perturbDuration_397000_SdeltaS.npy"
)


ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd4 / s4,
    color=[0.39, 0.05, 0.23],
    linestyle="-",
    linewidth=1.5,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd3 / s3,
    color=[0.77, 0.11, 0.44],
    linestyle="--",
    linewidth=2,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd2 / s2,
    color=[0.89, 0.51, 0.22],
    linestyle="-",
    linewidth=2,
)
ax[1, 2].plot(
    (np.arange(0, np.size(s1)) - 30000) / 1000,
    sd1 / s1,
    color=[0.90, 0.75, 0.10],
    linestyle=":",
    linewidth=2,
)
# ax[0,0].axvline(x=211, linewidth=1, color='red', linestyle='-')

# 25 000 to 40 000
ax[1, 2].set_ylim(21, 50)
ax[1, 2].set_xlim(-2.5, 10)
# ax[1,2].set_title('S$_{steady} = 5~mM$')
# ax[0,2].grid(True, linestyle=':', color='gray')
ax[1, 2].set_xlabel("Time [Myr]")

del s1, s2, s3, s4, sd1, sd2, sd3, sd4

fig.savefig(
    "/media/charline/ElementsSE/sulfur_cycle_box_model/figures_sims/qiakong_397kyr_weath_decrease.pdf",
    bbox_inches="tight",
)
