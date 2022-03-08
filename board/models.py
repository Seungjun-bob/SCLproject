from django.db import models
from libsearch.models import Library
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    view_cnt = models.PositiveIntegerField(default=0)
    Cdate = models.DateTimeField(auto_now_add=True)
    Udate = models.DateTimeField(auto_now=True)
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    starpoint = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    review = models.ForeignKey("Review", on_delete=models.CASCADE)
    comment = models.TextField()
    Cdate = models.DateTimeField(auto_now_add=True)
    Udate = models.DateTimeField(auto_now=True)