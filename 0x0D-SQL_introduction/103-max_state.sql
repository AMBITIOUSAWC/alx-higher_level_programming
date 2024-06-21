-- Connect to MySQL and select the database
USE hbtn_0c_0;

-- Query to find the maximum temperature of each state
SELECT state, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
