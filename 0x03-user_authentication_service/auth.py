#!/usr/bin/env python3
"""auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


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


def _generate_uuid() -> str:
    """Generate a new UUID

    Returns:
        str: String representation of the generated UUID.
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the provided login credentials are valid

        Args:
            email (str): Email of the user
            password (str): Password of the user

        Returns:
            bool: True if the login credential are valid, False
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """Create a session for tthe user with the given email

        Args:
            email (str): Email of the user

        Returns:
            str: Session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Retrieve the user corresponding to the given session ID.

        Args:
            session_id (str): The session ID to search for.

        Returns:
            User: The corresponding user if found, otherwise None.
        """
        if not session_id:
            return None

        user = self._db.find_user_by(session_id=session_id)
        return user if user else None
