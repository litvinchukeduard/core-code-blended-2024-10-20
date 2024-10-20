import sys
from pathlib import Path
from colorama import Fore, Back, Style

args = sys.argv
if len(args) < 2:
    print("Please provide a folder path")
    sys.exit()

folder_path = args[1]
# print(folder_path)

p = Path(folder_path)
# [x for x in p.iterdir() if x.is_dir()] # list comprehensions

# result = []
for x in p.iterdir():
    if x.is_dir():
        # result.append(x)
        print(Fore.YELLOW + x.name + '/' + Style.RESET_ALL)
    else:
        print(Fore.GREEN + x.name + Style.RESET_ALL)

# print(result)
