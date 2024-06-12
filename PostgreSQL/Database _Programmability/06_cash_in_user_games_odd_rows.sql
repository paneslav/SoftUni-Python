CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE(
	total_cash NUMERIC
) AS
$$
	BEGIN
		RETURN QUERY (
	    SELECT
	      SUM(TRUNC(cash, 2))
      FROM
        (SELECT
	        game_id,
	        cash,
	        ROW_NUMBER() OVER(PARTITION BY game_id ORDER BY cash DESC) AS row_num
        FROM 
	        users_games
        WHERE
	        game_id = (SELECT id FROM games WHERE name = game_name)
        ) AS row_ranked
      WHERE
	      row_num % 2 <> 0
      GROUP BY
	      game_id
);
	END;
$$
LANGUAGE plpgsql;