SELECT
	COUNT(*) AS countries_without_mountains
FROM countries AS c
FULL JOIN mountains_countries AS mc USING (country_code)
WHERE
	mc.country_code IS NULL
	
