CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INT AS
$$
	DECLARE
	BEGIN
		RETURN (
		SELECT
			COUNT(*)
		FROM accounts AS a
		JOIN accounts_photos AS ap ON a.id = ap.account_id
		JOIN photos AS p ON p.id = ap.photo_id
		WHERE username = account_username
		);
	END;
$$
LANGUAGE plpgsql;