# Arithmatic Module
<span>an abstraction layer on the arithmatic operators</span>
## Class
1. Arithmatic
## Methods
1. add
1. subtr
1. multi
1. div
1. div_floor
1. mod
1. div_mod
1. pow
## Method Description
1. **add:** function: add
		argument: `iterable_arg: [int, float]`
		use: `add([1,2,3,4,5])`
		description: returns the sum of elements in the iterable_arg, this is similar to sum
        By default iterable_arg is an empty list
        returns `0` when empty iterable_arg

1. **subtr:** function: subtr
		arguments: first_number:[int, float], second_number:[int, float]
		use: subtr(1, 2.1)
		description: returns the difference between first_number and second_number
        By defaultfirst_number and second_number are `0`

1. **multi:** function: multi
		argument: iterable_arg: [int, float]
		use: multi([1,2,3,4,5])
		description: returns the product of elements in the iterable_arg.
        By default iterable_arg is an empty list
        returns `1` when the iterable_arg is empty