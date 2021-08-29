SET max as 60
SET num as 1
SET sum as 0
FUNCTION Ops ()
	WHILE num is less than max
		IF num is completely divisible by 2 AND 3
			SET sum to (sum + num)
		ENDIF
		SET num to num+1
	ENDWHILE
	PRINT "The result is", sum