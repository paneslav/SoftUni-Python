CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT AS
$$
	DECLARE
		inspected_dep_id INT;
		total_workers INT;
	BEGIN
		inspected_dep_id := (SELECT id FROM volunteers_departments WHERE department_name = searched_volunteers_department);
		total_workers := (SELECT COUNT(*) FROM volunteers WHERE department_id = inspected_dep_id);
		RETURN total_workers;
	END;
$$
LANGUAGE plpgsql;