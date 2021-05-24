# Beautiful Strings

[![Build Status](https://travis-ci.com/HACKE-RC/beautifulstrings.svg?branch=master)](https://travis-ci.com/HACKE-RC/beautifulstrings)

Makes this possible (thanks to [forbiddenfruit](https://github.com/clarete/forbiddenfruit)):

```
>>> import beautifulstrings
>>> 'asdf'.bytes() # string to bytes.
b'asdf'
>>> b'asdf'.str() # bytes to string.
'asdf'
>>> 'asdf'.str() # for convenience, so you don't have to think about what data type an object was.
'asdf'
>>> b'asdf'.bytes() # for convenience, so you don't have to think about what data type an object was.
b'asdf'
>>> 'asdf'.hex() # string to hex
b'61736466'
>>> b'asdf'.hex() # python built-in
'61736466'
>>> b'asdf'.hex().unhex()
b'asdf'
>>> 'asdf'.hex().unhex()
b'asdf'
>>> 'asdf'.hex().unhex().str()
'asdf'
>>> 'asdf'.ascii() # ascii values of each value character in a string.
'97115100102'
>>> 'asdf'.ascii_list() # ascii values of each value character in a string as an integer list.
[97, 115, 100, 102]
```

## Why use BeautifulStrings?
Because it's the right thing to do and more convenient for any type of use.

## How does it work?
It uses a module called [forbiddenfruit](https://pypi.org/project/forbiddenfruit)