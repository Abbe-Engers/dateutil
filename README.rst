# Report for Assignment 1

## Installation

To install the package for coverage measurement, run the following command:

```bash
pip install python-dateutil
```

To install our own version of the package with our own coverage tool, run the following command in the root directory of the repository:

```bash
pip install -e .
```

## Project chosen

Name: dateutil

URL: https://github.com/dateutil/dateutil

Number of lines of code and the tool used to count it: 13.6 KLOC, counted using Lizard

Programming language: Python

## Coverage measurement

### Existing tool

We use the coverage.py library to measure the branch coverage, using the following command:
coverage run -m --branch pytest

Zakaria Hader
Function 1: ParserError._str_() in dateutil/parser/_parser.py, from 50% -> 100%
Function 2: ttinfo.__repr_() in ParserError.__str__, from 0% -> 100%

Amine el Alami
Function 1: tzrangebase.dst() in dateutil/tz/_common.py, from 80% -> 100%
Function 2: tzrangebase.__init__() in dateutil/tz/_common.py, from 0% -> 100%

Abbe Engers:
Function 1: tzrangebase._dst_base_offset() in dateutil/tz/_common.py, from 0% -> 100%
Function 2: tzrangebase.__repr__() in dateutil/tz/_common.py, from 0% -> 100%

Yasar Kocdas
Function 1: parser._parse() in dateutil/parser/_parser_hms, from 78% -> 100%
Function 2: rrulebase.__contains__() in dateutil/rrule.py, from 78% -> 100%

PER FUNCTIE NIEUWE SS, before & eind

### Overall

ZAKA SCREENSHOT
<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

Abbe and Amine:
File: dateutil/tz/_common.py
Methods Covered: tzrangebase._dst_base_offset, tzrangebase.__repr__, tzrangebase.dst, tzrangebase.__init__
Coverage Achieved: 0% to 100% for _dst_base_offset, __repr__, and __init__; 80% to 100% for dst
Summary: Abbe and Amine worked together to achieve full coverage these 4 functions in the tzrangebase class.

Zakaria:
Files and Methods:
dateutil/parser/_parser.py: ParserError.__str__ (50% to 100%)
dateutil/tz/tz.py: _ttinfo.__repr__ (0% to 100%)
Summary: Zakaria enhanced coverage for error handling and representation methods.

Yasar:
Files and Methods:
dateutil/parser/_parser_hms: parser._parse (78% to 100%)
dateutil/rrule.py: rrulebase.__contains__ (75% to 88%)
Summary: Yasar focused on increasing coverage for parsing and rule-based methods.