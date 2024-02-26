from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg
from django.utils import timezone

User = get_user_model()

DIFFICULTY_VALUES = {
    'AUTO': 1,
    'EASY': 2,
    'NORMAL': 3,
    'HARD': 4,
    'HARDER': 5,
    'INSANE': 6,
    'EASY DEMON': 7,
    'MEDIUM DEMON': 8,
    'HARD DEMON': 9,
    'INSANE DEMON': 10,
    'EXTREME DEMON': 11,
}


class Level(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    difficulty = models.IntegerField(
        choices=[(val, name) for name, val in DIFFICULTY_VALUES.items()]
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(
        blank=True,
        default=timezone.now,
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время '
                   'в будущем — можно делать отложенные публикации.'),
    )

    def average_difficulty(self):
        reviews = self.review_set.all()
        avg_difficulty = reviews.aggregate(Avg('difficulty'))
        return avg_difficulty['difficulty__avg'] if avg_difficulty['difficulty__avg'] else 0

    def __str__(self):
        return self.title[:50]


class Review(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.IntegerField(choices=[(val, name) for name, val in DIFFICULTY_VALUES.items()])
    text = models.TextField(max_length=1024)

    def __str__(self):
        return self.text[:50]
