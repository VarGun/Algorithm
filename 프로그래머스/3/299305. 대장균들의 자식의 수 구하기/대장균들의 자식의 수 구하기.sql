select a.ID,
    case
    when b.child is null then 0
    else b.child
    end as CHILD_COUNT
from ECOLI_DATA a
left join (
    select PARENT_ID, count(ID) as child
    from ECOLI_DATA 
    group by PARENT_ID
    having PARENT_ID is not null) b on a.ID = b.PARENT_ID
order by a.ID