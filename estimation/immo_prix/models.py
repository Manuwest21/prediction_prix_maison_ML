from django.db import models



class Formu(models.Model):
    # client = models.ForeignKey(max_length=100,
    #     on_delete=models.CASCADE,
    #     null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(default='Notes client:')
    creation_date = models.DateTimeField(auto_now_add=True)