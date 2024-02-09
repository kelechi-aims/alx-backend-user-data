#!/usr/bin/env python3
""" Encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes the input password using bcrypt with salt"""
    # Generate a random salt and hash the password
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check valid password"""
    return bcrypt.checkpw(password.encode('utf'), hashed_password)
