from django.db import models

class Board(models.Model):
    bno = models.AutoField(primary_key=True)    # 기본키 등록
    id = models.CharField(max_length=100)       # 작성자
    btitle = models.CharField(max_length=1000)  # 제목
    bcontent = models.TextField()               # 내용
    # 답글 달기
    bgroup = models.IntegerField(default=0)     # 답글 달기 묶음
    bstep = models.IntegerField(default=0)      # 답글 달기 순서
    bindent = models.IntegerField(default=0)    # 들여쓰기
    # -------
    bhit = models.IntegerField(default=0)
    # FileField : 모든 파일 업로드 가능
    bfile = models.ImageField(null=True, blank=True, upload_to='board')
    bdate = models.DateTimeField(auto_now=True)     # 현재 날짜, 시간 자동등록
    
    
    def __str__(self):
        return f"{self.bno}, {self.btitle}, {self.bgroup}"