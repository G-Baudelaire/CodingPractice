public class Solution7 {
  private String MAXIMUM_POSITIVE = "2147483647";
  private String MAXIMUM_NEGATIVE = "2147483648";

  public int reverse(int x) {
    String reversedX = getReversedAbsoluteValue(x);
    String comparison = (x < 0) ? MAXIMUM_NEGATIVE : MAXIMUM_POSITIVE;

    if (isLessThanOrEqualTo(reversedX, comparison)) {
      return (x < 0) ? Integer.valueOf("-" + reversedX) : Integer.valueOf(reversedX);
    } else {
      return 0;
    }
  }

  private String getReversedAbsoluteValue(int x) {
    String stringOfX = String.valueOf(x);

    if (x < 0) {
      stringOfX = stringOfX.substring(1);
    }

    return new StringBuilder(stringOfX).reverse().toString();
  }

  private boolean isLessThanOrEqualTo(String leftValue, String rightValue) {
    if (leftValue.length() < rightValue.length()) {
      return true;
    }

    for (int i = 0; i < rightValue.length(); i++) {
      int rightDigit = Integer.valueOf(rightValue.charAt(i));
      int leftDigit = Integer.valueOf(leftValue.charAt(i));

      if (leftDigit > rightDigit) {
        return false;
      } else if (leftDigit < rightDigit) {
        return true;
      }
    }
    return true;
  }
}
