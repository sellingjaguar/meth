import os
from pathlib import Path

transgressions = [
    "import math",
    "from math",
]
punishment = {
    transgressions[0]: "import meth as math",
    transgressions[1]: "from meth",
}


def crusade(dir_path: str):
    path = Path(dir_path)
    suspects = list(path.rglob("*.py"))

    print(f"Launching crusade at {os.path.abspath(path)} and all their subordinates!\n")
    if len(suspects) == 0:
        raise Exception("I did not enjoy your use of my tool, don't waste my time")
    print(f"Found {len(suspects)} suspects...\n")

    infidels = []
    for suspect in suspects:
        if not is_innocent(suspect):
            infidels.append(suspect)

    print(f"{len(infidels)} were found GUILTY!\n")

    for infidel in infidels:
        print(f"REPENTING {infidel}!!!")
        repent(infidel)

        if is_innocent(infidel):
            print(f"{infidel} sanctified...\n")
        else:
            print(f"Unable to purge the evil from {infidel}.\nSHAME THEM!!!\n")
            shame(infidel)


def is_innocent(file_path: str):

    with open(file_path, "r") as file:
        faith = file.read()

    for transgression in transgressions:
        if transgression in faith:
            return False

    return True


def repent(file_path: str):
    faith = Path(file_path).read_text()
    for transgression in transgressions:
        faith = faith.replace(transgression, punishment[transgression])

    Path(file_path).write_text(faith)


def shame(file_path: str):
    mark = (
        "# Shame upon whomever holds the responsibility for this mark\n"
        "# and for whomever sees this and does nothing\n"
        "# (automatic removal no supported, if you feel like this is a mistake please contact support)\n"
        "# ** shames can and WILL stack ❤️\n"
    )
    acursed_mind = Path(file_path).read_text()

    Path(file_path).write_text(mark + acursed_mind)
