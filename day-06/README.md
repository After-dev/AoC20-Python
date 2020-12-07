# Day 6: Custom Customs
https://adventofcode.com/2020/day/6

## Part 1
https://adventofcode.com/2020/day/6#part1

### Description
As your flight approaches the regional airport where you'll switch to a much larger plane, [customs declaration forms](https://en.wikipedia.org/wiki/Customs_declaration) are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked `a` through `z`. All you need to do is identify the questions for which **anyone in your group** answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:
```
abcx
abcy
abcz
```

In this group, there are **`6`** questions to which anyone answered "yes": `a`, `b`, `c`, `x`, `y`, and `z`. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:
```
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

* The first group contains one person who answered "yes" to **`3`** questions: `a`, `b`, and `c`.
* The second group contains three people; combined, they answered "yes" to **`3`** questions: `a`, `b`, and `c`.
* The third group contains two people; combined, they answered "yes" to **`3`** questions: `a`, `b`, and `c`.
* The fourth group contains four people; combined, they answered "yes" to only **`1`** question, `a`.
* The last group contains one person who answered "yes" to only **`1`** question, `b`.

In this example, the sum of these counts is `3 + 3 + 3 + 1 + 1` = **`11`**.

For each group, count the number of questions to which anyone answered "yes". **What is the sum of those counts?**

### Solution
To solve this problem, we count distinct answered questions for each group and sum them.

Result for my input data is: `6903`


## Part 2
https://adventofcode.com/2020/day/6#part2

### Description
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which **anyone** answered "yes"; you need to identify the questions to which **everyone** answered "yes"!

Using the same example as above:
```
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

* In the first group, everyone (all 1 person) answered "yes" to **`3`** questions: `a`, `b`, and `c`.
* In the second group, there is **no** question to which everyone answered "yes".
* In the third group, everyone answered yes to only **`1`** question, `a`. Since some people did not answer "yes" to `b` or `c`, they don't count.
* In the fourth group, everyone answered yes to only **`1`** question, `a`.
* In the fifth group, everyone (all 1 person) answered "yes" to **`1`** question, `b`.

In this example, the sum of these counts is `3 + 0 + 1 + 1 + 1` = **`6`**.

For each group, count the number of questions to which **everyone** answered "yes". **What is the sum of those counts?**

### Solution
To solve this part, we split each group and compare questions from passenger 1 (only this person of each group because we are searching common answers to all passengers of the group. If some question is not in passenger 1, is not common to all passengers of the group):
* Count number of occurrences of each questions in the group. If a question has a number of occurrences equal to number of passengers of the group, that question is common.
* Other case, is not a common question.

Result for my input data is: `3493`