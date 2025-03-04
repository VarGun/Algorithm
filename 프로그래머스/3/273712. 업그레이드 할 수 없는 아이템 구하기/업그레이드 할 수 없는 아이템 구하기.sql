select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO i
where ITEM_ID not in (
    select PARENT_ITEM_ID as ITEM_ID
    from ITEM_TREE
    group by PARENT_ITEM_ID
    having PARENT_ITEM_ID is not null)
order by i.ITEM_ID desc
