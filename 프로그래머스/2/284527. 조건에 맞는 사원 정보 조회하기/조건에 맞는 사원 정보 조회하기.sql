select g.SCORE, e.EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_EMPLOYEES e
join (select EMP_NO, sum(SCORE) as SCORE
        from HR_GRADE
        group by EMP_NO
        order by SCORE desc limit 1) g
on e.EMP_NO = g.EMP_NO

# 점수, 사번, 성명, 직책, 이메일을
# 점수 GRADE (HR_GRADE)
# 사번, 성명, 직책, 이메일을