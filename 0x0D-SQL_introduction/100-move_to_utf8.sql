-- Step 1: Connect to MySQL and select the database
USE hbtn_0c_0;

-- Step 2: Alter the database to use utf8mb4 encoding and utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 3: Iterate over each table and convert to utf8mb4
SET group_concat_max_len = 2048;
SELECT GROUP_CONCAT('ALTER TABLE `', table_name, '` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
INTO @sql
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0';

-- Step 4: Execute the generated SQL statements
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
