from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Following(models.Model):
    seed_user = models.ForeignKey(User, on_delete= models.CASCADE , related_name="seed_user")
    followers = models.ForeignKey(User, on_delete= models.CASCADE, related_name="followers")
    

