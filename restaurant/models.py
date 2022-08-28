from django.db import models

from accounts.models import User as UserModel


class Restaurant(models.Model):
    """
    Assignee : 상백

    User 모델과 1:N 관계를 가지는 Restaurant 모델입니다.
    사용자가 원하는 식당을 설정하는 모델로 이름과 시작 금액을 설정할 수 있습니다.
    또한, 삭제가 진행되는 경우 is_deleted 필드를 True로 변경합니다.
    """

    name = models.CharField("식당 이름", max_length=30)
    user = models.ForeignKey(to=UserModel, verbose_name="사용자", on_delete=models.CASCADE, related_name="user_restaurant")
    balance = models.IntegerField("시작 금액", default=0)
    is_deleted = models.BooleanField("삭제 여부", default=False)
    created_at = models.DateTimeField("생성일자", auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)


class AccountBookRecord(models.Model):
    """
    Assignee : 상백

    Restaurant 모델과 1:N 관계를 가지는 AccountBookRecord 모델입니다.
    하나의 Restaurant에 특정 날짜에 속하는 금액 및 메모를 기록할 수 있도록 설정합니다.
    또한, 삭제가 진행되는 경우 is_deleted 필드를 True로 변경합니다.
    """

    restaurant = models.ForeignKey(
        to=Restaurant, verbose_name="식당", on_delete=models.CASCADE, related_name="restaurant_record"
    )
    data = models.DateField("날짜")
    amount = models.IntegerField("금액", default=0)
    memo = models.CharField("메모", max_length=200)
    is_deleted = models.BooleanField("삭제 여부", default=False)
    created_at = models.DateTimeField("생성일자", auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)
