from django.contrib import admin
from .models import Bot
from .models import Deal
from .models import Admin
from .models import Purchase
from .models import Developer
from .models import Category
from .models import Comment
from .models import Response
from .models import users_token

admin.site.register(Bot)
admin.site.register(Deal)
admin.site.register(Admin)
admin.site.register(Purchase)
admin.site.register(Developer)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Response)
admin.site.register(users_token)
