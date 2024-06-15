UPDATE addresses
SET country = 
	CASE
		WHEN SUBSTRING(country, 1, 1) = 'B' THEN 'Blocked'
		WHEN SUBSTRING(country, 1, 1) = 'T' THEN 'Test'
		WHEN SUBSTRING(country, 1, 1) = 'P' THEN 'In Progress'
	END
WHERE
	SUBSTRING(country, 1, 1) IN ('B', 'T', 'P')
	