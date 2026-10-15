SELECT w0.id AS Id
FROM Weather w0
JOIN Weather w1 ON w1.recordDate = DATE_SUB(w0.recordDate, INTERVAL 1 DAY)
WHERE w0.temperature > w1.temperature;