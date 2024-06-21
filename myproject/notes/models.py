from django.db import models

class Notes(models.Model):
    tittle = models.CharField((""), max_length=50)
    text = models.TextField((""))
    created = models.DateTimeField(auto_now_add=True)

