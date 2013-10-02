/**
 * Abstract class for Ingredient objects.
 * Each Ingredient has a String name and an amount which is represented as a Fraction object.
 */

import java.util.Random;

public abstract class AIngredient implements IIngredient {

	/**
	 * The name of the ingredient.
	 */
	private String name;

	/**
	 * The denominator of the ingredient's amount; does not change.
	 */
	private int denominator;

	/**
	 * The range of integers from which a numerator for the ingredient's amount
	 * may be chosen.
	 */
	private int[] numeratorRange;

	/**
	 * Constructor that creates a new AIngredient object that can have any
	 * amount x/n, 1 <= x <= n, for a given denominator n.
	 *
	 * @param inName	the name of the ingredient
	 * @param inDenom	the denominator of the ingredient's amount
	 */
	public AIngredient(String inName, int inDenom) {
		name = inName;
		denominator = inDenom;
		setNumeratorRange(denominator);
	}

	/**
	 * Constructor that creates a new AIngredient object that can have any
	 * amount x/n, 1 <= x <= m, for a given denominator n and numerator limit m.
	 *
	 * @param inName	the name of the ingredient
	 * @param inDenom	the denominator of the ingredients' amount
	 * @param highest	the highest numerator the ingredient's amount can have
	 */
	public AIngredient(String inName, int inDenom, int highest) {
		name = inName;
		denominator = inDenom;
		setNumeratorRange(highest);
	}

	/* (non-Javadoc)
	 * @see IIngredient#getName()
	 */
	@Override
	public String getName() {
		return name;
	}

	/* (non-Javadoc)
	 * @see IIngredient#getDenominator()
	 */
	@Override
	public int getDenominator() {
		return denominator;
	}

	/* (non-Javadoc)
	 * @see IIngredient#getNumeratorRange()
	 */
	@Override
	public int[] getNumeratorRange() {
		return numeratorRange;
	}

	/* (non-Javadoc)
	 * @see IIngredient#getFraction()
	 */
	@Override
	public Fraction getFraction() {
		Random rand = new Random ();
		int numerator = numeratorRange[rand.nextInt(numeratorRange.length)];
		return new Fraction (numerator, denominator);
	}

	/* (non-Javadoc)
	 * @see IIngredient#setNumeratorRange(int)
	 */
	@Override
	public void setNumeratorRange(int highest) {
		numeratorRange = new int[highest];
		for (int i = 1; i <= highest; i++) {
			numeratorRange[i - 1] = i;
		}
	}

}
