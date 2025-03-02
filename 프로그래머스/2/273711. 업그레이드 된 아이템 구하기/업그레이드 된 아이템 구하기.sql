select ch.ITEM_ID, ch.ITEM_NAME, ch.RARITY
from ITEM_INFO as par
join ITEM_TREE as it on it.PARENT_ITEM_ID = par.ITEM_ID
join ITEM_INFO as ch on it.ITEM_ID = ch.ITEM_ID
where par.RARITY = 'RARE'
order by ch.ITEM_ID desc