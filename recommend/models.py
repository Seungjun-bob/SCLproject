from django.db import models

class Recommend(models.Model):
    recomNo = models.CharField(max_length=45)
    drCode = models.CharField(max_length=45, null=True)
    drCodeName = models.CharField(max_length=45, null=True)
    recomtitle = models.CharField(max_length=125, null=True)
    recomauthor = models.CharField(max_length=45, null=True)
    recompublisher = models.CharField(max_length=45, null=True)
    recomfilepath = models.TextField(null=True)
    recommokcha = models.TextField(null=True)
    recomcontens = models.TextField(null=True)
    publishYear = models.TextField(null=True)
    recomYear = models.CharField(max_length=45, null=True)
    recomMonth = models.CharField(max_length=45, null=True)
    recomisbn = models.CharField(max_length=45, null=True)


class RecommendComment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    recommend = models.ForeignKey("Recommend", on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

