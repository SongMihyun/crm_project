
from django.db.models import Q

# 고객 검색 Mixin
# model = Customer / model = Consult ...
#    <div class="search_area">
#         <form method="get">
#             {% csrf_token %}
# {#                고객이름 혹은 전화번호중에 일치하는값이 있는지 검색해서 보여줌#}
#             <input name="q" type="text" placeholder="이름 or 전화번호" value="{% if request.GET.q %}{{ request.GET.q }}{% endif %}">
#             <button>검색</button>
#         </form>
#     </div>
class SearchMixin:
    paginate_by = 5

    def get_queryset(self,*args, **kwargs):
        queryset = self.model.objects.all().order_by('id')

        q=self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(phone__icontains=q)
            )
        return queryset
