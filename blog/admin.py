from django.contrib import admin
from .models import cliente
from .models import orden
from .models import tecnico

admin.site.register( cliente )
admin.site.register( orden )
admin.site.register( tecnico )

