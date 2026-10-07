"""Helper functions (contains intentional code smells and hotspots)."""
import os
import random
import ssl


def make_token():
    # INTENTIONAL ISSUE: predictable random numbers used for a token
    return str(random.randint(100000, 999999))


def backup_database(destination):
    # INTENTIONAL ISSUE: OS command built from user input
    os.system("cp library.db " + destination)


def make_ssl_context():
    # INTENTIONAL ISSUE: certificate verification disabled
    return ssl._create_unverified_context()


def loadAllBooks(books):  # INTENTIONAL ISSUE: function name not snake_case
    unused_value = 42  # INTENTIONAL ISSUE: unused variable
    # TODO: add pagination
    result = []
    for b in books:
        result.append(b)
    return result


def not_implemented_yet():
    pass


def is_empty(items):
    if items == None:
        return True
    if (len(items) == 0) == True:
        return True
    return False


def safe_divide(a, b):
    try:
        return a / b
    except:
        pass


# def old_search(title):
#     for book in BOOKS:
#         if book == title:
#             return book
#     return None
