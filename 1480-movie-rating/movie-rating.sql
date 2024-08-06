# Write your MySQL query statement below
(SELECT
  u.name as results
FROM movierating mr
  JOIN users u
    ON mr.user_id = u.user_id
GROUP BY u.name
ORDER BY COUNT(*) DESC, u.name
LIMIT 1)

union all
(SELECT
  m.title 
FROM movierating mr
JOIN movies m ON mr.movie_id = m.movie_id
WHERE mr.created_at between '2020-02-01' and '2020-02-28'
group by m.title
ORDER BY avg(mr.rating) desc, m.title
LIMIT 1);