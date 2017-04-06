from django.contrib import admin
from .models import Article, Person


# Register your models here.
# admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)

    def save_model(self, request, obj, form, change):
        if change:  # 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:  # 新增的时候
            obj_original = None

        obj.user = request.user
        obj.save()

        def delete_model(self, request, obj):
            """
            Given a model instance delete it from the database.
            """
            # handle something here
            obj.delete()


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
