# Python scripts :snake: :

- Small set of scripts written in Python to automate some of the linux commands (Hopefully :grin:)
- Totally flexible and easy to understand

# About scripts:
## mongo_json_collection.py
- It will take folder containing JSON files as input and will automatically create and populate that collection in mongodb compass.
- It uses ```mongoimport``` command to populate data which do not preserve some data types correctly.
- :warning: Do not use with production database. Due to limitation of ```mongoimport``` some data may throw errors while restoring.
