#!/usr/bin/env python3
""" Auth class """
from flask import request
from typing import List, TypeVar


class Auth:
    """ A class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required for the given path. """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        path_slash = path.endswith('/')
        for excluded_path in excluded_paths:
            if path_slash and excluded_path == path:
                return False
            elif not path_slash and excluded_path == path + '/':
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the Authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request."""
        return None
