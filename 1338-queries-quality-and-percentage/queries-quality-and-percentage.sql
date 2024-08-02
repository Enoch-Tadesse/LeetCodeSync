# Write your MySQL query statement below
SELECT q.query_name, round(avg(q.rating/q.position),2) as quality, round(sum(case when rating < 3 then 1 else 0 end) / count(q.query_name) * 100,2) as poor_query_percentage
FROM Queries q
WHERE q.query_name is not null
GROUP BY query_name;