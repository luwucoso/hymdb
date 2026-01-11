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
        error_list.append({
            "type": "decode_error",
            "file_path": file_path,
            "error": e,
        })
        return

    try:
        jsonschema.validate(schema=schema, instance=file_parsed)
    except jsonschema.ValidationError as e:
        error_list.append({
            "type": "validation_error",
            "file_path": file_path,
            "error": e,
        })

def pretty_error(error):
    if error["type"] == "validation_error":
        return f"Validation error: {error["error"].message}. Path to error: {error["file_path"]}"
    elif error["type"] == "decode_error":
        return f"Error parsing JSON: {error["error"].msg} (line {error["error"].lineno}, column {error["error"].colno}). Error file at: {error["file_path"]}"

def github_error(error):
    if error["type"] == "validation_error":
        return f"::error file={error["file_path"]}::Validation error: {escape_github_message(error["error"].message)}."
    elif error["type"] == "decode_error":
        return f"::error file={error["file_path"]},line={error["error"].lineno},col={error["error"].colno}::Error parsing JSON: {escape_github_message(error["error"].msg)}"

# i hope this is enough? im not sure if any of the libs would spit these out, but i still want them
def escape_github_message(msg: str) -> str:
    return msg.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')