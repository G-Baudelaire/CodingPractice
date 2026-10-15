import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class Solution20 {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mapping = Map.of('(', ')', '[', ']', '{', '}');

        for (int i = 0; i < s.length(); i++) {
            char character = s.charAt(i);
            if (character == '(' || character == '[' || character == '{') {
                stack.push(character);
            } else {
                if (stack.isEmpty() || (mapping.get(stack.pop()) != character)) return false;
            }
        }

        return stack.isEmpty();
    }
}
