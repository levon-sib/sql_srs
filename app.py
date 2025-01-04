import streamlit as st
import pandas as pd
import duckdb

st.write("Hello world!")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["First tab", "Second tab"])

with tab1:
    sql_query = st.text_area(label = "Entrez votre input")
    result = duckdb.query(sql_query).df()
    st.write(f"Vous avez entre la query suivante : {sql_query}")
    st.dataframe(result)