from django.db import models

class User(models.Model):
    userid = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    def __unicode__(self):
        return self.userid

class App(models.Model):
    appid = models.CharField(max_length=128, unique=True)
    appname = models.CharField(max_length=128)
    description = models.TextField()
    averscore = models.FloatField()
    developer = models.CharField(max_length=128)
    iconurl = models.URLField()
    imageurl1 = models.URLField()
    imageurl2 = models.URLField()
    imageurl3 = models.URLField()

    def __unicode__(self):
        return self.appname

class Comment(models.Model):
    user = models.ForeignKey(User)
    app = models.ManyToManyField(App)
    score = models.IntegerField(default=0)
    content = models.TextField();
    date = models.DateField();

    def __unicode__(self):
        return self.content