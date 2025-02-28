select g.score, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from HR_EMPLOYEES e 
join (
    select EMP_NO, sum(score) as score
    from HR_GRADE
    group by EMP_NO
    order by sum(score) desc
    limit 1) g on e.EMP_NO = g.EMP_NO
order by g.SCORE desc
limit 1



