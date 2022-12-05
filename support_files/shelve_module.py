# https://docs.python.org/3/library/shelve.html
# shelve.open(filename, flag='c', protocol=None, writeback=False)
# c - default, open file, read, write; if file does not exist it would be created
# r - read only
# w - write only
# n - read only; if file does not exist it would be created

"""
Connect file:

import shelve
d = shelve.open(filename)
d.close()
"""

import shelve

FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])


# Edit data


import shelve

FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:

    states["London"] = "United Kingdom"
    states["Brussels"] = "Belgium"
    for key in states:
        print(key, " - ", states[key])


# Remove data
# 1

with shelve.open(FILENAME) as states:
    state = states.pop("London", "NotFound")
    print(state)

# Remove data
# 2
with shelve.open(FILENAME) as states:
    del states["Madrid"]

# Remove all data
with shelve.open(FILENAME) as states:
    states.clear()