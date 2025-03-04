select u.USER_ID, u.NICKNAME, b.sum_price as TOTAL_SALES
from USED_GOODS_USER u
join (
    select WRITER_ID, sum(PRICE) as sum_price
from USED_GOODS_BOARD
where STATUS = 'DONE'
group by WRITER_ID
having sum_price >= 700000 ) as b on u.USER_ID = b.WRITER_ID
order by b.sum_price


# select WRITER_ID, sum(PRICE) as sum_price
# from USED_GOODS_BOARD
# where STATUS = 'DONE'
# group by WRITER_ID
# having sum_price >= 700000