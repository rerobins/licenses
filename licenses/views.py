# Create your views here.
from django.views.generic import ListView
from licenses.models import LicensedSoftware


class LicensedSoftwareListView(ListView):
    model = LicensedSoftware
    context_object_name = 'software_list'
