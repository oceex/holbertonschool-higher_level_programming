-- wwwooowww
SELECT city, SUM(value)/COUNT(city) AS avg_temp
FROM temperatures
WHERE month=7 or month=8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;