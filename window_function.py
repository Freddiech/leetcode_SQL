#180. Consecutive Numbers
#https://leetcode.com/problems/consecutive-numbers/
with cte as(
select num,id+1-row_number()over(partition by num order by id asc) as rn
from Logs
)
select distinct num as ConsecutiveNums
from cte
group by num,rn
having count(*)>=3

#178. Rank Scores
#https://leetcode.com/problems/rank-scores/

select score, dense_rank()over(order by score desc) as rank from Scores



#626. Exchange Seats
#https://leetcode.com/problems/exchange-seats/
select
    case when mod(id,2)=1
    then coalesce(lead(id)over(order by id),id)
    else lag(id)over(order by id)
    end as id
    ,student
from Seat
order by id


