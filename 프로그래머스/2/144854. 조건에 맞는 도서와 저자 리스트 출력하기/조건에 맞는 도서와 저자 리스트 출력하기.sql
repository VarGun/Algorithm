select b.BOOK_ID, a.AUTHOR_NAME, date_Format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK b
join AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID
where b.CATEGORY = '경제'
order by PUBLISHED_DATE


































# select b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
# from book b
# join author a on b.AUTHOR_ID = a.AUTHOR_ID
# where b.CATEGORY = '경제'
# order by PUBLISHED_DATE