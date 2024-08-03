# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
CROSS JOIN Weather w2
WHERE w1.temperature - w2.temperature > 0 AND DATEDIFF(w1.recordDate, w2.recordDate) = 1