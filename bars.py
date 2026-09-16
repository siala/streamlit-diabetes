"""Bar chart of one category, split by class."""

import numpy as np
import pandas as pd
import streamlit as st
from matplotlib.figure import Figure

from lab_helpers_diabetes import load_data, CATEGORIES, CLASS_NAMES, COLOURS

df = load_data()["train"]

st.write("The use case we consider here is comparing one category between the same two groups.")

category = st.selectbox("Category", CATEGORIES)
counts = pd.crosstab(df[category], df["class"].map(CLASS_NAMES))
shares = 100 * counts / counts.sum()

fig = Figure(figsize=(8, 4), layout="constrained")
ax = fig.subplots()

pos = np.arange(len(shares))
width = 0.4

for i, (name, colour) in enumerate(COLOURS.items()):
    ax.bar(pos + i * width, shares[name], width, color=colour,
           label=f"{name}, n = {counts[name].sum()}")

ax.set_xticks(pos + width / 2, shares.index)
ax.set(title=category, xlabel="Category", ylabel="Share within group (%)")
ax.legend(frameon=False)


st.pyplot(fig)
