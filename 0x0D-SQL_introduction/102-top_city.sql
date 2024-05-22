-- Displays the average temperature of the top 3 cities in Jul to Aug --
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = '7' OR month = '8'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
