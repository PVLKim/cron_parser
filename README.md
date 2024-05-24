Cron Expression Parser
========================
This is the simple cron expression parsing program that expands each of the cron fields and displays their possible values. 

Supported fields, value ranges and supported special characters are described in the following table: 

| Field       	| Allowed Values 	| Allowed Special Characters 	|
|--------------	|----------------	|----------------------------	|
| minute       	| 0-59           	| ,-*/                       	|
| hour         	| 0-23           	| ,-*/                       	|
| day of month 	| 1-31           	| ,-*/                       	|
| month        	| 1-12           	| ,-*/                       	|
| day of week  	| 1-7            	| ,-*/                       	|

Currently, the output from parsed cron fields is produced independently from other cron fields' outputs. This means, the parser does not consider special cases when other fields constrain the field in question. For example, if the expression for `day of month` is `*`, but value for `month` is `2`, the parser will still produce output with full range of days from 1-31 inclusive.

## Project structure
```shell
├── LICENSE
├── README.md
├── pdm.lock
├── pyproject.toml
├── src
│   └── cron_parser
│       ├── __init__.py
│       ├── cli.py
│       ├── constants.py
│       ├── cron_expression.py
│       ├── cron_field.py
│       └── exceptions.py
└── tests
    └── test_cron_parser.py
```

---------------

## System Requirements

* Python >= 3.11
* `pdm` Package and dependency manager

## Installation (tested on Debian GNU/Linux 12 with pre-installed Python 3.11)

1. Install PDM:
   
   ```shell
    curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
    ```
    The command `pdm` might still be unavailable, so after the above command, please follow the post-install instruction to add your installed path to PATH by adding the specified line to `.bashrc`, `.profile` or `.bash_profile`. For example, on Debian GNU/Linux 12 it can be adding `export PATH=/root/.local/bin:$PATH` line to one of the files and then executing `source .bashrc`. 
    <br><br>
    Alternatively, you can install with `pip`:
    ```shell
    pip install pdm
    ```
2. Install dependencies from the project. <br>
    From the root of the project folder, execute:
    ```shell
    python -m pip install .
    ```

## Usage

1. Run application:
   ```shell
   cron-parser "*/15 0 1,15 * 1-5 /usr/bin/find"
   ```

   In case the command isn't registered, the alternative commands should also work:
   ```shell
   pdm cron-parser "*/15 0 1,15 * 1-5 /usr/bin/find"
   ```
   or
   ```shell
   pdm run cron-parser "*/15 0 1,15 * 1-5 /usr/bin/find"
   ```

   This should produce the following output:
   ```
   minute        0 15 30 45
   hour          0
   day of month  1 15
   month         1 2 3 4 5 6 7 8 9 10 11 12
   day of week   1 2 3 4 5
   command       /usr/bin/find
   ```
2. To run unit tests (`pytest`):
   ```shell
   pdm unit-test
   ```