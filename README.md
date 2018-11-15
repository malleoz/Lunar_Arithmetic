# Lunar_Arithmetic

Let's be honest, sometimes arithmetic is annoying. Having to carry numbers when you add? Oh, please. That's why I looked into a better form of arithmetic called Lunar Arithmetic!

Formally called Dismal Arithmetic, which is a pun on decimal, Lunar Arithmetic is incorporates different rules for adding and multiplying numbers. Oh, and you're not allowed to subtract or divide numbers. When adding the digits of two numbers, the sum is the larger of the two numbers while when multiplying two numbers, the product is the smaller of the two. Multiplying large numbers can get a little confusing, but you essentially multiply one digit of a number against all the digits of the other number, repeat that for each remaining digit from the first number, and then use Lunar addition to add together all those results and obtain the product of the two numbers. This fictionary arithmetic introduces some pretty bizarre number patterns.

The list of even numbers, 2 x n, is: 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 10, 11, 12, 12, 12, 12, 12, 12, 12, 12, 20, 21, 22, 22, ...

The list of squares, n x n, is: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 111, 112, 113, 114, 115, 116, 117, 118, 119, 200, ...

The list of a repeated sum, 0 + 1 + 2 + ... + n, is: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 29, 29, ...

The list of factorials, 1 x 2 x ... x n, is: 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 110, 1110, 11110, 1111110, 11111110, 111111110, ...

For more information, read the paper for Dismal Arithmetic here: https://cs.uwaterloo.ca/journals/JIS/VOL14/Sloane/carry2.pdf

Alternatively, you can watch this video that walks through the basis of how Lunar Arithmetic works: https://www.youtube.com/watch?v=cZkGeR9CWbk

I haven't seen any sort of program that made a calculator for this clearly superior form of arithmetic, so I decided to make it in Python. Within LunarArithmetic.py I have an addition function and a multiplication function that follow the rules of Lunar Arithmetic. You can use SolveExpressions.py to input an expression (But remember, only addition or multiplication exists!). With ListOfSquares.py you can generate a list of squares.
