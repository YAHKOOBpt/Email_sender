from django.db import models

# Create your models here.
class Todo(models.Model):
    name=models.CharField(max_length=100,null=False,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100 ,null=True,blank=True)
    post=models.IntegerField(50,null=True,blank=True)
    phone=models.IntegerField(60,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    document_name=models.FileField(upload_to="upload",null=True,blank=True)

#     def __str__(self):
#         return self.todo_name