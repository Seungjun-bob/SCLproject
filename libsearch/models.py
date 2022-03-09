from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Library(models.Model):
    lbrry_seq_no = models.CharField(primary_key=True, max_length=45)
    lbrry_name = models.CharField(max_length=45)
    gu_code = models.CharField(max_length=10, null=True)
    code_value = models.CharField(max_length=45)
    adres = models.CharField(max_length=45)
    tel_no = models.CharField(max_length=45, null=True)
    hmpg_url = models.CharField(max_length=200, null=True)
    op_time = models.CharField(max_length=200, null=True)
    fdrm_close_date = models.CharField(max_length=200, null=True)
    lbrry_se_name = models.CharField(max_length=45)
    xcnts = models.FloatField(null=True)
    ydnts = models.FloatField(null=True)
    avg = models.FloatField(null=True)

class LibraryComment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    library = models.ForeignKey("Library", on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(5)])

