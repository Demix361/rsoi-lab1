from django.test import TestCase, Client
from django.db import DataError
from rest_framework.generics import get_object_or_404
from django.http import Http404
from .models import Person
from .views import APIPersonList, APIPersonDetail

client = Client()


class PersonTest(TestCase):
    def setUp(self):
        self.personList = APIPersonList()
        self.personDetail = APIPersonDetail()

        Person.objects.create(
            name='Chel', age=29, address='Yes', work='Work'
        )
        Person.objects.create(
            name='Mujik', age=99, address='Ukraina', work='Kazah'
        )
        Person.objects.create(
            name='Salam', age=2, address='Russia', work='No'
        )

    def testCreated(self):
        person = Person.objects.get(age=99)

        self.assertEqual(99, person.age)

    def testWrong(self):
        try:
            person = Person.objects.get(name='Kto')
        except Person.DoesNotExist:
            self.assertEqual(1, 1)
        else:
            raise self.fail('Wrong!')

    def testChange(self):
        person = Person.objects.get(name='Chel')
        new_name = 'Ne Chel'
        person.name = new_name
        person.save(update_fields=['name'])

        self.assertEqual(person, Person.objects.get(name=new_name))

    def testDelete(self):
        Person.objects.filter(age=2).delete()

        try:
            person = Person.objects.get(age=2)
        except Person.DoesNotExist:
            self.assertEqual(1, 1)
        else:
            raise self.fail('Wrong!')

    def testWrongValue(self):
        person = Person.objects.get(name='Mujik')

        new_name = 'a' * 500
        person.name = new_name

        try:
            person.save(update_fields=['name'])
        except DataError:
            self.assertEqual(1, 1)
        else:
            raise self.fail('Wrong!')
# :)
