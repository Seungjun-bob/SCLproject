from django.db import models

class Recommend(models.Model):
    recomNo = models.CharField(primary_key=True, max_length=45)
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

class Comment_re(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    recommend = models.ForeignKey("Recommend", on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# drCode	Integer	분류번호
# drCodeName	String	분류명
# recom_title	String	추천도서 제목
# recom_author	String	추천도서 작가
# recom_publisher	String	추천도서 자료출판사
# recom_file_path	String	추천도서 이미지 경로
# recommokcha 목차 내용
# recom_contents	String	추천도서 자료내용
# publishYear  추천도서 발행 연도
# recom_year	Integer	추천도서 추천년도
# recom_month	Integer	추천도서 추천월
# recome_isbn	String	추천도서 ISBN