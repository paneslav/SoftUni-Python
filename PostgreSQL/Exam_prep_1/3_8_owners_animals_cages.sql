SELECT
	CONCAT(o."name", ' - ', a."name") AS "owners-animals",
	o.phone_number,
	ac.cage_id
FROM
	owners AS o
JOIN
	animals AS a ON a.owner_id = o.id
JOIN 
	animals_cages AS ac ON ac.animal_id = a.id
WHERE
	a.animal_type_id = (SELECT id FROM animal_types WHERE animal_type = 'Mammals')
ORDER BY
	o.name,
	a.name DESC
