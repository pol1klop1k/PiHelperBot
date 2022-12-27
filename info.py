import psycopg2
import os

def get_questions(subject):
    conn = psycopg2.connect(
        user = "postgres",
        password = "Btc601cr",
        host = "localhost",
        port = 5432,
        database = "pihelper"
    )

    cur = conn.cursor()

    cur.execute(f"SELECT question_id, question FROM questions WHERE subject='{subject}' ORDER BY question_id")
    questions = cur.fetchall()

    cur.close()
    conn.close()
    return questions



