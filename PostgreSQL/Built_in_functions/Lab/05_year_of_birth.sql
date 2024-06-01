SELECT
	first_name,
	last_name,
	EXTRACT('year' FROM born) AS year #date_part('year', born)
FROM
	authors