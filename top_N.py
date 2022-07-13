#176. Second Highest Salary
#https://leetcode.com/problems/second-highest-salary/
#solution 1: window function
with cte as(
select salary,dense_rank()over(order by salary desc) as dsrk from Employee
)
select (
select distinct salary from cte
where dsrk=2) as SecondHighestSalary

#solution 2: limit offset
select(
select distinct salary from Employee
order by salary desc
limit 1 offset 1
) as SecondHighestSalary


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



#185. Department Top Three Salaries
#https://leetcode.com/problems/department-top-three-salaries/submissions/
#solution 1: window function
with high_earners as(
select name,salary,departmentId from(
select name,salary,departmentId,dense_rank()over(partition by departmentId order by salary desc) as dsrk
from Employee ) as t1
where dsrk<=3)

select
    Department.name as Department
    ,high_earners.name as Employee
    ,high_earners.salary as Salary
from high_earners
,Department
where high_earners.departmentId=Department.id

#solution 2: join
SELECT
    d.name as "Department"
    ,e1.Name as "Employee"
    , e1.Salary as "Salary"
FROM
    Employee e1
    JOIN Employee e2  JOIN Department d
WHERE
    e1.DepartmentId = e2.DepartmentId
    AND e1.Salary <= e2.Salary  AND d.id = e2.DepartmentId
GROUP BY d.name,e1.id
HAVING COUNT(DISTINCT(e2.Salary)) <= 3


#185. Department Top Three Salaries
#https://leetcode.com/problems/department-top-three-salaries/
#184. Department Highest Salary
#https://leetcode.com/problems/department-highest-salary/
with cte as(
select name as Employee ,Salary ,departmentId
,dense_rank()over(partition by departmentId order by Salary desc) as dsrk
from Employee
)

select
     t2.name as Department
    ,t1.Employee
    ,t1.Salary
from cte as t1
,Department as t2
where t1.departmentId=t2.id
and t1.dsrk<=3
# and t1.dsrk=1
