# django-highlightselect-model-admin

## Description
A Django App that highlights selected rows on the admin UI.

### Usage

#### Installation
   
    pip install django-highlightselect-model-admin

#### in settings.py

    INSTALLED_APPS = [
    ...
    'highlightselect_model_admin',
    ...
    ]
    
### collect statics

    python manage.py collectstatic
    
#### in admin.py
    
    from highlightselect_model_admin import HighLightSelectModelAdmin
    from .model import MyModel
    
    @admin.register(MyModel)
    class MyModelAdmin(HighLightSelectModelAdmin):
        """
        Inherit from HighLightSelectModelAdmin insead of django.contrib.admin.ModelAdmin
        """
        ...
        action = ('my_action', )
        
        def my_action(self, request, queryset):
            selected_ids = []
            for q in queryset:
                selected_ids.append(q.id)
            
             self.highlight_message_user(request, 'Selected!', selected_ids)

### Issues
https://github.com/laonan/django-highlightselect-model-admin/issues
