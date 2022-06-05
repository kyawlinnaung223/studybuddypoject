
from django.db import models
from django.contrib.auth.models import User

# Create your models here
#this is topic models
class Topic(models.Model):
    name=models.TextField(max_length=200)
    def __str__(self):
        return self.name

#end topic modles

#this is room models
class Room(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    participants=models.ManyToManyField(User,related_name='participants', blank=True)
    update=models.DateTimeField(auto_now=True)
    Created=models.DateTimeField(auto_now_add=True)
  
    
    def __str__(self):
        return self.name
    # end room modles
    #start messages modles
    
class Messages(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    update=models.DateTimeField(auto_now=True)
    Created=models.DateTimeField(auto_now_add=True)
    #end messages modles
    
    def __str__(self):
        return self.body [0:50]
    

    

    