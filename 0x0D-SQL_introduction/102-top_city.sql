-- Connect to MySQL and select the database
USE hbtn_0c_0;

-- Query to select top 3 cities' temperatures during July and August
SELECT city, temperature
FROM temperatures
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
LIMIT 3;
