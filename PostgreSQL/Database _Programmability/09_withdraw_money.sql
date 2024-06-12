CREATE OR REPLACE PROCEDURE sp_withdraw_money(account_id INT, money_amount NUMERIC(4))
AS
$$
	DECLARE
		current_balance NUMERIC := (SELECT balance FROM accounts WHERE id = account_id);
	BEGIN

		IF money_amount > current_balance THEN
			RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
			RETURN;
		END IF;
	
		UPDATE accounts
		SET balance = balance - money_amount
		WHERE id = account_id;
	END;
$$
LANGUAGE plpgsql;