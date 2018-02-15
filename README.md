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

