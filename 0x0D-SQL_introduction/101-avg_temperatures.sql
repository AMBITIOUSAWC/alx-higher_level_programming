-- Calculate average temperature in Fahrenheit by city and order by temperature descending

USE hbtn_0c_0;

SELECT city,
       ROUND(AVG(temperature) * 9 / 5 + 32, 2) AS avg_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
