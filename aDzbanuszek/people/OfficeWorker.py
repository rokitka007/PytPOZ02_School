from datetime import date
import os
from aDzbanuszek.people.Person import Person


class OfficeWorker(Person):

    def __init__(self, name, second_name, born_data):
        super(OfficeWorker, self).__init__(name, second_name, born_data)
