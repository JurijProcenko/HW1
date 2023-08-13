""" Garbadge sorter
Take one argument - folder for sorting.
He's sorting and moving files to folders:
images, documents, video, audio, archives

"""

from sys import argv
import os
from pathlib import Path
import string


# Rename file name from cyrillic to latin
def normalize(cyrillic_name: str) -> str:
    ext = cyrillic_name[cyrillic_name.rfind(".") + 1 :]
    cyrillic_name = cyrillic_name[: cyrillic_name.rfind(".")]
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


def rename_all_files():
    dest_folders.pop("unknown")
    for key in dest_folders:
        # home = Path(dest_folders[key]+'\\')
        os.chdir(dest_folders[key])
        for next_file in Path.cwd().glob("*.*"):
            name = str(next_file.name)
            next_file.replace(normalize(name))


def make_dir():
    for key in dest_folders:
        try:
            os.mkdir(dest_folders[key])
        except:
            pass


def make_heap():
    os.mkdir(dest_folders["unknown"])
    for next_file in home.rglob("*.*"):
        if next_file.is_file():
            name = next_file.name
            next_file = str(next_file)
            try:
                os.rename(next_file, dest_folders["unknown"] + "\\" + name)
            except:
                print(f"File {next_file} exists in destination folder")


def move_files():
    for key in extentions:
        for ext in extentions[key]:
            for next_file in home.glob(f"**/*.{ext}"):
                name = next_file.name
                next_file = str(next_file)
                known_ext.add(next_file[next_file.rfind(".") + 1 :].lower())
                try:
                    os.rename(next_file, dest_folders[key] + "\\" + name)
                except:
                    # os.remove(next_file)
                    print(f"File {next_file} exists in destination folder")


def find_unknown_ext():
    # Собираем неизвестные расширения в множество
    for next_file in Path(dest_folders["unknown"]).glob("*.*"):
        name = next_file.name
        ext = next_file.suffix
        next_file = str(next_file)
        if ext not in known_ext:
            unknown_ext.add(next_file[next_file.rfind(".") + 1 :].lower())


def remove_empty_folders():
    # for next_file in Path(source_folder).rglob("*"):
    #     if next_file.is_dir() and len(os.listdir(next_file)) == 0:
    #         next_file.rmdir()
    for root, dirs, files in os.walk(source_folder, topdown=False):
        for d in dirs:
            curpath = os.path.join(root, d)
            if not os.listdir(curpath):
                os.rmdir(curpath)


def unpack_archives():
    for next_file in Path(dest_folders["archives"]).glob("*.*"):
        name = str(next_file)
        dest = name[: name.rfind(".")] + "\\"
        os.mkdir(dest)
        zip_command = f"tar -xqzf {name} -C {dest}"
        try:
            os.system(zip_command)
        except:
            print(f"Something wrong with file {name}")
        next_file.unlink()


def main():
    make_heap()  # перемещаем все в кучу в папку unknown
    remove_empty_folders()  # Удаляем пустые папки
    make_dir()  # Создаем папки назначения
    move_files()  # Переносим файлы известных типов в папки назначения
    find_unknown_ext()  # Собираем неизвестные расширения
    rename_all_files()  # Переводим названия фалов в транслит
    unpack_archives()  # Распаковываем архивы
    print("Известные найденные расширения файлов: ", known_ext)
    print("Неизвестные найденные расширения файлов: ", unknown_ext)


if __name__ == "__main__":
    # Taking an argument from command line
    source_folder = argv[1]
    # source_folder = "w:\\Projects\\HW1\\1"
    home = Path(source_folder)

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

    # Destination folders
    dest_folders = {
        "image": source_folder + "\\images",
        "doc": source_folder + "\\documents",
        "video": source_folder + "\\video",
        "audio": source_folder + "\\audio",
        "archives": source_folder + "\\archives",
        "unknown": source_folder + "\\unknown",
    }
    extentions = {
        "image": ["JPEG", "PNG", "JPG", "SVG"],
        "doc": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX", "XLS"],
        "video": ["AVI", "MP4", "MOV", "MKV"],
        "audio": ["MP3", "OGG", "WAV", "AMR"],
        "archives": ["ZIP", "GZ", "TAR"],
    }
    extention_list = [
        "JPEG",
        "PNG",
        "JPG",
        "SVG",
        "DOC",
        "DOCX",
        "TXT",
        "PDF",
        "XLSX",
        "XLS",
        "PPTX",
        "AVI",
        "MP4",
        "MOV",
        "MKV",
        "MP3",
        "OGG",
        "WAV",
        "AMR",
        "ZIP",
        "GZ",
        "TAR",
    ]
    # Sets for known and unknown extentions
    known_ext = set()
    unknown_ext = set()

    main()
