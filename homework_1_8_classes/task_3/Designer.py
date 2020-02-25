from netology_pyda.homework_1_8_classes.libs.Employee import Employee


class Designer(Employee):
    _awards = 0

    # дизайнеры получают каждое следующее повышение при увеличении кол-ва баллов на 7
    _grade_up_condition = 7

    #
    def __init__(self, name: str, seniority: int, awards: int):
        super().__init__(name, seniority)

        self.upgrade_if_need()

        for award in range(awards):
            self.received_award()

    #
    def _check_awards_valid(self, awards: object):
        if not isinstance(awards, int) or awards < 0:
            raise Exception('Некорректный параметр awards')

    # дизайнеры могут получать премии. Полученная премия эквивалентна 2м пройденным аккредитациям, т.е. увеличивает
    # значение super()._seniority на 2.
    def received_award(self):
        self._awards += 1
        super().set_seniority(super().get_seniority() + 2)
        self.upgrade_if_need()

    def passed_accreditation(self):
        super().set_seniority(super().get_seniority() + 1)
        self.upgrade_if_need()

    #
    def upgrade_if_need(self):
        seniority_step = 0
        step_count = 0

        current_seniority = super().get_seniority()
        current_grade = None

        while seniority_step <= current_seniority:
            if seniority_step > 0:
                step_count += 1
                current_grade = super().get_grade()

                if  current_grade < step_count:
                    print('Designer upgrade event')
                    super().grade_up()
                    super().publish_grade()

            seniority_step += self._grade_up_condition

