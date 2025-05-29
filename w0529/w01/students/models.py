from django.db import models

class Student(models.Model):
    # 순번이 순차적으로 증가
    no = models.AutoField(primary_key=True)     # Sequence
    name = models.CharField(max_length=100)     # varchar2
    major = models.CharField(max_length=100)
    # 숫자 타입
    grade = models.IntegerField(default=0)      # number
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=30, blank=True)    # 추가
    hobby = models.CharField(max_length=100, blank=True)    # 추가
    sdate = models.DateTimeField(auto_now=True) # date - sysdate
    memo = models.TextField(blank=True)         # clob
    

    def __str__(self):      # 관리자페이지 뿐만 아니라 다른 곳에서도 객체를 볼 수 있게 하는 함수
        return f"{self.no}, {self.name}, {self.sdate}"