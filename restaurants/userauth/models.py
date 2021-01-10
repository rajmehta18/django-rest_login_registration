from django.db import models
import uuid
import hashlib
# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    #favourite  = models.CharField(max_length=250,null=True,blank=True)
    
    def __str__(self):
        return self.firstname + " " + self.lastname

    def save(self, *args, **kwargs):
        raj=self.password
        self.password = hashlib.md5(self.password.encode())
        self.password = self.password.hexdigest()
        super(User, self).save(*args, **kwargs)    

class Favourite(models.Model):
    favourite = models.CharField(max_length=250,null=True,blank=True)
    fav = models.ForeignKey(User,on_delete=models.CASCADE,related_name='favourites')

    def __str__(self):
        return self.favourite