import sqlite3
from contextlib import closing

DB_NAME = "database.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with closing(get_connection()) as conn:
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT,
                bot_response TEXT
            )
            """)


def save_message(user_msg, bot_msg):
    if not user_msg or not bot_msg:
        return

    with closing(get_connection()) as conn:
        with conn:
            conn.execute(
                "INSERT INTO conversations (user_message, bot_response) VALUES (?, ?)",
                (user_msg.strip(), bot_msg.strip())
            )


def get_last_messages(limit=5, include_bot=True):
    with closing(get_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT user_message, bot_response FROM conversations ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()

    rows.reverse()

    messages = []
    for u, b in rows:
        messages.append(f"User: {u}")
        messages.append(f"Bot: {b}")

    return messages