# Write your MySQL query statement below
SELECT round(avg(t.immediate) * 100,2) AS immediate_percentage
FROM (SELECT customer_id, MIN(order_date) = MIN(customer_pref_delivery_date) as immediate
		FROM delivery
		GROUP BY customer_id) t