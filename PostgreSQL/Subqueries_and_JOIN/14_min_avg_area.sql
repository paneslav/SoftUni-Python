SELECT
	MIN(average_area) AS min_average_area
FROM (
	SELECT
		AVG(c.area_in_sq_km) AS average_area
	FROM
		countries c
	GROUP BY
		continent_code
) AS min_average_area
	
