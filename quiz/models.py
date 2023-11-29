from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='question')
    question = models.TextField()

    def __str__(self):
        return self.question
    

    

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option')
    option = models.TextField()
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.option
    








