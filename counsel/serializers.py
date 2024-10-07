from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Counsel

class CounselSerializer(ModelSerializer):
    customer = StringRelatedField()  # 고객 이름을 출력

    class Meta:
        model = Counsel
        fields = '__all__'
        # fields = ['id', 'customer', 'category', 'description', 'status', 'created_at', 'updated_at',]