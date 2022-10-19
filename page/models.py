from django.db import models

# Create your models here.
# Post 모델 작성
class Posting(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # [코드 작성] admin 페이지에서 Posting 객체들이 title로 보여지도록 코드 작성
    def __str__(self):
        return self.title