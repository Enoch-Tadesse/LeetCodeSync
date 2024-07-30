# Write your MySQL query statement below
SELECT s.student_id, s.student_name, su.subject_name, count(e.subject_name) as attended_exams
FROM subjects su
CROSS JOIN students s
left JOIN examinations e ON (s.student_id , su.subject_name) = (e.student_id, e.subject_name)
group by s.student_id, su.subject_name, s.student_name
order by s.student_id, su.subject_name