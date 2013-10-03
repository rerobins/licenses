from django.contrib import admin
from licenses.models import License, LicensedSoftware


class LicenseAdmin(admin.ModelAdmin):
    pass


class LicensedSoftwareAdmin(admin.ModelAdmin):
    pass

admin.site.register(License, LicenseAdmin)
admin.site.register(LicensedSoftware, LicensedSoftwareAdmin)

