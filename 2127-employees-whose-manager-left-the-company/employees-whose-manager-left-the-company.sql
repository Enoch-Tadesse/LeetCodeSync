# Write your MySQL query statement below

SELECT employee_id
from employees e
WHERE e.manager_id NOT IN (
  SELECT employee_id
  FROM employees e1
) AND e.salary < 30000
order by e.employee_id;