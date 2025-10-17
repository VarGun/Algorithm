select c.CAR_ID
from CAR_RENTAL_COMPANY_CAR c
join (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where month(start_date) = 10
    group by CAR_ID
    ) h
on c.CAR_ID = h.CAR_ID
where CAR_TYPE = '세단'
order by c.CAR_ID desc























# select a.CAR_ID
# from CAR_RENTAL_COMPANY_CAR a
# join (
#     select CAR_ID, START_DATE
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     where month(START_DATE) = 10 
#     group by CAR_ID ) b on a.CAR_ID = b.CAR_ID
# where a.CAR_TYPE = '세단'
# order by a.car_id desc