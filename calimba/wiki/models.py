from django.db import models

import logging

logger = logging.getLogger(__name__)

# Create your models here.
class Page(models.Model):
  
  name = models.CharField(max_length="20")
  slug = models.SlugField(max_length = 64)
  content = models.TextField(blank=True)
  pub_date = models.DateTimeField(blank=True, null = True)
  

  def list_pages(self, limit=5):
    pages = Page.objects.all()
    logger.info(__name__ + ' pages count: ' + str(pages.count()))
    return pages
  
class Tag(models.Model):
  name = models.CharField(max_length="20")
  