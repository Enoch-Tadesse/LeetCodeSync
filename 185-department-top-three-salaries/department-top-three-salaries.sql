# Write your MySQL query statement below
WITH mytable
AS
(SELECT
    ID,
    departmentId
  FROM (SELECT
      id,
      departmentId,
      DENSE_RANK() OVER (w) AS ranked
    FROM employee e
    WINDOW w AS (PARTITION BY departmentId
    ORDER BY salary DESC)) t
  WHERE ranked <= 3)

SELECT
  d.name AS Department,
  e.name AS Employee,
  e.salary AS Salary
FROM mytable m
  LEFT JOIN employee e
    ON m.id = e.id
  LEFT JOIN department d
    ON d.id = e.departmentId; 