from django.contrib import admin
from .models import Post
from .models import Client
from .models import Bot
from .models import Deal
from .models import Admin
from .models import Purchase
from .models import Developer

admin.site.register(Post)
admin.site.register(Client)
admin.site.register(Bot)
admin.site.register(Deal)
admin.site.register(Admin)
admin.site.register(Developer)
 