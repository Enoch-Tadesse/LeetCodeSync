# Write your MySQL query statement below
SELECT m.name
FROM Employee m
JOIN Employee e on e.managerId = m.id
GROUP BY m.id
HAVING count(e.id) >= 5