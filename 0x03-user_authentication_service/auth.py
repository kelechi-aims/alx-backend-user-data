#!/usr/bin/env python3
"""auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes the class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user

        Args:
            emsil (str): Email of the user
            password (str): Password of the user

        Return:
            User: User object representing the newly registered user

        Raises:
            ValueError: If a user with the provided email already esixts
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
