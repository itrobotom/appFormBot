from django.contrib import admin
# для регистации модели добавим: 
from sitetomadmin.models import requestOrder

admin.site.register(requestOrder)