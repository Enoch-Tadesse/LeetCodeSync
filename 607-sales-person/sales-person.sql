# Write your MySQL query statement below
SELECT s.name
FROM SalesPerson s
WHERE s.sales_id NOT IN(
    SELECT s.sales_id
    FROM SalesPerson s
    LEFT JOIN Orders o USING(sales_id)
    JOIN Company c USING(com_id)
    WHERE c.name = 'RED' 
);