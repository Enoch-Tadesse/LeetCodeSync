CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT DETERMINISTIC
BEGIN
  RETURN (
    select t.salary from(SELECT DENSE_RANK() over(order by salary desc) as rnk,
                    e.salary
    FROM Employee e ) t
    where t.rnk = N
    limit 1
  );
END