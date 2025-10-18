SELECT MONTH(START_DATE) AS MONTH,
       CAR_ID,
       COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
)
AND START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH(START_DATE), CAR_ID
ORDER BY MONTH, CAR_ID DESC;



















































# select month(start_date) as MONTH, CAR_ID, count(history_id) as RECORDS
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where (year(START_DATE) = 2022 and (month(START_DATE) between 08 and 10) )
# group by MONTH, car_id
# having RECORDS != 0 and RECORDS >= 5
# order by MONTH, car_id desc


# select car_id 
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
# where start_date>="2022-08-01" and start_date<"2022-11-01" 
# group by car_id 
# having count(history_id) > 4