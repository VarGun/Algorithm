-- 코드를 입력하세요
# SELECT FOOD_TYPE, REST_ID, REST_NAME, max(FAVORITES) as FAVORITES
# from REST_INFO
# group by FOOD_TYPE
# order by FOOD_TYPE desc
select a.FOOD_TYPE, a.REST_ID, a.REST_NAME, a.FAVORITES
from REST_INFO a
right join (select FOOD_TYPE, max(FAVORITES) as FAVORITES
from REST_INFO
group by FOOD_TYPE) b
on a.FOOD_TYPE = b.FOOD_TYPE and a.FAVORITES = b.FAVORITES
order by FOOD_TYPE desc





# REST_INFO 테이블에서 음식종류별로 
# 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기
# 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.