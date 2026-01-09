#!/usr/bin/env python

from validade import *
import sys
import os

schema_path = "schemas/mod.schema.json"

schema = load_schema(schema_path)

error_list = []

mods_dir = "mods/"

for dirpath, dirnames, filenames in os.walk(mods_dir):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        validade_file(schema, file_path, error_list)

if error_list:
    # Print red text to the terminal
    print("\033[91mThe following errors were found:\033[0m")
    for e in error_list:
        print(f"\033[91m- {e}\033[0m")
    
    # Exit with an error code
    sys.exit(1)

print(f"\033[0;32mEvery mod parsed correctly!\033[0m")