from django.contrib import admin
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)

from .models import gods_crist_m, insulti_h_m, insulti_s_m, insulti_n_m

admin.site.register(gods_crist_m)
admin.site.register(insulti_h_m)
admin.site.register(insulti_s_m)
admin.site.register(insulti_n_m)
