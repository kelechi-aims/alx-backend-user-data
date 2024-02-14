#!/usr/bin/env python3
"""Empty session"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    A new authentication mechanism:
    - validate if everything inherits correctly without any overloading
    - validate the “switch” by using environment variables
    """
    pass
