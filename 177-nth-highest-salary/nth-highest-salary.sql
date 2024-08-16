CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT DETERMINISTIC
BEGIN
set N = N-1;
  RETURN (
    select distinct salary
    from employee e
    order by e.salary desc
    limit 1
    offset N
  );
END