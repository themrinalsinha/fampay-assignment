from django.contrib import admin
from .models        import KeyManager
from .utils         import mask_access_key

admin.site.site_header = "Fampay Admin Panel"
admin.site.site_title  = "Fampay Administrator"
admin.site.index_title = "Welcome to Fampay Admin Panel"


@admin.register(KeyManager)
class KeyManagerAdmin(admin.ModelAdmin):
    list_display = ('name', '_access_key', 'status', 'created_on', 'modified_on')

    def _access_key(self, obj):
        return mask_access_key(obj.access_key)
