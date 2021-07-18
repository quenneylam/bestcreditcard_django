from django.contrib import admin
from .models import CardInformation, Partner, PartnerToProduct

# Register your models here.

admin.site.register(CardInformation)
admin.site.register(Partner)
admin.site.register(PartnerToProduct)

