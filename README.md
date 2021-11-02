# fraction  [![Downloads](https://pepy.tech/badge/fraction/week)](https://pepy.tech/project/fraction)

fraction is a _Python_ module that is designed for fractional values **_numerator/denominator_**

### Installation
Easy to install
```
$ python -m pip install Fraction
```
### Usage
#### Import
```
>>> from fraction import Fraction
```
#### Initialization
##### Creates a fraction equal to 0/1
```
>>> f1 = Fraction()
```
##### Creates a fraction equal to (1/2) / (1/4)
```
>>> print(Fraction('1/2', '1/4'))
2/1
```
##### Create fraction objects from strings and decimals
```
>>> print(Fraction('1.2'))
6/5
>>> print(Fraction('1.22/6'))
61/300
```
##### Create fraction objects from recurring decimals
```
>>> f = Fraction.fromdecimal(1.3, rec='3')
>>> print(f)
4/3
>>> f = Fraction.fromdecimal(24.5067, rec='067')
>>> print(f)
122411/4995
```
##### Creates a fraction equal to 3/10
```
>>> a = Fraction('3/10')
>>> b = Fraction('1/2')

# Get numerator/denominator
>>> a.numerator, a.denominator
(3, 10)
```
### Arithmetic Operations
##### Computes reciprocal of fraction as Fraction object
```
>>> recip_a = Fraction.reciprocal(a)
>>> recip_a.numerator, recip_a.denominator
(10, 3)
```
##### Perform addition of Fraction objects (returns a Fraction object)
```
>>> sum_ab = a + b
>>> sum_ab.numerator, sum_ab.denominator
(4, 5)
```
##### Perform subtraction of Fraction objects (returns a Fraction object)
```
>>> diff_ab = a - b
>>> diff_ab.numerator, diff_ab.denominator
(-1, 5)
```
##### Perform multiplication of Fraction objects (returns a Fraction object)
```
>>> mul_ab = a * b
>>> mul_ab.numerator, mul_ab.denominator
(3, 20)
```
##### Perform div of Fraction objects (returns a Fraction object)
```
>>> div_ab = a / b
>>> div_ab.numerator, div_ab.denominator
(3, 5)
```
### Comparison/Relational operations
##### Supports comparison operations [<, <=, >, >=, ==, !=] (returns boolean)
```
>>> a < b
True
>>> a == Fraction(7, 10)
False
```
### Convert fraction into a float string
```
>>> a = Fraction('1/3')
>>> a.todecimal(decplaces=5)
'0.33333'
```
### For debugging 
##### Supports str() and repr() built in objects methods
```
>>> a = Fraction()
>>> print a
0/1
>>> a
Fraction: 0/1
```
