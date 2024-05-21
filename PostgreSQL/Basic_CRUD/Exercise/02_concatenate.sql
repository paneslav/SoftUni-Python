ALTER TABLE cities
RENAME COLUMN area TO area_km2
;
SELECT
	concat(name, ' ', state) AS cities_information,
	area_km2
FROM cities
ORDER BY id
;