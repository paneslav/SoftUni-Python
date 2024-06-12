SELECT
	a.name AS animal,
	EXTRACT('YEAR' FROM a.birthdate) AS birth_year,
	at.animal_type
FROM
	animals AS a
JOIN
	animal_types AS at ON a.animal_type_id = at.id
WHERE
	a.owner_id IS NULL
		AND
	EXTRACT('YEAR' FROM AGE('01/01/2022', a.birthdate)) < 5
		AND
	at.animal_type <> 'Birds'
	-- animal_type_id <> (SELECT id FROM animal_types WHERE animal_type = 'Birds')
ORDER BY
	name