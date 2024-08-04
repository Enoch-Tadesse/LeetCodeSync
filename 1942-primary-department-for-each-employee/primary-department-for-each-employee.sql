# Write your MySQL query statement below
SELECT employee_id , department_id
FROM employee
WHERE employee_id IN (
		SELECT employee_id
		FROM employee
		GROUP BY employee_id
		HAVING COUNT(employee_id) = 1)
UNION
SELECT employee_id , department_id
FROM employee
where primary_flag = 'Y';