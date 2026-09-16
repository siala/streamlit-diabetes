"""Load the diabetes data and split it into a train and a test set."""

from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split

CLASS_NAMES = {0: "Not readmitted", 1: "Readmitted < 30 days"}
COLOURS = {"Not readmitted": "#3176B5", "Readmitted < 30 days": "#C97932"}

DATA_FILE = Path(__file__).resolve().parent / "data_diabetes.csv"
FEATURES = [
    "time_in_hospital", "num_lab_procedures", "num_procedures", "num_medications",
    "number_outpatient", "number_emergency", "number_inpatient", "number_diagnoses",
]

CATEGORIES = [
    "race", "gender", "age", "max_glu_serum", "A1Cresult",
    "metformin", "insulin", "change", "diabetesMed", "readmitted",
]


@st.cache_data
def load_data() -> dict:
    """Return {"train": ..., "test": ...}, each with a 0/1 class column.

    Missing values are stored as '?'. class is 1 when readmitted is '<30'.
    The split is a fixed, stratified 80 / 20.
    """
    df = pd.read_csv(DATA_FILE, na_values="?")
    df["class"] = df["readmitted"].eq("<30").astype(int)
    train, test = train_test_split(df, test_size=0.20, stratify=df["class"], random_state=42)
    return {"train": train, "test": test}
