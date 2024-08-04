# Write your MySQL query statement below
select *, (
	CASE
		WHEN (x + y + z) - 2 * greatest(x,y,z) > 0 THEN 'Yes'
        ELSE 'No'
	END
) as triangle
from triangle;