# Write your MySQL query statement below
update Salary
set sex = coalesce(nullif("f", sex), "m")