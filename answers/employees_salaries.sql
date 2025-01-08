with cte as (

SELECT
    employee_id,
    employee_name,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
FROM employees
WHERE department = 'Engineering'

)

SELECT *
FROM cte
WHERE rn = 1