from django.core.management.base import BaseCommand, CommandError
from ask.models import Question, Profile, Answer, Tags_Question
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Fill the database'

    def handle(self, *args, **options):
        u = User.objects.create_user(
            username = 'New',
            first_name = 'Ilya',
            last_name = 'Nikitin',
            password = 'password',
            email = 'email@mail.ru',
            last_login = datetime.datetime(2013, 4, 29, 15, 59),
        )
        # User.objects.create_user
        p = Profile(
            profile = u,
            profile_avatar = 'cute-cat.jpg',
        )
        p.save()
        tag1 = Tags_Question(
                tag_question = 'Mozilla',
        )
        tag1.save()
        tag2 = Tags_Question(
                tag_question = 'Web'
        )
        tag2.save()
        tag3 = Tags_Question(
                tag_question = 'Dz'
            )
        tag3.save()
        for j in range (1,50):
            q = Question(
                profile = u,
                question_title = 'How to build a moonpark?',
                question_text = 'I want to build a moonpark. What should I do?',
                question_num_answers = 10,
                question_rank = j * 10,
            )
            q.save()
            q.question_tag.add(tag1)
            q.question_tag.add(tag2)
            q.question_tag.add(tag3)
            for k in range(1,50):
                a = Answer(
                    question = q,
                    profile = u,
                    answer_text = 'I dont know',
                    answer_rank = 9 * k,
                )
                a.save()

