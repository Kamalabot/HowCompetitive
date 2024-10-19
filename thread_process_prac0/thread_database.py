import threading
import sqlite3
import time


def fetch_data(filter_value):
    # establish new connection
    connection = sqlite3.connect("thread_python.db")
    cursor = connection.cursor()

    # build the query
    query = f"SELECT * FROM users WHERE age > {filter_value}"

    # Execute the query
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchall()

    print(
        f"Thread {threading.current_thread().name} fetched data where age is > {filter_value}"
    )

    connection.close()


def create_sample_db():
    connection = sqlite3.connect("thread_python.db")
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"""
    )
    cursor.executemany(
        "INSERT INTO users(name, age) VALUES (?, ?)",
        [(f"user-{i}", i % 50 + 20) for i in range(100)],
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_sample_db()
    threads = []
    for i in range(100):
        filter = i % 50
        thread = threading.Thread(target=fetch_data, args=(filter,), name=f"Client-{i}")
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
    print("All threads completed...")
