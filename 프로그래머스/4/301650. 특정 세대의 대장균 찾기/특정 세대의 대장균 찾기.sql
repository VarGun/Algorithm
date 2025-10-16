# 1. 부모가 없는, 1세대 대장균 찾기
# select *
# from ECOLI_DATA
# where PARENT_ID is null 

# 2. 2세대 연결
# select ch.id
# from ECOLI_DATA ch
# join (select ID
#     from ECOLI_DATA
#     where PARENT_ID is null) par
# on ch.PARENT_ID = par.ID

# 3. 3세대 연결
select gen3.id
from ECOLI_DATA gen3
join (select ch.id
from ECOLI_DATA ch
join (select ID
    from ECOLI_DATA
    where PARENT_ID is null) par
on ch.PARENT_ID = par.ID) gen2
on gen2.id = gen3.PARENT_ID
order by gen3.ID

