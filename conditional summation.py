#1841. League Statistics
#https://leetcode.com/problems/league-statistics/
with cte1 as(
select *
    ,case when home_team_goals > away_team_goals then 3
     when home_team_goals = away_team_goals then 1
     else 0
     end as home_team_points
    ,case when home_team_goals < away_team_goals then 3
     when home_team_goals = away_team_goals then 1
     else 0
     end as away_team_points
from Matches
)
,cte2 as(
select home_team_id as team_id
    ,home_team_points as points
    ,home_team_goals as goal_for
    ,away_team_goals as goal_against
    ,home_team_goals-away_team_goals as goal_diff
from cte1
union all
select away_team_id as team_id
    ,away_team_points as points
    ,away_team_goals as goal_for
    ,home_team_goals as goal_against
    ,away_team_goals-home_team_goals as goal_diff
from cte1
)
select t2.team_name
    ,count(*) as matches_played
    ,sum(points) as points
    ,sum(goal_for) as goal_for
    ,sum(goal_against) as goal_against
    ,sum(goal_diff) as goal_diff
from cte2 as t1
    ,Teams as t2
where t1.team_id=t2.team_id
group by t2.team_name
order by points desc, goal_diff desc, t2.team_name asc

