# Analysis

## Summary

## Set up

First, set up a docker container running postgres.

Then, from `/analysis`:

```
python3 -m venv venv
pip install -r requirements.txt
python3 create_db.py
```

## Running analysis

From `/analysis`:
```
python3 run_analysis.py
```
