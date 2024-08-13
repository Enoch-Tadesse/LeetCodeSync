# Write your MySQL query statement below
WITH cte
AS
(SELECT
    id,
    name,
    departmentId,
    salary,
    RANK() OVER (PARTITION BY departmentId
    ORDER BY salary DESC) AS highest
  FROM employee)
SELECT
  d.name as Department,
  cte.name as Employee,
  cte.salary as Salary
FROM cte
  JOIN department d
    ON cte.departmentId = d.id
WHERE cte.highest = 1;