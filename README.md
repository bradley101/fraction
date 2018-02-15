## fraction
fraction is a _Python_ module that is designed for fractional values **_numerator/denominator_**

### Installation
Easy to install
```
$ sudo pip install Fraction
```
### Usage
```
>>> from fraction.Fraction import Fraction

# Creates a fraction equal to 0/1
>>> def_fraction = Fraction()

# Creates a fraction equal to 3/10
>>> a = Fraction(3, 10)

# Get numerator/denominator
>>> a.numerator, a.denominator
(3, 10)

# Computes reciprocal of fraction as Fraction object
>>> recip_a = Fraction.reciprocal(a)
>>> recip_a.numerator, recip_a.denominator
(10, 3)

# Perform addition of Fraction objects (returns a Fraction object)
>>> b = Fraction(1, 2)
>>> sum_ab = a + b
>>> sum_ab.numerator, sum_ab.denominator
(4, 5)

# Perform subtraction of Fraction objects (returns a Fraction object)
>>> b = Fraction(1, 2)
>>> diff_ab = a - b
>>> diff_ab.numerator, diff_ab.denominator
(-1, 5)

# Perform multiplication of Fraction objects (returns a Fraction object)
>>> b = Fraction(1, 2)
>>> mul_ab = a * b
>>> mul_ab.numerator, mul_ab.denominator
(3, 20)

# Perform div of Fraction objects (returns a Fraction object)
>>> b = Fraction(1, 2)
>>> div_ab = a / b
>>> div_ab.numerator, div_ab.denominator
(3, 5)
```
