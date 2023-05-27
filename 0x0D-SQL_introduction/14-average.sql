-- computes the score average of all records in mySQL server
UPDATE second_table SET average = (SELECT AVG(*) FROM second_table);
