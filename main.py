# This is a sample Python script for AWS Fargate test
import time


def dummy_task():
    overall_count = 5
    i = 0
    while i < overall_count:
        print('Task Status: ' + str(i * 20) + '%')
        time.sleep(1)
        i += 1
    print('Test Completed')
    print(time.time())
    return time.time()


if __name__ == '__main__':
    dummy_task()
