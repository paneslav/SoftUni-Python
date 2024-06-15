SELECT
	d.first_name,
	d.last_name,
	c.make,
	c.model,
	c.mileage
FROM
	cars_drivers AS cd
JOIN
	drivers AS d ON d.id = cd.driver_id
JOIN
	cars AS c ON c.id = cd.car_id
WHERE 
	mileage IS NOT NULL
ORDER BY
	mileage DESC,
	d.first_name