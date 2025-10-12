
-- 코드를 입력하세요
SELECT TITLE, b.BOARD_ID, REPLY_ID, r.WRITER_ID, r.CONTENTS, date_format(r.CREATED_DATE, '%Y-%m-%d') -- 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일
from USED_GOODS_BOARD b, USED_GOODS_REPLY r
where b.BOARD_ID = r.BOARD_ID
and year(b.CREATED_DATE) = 2022
and month(b.CREATED_DATE) = 10
order by r.CREATED_DATE, b.title
