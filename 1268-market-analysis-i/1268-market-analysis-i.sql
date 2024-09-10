with cte as(select user_id , count(order_id) as 'orders_in_2019'
from users u
join orders o on u.user_id = o.buyer_id
where year(o.order_date) = 2019
group by user_id)

select u.user_id buyer_id, u.join_date, coalesce(cte.orders_in_2019,0) orders_in_2019
from users u
left join cte on u.user_id = cte.user_id;