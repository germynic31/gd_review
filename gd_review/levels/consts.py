from django.db.models import Count


# forms
DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'

# views and mixins
COUNT_POSTS_ON_PAGE = 10
PK_URL_KWARG_FOR_LEVELS = 'level_id'


SETTINGS_RELATED = [
    'author',
]
SETTINGS_ORDER_BY = [
    '-pub_date',
]
