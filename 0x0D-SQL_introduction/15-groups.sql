-- Use the specified database
USE hbtn_0c_0;

-- List scores and their counts, sorted by count descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
