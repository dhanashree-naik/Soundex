# Soundex
## Background: 
The Soundex algorithm is a phonetic algorithm commonly used by libraries and the Census Bureau to represent people’s names as they
are pronounced in English. It has the advantage that name variations with minor spelling differences will map to the same representation, as long as they have the same pronunciation in English. Here is how the algorithm works:

Step 1: Retain the first letter of the name. This may be uppercased or lowercased.

Step 2: Remove all non-initial occurrences of the following letters: a, e, h, i, o, u, w, y. (To clarify, this step removes all occurrences of the given characters except when they occur in the first position.)

Step 3: Replace the remaining letters (except the first) with numbers:
• b, f, p, v → 1
• c, g, j, k, q, s, x, z → 2
• d, t → 3
• l → 4
• m, n → 5
• r → 6
If two or more letters from the same number group were adjacent in the original name (i.e. before any letter removal is done), then only replace the first of those letters with the corresponding number and ignore the others.

Step 4: If there are more than 3 digits in the resulting output, then drop the extra ones. 

Step 5: If there are less than 3 digits, then pad at the end with the required
number of trailing zeros.The final output of applying Soundex algorithm to any input string should be of the form Letter Digit Digit Digit. Table shows the out-put of the Soundex algorithm for some example names.
                                                Input        Output
                                                Jurafsky     J612
                                                Jarovski     J612
                                                Resnik       R252
                                                Reznick      R252
                                                Euler        E460
                                                Peterson     P362

Three transducers are implemented using FST code provided by the Professor:
1. Transducer 1: Performs steps 1-3 of the algorithm, i.e, retaining the first letter, removing letters and replacing letters with numbers.
2. Transducer 2: Performs step 4 of the algorithm, i.e., truncating extra digits.
3. Transducer 3: Performs step 5 of the algorithm, i.e., padding with zeros if required.
