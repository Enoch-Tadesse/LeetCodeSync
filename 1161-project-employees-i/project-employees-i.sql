# Write your MySQL query statement below
SELECT p.project_id, round(AVG(e.experience_years),2) as average_years
FROM Project p
JOIN Employee e USING (employee_id)
GROUP BY (p.project_id)