# Write your MySQL query statement below
with class as (
			select *, (case when a.income < 20000 then 'Low Salary' when a.income between 20000 and 50000 then 'Average Salary' else 'High Salary' End) as state
            from accounts a),
	state as(
			select 'Low Salary' as category
            union
            select 'Average Salary' as category
            union
            select 'High Salary' as category)
		
select s.category, count(class.state) as accounts_count
from state s
left join class on s.category = class.state
group by s.category;