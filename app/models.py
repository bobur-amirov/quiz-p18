from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'kategoriya'
        verbose_name_plural = 'kategoriyalar'
        ordering = ['-name']


class Question(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_correct_check(self, id):
        return self.answers.filter(id=id, is_correct=True).exists()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    name = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_question = models.IntegerField(default=0)
    total_correct = models.IntegerField(default=0)
    score = models.FloatField(default=0)

    def __str__(self):
        return self.user.phone

    def save(self, *args, **kwargs):
        self.score = (self.total_correct * 100) / self.total_question
        return super().save(*args, **kwargs)

    @property
    def is_passed(self):
        return self.score >= 60

    @property
    def is_failed(self):
        return self.score < 60
