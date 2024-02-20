# User Authentication Service
**By**: Emmanuel Turlay, Staff Software Engineer at Cruise
**Weight**: 1

## Introduction
This project implements a user authentication service using Flask, a micro web framework for Python. The goal is to understand the authentication process by building it from scratch, rather than relying on existing authentication frameworks or modules like Flask-User. The service will allow users to register, log in, log out, and authenticate their identity securely.

## Resources
- [Resources](https://intranet.alxswe.com/rltoken/lKExyvivrrW4eh0eI8UV6A)
- [Requests module](https://intranet.alxswe.com/rltoken/py7LuuD1u2MUwcaf8wnDzQ)
- [https://intranet.alxswe.com/rltoken/cj-mc5ZHp_KyXn1yikHC0A](https://intranet.alxswe.com/rltoken/cj-mc5ZHp_KyXn1yikHC0A)
- [mapping declaration ](https://intranet.alxswe.com/rltoken/-a69l-rGqoFdXnnu6qfKdA)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/oAqmZmipBdjCcfI5QqyFXA), **without the help of Google**:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements
- Editors: Allowed editors include vi, vim, and emacs.
- Python Version: All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- Line Endings: All files should end with a new line.
- Shebang: The first line of all files should be exactly #!/usr/bin/env python3.
- README.md: A README.md file at the root of the project folder is mandatory.
- Coding Style: Use the pycodestyle style (version 2.5).
- Dependency: Use SQLAlchemy 1.3.x.
- Executable Files: All files must be executable.
- File Length: The length of your files will be tested using wc.
- Documentation: All modules, classes, and functions should have proper documentation.
- Type Annotations: All functions should be type annotated.
- Interactions: The Flask app should only interact with Auth and never with the database directly.
- Public Methods: Only public methods of Auth and DB should be used outside these classes.

## Setup
Ensure you have bcrypt installed:
```bash
pip3 install bcrypt
```

## Usage
- Clone the repository:
```bash
git clone https://github.com/kelechi-aims/alx-backend-user-data/tree/main/0x03-user_authentication_service 
cd 0x03-user_authentication_service
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
