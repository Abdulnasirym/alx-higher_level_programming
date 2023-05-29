-- list cities of california that can be found in the database hbtn_0d_usa
SELECT (SELECT NAME FROM hbtn_0d_usa.states ORDER BY cities.id DESC) FROM hbtn_0d_usa;
