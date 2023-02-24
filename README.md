
by Omer Taitelman
----------------------------------------------------------------------------------------------


                                    PI Approximation  
                           ----------------------------------


About
---------------
as a part of "intro to probability" course, we encountred the following example:
the unit circle inscribed in a square (R = 1).
choose randomly a point in the square area.
the probability of a point to be in the circle area is PI/4.
that is because the ratio between the circle area and the square area (PI*1^2 / 4 = PI / 4).
define X as the number of points that in the circle from 'n' points chosen.
X is binomial distributed  ~(n, PI/4) and the expected value is n*PI/4.
lookin at P^ (the avrage) is X/n,
by the Law of large numbers P^ converges to its expected value which is (PI/4) when n is large.
so by calculating P^ and multiply it by 4 we get approximated PI value.

     ____________________
	|     .........     |
	|*  ..         .. * |
	| ..  *          .. |
	|.         *       .|
	|.                 .|
	|.            *    .|
	| ..             .. |
	|   ..         ..   |
	|_____........._____|


Remarks
-------
the approximation is limited by the randomness and the float accuracy.
	


