from django.contrib import admin

from .. import models

# Register your models here.
# To get django model: models.<ModelName>.DjangoModel

admin.site.register(models.TelegramUser.DjangoModel)
admin.site.register(models.HelpRequest.DjangoModel)
