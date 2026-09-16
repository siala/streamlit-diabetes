import streamlit as st

st.write("# :red[Welcome to my dashboard]")

st.write("## Dataset: [Diabetes 130-US Hospitals]"
         "(https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)")

table = st.Page("dataframe.py", title="Data table", icon="💃")
histograms = st.Page("histograms.py", title="Histograms", icon="🎉")
bars = st.Page("bars.py", title="Bar charts", icon="📊")
prescriptive = st.Page("prescriptive.py", title="Prescriptive", icon="🎯")

st.navigation([table, histograms, bars, prescriptive]).run()
