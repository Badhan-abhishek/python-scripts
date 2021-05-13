# Python scripts :snake: :

- Small set of scripts written in Python to automate some of the linux commands (Hopefully :grin:)
- Totally flexible and easy to understand

# About scripts:
## 1 mongo_json_collection.py
- It will take path of folder containing JSON files as input and will automatically create and populate that collection in mongodb compass.
- It uses ```mongoimport``` command to populate data which do not preserve some data types correctly.
- :warning: Do not use with production database. Due to limitations of ```mongoimport``` some data may throw errors while restoring.

## 2 mongo_json_collection.py
- It will take path of folder containing pdf/docx/jpg etc files and will convert them to JSON-like format.
- Format of result will be: 
`
{
    title: 'Title of file the file',
    path: 'original name of file for path'
}
`
- example:
    - file: random_file.pdf
    - result: 
        `{
            title: 'random file',
            path: 'random_file.pdf'
        }` 
- Limitations:
    - Currently it will only identify "_" as seperator.