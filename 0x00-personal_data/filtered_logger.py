#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values.
"""
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "password", "ssn")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ A function that returns the log message obfuscated """
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes the class RedactingFormatter"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Filter values in incoming log records using filter_datum"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)

    # Create a StreamHandler with RedactingFormatter
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    # Disable propagation to other loggers
    logger.propagate = False

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return a connector to the MySQL database"""
    # Obtain database credentials from environment variables
    db_username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    # Connect to the MySQL database
    db = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )

    return db


def main() -> None:
    """
    Obtain a database and retrieve all rows in ther users table
    and display each row under a filtered format
    """
    # Set up logging
    logger = get_logger()

    # Obtain a database connection
    db = get_db
    cursor = db.cursor()

    # Retrieve all rows from the users table
    cursor.execute("SELECT * FROM users")
    row = cursor.fetchall()

    # Display each row under a filtered format
    for row in rows:
        message = "; ".join(
            f"{field}={value} " for field, value in zip(PII_FIELDS, row)
        )
        logger.info(message)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
