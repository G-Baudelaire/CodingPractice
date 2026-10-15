SELECT MAX(subquery.num) AS num
FROM (
    SELECT DISTINCT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS subquery;