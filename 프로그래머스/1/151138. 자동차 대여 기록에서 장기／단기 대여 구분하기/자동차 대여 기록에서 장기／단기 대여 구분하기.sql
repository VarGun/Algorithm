-- 코드를 입력하세요
# SELECT history_id, car_id, date_format(START_DATE, '%Y-%m-%d') as START_DATE, date_format(END_DATE, '%Y-%m-%d') as END_DATE,
#     CASE 
#     WHEN END_DATE - START_DATE >= 30 THEN '장기 대여' 
#     ELSE '단기 대여' 
#     END AS RENT_TYPE
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where START_DATE >= '2022-09-01'
# and START_DATE < '2022-10-01'
# order by HISTORY_ID desc

SELECT HISTORY_ID, CAR_ID, 
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE, 
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       CASE 
           WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여' 
           ELSE '단기 대여' 
       END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE >= '2022-09-01' AND START_DATE < '2022-10-01'
ORDER BY HISTORY_ID DESC;