from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Board(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.FileField(blank=True, upload_to="photo_%Y_%m_%d")
    view_cnt = models.PositiveIntegerField(default=0)
    Cdate = models.DateTimeField(auto_now_add=True)


    @property
    def view_counter(self):
        self.view_cnt = self.view_cnt + 1
        self.save()

class Comment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    board = models.ForeignKey("Board", on_delete=models.CASCADE)
    comment = models.TextField()
    Cdate = models.DateTimeField(auto_now_add=True)