-- 코드를 입력하세요
SELECT category, sum(SALES) as TOTAL_SALES
from BOOK a
inner join BOOK_SALES b
on a.BOOK_ID = b.BOOK_ID
where b.SALES_DATE between "2022-01-01" AND "2022-01-31"
group by category
order by category

# 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 
# 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성해주세요.