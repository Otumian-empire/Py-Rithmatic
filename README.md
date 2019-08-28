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
        returns `0` when first_number and second_number is not given
        By defaultfirst_number and second_number are `0`

1. **multi:** function: multi
		argument: iterable_arg: [int, float]
		use: multi([1,2,3,4,5])
		description: returns the product of elements in the iterable_arg.
        By default iterable_arg is an empty list
        returns `1` when the iterable_arg is empty

1. **div:** function: div
		arguments: first_number:[int, float], second_number:[int, float]
		use: div(1, 2.1)
		description: returns a float when second_number divides first_number
        returns `0` when first_number and second_number is not given
		By default, first_number = 0 and second_number = 1 (to prevent ZeroDivisionError)

1. **div_floor:**  function: div_floor
		arguments: first_number:[int, float], second_number:[int, float]
		use: div_floor(1, 2.1)
		description: returns the quotient (int) when second_number divides first_number
        returns `0` when first_number and second_number is not given
		By default, first_number = 0 and second_number = 1 (to prevent ZeroDivisionError)

1. **mod:** function: mod
		arguments: first_number:[int, float], second_number:[int, float]
		use: mod(1, 2.1)
		description: returns a remainder when second_number divides first_number
        returns `0` when first_number and second_number is not given
		By default, first_number = 0 and second_number = 1 (to prevent ZeroDivisionError)

1. **div_mod:** function: div_mod
		arguments: first_number:[int, float], second_number:[int, float]
		use: div_mod(1, 2.1)
		description: returns a tuple of the quotient and  remainder when second_number divides first_number
        returns `0` when first_number and second_number is not given
		By default, first_number = 0 and second_number = 1 (to prevent ZeroDivisionError)

1. **pow:** function: pow
		arguments: first_number:[int, float], second_number:[int, float]
		use: pow(1, 2.1)
		description: returns first_number raised to the exponent, second_number
		By default, first_number = 1 and second_number = 0
		returns `1` when first_number and second_number is not given