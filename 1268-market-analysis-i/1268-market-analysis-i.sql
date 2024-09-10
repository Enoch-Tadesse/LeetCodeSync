select distinct u.user_id buyer_id, u.join_date,
	count(case when year(o.order_date) = 2019 then 1 end) over(partition by u.user_id ) as orders_in_2019
from users u
left join orders o on u.user_id = o.buyer_id;