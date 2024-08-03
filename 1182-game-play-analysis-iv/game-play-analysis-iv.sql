# Write your MySQL query statement below
select round(count(distinct a1.player_id) / (select count(distinct player_id) from activity) , 2) AS fraction  
from activity a1 
join activity a2 using(player_id)
where (a1.player_id, a2.event_date) IN (SELECT player_id, min(event_date)
	FROM activity
	group by player_id)
    and datediff(a1.event_date, a2.event_date) = 1;