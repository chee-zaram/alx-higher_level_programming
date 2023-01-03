# Python - Test-Driven Development (TDD)

---

This project aims to build industry best-practices with regards to writing efficient
code that remains maintainable and less error-prone, by performing quality checks on
different segments of codes, to ensure that a given program works as intended.

#### Running tests

You could clone the entire repository and navigate to the root of the TDD directory,
but if you have Subversion installed, you could run the following commands:

```shell
svn export https://github.com/chee-zaram/alx-higher_level_programming/trunk/0x07-python-test_driven_development chee-zaram-tdd
cd chee-zaram-tdd
```

To run a test, use the following command:

```shell
python3 -m doctest -v test/test-file.txt
```

where `test-file.txt` is any of the `.txt` files which tests for a module present
at the root of the TDD.
