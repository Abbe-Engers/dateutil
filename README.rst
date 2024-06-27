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

<Show the coverage results provided by the existing tool with a screenshot>

### Your own coverage tool

<The following is supposed to be repeated for each group member>

Zakaria Hader
ParserError._str_()

    ttinfo.__repr_()

<Group member name>

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
