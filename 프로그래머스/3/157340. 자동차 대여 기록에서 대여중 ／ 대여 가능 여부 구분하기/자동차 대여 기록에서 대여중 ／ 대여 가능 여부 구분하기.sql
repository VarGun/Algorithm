select car_id,
    case when sum(
        case when '2022-10-16' BETWEEN START_DATE AND END_DATE THEN 1
        ELSE 0 END
    ) > 0 THEN '대여중'
    ELSE '대여 가능' END as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc