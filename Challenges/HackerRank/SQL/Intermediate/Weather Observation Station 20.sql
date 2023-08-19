SELECT cast(round(LAT_N,4) as numeric(36,4))
FROM
    STATION
ORDER BY
    LAT_N
OFFSET CAST(CEILING((SELECT COUNT(LAT_N) FROM STATION)/2.0)- 1 AS INT) ROWS 
FETCH NEXT 1 ROWS ONLY;

