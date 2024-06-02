SELECT
	*
FROM
	departments d
INNER JOIN
	employees e ON d.id = e.department_id