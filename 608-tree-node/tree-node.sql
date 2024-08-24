# Write your MySQL query statement below
with parent AS (SELECT distinct p_id FROM tree)
select id , (case WHEN p_id is NULL THEN "Root" WHEN id IN (SELECT * FROM parent) THEN "Inner" ELSE "Leaf" end) AS type
FROM tree;