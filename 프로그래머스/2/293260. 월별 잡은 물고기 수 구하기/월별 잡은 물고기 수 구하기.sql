select count(*) as FISH_COUNT, month(TIME) as MONTH
from FISH_INFO
group by month(TIME) having count(*) != 0
order by MONTH













































# -- 코드를 작성해주세요
# SELECT COUNT(*) AS FISH_COUNT, MONTH(TIME) AS MONTH
# FROM FISH_INFO
# GROUP BY MONTH(TIME)
# ORDER BY MONTH(TIME)