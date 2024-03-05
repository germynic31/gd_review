from django.db.models import Count


# forms
DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'

# views and mixins
COUNT_POSTS_ON_PAGE = 9
PK_URL_KWARG_FOR_LEVEL = 'level_id'


SETTINGS_RELATED = [
    'author',
]
SETTINGS_ORDER_BY = [
    '-pub_date',
]
