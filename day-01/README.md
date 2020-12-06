# Day 1: Report Repair
https://adventofcode.com/2020/day/1

## Part 1
https://adventofcode.com/2020/day/1#part1

### Description
After saving Christmas [five years in a row](https://adventofcode.com/events), you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them **stars**. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all **fifty stars** by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

Before you leave, the Elves in accounting just need you to fix your **expense report** (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to **find the two entries that sum to 2020** and then multiply those two numbers together.

For example, suppose your expense report contained the following:
```
1721
979
366
299
675
1456
```

In this list, the two entries that sum to `2020` are `1721` and `299`. Multiplying them together produces `1721 * 299 = 514579`, so the correct answer is **`514579`**.

Of course, your expense report is much larger. **Find the two entries that sum to 2020; what do you get if you multiply them together?**

### Solution
To solve this problem, we are going to use two pointers as follows:

```
n1, n2, n3, n4, n5, ...
^   ^
1   2
```

Pointers always are initialized as follows:
* `pointer 1`: position **`0`**.
* `pointer 2`: next position of `pointer 1`.

In each step, their values are compared as follows:
* If both sum 2020: Return their product. **Solution!!!**
* Other case: If current position of `pointer 2` is the last, move the `pointer 1` one position and initialize `pointer 2` at the right position of `pointer 1`. In other case, move `pointer 2` one position.

Let's try example step by step:
* Step 1: Both nums sums `1721+979=2700` != `2020`. Move `pointer 2` to next position.
```
1721, 979, 366, 299, 675, 1456
^     ^
1     2
```

* Step 2: Both nums sums `1721+366=2087` != `2020`. Move `pointer 2` to next position.
```
1721, 979, 366, 299, 675, 1456
^          ^
1          2
```

* Step 3: Both nums sums `1721+299=2020` == `2020`. **Solution!!!**
```
1721, 979, 366, 299, 675, 1456
^               ^
1               2
```

Finally: Return 1721 * 299 = **`514579`**

Result for my input data is: `270144`


## Part 2
https://adventofcode.com/2020/day/1#part2

### Description
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find **three** numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to `2020` are `979`, `366`, and `675`. Multiplying them together produces the answer, **`241861950`**.

In your expense report, **what is the product of the three entries that sum to `2020`?**

### Solution
To solve this part, we are going to use three pointers as follows:
```
n1, n2, n3, n4, n5, ...
^   ^   ^
1   2   3
``` 

Pointers always are initialized as follows:
* `pointer 1`: position **`0`**.
* `pointer 2`: next position of `pointer 1`.
* `pointer 3`: next position of `pointer 2`.

In each step, their values are compared as follows:
* If values from pointers 1 and 2 sum more than 2020, move `pointer 3` one position. If `pointer 3` is in the last position, move `pointer 2` and initialize `pointer 3`. If both pointers are at last two positions, move `pointer 1` one position and initialize `pointer 2` and `pointer 3`.
* If values from pointers 1 and 2 sum less than 2020, continue by adding value from `pointer 3`.
* If final value is 2020: Return their product. **Solution!!!**
* Other case: Move `pointer 3` one position. If `pointer 3` is in the last position, move `pointer 2` and initialize `pointer 3`. If both pointers are at last two positions, move `pointer 1` one position and initialize `pointer 2` and `pointer 3`.

Let's try example step by step:
* Step 1: Nums from `pointer 1` and `pointer 2` sum `1721+979=2700` > `2020`. Move `pointer 2` to next position and initialize `pointer 3`.
```
1721, 979, 366, 299, 675, 1456
^     ^    ^
1     2    3
```

* Step 2: Nums from `pointer 1` and `pointer 2` sum `1721+366=2087` > `2020`. Move `pointer 2` to next position and initialize `pointer 3`.
```
1721, 979, 366, 299, 675, 1456
^          ^    ^
1          2    3
```

* Step 3: Nums from `pointer 1` and `pointer 2` sum `1721+299=2020` == `2020`. Move `pointer 2` to next position and initialize `pointer 3`.
```
1721, 979, 366, 299, 675, 1456
^               ^    ^
1               2    3
```

* Step 4: Nums from `pointer 1` and `pointer 2` sum `1721+675=2396` > `2020`. `pointer 2` and `pointer 3` are at last two positions, so `pointer 1` is moved one position and `pointer 2` and `pointer 3` are initialized.
```
1721, 979, 366, 299, 675, 1456
^                    ^    ^
1                    2    3
```

* Step 5: Nums from `pointer 1` and `pointer 2` sum `979+366=1345` < `2020`. `1345+299=1644` != 2020. Move `pointer 3` to next position.
```
1721, 979, 366, 299, 675, 1456
      ^    ^    ^
      1    2    3
```

* Step 6: Nums from `pointer 1` and `pointer 2` sum `979+366=1345` < `2020`. `1345+675=2020` == 2020. **Solution!!!**
```
1721, 979, 366, 299, 675, 1456
      ^    ^         ^
      1    2         3
```

Finally: Return 979 * 366 * 675 = **`241861950`**

Result for my input data is: `261342720`
