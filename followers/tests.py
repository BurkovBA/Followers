from django.test import TestCase
import django.core.exceptions
from models import Man, Follow

class TestManFollow(TestCase):
    def setUp(self):
        Man(name="Stepan Ivanov").save()
        Man(name="Modest Musorgsky").save()
        Follow(who=Man.objects.get(name="Stepan Ivanov"), whom=Man.objects.get(name="Modest Musorgsky")).save()

    def test_remove(self):
        Man.objects.get(name="Modest Musorgsky").delete()
        ivanov_follows = Follow.objects.filter(who=Man.objects.get(name="Stepan Ivanov"))
        self.assertEqual(len(ivanov_follows), 0)

    def test_follow_non_existent(self):
        katya = Man(name="Katya Ryabchikova")
        katya.save()
        try:
            Follow(who=katya, whom=Man.objects.get(name="non-existent")).save()
        except Exception as e:
            self.assertEquals(True, isinstance(e, django.core.exceptions.ObjectDoesNotExist))
            

    def test_duplicated_follow(self):
        Follow(who=Man.objects.get(name="Stepan Ivanov"), whom=Man.objects.get(name="Modest Musorgsky")).save()
        self.assertEqual(len(Follow.objects.filter(who=Man.objects.get(name="Stepan Ivanov"), whom=Man.objects.get(name="Modest Musorgsky"))), 2)
