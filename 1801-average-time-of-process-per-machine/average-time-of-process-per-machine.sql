# Write your MySQL query statement below
SELECT t.machine_id, ROUND(AVG(diff),3) AS processing_time 
FROM (
	SELECT a1.machine_id as machine_id , round(a1.timestamp - a2.timestamp, 3) AS diff
	FROM Activity a1
    JOIN Activity a2 ON (a1.machine_id, a1.process_id ) = (a2.machine_id, a2.process_id) AND (a1.activity_type, a2.activity_type) = ('end', 'start')
) t
GROUP BY (t.machine_id)