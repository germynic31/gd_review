from .models import Level


class GetQuerysetMixin:
    model = Level

    def get_queryset(self):
        queryset = self.model.objects.prefetch_related(
            *SETTINGS_RELATED
        ).annotate(
            **SETTINGS_ANNOTATE
        ).order_by(
            *SETTINGS_ORDER_BY
        ).filter(
            pub_date__lte=timezone.now(),
            **SETTINGS_FILTER
        )
        return queryset
