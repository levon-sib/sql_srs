import duckdb
import streamlit as st
import ast

con = duckdb.connect(database="data/ex_sql_tables.duckdb", read_only=False)

st.write(
    """
# SQL SRS
Space Repetition System SQL practice
"""
)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ["cross_joins", "group_by", "window_functions"],
        index=0,
        placeholder="Select a theme :)",
    )

    st.write("You selected: ", theme)
    exo = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exo)

    exercise_name = exo.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("Enter your code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.write("Resultat de votre query:")
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing 😕")

    n_lines_difference = abs(result.shape[0] - solution_df.shape[0])

    if n_lines_difference != 0:
        st.write(
            f"Your result has {n_lines_difference} lines difference with the solution"
        )

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exo_tables = ast.literal_eval(exo.loc[0, "tables"])
    for table in exo_tables:
        print(table)
        st.write(f"table : {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()


with tab3:
    st.write(answer)
