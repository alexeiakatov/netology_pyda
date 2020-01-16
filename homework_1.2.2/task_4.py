stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

CHANNEL_SALES_INDEX = 1
CHANNEL_NAME_INDEX = 0

MAX_SALES_CHANNEL_INDEX = 0


get_stats = lambda: stats


map_to_list = lambda map: [[k, v] for k, v in stats.items()]


max_sales_sort_lambda = lambda item: item[CHANNEL_SALES_INDEX]


def main():
    stats_list = map_to_list(get_stats())
    stats_list.sort(key = max_sales_sort_lambda, reverse = True)
    max_sales_channel = stats_list[MAX_SALES_CHANNEL_INDEX]

    print(f'{max_sales_channel[CHANNEL_NAME_INDEX]} : {max_sales_channel[CHANNEL_SALES_INDEX]}')


if __name__ == '__main__':
    main()
