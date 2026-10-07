from library.database import add_book, add_member, find_book, get_connection, hash_password
from library.services import (book_status, calculate_fine, checkout, count_books,
                              report_for_students)
from library.utils import is_empty, loadAllBooks


def test_find_book():
    conn = get_connection()
    add_book(conn, "Dune", "Herbert", 2)
    assert find_book(conn, "Dune")[0][1] == "Dune"


def test_add_member_and_hash():
    conn = get_connection()
    add_member(conn, "ali", "pw")
    assert len(hash_password("pw")) == 32


def test_fine_student_novel():
    assert calculate_fine(3, "student", "novel", False, False) == 6
    assert calculate_fine(0, "student", "novel", False, False) == 0


def test_count_and_status():
    assert count_books([1, 2]) == 2
    assert book_status(1) == "available"
    assert checkout(3) == 2


def test_report_students():
    assert "Grand total: 4" in report_for_students([{"title": "A", "days": 2}])


def test_helpers():
    assert is_empty([])
    assert loadAllBooks([1]) == [1]
