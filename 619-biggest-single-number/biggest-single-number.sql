# Write your MySQL query statement below
select (case when count(num) > 1 then null else num end) as num
from mynumbers m
group by num
order by count(num), num desc
limit 1