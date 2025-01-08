import io
import duckdb
import pandas as pd
import streamlit as st

con = duckdb.connect(database="data/ex_sql_tables.duckdb", read_only=False)

# ------------------------------------------
# EX LIST
# ------------------------------------------

data = {
    "theme": ["cross_joins", "group_by", "window_function"],
    "exercise_name": [
        "beverages_and_food",
        "orders_and_customers",
        "employees_salaries",
    ],
    "tables": [["beverages", "food_items"], ["orders", "customers"], ["employees"]],
    "last_reviewed": ["1970-01-01", "1970-01-01", "1970-01-01"],
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

CSV3 = """
customer_id,customer_name,city
1,John,New York
2,Alice,Los Angeles
3,Bob,New York
4,Sarah,Chicago
5,Mike,Chicago
6,Anna,Los Angeles
"""
customers = pd.read_csv(io.StringIO(CSV3))
con.execute("CREATE TABLE IF NOT EXISTS customers AS SELECT * FROM customers")

CSV4 = """
order_id,customer_id,order_amount
101,1,150
102,2,200
103,3,120
104,1,300
105,4,80
106,5,150
107,6,220
108,2,100
"""
orders = pd.read_csv(io.StringIO(CSV4))
con.execute("CREATE TABLE IF NOT EXISTS orders AS SELECT * FROM orders")

CSV5 = """
employee_id,employee_name,department,salary
1,John,Engineering,80000
2,Alice,Engineering,90000
3,Bob,Sales,70000
4,Sarah,Sales,75000
5,Mike,HR,60000
6,Anna,Engineering,95000
"""
employees = pd.read_csv(io.StringIO(CSV5))
con.execute("CREATE TABLE IF NOT EXISTS employees AS SELECT * FROM employees")
