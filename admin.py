from django.contrib import admin
from {{app_name}}.models import {{model_name}}

class {{model_name}}Admin(admin.ModelAdmin):
	#list_filter = ('',)
	#list_display = ('',)
	#ordering = ('',)
	#search_fields = ('',)

admin.site.register({{model_name}}, {{model_name}}Admin)
