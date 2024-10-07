from rest_framework.relations import RelatedField, ManyRelatedField, HyperlinkedRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Customer, FamilyGroup
from counsel.serializers import CounselSerializer

class FamilySerializer(ModelSerializer):
    group_name = PrimaryKeyRelatedField(read_only=True)
    members = StringRelatedField(many=True)

    class Meta:
        model = FamilyGroup
        fields = ['id', 'members', 'group_name', ]

class CustomerSerializer(ModelSerializer):
    counsels = CounselSerializer(many=True, read_only=True)  # 고객의 상담 리스트
    family_members = FamilySerializer(many=True, read_only=True) # 고객의 가족 리스트

    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'address', 'email', 'created_at', 'updated_at', 'counsels','family_members',]


