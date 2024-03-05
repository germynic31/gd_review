from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from levels.consts import COUNT_POSTS_ON_PAGE
from levels.models import Review
from .models import MyUser


class UsersView(ListView):
    model = MyUser
    template_name = 'users/users.html'
    paginate_by = COUNT_POSTS_ON_PAGE

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = MyUser.objects.filter(
                Q(username__icontains=query)
            )
            return object_list
        queryset = self.model.objects.order_by(
            'username',
        )
        return queryset


class ProfileView(DetailView):
    model = MyUser
    template_name = 'users/profile.html'
    pk_url_kwarg = 'username'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, username=self.kwargs.get(self.pk_url_kwarg))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.select_related('author')
        return context

