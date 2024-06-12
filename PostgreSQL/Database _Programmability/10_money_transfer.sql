CREATE OR REPLACE PROCEDURE sp_transfer_money(sender_id INT, receiver_id INT, amount NUMERIC(4))
AS
$$
	DECLARE
		v_error_message TEXT;
	BEGIN
		BEGIN
			CALL sp_withdraw_money(sender_id, amount);
			CALL sp_deposit_money(receiver_id, amount);
		EXCEPTION
			WHEN OTHERS THEN
			GET STACKED DIAGNOSTICS v_error_message = MESSAGE_TEXT;
			RAISE EXCEPTION 'Transfer failed: %', v_error_message;
		END;
	END;
$$
LANGUAGE plpgsql;