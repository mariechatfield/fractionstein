/**
 * Interface for Ingredient objects.
 * Each Ingredient has a String name and an amount which is represented as a Fraction object.
 */

interface IIngredient {

	/**
	 * @return the name of the ingredient
	 */
	String getName ();

	/**
	 * @return the denominator of the ingredient's amount, which is fixed
	 */
	int getDenominator ();

	/**
	 * @return the array of integers that can be selected as the numerator for the amount
	 */
	int[] getNumeratorRange ();

	/**
	 * @return a randomly generated Fraction, using the set denominator
	 * and a randomly selected numerator from the numerator range
	 */
	Fraction getFraction ();

	/**
	 * @param highest   create a new numerator range from 1 - highest
	 */
	void setNumeratorRange (int highest);


}
