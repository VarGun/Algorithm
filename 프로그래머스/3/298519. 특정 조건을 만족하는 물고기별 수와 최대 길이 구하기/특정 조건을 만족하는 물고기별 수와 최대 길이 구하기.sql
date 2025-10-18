select count(*) as FISH_COUNT, max(LENGTH) as MAX_LENGTH, FISH_TYPE
from (select ID, FISH_TYPE, 
    case when LENGTH is null then 10
    else LENGTH end as LENGTH
    ,TIME
from FISH_INFO) a
group by a.FISH_TYPE having avg(LENGTH) >= 33
order by FISH_TYPE




































































# select count(*) as FISH_COUNT, max(length) as MAX_LENGTH, FISH_TYPE
# from (select ID, FISH_TYPE,
#     case
#     when LENGTH is null then 10
#     else LENGTH
#     end as LENGTH
# from FISH_INFO) a
# group by FISH_TYPE
# having avg(length) >= 33
# order by FISH_TYPE





# # 중식, 한술, 양식