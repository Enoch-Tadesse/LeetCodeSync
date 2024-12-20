# Write your MySQL query statement below
WITH cte
AS
(SELECT
    product_id,
    SUM(unit) AS units
  FROM orders
  WHERE DATE_FORMAT(order_date, '%m%y') = '0220'
  GROUP BY product_id
  HAVING units >= 100)

SELECT
  p.product_name AS product_name,
  c.units AS unit
FROM cte c
  JOIN products p
    ON p.product_id = c.product_id;