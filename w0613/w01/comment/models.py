from django.db import models
from board.models import Board
from member.models import Member

class Comment(models.Model):
    cno = models.AutoField(primary_key=True)                        # primary key가 있어야 에러 X
    board = models.ForeignKey(Board, on_delete=models.CASCADE)      # 게시글 삭제 시 하단 댓글 모두 삭제
    # member = models.CharField(max_length=100, defualt='aaa') # 그대로
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True)   # 작성자 탈퇴 시 NULL 집어넣음
    cpw = models.CharField(max_length=20, null=True, blank=True)
    ccontent = models.TextField(blank=True)
    cdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.cno}, {self.member.id}, {self.ccontent}"