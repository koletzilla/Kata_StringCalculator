# StringCalculator kata
[![Build Status](https://travis-ci.org/koletzilla/Kata_StringCalculator.svg)](https://travis-ci.org/koletzilla/Kata_StringCalculator) [![Coverage Status](https://coveralls.io/repos/koletzilla/Kata_StringCalculator/badge.svg?branch=master&service=github)](https://coveralls.io/github/koletzilla/Kata_StringCalculator?branch=master)

Example of the String Calculator made in python after the Kata TDD from @pedro_g_s and @davideme at Codeweek Cáceres.

- [Link to @pedro_g_s's code](http://https://github.com/pedrovgs/StringCalculator-Kata)
- [More info about the cata at Roy Osherove's blog](http://osherove.com/tdd-kata-1/)

## Introducction

The following is a TDD Kata, an exercise in coding, refactoring and test-first.

## Before you start:
- Try not to read ahead.
- Do one task at a time. The trick is to learn to work incrementally.
- Make sure you only test for correct inputs. there is no need to test for invalid inputs for this kata

## String Calculator

1. Create a simple String calculator with a method int Add(string numbers)
	1. The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example “” or “1” or “1,2”
	2. Start with the simplest test case of an empty string and move to 1 and two numbers
	3. Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
	4. Remember to refactor after each passing test
2. Allow the Add method to handle an unknown amount of numbers
3. Allow the Add method to handle new lines between numbers (instead of commas).
	1. The following input is ok:  “1\n2,3”  (will equal 6)
	2. The following input is NOT ok:  “1,\n” (not need to prove it - just clarifying)
4. **Support different delimiters**
	1. to change a delimiter, the beginning of the string will contain a separate line that looks like this:   “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
	2. the first line is optional. all existing scenarios should still be supported
5. Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was passed.if there are multiple negatives, show all of them in the exception message
    _ _ _
    **Stop here if you are a beginner**. Continue if you can finish the steps so far in less than 30 minutes.
    _ _ _
6. Numbers bigger than 1000 should be ignored, so adding 2 + 1001  = 2
7. Delimiters can be of any length with the following format:  `"//[delimiter]\n"` for example: `"//[***]\n1***2***3"` should return 6
8. Allow multiple delimiters like this:  `"//[delim1][delim2]\n"` for example `"//[*][%]\n1*2%3"` should return 6.
9. Make sure you can also handle multiple delimiters with length longer than one char

### Developed by

- Jose María Muñoz

### License

    Copyright 2015 Jose María Muñoz

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.