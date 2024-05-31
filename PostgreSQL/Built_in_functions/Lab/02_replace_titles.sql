SELECT
	replace(title, 'The', '***') 
FROM
	books
WHERE
	LEFT(title, 4) = 'The '
;

UPDATE books
SET 
	title = replace(title, 'The', '***') 
WHERE
	LEFT(title, 4) = 'The '
RETURNING *;

