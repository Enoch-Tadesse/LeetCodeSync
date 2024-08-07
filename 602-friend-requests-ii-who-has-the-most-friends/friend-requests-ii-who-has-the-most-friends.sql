# Write your MySQL query statement below
WITH cte AS (
SELECT requester_id AS id
FROM requestaccepted
union ALL
select accepter_id AS id
FROM requestaccepted
) SELECT id, count(id) AS num
FROM cte
group BY (id)
ORDER BY num DESC
limit 1