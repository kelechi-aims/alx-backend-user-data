#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values.
"""
import re


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    A function that returns the log message obfuscated

    Args
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is
    separating all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message
