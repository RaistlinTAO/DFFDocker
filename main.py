# This is a sample Python script for AWS Fargate test
import time
import mysql.connector


def dummy_task():
    db_connection = mysql.connector.connect(
        host="twocent.icu",
        user="test",
        password="test",
        database="seamless"
    )
    db_cursor = db_connection.cursor()
    overall_count = 5
    i = 0
    while i < overall_count:
        print('Task Status: ' + str(i * 20) + '%')
        time.sleep(1)
        i += 1
    print('Test Completed')
    timestamp = time.time()
    print()
    sql = "INSERT INTO test (testResult) VALUES (" + str(timestamp) + ")"
    db_cursor.execute(sql)
    db_connection.commit()
    db_connection.close()
    return timestamp


if __name__ == '__main__':
    dummy_task()
