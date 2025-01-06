import io
import duckdb
import pandas as pd
import streamlit as st

con = duckdb.connect(database="data/ex_sql_tables.duckdb", read_only=False)

# ------------------------------------------
# EX LIST
# ------------------------------------------

data = {
    "theme": ["cross_joins", "window_functions", "group_by"],
    "exercise_name": ["beverages_and_food", "simple_window", "group_by"],
    "tables": [["beverages", "food_items"], "simple_window", "group_by"],
    "last_reviewed": ["1970-01-01", "1970-01-01", "1970-01-01"],
    "answer": ["SELECT * FROM beverages CROSS JOIN food_items", "", ""],
}

memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


# ------------------------------------------
# CROSS JOIN EX
# ------------------------------------------

CSV = """
beverage,price
orange juice,2.5
expresso,2
tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS beverages as SELECT * FROM beverages")

CSV2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin, 3
"""

food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items as SELECT * FROM food_items")
