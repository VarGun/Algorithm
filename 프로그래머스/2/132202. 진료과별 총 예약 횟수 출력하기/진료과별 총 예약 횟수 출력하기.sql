# select MCDP_CD as '진료과 코드', count(*) as '5월예약건수'
# from APPOINTMENT
# # where APNT_YMD like '2022-05%'
# WHERE (YEAR(APNT_YMD) = '2022' AND MONTH(APNT_YMD) = '05')
# group by MCDP_CD
# order by '5월예약건수', MCDP_CD asc

select MCDP_CD as '진료과코드', count(*) as '5월예약건수'
from APPOINTMENT
where APNT_YMD like '2022-05%'
# WHERE (YEAR(APNT_YMD) = '2022' AND MONTH(APNT_YMD) = '05')
group by MCDP_CD
order by 5월예약건수, 진료과코드 asc