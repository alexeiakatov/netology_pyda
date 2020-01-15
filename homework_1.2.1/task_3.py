stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]

VISITS_INDEX = 2
USER_ID_INDEX = 1


def is_valid_logs(log_list):

    if log_list is None or len(log_list) == 0:
        return False

    for log_item in log_list:

        if log_item is None or len(log_item) == 0:
            return False

        log_split = log_item.split(',')

        if len(log_split) < 3:
            return False

        if not log_split[VISITS_INDEX].isnumeric():
            return False

    return True


def main():

    if is_valid_logs(stream):

        all_visits_count = 0
        unique_users = []

        for log_item in stream:
            log_split = log_item.split(',')

            all_visits_count += int(log_split[VISITS_INDEX])

            user_id = log_split[USER_ID_INDEX]

            if user_id not in unique_users:
                unique_users.append(user_id)

    print(f'Среднее значение просмотров на пользователя: {round(all_visits_count / len(unique_users), 2)}')


main()
