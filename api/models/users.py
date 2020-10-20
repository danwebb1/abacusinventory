from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    app_id = models.CharField(max_length=50)
    portal_key = models.CharField(max_length=50)

    class Meta:
        app_label = 'User'

