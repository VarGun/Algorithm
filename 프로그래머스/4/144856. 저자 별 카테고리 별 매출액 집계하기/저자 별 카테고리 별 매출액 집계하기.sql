-- 코드를 입력하세요
SELECT a.AUTHOR_ID, b.AUTHOR_NAME, a.CATEGORY, (sum(c.SALES * a.PRICE)) as TOTAL_SALES
from BOOK a
inner join AUTHOR b
on a.AUTHOR_ID = b.AUTHOR_ID
inner join BOOK_SALES c
on a.BOOK_ID = c.BOOK_ID
where date_format(c.sales_date, "%Y-%m") = "2022-01"
group by a.AUTHOR_ID, a.CATEGORY
order by a.AUTHOR_ID, a.CATEGORY desc

