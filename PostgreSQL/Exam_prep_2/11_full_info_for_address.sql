CREATE OR REPLACE PROCEDURE sp_courses_by_address(address_name VARCHAR(100))
AS
$$
	DECLARE
	BEGIN
		TRUNCATE TABLE search_results;

		INSERT INTO search_results (address_name, full_name, level_of_bill, make, condition, category_name)
		SELECT
			address_name,
			cl.full_name,
			CASE
				WHEN co.bill <= 20 THEN 'Low'
				WHEN co.bill <= 30 THEN 'Medium'
				ELSE 'High'
			END,
			ca.make,
			ca.condition,
			(SELECT name FROM categories WHERE id = ca.category_id) AS category_name
		FROM 
			clients AS cl
		JOIN
			courses AS co ON cl.id = co.client_id
		JOIN
			cars AS ca ON ca.id = co.car_id
		JOIN 
			addresses AS a ON a.id = co.from_address_id
		WHERE
			a.name = address_name
		ORDER BY
			ca.make,
			cl.full_name;
	END;
$$
LANGUAGE plpgsql;

CREATE TABLE search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);