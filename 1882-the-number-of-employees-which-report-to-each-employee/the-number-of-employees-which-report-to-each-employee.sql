# Write your MySQL query statement below
SELECT m.employee_id, m.name, count(e.employee_id) as reports_count, ROUND(avg(e.age), 0) as average_age
FROM Employees m
JOIN Employees e ON m.employee_id = e.reports_to
GROUP BY m.employee_id
ORDER BY m.employee_id