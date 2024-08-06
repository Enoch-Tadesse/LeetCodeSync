# Write your MySQL query statement below
SELECT
  s.id as id,
  COALESCE((case WHEN s.id % 2 = 0 THEN lag(student) over(order BY s.id) ELSE LEAD (student) over(order BY s.id) end), s.student ) as student
FROM seat s;