# Write your MySQL query statement below
with cte as (
    select product_id, max(sale_date) latest, min(sale_date) first
    from sales s
    group by product_id
)
select p.product_id, p.product_name
from Product p
Join cte s Using (product_id)
where (s.latest between '2019-01-01' and '2019-03-31') and (s.first between '2019-01-01' and '2019-03-31')