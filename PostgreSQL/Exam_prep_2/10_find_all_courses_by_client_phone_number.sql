CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT AS
$$
	DECLARE
		result INT;
	BEGIN
		SELECT INTO result
			COUNT(*)
		FROM
			courses
		WHERE
			client_id = 
			(
			SELECT
			id
			FROM
				clients
			WHERE
				phone_number = phone_num
			GROUP BY
				id
			);
		RETURN result;
	END;
$$
LANGUAGE plpgsql;