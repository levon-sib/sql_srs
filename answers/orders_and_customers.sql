SELECT
    c.customer_id,
    sum(o.order_amount) as amount_spent
FROM customers as c
INNER JOIN orders as o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id
