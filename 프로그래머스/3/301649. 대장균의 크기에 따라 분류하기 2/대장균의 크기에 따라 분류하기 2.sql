select ranking.ID, 
    case
    when ranking.per <= 0.25 then 'CRITICAL'
    when ranking.per <= 0.5 then 'HIGH'
    when ranking.per <= 0.75 then 'MEDIUM'
    else 'LOW' end as COLONY_NAME
from 
    (select ID, PERCENT_RANK() over (order by SIZE_OF_COLONY desc) as per, SIZE_OF_COLONY
    from ECOLI_DATA) as ranking
order by ranking.ID
