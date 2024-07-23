# Write your MySQL query statement below
SELECT customer_id, count(v.visit_id) as count_no_trans
FROM Visits v
LEFT OUTER JOIN Transactions t USING (visit_id)
WHERE transaction_id is null
GROUP BY customer_id;