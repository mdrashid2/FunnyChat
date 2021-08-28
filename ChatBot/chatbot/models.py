from django.db import models
from django.contrib.auth.models import User

class Audit(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fat = models.IntegerField(default=0)
    dumb = models.IntegerField(default=0)
    stupid = models.IntegerField(default=0)

    def update_counts(self, joke_type):

        if joke_type == 'fat':
            self.fat += 1
        elif joke_type =='dumb':
            self.dumb += 1
        else:
            self.stupid += 1
        self.save()
    