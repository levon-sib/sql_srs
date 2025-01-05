import duckdb
import streamlit as st

con = duckdb.connect(database="data/ex_sql_tables.duckdb", read_only=False)

st.write(
    """
# SQL SRS
Space Repetition System SQL practice
"""
)

ANSWER_STR = """
select *
from beverages
cross join food_items
"""

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ["cross_joins", "Groups by", "window_functions"],
        index=None,
        placeholder="Select a theme...",
    )

    st.write("You selected: ", theme)
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

st.header("Enter your code:")
query = st.text_area(
    label="Votre code SQL ici", value="select * from beverages", key="user_input"
)

# if query:
#     result = duckdb.query(query).df()
#     st.write("Resultat de votre query:")
#     st.dataframe(result)
#
#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("Some columns are missing 😕")
#
#     n_lines_difference = abs(result.shape[0] - solution_df.shape[0])
#
#     if n_lines_difference != 0:
#         st.write(
#             f"Your result has {n_lines_difference} lines difference with the solution"
#         )
#
#
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#     st.write("table : beverages")
#     st.dataframe(beverages)
#     st.write("table : food items")
#     st.dataframe(food_items)
#     st.write("expected : ")
#     st.dataframe(solution_df)
#
# with tab3:
#     st.write(ANSWER_STR)
