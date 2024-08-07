# Write your MySQL query statement below
select distinct visited_on,
    (select sum(amount)
    from customer c1
    where c1.visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on) as amount,
    (select round(sum(amount)/7,2)
    from customer c2
    where c2.visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on) as average_amount

from customer c
where c.visited_on >= date_add((select min(visited_on) from customer), interval 6 day) 