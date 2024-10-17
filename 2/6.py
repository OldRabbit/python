keywords = ('for', 'if', 'else', 'in', ':')


code_structure = [
    f"{keywords[0]} item {keywords[3]} items{keywords[4]}",
    "    " + f"{keywords[1]} condition{keywords[4]}",
    "        do_something()",
    "    " + f"{keywords[2]}{keywords[4]}",
    "        do_something_else()"
]

for line in code_structure:
    print(line)