# RDict

## Overview

A dictionary collection for the purpose of learning foreign languages. Still under development, supports only the Oxford Dictionary.

## Planned features

1. Add support for other dictionaries
2. Improve the interface
3. Fix bugs and add features

## Installation

### Clone the repository

```shell
git clone https://github.com/ruangustavo/RDict.git
```

### Install the requirements

```shell
python -m pip install -r requirements.txt
```

## Usage

### Oxford Dictionary

1. Create a file `rdict/config.py` with the following content:
    - OXFORD_API_ID
    - OXFORD_API_KEY
2. Create an instance of the OxfordDictionary class in your code
3. Use the method `query` to get all the results for a given word
4. Use the method `show` to show the definition of a given word previously queried
