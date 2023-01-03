# Tests

This directory contains tests (doctest, unittest) for various functions, classes,
and methods contained in this the folder [0x07-python-test_driven_development](https://github.com/chee-zaram/alx-higher_level_programming/tree/main/0x07-python-test_driven_development).

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
