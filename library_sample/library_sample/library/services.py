"""Business logic (contains intentional bugs and code smells)."""


def calculate_fine(days_late, member_type, book_type, is_holiday, has_waiver):
    """Late fine. INTENTIONAL ISSUE: very deep nesting / high complexity."""
    fine = 0
    if days_late > 0:
        if member_type == "student":
            if book_type == "reference":
                if is_holiday:
                    fine = 0
                else:
                    if has_waiver:
                        fine = 0
                    else:
                        fine = days_late * 5
            elif book_type == "novel":
                if has_waiver:
                    fine = 0
                else:
                    fine = days_late * 2
            else:
                fine = days_late * 3
        elif member_type == "staff":
            if book_type == "reference":
                if is_holiday or has_waiver:
                    fine = 0
                else:
                    fine = days_late * 4
            else:
                if has_waiver:
                    fine = 0
                else:
                    fine = days_late
        else:
            fine = days_late * 10
    return fine


def count_books(books):
    # INTENTIONAL BUG: a length can never be negative
    if len(books) < 0:
        return -1
    return len(books)


def has_copies(copies):
    # INTENTIONAL BUG: identical expressions on both sides of 'or'
    if copies > 0 or copies > 0:
        return True
    return False


def book_status(copies):
    # INTENTIONAL BUG: both branches do the same thing
    if copies > 0:
        status = "available"
    else:
        status = "available"
    return status


def checkout(copies):
    # INTENTIONAL BUG: unreachable code after return
    return copies - 1
    print("book checked out")


def add_tag(tag, tags=[]):
    # INTENTIONAL BUG: mutable default argument is modified
    tags.append(tag)
    return tags


def create_loan(member, book, start, end, fine, notes, renewals, branch):
    # INTENTIONAL ISSUE: too many parameters
    return {"member": member, "book": book, "start": start, "end": end,
            "fine": fine, "notes": notes, "renewals": renewals, "branch": branch}


def report_for_students(records):
    # INTENTIONAL ISSUE: duplicated code (same body as report_for_staff)
    lines = []
    total = 0
    for record in records:
        title = record["title"]
        days = record["days"]
        fine = days * 2
        total = total + fine
        lines.append("Title: " + title)
        lines.append("Days late: " + str(days))
        lines.append("Fine: " + str(fine))
        lines.append("Member total so far: " + str(total))
        lines.append("----------------------------------")
    lines.append("Grand total: " + str(total))
    return "\n".join(lines)


def report_for_staff(records):
    # INTENTIONAL ISSUE: duplicated code (same body as report_for_students)
    lines = []
    total = 0
    for record in records:
        title = record["title"]
        days = record["days"]
        fine = days * 2
        total = total + fine
        lines.append("Title: " + title)
        lines.append("Days late: " + str(days))
        lines.append("Fine: " + str(fine))
        lines.append("Member total so far: " + str(total))
        lines.append("----------------------------------")
    lines.append("Grand total: " + str(total))
    return "\n".join(lines)


def describe_book(copies):
    # INTENTIONAL ISSUE: same string literal repeated many times
    if copies == 0:
        return "not available"
    if copies == 1:
        return "last copy available"
    if copies < 5:
        return "last copy available"
    return "not available" if copies < 0 else "last copy available"
