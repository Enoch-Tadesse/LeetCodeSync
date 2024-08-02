# Write your MySQL query statement below
SELECT r.contest_id, round(count(r.user_id)/ (SELECT count(user_id) FROM Users) * 100,2) as percentage
FROM Register r
JOIN Users u USING (user_id)
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC
