DELETE FROM clients
WHERE id IN (
	SELECT
		cl.id
	FROM
		clients AS cl
	LEFT JOIN
		courses AS co ON  cl.id = co.client_id
	WHERE
		co.client_id IS NULL
			AND
		LENGTH(cl.full_name) > 3
	)
;