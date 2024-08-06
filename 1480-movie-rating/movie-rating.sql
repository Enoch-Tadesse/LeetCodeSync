# Write your MySQL query statement below
(SELECT
  u.name as results
FROM movierating mr
  JOIN users u
    ON mr.user_id = u.user_id
GROUP BY mr.user_id,
         u.name
ORDER BY COUNT(movie_id) DESC, u.name
LIMIT 1)

union all
(SELECT
  m.title 
FROM (
  SELECT *
  FROM movierating
  WHERE created_at between '2020-02-01' and '2020-02-28'
) t
JOIN movies m ON t.movie_id = m.movie_id
ORDER BY avg(t.rating) OVER (PARTITION BY t.movie_id) desc, m.title
LIMIT 1);