-- list all cities contained in the database hbtn_0d_usa
SELECT cities.id , cities.name , states.name
FROM cities JOIN states ON cities.id=cities.states_id ORDER BY cities.id;
