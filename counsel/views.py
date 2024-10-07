from django.db.models import Q
from rest_framework import status
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from counsel.models import Counsel
from counsel.serializers import CounselSerializer
from customer.models import Customer


class CounselListCreateView(ListCreateAPIView):
    model = Counsel
    serializer_class = CounselSerializer

    def get_queryset(self):
        customer_pk = self.kwargs['customer_pk']  # URL에서 customer_pk 가져오기
        queryset = Counsel.objects.filter(customer__pk=customer_pk)  # 특정 고객의 counsel만 필터링

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(category__icontains=q) |
                Q(description__icontains=q)
            )
        return queryset

    def create(self, request, *args, **kwargs):
        customer_pk = self.kwargs['customer_pk']  # URL에서 customer_pk 가져오기
        customer = get_object_or_404(Customer, pk=customer_pk)  # 고객 객체 가져오기

        # 고객 정보를 시리얼라이저에 포함해서 저장
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=customer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class CounselDetailView(RetrieveUpdateDestroyAPIView):
    model = Counsel
    serializer_class = CounselSerializer
    queryset = Counsel.objects.all()