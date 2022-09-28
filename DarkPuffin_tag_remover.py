# I want to remove all tags in DarkPuffin audiobooks

import re
from pathlib import Path
import os

folder_path = '/Users/evgeniy/Movies/Youtube/Dark Puffin аудиокниги фантастика/return_extension'


def extension_back(file_name):
    os.rename(f'{folder_path}/{file_name}', f'{folder_path}/{file_name}.mp4')


def rename_files(renamed_rezult):
    for k, v in renamed_rezult.items():
        original_name = f'{folder_path}/{k}'
        new_name = f'{folder_path}/{v}.mp4'
        # print(f'ORIGINAL_NAME : {k} \n     NEW_NAME : {v}\n')
        os.rename(original_name, new_name)


def remove_tags_from_name(file_name):  # function to create new name
    # mask1 = r' [^А-Я]{1}[а-я]+'  # problem - save one letter words
    mask1 = r".+([А-Я]{1}[а-я,й]+)"
    return re.search(mask1, file_name).group()


def dict_with_new_and_old_names(file_name, renamed_rezult):  # create a dictionary with old and new names

    renamed_rezult[file_name] = remove_tags_from_name(file_name)
    return renamed_rezult


def take_file_names_from_folder():  #
    files = Path(folder_path).iterdir()
    renamed_rezult = {}
    for file in files:
        file_name = Path(file).name
        if re.search(r'\.mp4', file_name) is not None:
            dict_with_new_and_old_names(file_name, renamed_rezult)
        else:
            print(file_name)
            extension_back(file_name)

    for k, v in renamed_rezult.items():
        # if len(k) != len(v):
        print(f'ORIGINAL_NAME : {k} \n     NEW_NAME : {v}\n')
    rename_files(renamed_rezult)


take_file_names_from_folder()

# print(f'ORIGINAL_NAME : {file_name} \n     NEW_NAME : {remove_tags_from_name(file_name)}\n' )
