#!/usr/bin/env python

from shared import *
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
    print("::group::Errors validating")
    for e in error_list:
        print(github_error(e))
    print("::endgroup::")
    
    # Exit with an error code
    sys.exit(1)

sys.exit(0)