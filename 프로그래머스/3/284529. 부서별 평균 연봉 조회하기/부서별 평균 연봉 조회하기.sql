select d.DEPT_ID, d.DEPT_NAME_EN, i.AVG_SAL as AVG_SAL
from HR_DEPARTMENT d
join (
    select DEPT_ID, round(avg(SAL), 0) as AVG_SAL
    from HR_EMPLOYEES
    group by DEPT_ID) i on d.DEPT_ID = i.DEPT_ID
order by AVG_SAL desc