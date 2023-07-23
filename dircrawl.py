import argparse

logo = """
 /$$$$$$$  /$$            /$$$$$$                                   /$$
| $$__  $$|__/           /$$__  $$                                 | $$
| $$  \ $$ /$$  /$$$$$$ | $$  \__/  /$$$$$$  /$$$$$$  /$$  /$$  /$$| $$
| $$  | $$| $$ /$$__  $$| $$       /$$__  $$|____  $$| $$ | $$ | $$| $$
| $$  | $$| $$| $$  \__/| $$      | $$  \__/ /$$$$$$$| $$ | $$ | $$| $$
| $$  | $$| $$| $$      | $$    $$| $$      /$$__  $$| $$ | $$ | $$| $$
| $$$$$$$/| $$| $$      |  $$$$$$/| $$     |  $$$$$$$|  $$$$$/$$$$/| $$
|_______/ |__/|__/       \______/ |__/      \_______/ \_____/\___/ |__/
"""
# parser = argparse.ArgumentParser("DirCrawler", "Filtering most important Windows OS files.")
# parser.add_argument("file", help="cmd.exe /b /a /s C:\ > dir.txt", default="dir.txt")
# args = parser.parse_args()

lines = []
with open("dir.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

filters = []
with open("extensions.txt", 'r', encoding="utf-8") as f:
    filters = f.readlines()

for filt in filters:
    matching_lines = []
    openning = "=" * 20 + " " + filt[0:-1] + " " + "=" * 10
    print(openning)
    for i in lines:
        if filt in i:
            matching_lines.append(i[0:-1])
    if len(matching_lines) < 1:
        print("\tNONE")
    else:
        for ml in matching_lines:
            print("[+] | " + ml)