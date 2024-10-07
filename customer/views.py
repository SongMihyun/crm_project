from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, ListAPIView
from customers.models import Customer, FamilyGroup
from customers.serializers import CustomerSerializer, FamilySerializer
from utils.search import SearchMixin

# http://127.0.0.1:8000/customer/
class CustomerListCreateView(SearchMixin,ListCreateAPIView):
    model = Customer
    serializer_class = CustomerSerializer

# http://127.0.0.1:8000/customer/1/
class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    model = Customer
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all().prefetch_related('family_members','counsels')


################<<가족 그룹>>######################
# 개인별 가족 그룹 리스트 및 생성 뷰
class CustomerFamilyListCreateView(ListCreateAPIView):
    model = FamilyGroup
    serializer_class = FamilySerializer
    # queryset = FamilyGroup.objects.all()
    def get_queryset(self):
        customer_pk = self.kwargs['customer_pk']
        queryset = FamilyGroup.objects.filter(members__pk=customer_pk)
        return queryset

# 가족 그룹 수정 및 삭제 뷰
class CustomerFamilyDetailView(RetrieveUpdateDestroyAPIView):
    model = FamilyGroup
    queryset = FamilyGroup.objects.all()
    serializer_class = FamilySerializer

# 전체 가족 그룹 조회및 생성
class FamilyGroupListCreateView(ListCreateAPIView):
    model = FamilyGroup
    serializer_class = FamilySerializer
    queryset = FamilyGroup.objects.all()

class FamilyDetailView(RetrieveUpdateDestroyAPIView):
    model = FamilyGroup
    queryset = FamilyGroup.objects.all()
    serializer_class = FamilySerializer



##################<<html과 연결 뷰>>####################
# 고객 리스트 페이지를 보여주는 HTML View (CBV)
class CustomerListPageView(TemplateView):
    template_name = 'customer/customer_list.html'

class CustomerDetailPageView(TemplateView):
    template_name = 'customer/customer_detail.html'
