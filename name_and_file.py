import os

path = input('Please enter path of directory: ')

ext = input('Please enter extension of file without dot (.): ')

# List of all files in directory
file_names = os.listdir(path)

ext = f'.{ext}'

split_name = [f.split('_') for f in file_names]

title_with_ext = [(' ').join(f) for f in split_name]

remove_ext = [f.replace(ext, '') for f in title_with_ext]

# Convert to zip
get_dict = dict(zip(file_names, remove_ext))

# Print JSON-like response
for key in get_dict:
    print(f'''{{
    title: "{get_dict[key]}",
    path: "{key}"
    }},\n''')

