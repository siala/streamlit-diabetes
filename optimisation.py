"""The MiniZinc model that picks the highest-priority patient."""

from minizinc import Instance, Solver

PRIORITY_FEATURES = [
    "number_inpatient",
    "number_emergency",
    "number_diagnoses",
    "time_in_hospital",
    "num_medications",
]

MODEL = """
    int: n;
    array[1..n, 1..5] of 0..100: features;
    array[1..5] of int: weights = [35, 25, 20, 10, 10];

    var 1..n: patient;

    solve maximize
        sum(j in 1..5)(weights[j] * features[patient, j]);
"""


def choose_patient(features: list[list[int]]) -> int:
    """Return the row number of the patient with the highest weighted score."""
    instance = Instance(Solver.lookup("gecode"))
    instance.add_string(MODEL)
    instance["n"] = len(features)
    instance["features"] = features
    # MiniZinc indexes from 1; pandas iloc indexes from 0.
    return instance.solve()["patient"] - 1
