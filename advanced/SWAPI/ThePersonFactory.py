from ThePerson import ThePerson


class ThePersonFactory:

    @staticmethod
    def create_person_from_data(data):
        new_person = ThePerson()
        new_person.load_from_json(data)

        return new_person

    @staticmethod
    def create_persons_from_data_list(data_list):
        person_list = []
        for data in data_list:
            person_list.append(ThePersonFactory.create_person_from_data(data))

        return person_list
