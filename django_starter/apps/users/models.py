from django.db import models
from django.contrib.auth.models import User
import uuid, os

def avatarUploadToFn(i, filename):
    return os.path.join('avatars', "%s.%s" % (uuid.uuid4(), filename.split('.')[-1]))

class Profile(models.Model):

  # Fields
  user = models.OneToOneField(User)

  role = models.CharField(
    max_length=2,
    choices=(('U', 'User'),
             ('A', 'Admin')),
    blank=False,
    default="G"
  )

  avatar = models.ImageField(
    upload_to=avatarUploadToFn,
    blank=True,
    default=""
  )

  joined_timestamp = models.DateTimeField(
    auto_now_add=True,
    editable=False
  )

  def __str__(self):
    return self.user.first_name+" "+self.user.last_name

  def name(self):
    return self.user.first_name+" "+self.user.last_name

