# Write your MySQL query statement below
SELECT s.user_id,round(count(case when c.action = 'confirmed' then 1 end)/count(*), 2) as confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;
