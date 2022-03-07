from django.db import models
from libsearch.models import Library
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    view_cnt = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    starpoint = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField()