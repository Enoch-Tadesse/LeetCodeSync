# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b USING (empID)
WHERE b.bonus is NULL or b.bonus < 1000;