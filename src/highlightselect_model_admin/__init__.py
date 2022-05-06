from django.contrib import admin, messages
from django.utils.html import mark_safe


class HighLightSelectModelAdmin(admin.ModelAdmin):
    def highlight_message_user(self, request, message, ids, level=messages.SUCCESS, fail_silently=False):
        self.message_user(request,
                          mark_safe(f'{message} <input id="selected_ids" type="hidden" value="{ids}" />'),
                          level=level, fail_silently=fail_silently)

    class Media:
        js = ('admin/js/jquery.init.js', 'highlightselect_model_admin/js/highlight_selected_rows.js', )
