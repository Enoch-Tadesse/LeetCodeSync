# Write your MySQL query statement below
select round(count(distinct a1.player_id) / (select count(distinct player_id) from activity) , 2) AS fraction  
from activity a1 
where (a1.player_id, date_sub(a1.event_date, interval 1 day)) IN (SELECT player_id, min(event_date)
	FROM activity
	group by player_id);