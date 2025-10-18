select i.FISH_COUNT, ni.FISH_NAME
from (select FISH_TYPE, count(*) as FISH_COUNT
    from FISH_INFO
    group by FISH_TYPE) i
left join FISH_NAME_INFO ni
on i.FISH_TYPE = ni.FISH_TYPE
order by i.FISH_COUNT desc