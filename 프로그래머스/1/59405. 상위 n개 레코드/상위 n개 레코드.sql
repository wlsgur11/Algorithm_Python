select name
from ANIMAL_INS
where DATETIME = (select min(DATETIME)
from ANIMAL_INS)