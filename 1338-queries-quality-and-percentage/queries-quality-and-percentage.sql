# Write your MySQL query statement below
SELECT q.query_name, round(avg(q.rating/q.position),2) as quality, round(sum(rating<3) / count(*) * 100,2) as poor_query_percentage
FROM Queries q
WHERE q.query_name is not null
GROUP BY query_name;

-- sum(case when rating < 3 then 1 else 0 end