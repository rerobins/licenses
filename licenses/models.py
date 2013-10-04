from django.db import models


class License(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)
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
    version = models.CharField(max_length=50, blank=True)
    source_url = models.URLField(blank=True)
    license = models.ForeignKey(License, blank=True)
    website_url = models.URLField(max_length=256, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        """
            Means of printing out basic information for this record.
        """
        return "Software: %s" % self.name

    class Meta:
        ordering = ['name']
