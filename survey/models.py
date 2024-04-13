from django.db import models

# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age_group = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Question(models.Model):
    content = models.CharField(max_length=255)
    order_num = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.content

class Answer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='quizzes')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='quizzes')
    chosen_answer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.participant.name} - {self.question.content}"