#!/bin/bash

DB_NAME="hbtn_0c_0"

# MySQL command to drop database if exists
MYSQL_CMD="mysql -u root -e 'DROP DATABASE IF EXISTS $DB_NAME;'"

# Execute MySQL command and capture output
OUTPUT=$(eval $MYSQL_CMD 2>&1)

# Check if there was an error
if [ $? -ne 0 ]; then
    echo "Error deleting database $DB_NAME:"
    echo "$OUTPUT"
    exit 1
else
    echo "Database $DB_NAME deleted successfully (if it existed)."
fi
