SELECT
	v.name,
	v.phone_number,
	TRIM(TRIM(v.address), 'Sofia, ')
FROM
	volunteers AS v
JOIN
	volunteers_departments AS vd ON v.department_id = vd.id
WHERE
	vd.department_name = 'Education program assistant'
		AND
	v.address LIKE '%Sofia%'
ORDER BY
	v.name