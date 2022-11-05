__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

parent_dir = os.path.abspath("files")
cache_path = os.path.join("files", "cache")
zip_path = os.path.join("files", "data.zip")
cache_abspath = os.path.abspath(cache_path)


def clean_cache():
    if os.path.exists(cache_path):
        for f in os.listdir(cache_path):
            os.remove(os.path.join(cache_path, f))
    else:
        directory = 'cache'
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)


def cache_zip(zip_path, cache_path):
    with ZipFile(zip_path, 'r') as zObject:
        zObject.extractall(
            path=cache_path)


def cached_files():
    return [os.path.join(cache_abspath, file)
            for file in os.listdir(cache_abspath)]


def find_password(file_list):
    word = 'password'
    for file_name in file_list:
        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                if word in f.read():
                    with open(file_name, 'r', encoding='utf-8') as f:
                        for line in f:
                            if word in line:
                                return line.strip().split(':')[1][1:]


def main():
    clean_cache()
    cache_zip(
        zip_path,
        cache_path
        )
    file_list = cached_files()
    password = find_password(file_list)
    print(password)


if __name__ == "__main__":
    main()
