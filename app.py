import streamlit as st
import pandas as pd
import duckdb
import io

st.write("""
# SQL SRS
Space Repetition System SQL practice
""")

csv = '''
beverage,price
orange juice,2.5
expresso,2
tea,3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie,2.5
chocolatine,2
muffin, 3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
select *
from beverages
cross join food_items
"""

solution = duckdb.sql(answer).df()

st.header("Enter your code:")
query = st.text_area(label = "Votre code SQL ici", value = "select * from beverages", key = "user_input")

result = duckdb.query(query).df()
st.write(f"Resultat de votre query:")
st.dataframe(result)

# with st.sidebar:
#     option = st.selectbox(
#         "What would you like to review?",
#         ["Joins", "Groups by", "Window functions"],
#         index=None,
#         placeholder="Select a theme..."
#     )
#
#     st.write("You selected: ", option)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table : beverages")
    st.dataframe(beverages)
    st.write("table : food items")
    st.dataframe(food_items)
    st.write("expected : ")
    st.dataframe(solution)

with tab3:
    st.write(answer)