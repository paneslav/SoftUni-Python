CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(animal_name VARCHAR(30), OUT owner_name VARCHAR(30))
AS
$$
	DECLARE
	BEGIN
		SELECT
			COALESCE(o.name, 'For adoption')
		INTO
			owner_name
		FROM 
			animals AS a
		LEFT JOIN
			owners AS o ON o.id = a.owner_id
		WHERE
			a.name = animal_name;
	END;
$$
LANGUAGE plpgsql;