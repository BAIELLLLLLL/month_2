import datetime


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def age(self):
        day, month, year = map(int, self.__birth_date.split('.'))
        birthday = datetime.date(year, month, day)
        today = datetime.date.today()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.__higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. {edu_text}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        # Передаем все необходимые параметры в родительский класс
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Я учился с Айсулуу в группе {self.group_name}. "
            f"{edu_text}"
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        # Передаем все необходимые параметры в родительский класс
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Мое хобби {self.hobby}. "
            f"{edu_text}"
        )


if __name__ == '__main__':

    cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
    cl1.introduce()

    fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
    fr1.introduce()

    print(f"Возраст: {fr1.age}")
