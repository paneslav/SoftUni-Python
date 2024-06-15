SELECT
	a."name" AS address,
	CASE
		WHEN EXTRACT('hour' FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
		ELSE 'Night'
	END AS day_time,
	co.bill,
	cl.full_name,
	ca.make,
	ca.model,
	cate.name
FROM
	courses AS co
JOIN
	addresses AS a ON a.id = co.from_address_id
JOIN 
	cars AS ca ON ca.id = co.car_id
JOIN 
	categories AS cate ON cate.id = ca.category_id
JOIN
	clients AS cl ON cl.id = co.client_id
ORDER BY
	co.id