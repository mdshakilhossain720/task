from django.db import models


# Create your models here.

class PostModel(models.Model):
    title=models.CharField(max_length=100)
    #memberid = models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    



