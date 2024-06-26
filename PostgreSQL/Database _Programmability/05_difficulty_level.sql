CREATE OR REPLACE FUNCTION fn_difficulty_level(level INT)
RETURNS VARCHAR AS
$$
	DECLARE
	BEGIN
		IF level <= 40 THEN
			RETURN 'Normal Difficulty';
		ELSIF level BETWEEN 41 AND 60 THEN
			RETURN 'Nightmare Difficulty';
		ELSE
			RETURN 'Hell Difficulty';
		END IF;
	END;
$$
LANGUAGE plpgsql;