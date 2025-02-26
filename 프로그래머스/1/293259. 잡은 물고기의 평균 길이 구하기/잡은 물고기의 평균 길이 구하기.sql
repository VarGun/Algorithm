-- 코드를 작성해주세요
select round(avg(len), 2) as AVERAGE_LENGTH
from (select
      case when length IS NULL
      then 10 
      else length
      end as len
      from FISH_INFO
) AS gun;