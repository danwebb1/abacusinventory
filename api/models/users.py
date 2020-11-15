from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    portal_firestore_key = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'users'
        app_label = 'User'

