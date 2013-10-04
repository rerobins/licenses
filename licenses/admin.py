from django.contrib import admin
from licenses.models import License, LicensedSoftware
from django.conf import settings

use_admin = False

try:
    use_admin = settings.LICENSE_ADMIN
except AttributeError:
    use_admin = False


class LicenseAdmin(admin.ModelAdmin):
    pass


class LicensedSoftwareAdmin(admin.ModelAdmin):
    pass

if use_admin:
    admin.site.register(License, LicenseAdmin)
    admin.site.register(LicensedSoftware, LicensedSoftwareAdmin)

