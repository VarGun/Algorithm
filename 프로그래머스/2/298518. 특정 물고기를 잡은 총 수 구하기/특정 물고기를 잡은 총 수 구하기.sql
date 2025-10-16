# select *
# from FISH_INFO i
# join FISH_NAME_INFO ni
# on i.FISH_TYPE = ni.FISH_TYPE and ni.FISH_NAME in ('BASS', 'SNAPPER')

select count(*) as FISH_COUNT
from FISH_INFO i
join (select FISH_TYPE
    from FISH_NAME_INFO
    where FISH_NAME in ('BASS', 'SNAPPER')) ni
on i.FISH_TYPE = ni.FISH_TYPE