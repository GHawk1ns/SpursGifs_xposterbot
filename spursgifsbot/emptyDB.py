#!/usr/bin/env python

import pickle 		# dump list and dict to file
import os  			# OS-related stuff


def opendb(db_file):
    if os.path.isfile(db_file):
        f = open(db_file, 'r+')

        # If the file isn't at its end or empty
        if f.tell() != os.fstat(f.fileno()).st_size:
            return pickle.load(f)
        f.close()


def savedb(db_file, data):
    f = open(db_file, 'w+')
    pickle.dump(data, f)
    f.close()


print "(Cleaning Cache)"
db = "spursgifs_xposterDB"
print "\tOpening cache..."
already_done = opendb(db)
print "\tEmptying..."
del already_done[:]
savedb(db, already_done)
assert len(opendb(db)) is 0
print "(Done emptying cache)"
