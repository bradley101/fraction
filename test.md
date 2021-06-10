# Doctest tests
To run these tests, just do `python -m doctest test.md`.

```
>>> from fraction import Fraction
>>> print(Fraction(2,5)+Fraction(1,5))
3/5
>>> a = Fraction(1, 2)
>>> b = Fraction(1, 4)
>>> print(a/b)
2/1
>>> print(Fraction(a, Fraction(b, Fraction(1, 8))))
1/4
>>> print(Fraction(2, a))
4/1
>>> print(Fraction(a, 2))
1/4

```