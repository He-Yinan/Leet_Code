import java.util.*;

class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        Set<Character> set = new HashSet<Character>();
        
        // put every letter in allowed into set.
        for(int i = 0; i < allowed.length(); i++) {
            set.add(allowed.charAt(i));
        }
        
        // initialize count to number of words
        int count = words.length;
        
        for(int i = 0; i < words.length; i++) {
            for(int j = 0; j < words[i].length(); j++) {
                // minus one if word exist one letter that is not in set
                if(!set.contains(words[i].charAt(j))) {
                    count -= 1;
                    break;
                }
            }
        }
        return count;
    }
}