#177. Nth Highest Salary
#https://leetcode.com/problems/nth-highest-salary/
#solution 1: window function
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select max(salary) from(
      select salary,dense_rank()over(order by salary desc) as dsrk from Employee
          ) as t1
      where dsrk=@N
  );
END

#solution 2: limit offset
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
    select distinct salary from Employee
    order by salary desc
    limit 1 offset M
  );
END
