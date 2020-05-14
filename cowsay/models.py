from django.db import models


class CowText(models.Model):
    text = models.CharField(max_length=60)

    def __str__(self):
        return self.text
