from django.db.models import Q
from django.views.generic import ListView, DetailView

from .consts import COUNT_POSTS_ON_PAGE, PK_URL_KWARG_FOR_LEVEL
from .forms import ReviewForm
from .models import Level, Review


class LevelView(ListView):
    model = Level
    template_name = 'levels/level_list.html'
    paginate_by = COUNT_POSTS_ON_PAGE

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Level.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            return object_list
        queryset = self.model.objects.prefetch_related(
            'author',
        ).order_by(
            '-pub_date',
        )
        return queryset


class LevelDetailsView(DetailView):
    model = Level
    template_name = 'levels/level_detail.html'
    pk_url_kwarg = PK_URL_KWARG_FOR_LEVEL

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            id=self.kwargs[PK_URL_KWARG_FOR_LEVEL],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        context['reviews'] = Review.objects.select_related('author').filter(
            level_id=self.kwargs[PK_URL_KWARG_FOR_LEVEL],
        )
        return context
