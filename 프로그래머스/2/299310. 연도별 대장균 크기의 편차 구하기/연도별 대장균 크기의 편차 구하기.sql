select YEAR(A.DIFFERENTIATION_DATE) AS YEAR, (B.MAX_SIZE - A.SIZE_OF_COLONY) AS YEAR_DEV, ID
from  ECOLI_DATA A
JOIN (
        select year(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) AS MAX_SIZE
        from ECOLI_DATA
        group by year(DIFFERENTIATION_DATE)
    ) B 
ON YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY YEAR(A.DIFFERENTIATION_DATE), B.MAX_SIZE - A.SIZE_OF_COLONY