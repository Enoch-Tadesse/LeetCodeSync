SELECT d.name AS Department,
  e.name AS Employee,
  e.salary AS Salary
from employee e
JOIN department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (SELECT departmentId, max(salary)
FROM employee
GROUP BY departmentId);