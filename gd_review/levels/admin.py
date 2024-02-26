from django.contrib import admin

from .models import Level, Review, DIFFICULTY_VALUES


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_difficulty_display', 'author', 'level', 'text')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "difficulty":
            kwargs["choices"] = [(val, name) for name, val in DIFFICULTY_VALUES.items()]
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Level)
admin.site.register(Review, ReviewAdmin)
