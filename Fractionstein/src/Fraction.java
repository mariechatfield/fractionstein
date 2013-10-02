/**
 * This is a wrapper class for Fractions with a fixed denominator.
 */

public class Fraction {

	/**
	 * the numerator value of the fraction
	 */
	private int numerator;

	/**
	 * the denominator value of the fraction
	 */
	private int denominator;

	/**
	 * indicates if fraction is improper (i.e. greater than 1)
	 */
	private boolean isImproper;

	/**
	 * @param num      value of the numerator
	 * @param denom    value of the denominator
	 */
	public Fraction (int num, int denom) {
		numerator = num;
		denominator = denom;
		isImproper = numerator > denominator;
	}

	/**
	 * @param num      value of the numerator
	 */
	public void setNumerator (int num) {
		numerator = num;
		isImproper = numerator > denominator;
	}

	/**
	 * @return value of numerator
	 */
	public int getNumerator () {
		return numerator;
	}

	/**
	 * @return value of denominator
	 */
	public int getDenominator () {
		return denominator;
	}

	/**
	 * @return decimal value of the fraction
	 */
	public double getValue () {
		return numerator * 1.0 / denominator;
	}

	/**
	 * @return if fraction is improper
	 */
	public boolean isImproper () {
		return isImproper;
	}

}
