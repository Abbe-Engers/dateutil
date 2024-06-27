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


<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

Zakaria Hader

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
