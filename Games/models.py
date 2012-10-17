from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    release_date = models.DateTimeField()           #not required
    publisher = models.CharField(max_length=100)    #not required
    developer = models.CharField(max_length=100)    #not required
    metascore = models.IngegerField()               #not required
    description = models.CharField(max_length=2000) #not required
    box_art = models.URLField()                     #not required
    esrb_rating = models.CharField(max_lenth=2)     #not required
    esrb_reason = models.CharField(max_length=1000)

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField()
    salt = models.CharField()
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField()
    birth_date = models.DateTimeField()
    
class Store(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    url = models.URLField()
    game_url = models.URLField()
    icon = models.URLField()
    
class Sells(models.Model):
    store = models.ForeignKey(Store)
    game = models.ForeignKey(Game)
    store_id = models.CharField()
    retail_price = models.FloatField()
    current_price = models.FloatField()         #not required - default to retail price
    timestamp = models.DatetimeField(auto_now=True)
    digital = models.Booleanfield(default=True)
    
class Wants(models.Model):
    username = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    desired_price = models.FloatField()         #not required
    notify_me = models.BooleanField()           #not required
    prefered_store = models.ForeignKey(Store)   #not required

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=40)

class GameTags(models.Model):
    game = models.ForeignKey(Game)
    tag_id = models.ForeignKey(Tag)

class SearchHistory(models.Model):
    username = models.ForeignKey(User)
    search_term = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now=True)
    
