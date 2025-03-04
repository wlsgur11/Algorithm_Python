with FIRST_GEN as (
    select ID
    from ECOLI_DATA
    where PARENT_ID is null
),
    SECOND_GEN as (
    select A.ID, A.PARENT_ID
    from ECOLI_DATA A join FIRST_GEN B on A.PARENT_ID = B.ID
)

select A.ID
from ECOLI_DATA A join SECOND_GEN B on A.PARENT_ID = B.ID 