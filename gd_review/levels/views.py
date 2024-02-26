from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from .consts import COUNT_POSTS_ON_PAGE, SETTINGS_RELATED, SETTINGS_ORDER_BY
from .models import Level


def level_list(request):
    return render(request, 'levels/level_list.html')


class LevelView(ListView):
    template_name = 'levels/level_list.html'
    paginate_by = COUNT_POSTS_ON_PAGE
    model = Level

    def get_queryset(self):
        queryset = self.model.objects.prefetch_related(
            *SETTINGS_RELATED
        ).order_by(
            *SETTINGS_ORDER_BY
        ).filter(
            pub_date__lte=timezone.now()
        )
        return queryset
