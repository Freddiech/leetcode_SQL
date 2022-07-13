#181. Employees Earning More Than Their Managers
#https://leetcode.com/problems/employees-earning-more-than-their-managers/
#solition 1: left join
select name as Employee from(
select t1.*, t2.salary as managersalary from Employee as t1
left join Employee as t2
on t1.managerId=t2.id
) as a
where salary>managersalary

#solution 2:
select t1.name as Employee
from Employee as t1
,Employee as t2
where t1.managerId=t2.id
and t1.salary>t2.salary

#262. Trips and Users
#https://leetcode.com/problems/trips-and-users/
select
    request_at as Day
    ,round(count(case when status<>'completed' then 1 else NULL end)/count(*),2) as "Cancellation Rate"
from
    Trips
    ,Users as t2
    ,Users as t3
where
    Trips.client_id = t2.users_id
    and t2.banned = 'No'
    and Trips.driver_id = t3.users_id
    and t3.banned = 'No'
    and request_at between '2013-10-01' and '2013-10-03'
group by request_at

#197. Rising Temperature
#https://leetcode.com/problems/rising-temperature/
select t1.id from Weather as t1
,Weather as t2
where datediff(t1.recordDate,t2.recordDate)=1
and t1.temperature > t2.temperature



