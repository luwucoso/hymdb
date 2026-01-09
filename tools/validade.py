#!/usr/bin/env python

import jsonschema
import json

def load_schema(schema_path):
    schema_text = open(schema_path, "r");
    try:
        parsed = json.load(schema_text)
        return parsed
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e.msg} (line {e.lineno}, column {e.colno})")

def validade_file(schema, file_path, error_list):
    # no need to push those errors to the error list
    file_text = open(file_path, "r")

    try:
        file_parsed = json.load(file_text)
    except json.JSONDecodeError as e:
        error_list.append(f"Error parsing JSON: {e.msg} (line {e.lineno}, column {e.colno}). Error file at: {file_path}")
        return

    try:
        jsonschema.validate(schema=schema, instance=file_parsed)
    except jsonschema.ValidationError as e:
        error_list.append(f"Validation error: {e.message}. Path to error: {file_path}")
