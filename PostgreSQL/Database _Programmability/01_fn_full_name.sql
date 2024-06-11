CREATE OR REPLACE FUNCTION fn_full_name(VARCHAR, VARCHAR)
RETURNS VARCHAR AS
$$
	DECLARE
		first_name VARCHAR := lower($1);
		last_name VARCHAR := lower($2);
		full_name VARCHAR(30);
	BEGIN
		
		IF first_name IS NULL AND last_name IS NULL THEN
			RETURN NULL;
		ELSIF first_name IS NULL AND last_name IS NOT NULL THEN
			full_name := INITCAP(last_name);
		ELSIF first_name IS NOT NULL AND last_name IS NULL THEN
			full_name := INITCAP(first_name);
		ELSE
			full_name := CONCAT_WS(' ', INITCAP(first_name), INITCAP(last_name));
		END IF;

		RETURN full_name;
	END;
$$
LANGUAGE plpgsql;