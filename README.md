# Immersed Sounds App

## Instructions

1. The tools takes two kind of inputs only
    a. txt files - (requirements.txt for pip) [make sure all the requirements.txt are uniquely labelled]
    b. json files - (package.json for npm)
2. Check in requirements.txt if there are any invalid naming conventions
3. The output file will contain the SOUP List once you run the tool
4. Please clear the files that are given in inputs and outputs folder if you are planning to use these folders itself. The old results are kept as it is to give you a sense of how the inputs and the outputs can be expected.

## Working

- The tool takes the all requirements and combines them in one and sorts them by descending order and the latest packages are selected in the case of pip
- The tool checks for the npm packages directly
- The tool installs the pip packages as I couldn't find any proper way of checking the package details directly.

## Warning

The tool is reflecting what it receives from the internet. It would be prudent to check the outputs once and deem if it is fit to be used in documentation. If discrepancies are found, please see if you can manually edit those.

## Running tool in linux

### Checkout the repository and launch VSCode
    % git clone git@github.com:NeuralAnalytics/Cloud_Testing.git

    % git checkout vivek/venus/all/tests

    % cd Cloud_Testing/tools/automation/soup_list

    % code .

### Setup python virtual environment
    % virtualenv .venv -p /usr/bin/python3.8

### Activate it
Open hello.py in the edit window
Select python interpreter as .venv/bin/python
Launch a terminal and ensure the command prompt has (.venv)

### Install python libraries
    % make python_setup
    % make vs_code_setup

### Run Tool in Linux
    % make soup_list

## Running tool in windows

Not supported yet!