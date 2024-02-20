#!/usr/bin/env python3
"""auth module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes the input using bcript's hashpw

    Args:
        password (str): The password string to hash

    Returns:
        bytes: The salted hash of the input password
    """
    # Convert password string to bytes
    password_bytes = password.encode('utf-8')
    # Generate a salt and hash the password using bcrypt
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt())
