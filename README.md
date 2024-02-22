# airbyteTest

A short Python script which tests the Astra DB integration found in Airbyte's documentation: [Airbyte's Astra DB document store integration](https://docs.haystack.deepset.ai/v2.0/docs/astradocumentstore)

## requirements

Set the following environment variables:
```
export ASTRA_DB_APP_TOKEN=AstraCS:abcdefNOTREALghijk:lmnopqrsBLAHBLAHBLAHtuvwxyz
export ASTRA_DB_API_ENDPOINT=https://b9aff773-also-not-real.apps.astra.datastax.com
```

Install the following libraries:
```
pip install astrapy python-dotenv
```

## Execution
```
python airbyte_test.py
```