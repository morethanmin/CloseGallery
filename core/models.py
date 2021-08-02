from django.db import models
from django.conf import settings

# Create your models here.

class Painting(models.Model):
  title = models.CharField('제목', max_length=32)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  thumbnail = models.CharField('이미지_url',max_length=300)
  def __str__(self):
      return self.title

class Review_user(models.Model):
  space_name = models.CharField('공간 이름', max_length=32)
  thumbnail = models.CharField('공간 사진',max_length=300)
  painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
  reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
      return self.reviewer.username


class Review_celebrity(models.Model):
  space_name = models.CharField('공간 이름', max_length=32)
  thumbnail = models.CharField('공간 사진',max_length=300)
  painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
  reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
      return self.reviewer.username

# for main page

class Main_event_slide(models.Model):
  title = models.CharField('제목', max_length=300)
  type = models.CharField('이벤트 타입', max_length=32)
  comment = models.CharField('코멘트', max_length=300)
  btn_comment = models.CharField('버튼 코멘트', max_length=300)
  thumbnail = models.CharField('이미지_url', max_length=300)
  def __str__(self):
      return self.title

class Weekly_painting(models.Model):
  painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
  def __str__(self):
      return self.painting.title



