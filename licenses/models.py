from django.db import models

# Create your models here.
# Description Implementation of a website using the Automaintenance library.
#License Affero General Public License
#Version 1.0
#Website None
#Source None


class License(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    text = models.TextField()

    def __unicode__(self):
        """
            Means of printing out basic information for this record.
        """
        return self.name

    class Meta:
        ordering = ['name']


class LicensedSoftware(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    source_url = models.URLField()
    license = models.ForeignKey(License)
    website_url = models.URLField(max_length=256)
    description = models.TextField()

    class Meta:
        ordering = ['name']
