# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from logs l
where ((select num from logs where id = l.id-1) = num) and (num = (select num from logs where id = l.id+1));
