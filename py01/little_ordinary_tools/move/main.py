# coding=utf8

def init_test_list(*tests):

    test_list = []

    for test in tests:
        test_list.append(test)

    return test_list

def run_test_list(tests):
    for test in tests:
        test.check()


if __name__ == '__main__':
    test_list = init_test_list()
    run_test_list(test_list)