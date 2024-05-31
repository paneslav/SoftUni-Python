ALTER TABLE countries
ADD COLUMN capital_code char(2);
UPDATE countries
SET capital_code = LEFT(capital, 2)
RETURNING *;