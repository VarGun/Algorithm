SELECT
    case
    when month(DIFFERENTIATION_DATE) < 4 then '1Q'
    when month(DIFFERENTIATION_DATE) < 7 then '2Q'
    when month(DIFFERENTIATION_DATE) < 10 then '3Q'
    else '4Q'
    end as QUARTER
    , COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER
