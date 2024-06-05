SELECT
	c.country_name,
	r.river_name
FROM
	countries c
LEFT JOIN countries_rivers AS cr ON c.country_code = cr.country_code
LEFT JOIN rivers AS r ON r.id = cr.river_id
WHERE
	c.continent_code = (SELECT continent_code FROM continents WHERE continent_name = 'Africa')
ORDER BY
	country_name
LIMIT
	5