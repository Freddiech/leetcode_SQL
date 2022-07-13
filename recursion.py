#1384. Total Sales Amount by Year
#https://leetcode.com/problems/total-sales-amount-by-year/
with recursive cte as(
select year(min(period_start)) as yr from Sales
union all
select yr+1 from cte
where yr<(select year(max(period_end)) as yr from Sales)
)

select t1.product_id
,t3.product_name
,cast(t2.yr as CHAR) as report_year
,(DATEDIFF(
    LEAST(period_end,DATE(CONCAT_WS('-', t2.yr, 12, 31)))
    ,GREATEST(period_start,DATE(CONCAT_WS('-', t2.yr, 1, 1)))
)+1)*average_daily_sales as total_amount
from Sales as t1
,cte as t2
,Product as t3
where year(t1.period_start)<=t2.yr
and year(t1.period_end)>=t2.yr
and t1.product_id=t3.product_id
order by product_id, report_year
