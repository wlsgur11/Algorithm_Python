select A.ID,
    case
        when (PER <= 0.25) then 'CRITICAL'
        when (PER <= 0.5) then 'HIGH'
        when (PER <= 0.75) then 'MEDIUM'
        else 'LOW'
    end as COLONY_NAME
from (
    select ID,
    PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PER
    FROM ECOLI_DATA) as A
order by A.ID