CREATE OR REPLACE FUNCTION fn_is_word_comprised(set_of_letters VARCHAR(50), word VARCHAR(50))
RETURNS BOOLEAN AS
$$
	DECLARE

		word_len INT := LENGTH(word);
		current_char CHAR;
		counter INT := 1;
		word_to_lower VARCHAR(50) := lower(word);
		set_to_lower VARCHAR(50) := lower(set_of_letters);

	BEGIN

		WHILE counter <= word_len LOOP
			current_char := SUBSTRING(word_to_lower, counter, 1);

			IF POSITION(current_char IN set_to_lower) = 0 THEN
				RETURN FALSE;
			END IF;

			counter := counter + 1;

		END LOOP;

		RETURN TRUE;
	END;
$$
LANGUAGE plpgsql;

_______________________________________________________________________________________________________________________________________________

CREATE OR REPLACE FUNCTION fn_is_word_comprised (
	set_of_letters VARCHAR(50),
	word VARCHAR(50)
) RETURNS BOOLEAN
AS 
$$
BEGIN
	RETURN TRIM(LOWER(word), LOWER(set_of_letters)) = ''; --delete characters from word that are found in set_of_letters and compare to empty string
END;
$$
LANGUAGE plpgsql;