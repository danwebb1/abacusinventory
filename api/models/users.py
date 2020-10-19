from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    portal_key = models.CharField(max_length=50)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
