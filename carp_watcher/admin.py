from django.contrib import admin
from carp_watcher.models import Fish, Stream, Data_Stream

# Register your models here.

admin.site.register(Fish)
admin.site.register(Stream)
admin.site.register(Data_Stream)
