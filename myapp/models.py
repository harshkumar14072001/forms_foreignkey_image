from django.db import models

class author(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return self.name


class books(models.Model):
    title = models.CharField(max_length=20)
    pages= models.IntegerField()
    image=models.FileField(upload_to='pic',null=True)
    created_by=models.ForeignKey(author,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
# Create your models here.
