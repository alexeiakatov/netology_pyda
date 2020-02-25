from netology_pyda.homework_1_8_classes.task_3.Designer import Designer


class DesignerTest:

    #
    def run_tests(self):
        self.test_correct_grade_after_object_creation()
        self.test_designer_award_adds_2_points_to_seniority()
        self.test_designer_accreditation_adds_1_point_to_seniority()
        self.test_grade_incremented_when_need
        self.test_grade_incremented_when_needed()

    #
    def test_correct_grade_after_object_creation(self):
        test_data = [
            {'designer': Designer('Иванов Иван Иванович', 24, 0), 'success_grade': 3},
            {'designer': Designer('Иванов Иван Иванович', 21, 0), 'success_grade': 3},
            {'designer': Designer('Иванов Иван Иванович', 0, 0), 'success_grade': 0},
            {'designer': Designer('Иванов Иван Иванович', 0, 4), 'success_grade': 1},
            {'designer': Designer('Иванов Иван Иванович', 1, 3), 'success_grade': 1},
            {'designer': Designer('Иванов Иван Иванович', 6, 4), 'success_grade': 2},
        ]

        for test_item in test_data:

            actual_grade = test_item['designer'].get_grade()
            success_grade = test_item['success_grade']

            if actual_grade != success_grade:
                raise Exception('Тест не пройден: test_correct_grade_after_object_creation')

    #
    def test_designer_award_adds_2_points_to_seniority(self):
        test_designers = [
            Designer('Иванов Иван Иванович', 0, 0),
            Designer('Иванов Иван Иванович', 5, 0),
            Designer('Иванов Иван Иванович', 23, 0),
            Designer('Иванов Иван Иванович', 11, 0)
        ]

        for designer in test_designers:
            for i in range(1, 50):
                current_seniority = designer.get_seniority()
                success_seniority = current_seniority + 2
                designer.received_award()
                actual_seniority = designer.get_seniority()

                if success_seniority != actual_seniority:
                    raise Exception('Тест не пройден: test_designer_award_adds_2_points_to_seniority')

    #
    def test_designer_accreditation_adds_1_point_to_seniority(self):
        test_designers = [
            Designer('Иванов Иван Иванович', 0, 0),
            Designer('Иванов Иван Иванович', 5, 0),
            Designer('Иванов Иван Иванович', 23, 0),
            Designer('Иванов Иван Иванович', 11, 0)
        ]

        for designer in test_designers:
            for i in range(1, 50):
                success_seniority = designer.get_seniority() + 1
                designer.passed_accreditation()
                actual_seniority = designer.get_seniority()

                if success_seniority != actual_seniority:
                    raise Exception('Тест не пройден: test_designer_accreditation_adds_1_point_to_seniority')

    #
    def test_grade_incremented_when_needed(self):
        test_designers = [
            {'designer': Designer('Иванов Иван Иванович', 6, 0), 'event': 'accreditation', 'success_grade': 1},
            {'designer': Designer('Иванов Иван Иванович', 5, 0), 'event': 'award', 'success_grade': 1},
            {'designer': Designer('Иванов Иван Иванович', 6, 0), 'event': 'award', 'success_grade': 1},
            {'designer': Designer('Иванов Иван Иванович', 13, 0), 'event': 'accreditation', 'success_grade': 2},
            {'designer': Designer('Иванов Иван Иванович', 11, 1), 'event': 'accreditation', 'success_grade': 2},
        ]

        for test_item in test_designers:
            event = test_item['event']
            designer = test_item['designer']

            if event == 'accreditation':
                designer.passed_accreditation()

            elif event == 'award':
                designer.received_award()

            else:
                raise Exception('Ошибка в тестовых данных: test_grade_incremented_when_need')

            succcess_grade = test_item['success_grade']
            actual_grade = designer.get_grade()

        if succcess_grade != actual_grade:
            raise Exception('Тест не пройден: test_grade_incremented_when_need')
