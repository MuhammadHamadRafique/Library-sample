"""Database access layer (contains intentional security issues)."""
import hashlib
import pickle
import sqlite3


def get_connection(path=":memory:"):
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS books "
        "(id INTEGER PRIMARY KEY, title TEXT, author TEXT, copies INTEGER)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS members "
        "(id INTEGER PRIMARY KEY, name TEXT, password TEXT)"
    )
    return conn


def add_book(conn, title, author, copies=1):
    conn.execute(
        "INSERT INTO books (title, author, copies) VALUES (?, ?, ?)",
        (title, author, copies),
    )
    conn.commit()


def find_book(conn, title):
    # INTENTIONAL ISSUE: SQL injection through string concatenation
    query = "SELECT * FROM books WHERE title = '" + title + "'"
    return conn.execute(query).fetchall()


def hash_password(password):
    # INTENTIONAL ISSUE: weak hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()


def add_member(conn, name, password):
    # INTENTIONAL ISSUE: SQL injection through string formatting
    conn.execute(
        "INSERT INTO members (name, password) VALUES ('%s', '%s')"
        % (name, hash_password(password))
    )
    conn.commit()


def load_backup(data):
    # INTENTIONAL ISSUE: unsafe deserialization
    return pickle.loads(data)
