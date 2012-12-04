from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class {{model_name}}(object):

#    user = models.ForeignKey(User)

    def __unicode__(self):
        pass

    def get_absolute_url(self):
        return reverse({{app_name}}_detail, args=[str(self.id)])
