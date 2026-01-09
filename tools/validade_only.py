#!/usr/bin/env python

from validade import *
import sys
import os

schema_path = "schemas/mod.schema.json"

schema = load_schema(schema_path)

error_list = []

if len(sys.argv) < 2:
    print("Usage: python script.py <filepath>")
    print("Please pass in a file to validade.")
    sys.exit(1)

file_path = filepath = sys.argv[1]

validade_file(schema, file_path, error_list)

if error_list:
    # Print red text to the terminal
    print("\033[91mThe following errors were found:\033[0m")
    for e in error_list:
        print(f"\033[91m- {e}\033[0m")
    
    # Exit with an error code
    sys.exit(1)

print(f"\033[0;32mParsed file correctly!\033[0m")