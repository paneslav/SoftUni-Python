CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
AS
$$
	DECLARE
		cur CURSOR FOR
			SELECT
				ah.first_name,
				ah.last_name,
				SUM(a.balance) AS balance
			FROM
				account_holders AS ah
			JOIN
				accounts AS a ON a.account_holder_id = ah.id
			GROUP BY
				ah.id
			HAVING
        SUM(a.balance) > searched_balance
			ORDER BY
				ah.first_name,
				ah.last_name;

		rec RECORD;
	BEGIN
		OPEN cur;
			LOOP
				FETCH cur INTO rec;
				EXIT WHEN NOT FOUND;
				RAISE NOTICE '% % - %', rec.first_name, rec.last_name, SUM(rec.balance);
			END LOOP;
		CLOSE cur;
	END;
$$
LANGUAGE plpgsql;

CALL sp_retrieving_holders_with_balance_higher_than(200000)