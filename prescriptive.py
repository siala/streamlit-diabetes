"""Pick the patient with the highest priority score."""

import streamlit as st

from lab_helpers_diabetes import load_data
from optimisation import PRIORITY_FEATURES, choose_patient

df = load_data()["train"]

st.write("The use case we consider here is choosing which patient to follow up first.")

st.write("Tick the candidate patients, then press OK")
rows = st.dataframe(df, on_select="rerun").selection.rows

if st.button("OK") and rows:
    patients = df.iloc[rows]

    # Scale each feature to 0-100 across the selected patients.
    # Constant columns become zero.
    x = patients[PRIORITY_FEATURES]
    scaled = (100 * (x - x.min()) / (x.max() - x.min()).replace(0, 1)).round().astype(int)

    winner = choose_patient(scaled.values.tolist())

    st.write("Selected patient")
    st.dataframe(patients.iloc[[winner]][["patient_nbr"] + PRIORITY_FEATURES])
