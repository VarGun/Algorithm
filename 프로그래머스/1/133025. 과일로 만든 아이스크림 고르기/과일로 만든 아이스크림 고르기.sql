-- 코드를 입력하세요
SELECT f.FLAVOR
from FIRST_HALF f, ICECREAM_INFO i
where f.FLAVOR = i.FLAVOR
and i.INGREDIENT_TYPE = 'fruit_based'
and f.TOTAL_ORDER > 3000
order by f.TOTAL_ORDER desc