from django.db import models
from customer.models import Customer


class Counsel(models.Model):
    CATEGORY_CHOICES = [
        ('일반', '일반 문의'),
        ('정보', '고객 정보 변경'),
        ('불편', '불편 민원'),
        ('안내', '결과 안내'),
    ]

    # 상담과 연결된 고객 정보 (외래 키)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='counsels')

    # 상담 카테고리 (선택 필드)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    # 상담 내용
    description = models.TextField()

    # 상담 일시
    created_at = models.DateTimeField(auto_now_add=True)

    # # 상담 담당자 (User 모델과 연결)
    # assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # 상담 상태 (예: 진행 중, 완료 등)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ])

    # 상담 기록 업데이트 시각
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name} - {self.get_category_display()}"

    class Meta:
        verbose_name = "Counsel"
        verbose_name_plural = "Counsels"
        ordering = ['-created_at']
