from django.db import models

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
