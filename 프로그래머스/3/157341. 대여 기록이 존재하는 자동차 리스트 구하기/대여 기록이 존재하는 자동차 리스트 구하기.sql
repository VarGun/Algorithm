select a.CAR_ID
from CAR_RENTAL_COMPANY_CAR a
join (
    select CAR_ID, START_DATE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where month(START_DATE) = 10 
    group by CAR_ID ) b on a.CAR_ID = b.CAR_ID
where a.CAR_TYPE = '세단'
order by a.car_id desc
# select CAR_ID, START_DATE
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     where month(START_DATE) = 10 
#     group by CAR_ID