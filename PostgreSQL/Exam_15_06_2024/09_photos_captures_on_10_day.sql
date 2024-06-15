SELECT
	CONCAT(LEFT(description, 10), '...'),
	TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM
	photos
WHERE
	EXTRACT('day' FROM capture_date) = 10
ORDER BY
	capture_date DESC