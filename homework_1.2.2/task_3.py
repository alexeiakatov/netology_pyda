queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


get_queries = lambda: queries


def remove_invalid_elements(queries_list):
    return ([query for query in queries
             if query is not None
             and type(query) == str
             and len(query) > 0])


def normalize_queries(queries):
    not_empty_queries = remove_invalid_elements(queries)

    # нормализуем сплит-массив, т.к. между словами могло быть больше одного пробела
    result = []
    for query in queries:
        query_split = [word for word in query.split(' ') if len(word) > 0]
        result.append(query_split)

    return result


def show_result(words_to_percent):
    for key, value in words_to_percent.items():
        print(f'{key} : {value}')


def get_words_to_queries(unique_word_counts, normalized_queries):
    words_to_queries = {}

    for word_count in unique_word_counts:
        for query_split in normalized_queries:
            if len(query_split) == word_count:
                words_to_queries[word_count] = words_to_queries.get(word_count, 0) + 1

    return words_to_queries


def get_words_to_percent(all_queries_count, words_to_queries):
    words_to_percent = {}

    for word_count, query_count in words_to_queries.items():
        words_to_percent[word_count] = round(query_count / all_queries_count * 100, 2)

    return words_to_percent


def main():
    normalized_queries = normalize_queries(get_queries())
    unique_word_counts = {len(query_split) for query_split in normalized_queries}

    words_count_to_query_count = get_words_to_queries(unique_word_counts, normalized_queries)

    all_queries_count = len(normalized_queries)
    words_count_to_percent = get_words_to_percent(all_queries_count, words_count_to_query_count)

    show_result(words_count_to_percent)


if __name__ == '__main__':
    main()
