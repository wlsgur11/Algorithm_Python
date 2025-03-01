select ID, LENGTH
from FISH_INFO
order by IFNULL(LENGTH, 10) DESC, ID
limit 10