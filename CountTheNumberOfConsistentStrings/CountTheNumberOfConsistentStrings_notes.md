# **1684. Count the Number of Consistent Strings**

# Question

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.\
\
Difficulty: Easy
<br/>

# Example test cases
1. Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2

    Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
   
2. Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7

    Explanation: All strings are consistent.

3. Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4

    Explanation: Strings "cc", "acd", "ac", and "d" are consistent.


<br/>

# Constraints
- 1 <= words.length <= 104
- 1 <= allowed.length <= 26
- 1 <= words[i].length <= 10
- The characters in allowed are distinct.
- words[i] and allowed contain only lowercase English letters.

<br/>

# Solution
## Thought process:
1. Create a set containing the letters in allowed. This allows checking if a letter is in allowed in the future to be O(1).
2. Set number of consistent strings to be number of strings.(count)
3. Iterate through each word in words, if any letter in a word does not exist in set, count minus one, go on to check the next word.
<br/><br/>
- Time complexity: O(n*m) (n is length of array, m is length of string)
- Space complexity: O(allowed.length())
<br/><br/>

## Code:
```java
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
```