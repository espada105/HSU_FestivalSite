from django.db import models

# Create your models here.

class intruduce(models.Model):
    title = models.CharField(max_length=100) # 부스 이름 적기
    shortin = models.CharField(max_length=100) # 부스 리스트에 적힐 소개문구
    intruduce = models.CharField(max_length=500) # 부스 디테일에 적힐 소개문구
    likecount = models.PositiveIntegerField(default=0)
    x = models.IntegerField(default=0,null=True)
    y = models.IntegerField(default=0,null=True)
    loc = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True,blank=True)
    imagecheack = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/intru/{self.pk}/'
    
    def like_url(self):
        return f'/intru/like/{self.pk}/'

