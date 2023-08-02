""" Garbadge sorter
Take one argument - folder for sotring.
It's moving files to folders:
images, documents, video, audio, archives

"""

from sys import argv
import os
import string


# Check folder for empty and delete
def isempty(folder: str):
    pass


# Rename file name from cyrillic to latin
def normalize(cyrillic_name: str) -> str:
    ext = cyrillic_name[cyrillic_name.find(".") + 1 :]
    cyrillic_name = cyrillic_name[: cyrillic_name.find(".")]
    name_out = ""
    # Convert cyrilic letters to latin, latin letters and
    # numbers remain as they are, other characters are replaced by the _ character
    for c in cyrillic_name:
        if c in string.ascii_letters or c in string.digits:
            name_out += c
        elif c in cyr_lat.keys() or c.lower() in cyr_lat.keys():
            if c.isupper():
                name_out += cyr_lat[c.lower()].upper()
            else:
                name_out += cyr_lat[c]
        else:
            name_out += "_"
    return name_out + "." + ext


# Sort and move files from current folder to destination
# If there are subfolders call himself for these folders
def sort_and_move(folder: str):
    pass


# Taking an argument from command line
# source_folder = argv[1]
source_folder = "w:\\Projects\\HW1\\Downloads"

# Cyrillic and latin
cyr_lat = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "j",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "shh",
    "ь": "",
    "ы": "y",
    "ъ": "",
    "э": "je",
    "ю": "ju",
    "я": "ja",
}

# Iniatializing variables
img = ["JPEG", "PNG", "JPG", "SVG"]
doc = ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"]
video = ["AVI", "MP4", "MOV", "MKV"]
audio = ["MP3", "OGG", "WAV", "AMR"]
archives = ["ZIP", "GZ", "TAR"]

# Destination folders
img_folder = source_folder + "images"
doc_folder = source_folder + "documents"
video_folder = source_folder + "video"
audio_folder = source_folder + "audio"
archives_folder = source_folder + "archives"

# Lists for known and unknown extentions
known_ext = set()
unknown_ext = set()

# print(normalize("Выхожу   odin (я) на дорогу&*!2.mp3"))
work_list = os.listdir(source_folder)
# for w in work_list:
#     print(w)


# os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
#  - переименовывает файл или директорию из src в ds
# os.listdir(path=".") - список файлов и директорий в папке.
# os.chdir(path) - смена текущей директории.
# os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.
# os.rmdir(path, *, dir_fd=None) - удаляет пустую директорию.os.system(command) -
# исполняет системную команду, возвращает код её завершения (в случае успеха 0)
# os.path.isdir(path) - проверка является ли путь директорией.
# os.path.isfile(path) - является ли путь файлом.
result = None
# if result.is
print(type(result))
