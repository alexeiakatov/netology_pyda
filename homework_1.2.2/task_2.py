ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def main():
    unique_ids = {value for id_list in ids.values() for value in id_list}
    print(unique_ids)


if __name__ == '__main__':
    main()