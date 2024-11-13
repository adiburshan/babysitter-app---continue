from django.contrib import admin
from .models import Babysitter, Meetings, Requests, TimeWindow
from .models import Parents
from .models import Kids
from .models import Reviews
from .models import Availability



admin.site.register(Kids)
admin.site.register(Meetings)
admin.site.register(Reviews)
admin.site.register(Availability)
admin.site.register(Requests)
admin.site.register(TimeWindow)
admin.site.register(Parents)
admin.site.register(Babysitter)



