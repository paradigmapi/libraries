---
title: Python API Library
description: A Python Library to query to query ParadigmAPI
---

# Requirements

> pandas (only if needed)

## Setting Up

To use the library, simply clone this repo (or copy the file) into your working directory. If no API key is specified, the freekey is used.

```python
from paradigmAPI import ParadigmAPI
pAPI = ParadigmAPI()
# or to use your own API key
pAPI = ParadigmAPI('YOUR_API_KEY')
```

## Methods

Currently there are two methods: `query` and `paginate`.

### Query

`paradigmAPI.query` is a simple method to query any Paradigm method. 

#### Arguments

- *method*: The name of the method. All methods are listed on the (documentation)[https://docs.paradigmapi.com]
- args: A dictionary of parameters. All parameters are listed per method on the (documentation)[https://docs.paradigmapi.com]
- df: A boolean value to convert the output to a Pandas DataFrame. If ignored, the function will return a JSON object.

#### Examples

```python
out = pAPI.query('api-status')
out = pAPI.query('his-ohlcv-day', {'symbol': 'BTC'})
```


### Paginate

`paradigmAPI.paginate` is a simple method to paginate through any historical Paradigm method. Examples include `ta-his-day`, `ohlcv-his-day`.
**Note**: Be careful with the pagination window. If the number of requests exceeds your current quota, the data will not be returned.

#### Arguments

- *method*: The name of the method. All methods are listed on the (documentation)[https://docs.paradigmapi.com]
- *start*: The start date of the pagination. Format is `YYYY-mm-dd` (2019-01-01)
- *end*: The end date of the pagination. Format is `YYYY-mm-dd` (2019-01-01)
- args: A dictionary of parameters. All parameters are listed per method on the (documentation)[https://docs.paradigmapi.com]
- df: A boolean value to convert the output to a Pandas DataFrame. If ignored, the function will return a JSON object.

#### Examples

```python
out = pAPI.paginate('his-ohlcv-day', '2018-01-01', '2019-01-01', {'symbol': 'BTC'})
```
