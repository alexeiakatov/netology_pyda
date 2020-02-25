
class Employee:

    # фио сотрудника
    _name = ''

    # количество пройденных аккредитаций
    _seniority = 0

    # уровень сотрудника по шкале, определенной в конкретной организации
    _grade = 0

    #
    def __init__(self, name: str, seniority: int):
        self._check_name_valid(name)
        self._check_seniority_valid(seniority)

        self._name = name
        self._seniority = seniority

    #
    def _check_name_valid(self, name: object):
        if (not isinstance(name, str)
                or len(name) > 100
                or len(name) == 0):

            raise Exception('Некорректный параметр name')

    #
    def _check_seniority_valid(self, seniority: object):
        if not isinstance(seniority, int) or seniority < 0:
            raise Exception('Некорректный параметр seniority')

    #
    def grade_up(self) -> None:
        """Повышает уровень сотрудника"""
        self._grade += 1

    #
    def publish_grade(self) -> None:
        """Публикация результатов аккредитации сотрудников"""
        print(self._name, self._grade)

    #
    def upgrade_if_need(self):
        pass

    #
    def passed_accreditation(self):
        self._seniority += 1

    #
    def get_seniority(self):
        return self._seniority

    #
    def set_seniority(self, seniority):
        self._check_seniority_valid(seniority)
        self._seniority = seniority

    #
    def get_grade(self):
        return self._grade
