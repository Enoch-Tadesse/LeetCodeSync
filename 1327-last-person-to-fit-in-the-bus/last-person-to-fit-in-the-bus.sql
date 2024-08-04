# Write your MySQL query statement below
select person_name
from queue q
where (select sum(weight)
				from queue
				where turn <= q.turn) <= 1000
order by q.turn desc
limit 1