import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_message(user_msg, bot_msg):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO conversations (user_message, bot_response) VALUES (?, ?)",
        (user_msg, bot_msg)
    )

    conn.commit()
    conn.close()


def get_last_messages(limit=8):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_message FROM conversations ORDER BY id DESC LIMIT ?",
        (limit,)
    )

    rows = cursor.fetchall()
    conn.close()

    # The rows are in DESC (newest first). Let's reverse to be chronological.
    messages = [row[0] for row in rows]
    messages.reverse()
    
    # Filter out short conversational fillers
    valid_messages = []
    for m in messages:
        if len(m.strip()) > 3 and m.lower().strip() not in ["yes", "no", "hi", "hello", "hey", "ok", "okay", "yeah", "yep", "sure"]:
            valid_messages.append(m)

    return valid_messages