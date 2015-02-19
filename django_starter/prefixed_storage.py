import storages.backends.s3boto

class PrefixedStorage(storages.backends.s3boto.S3BotoStorage):
  def __init__(self, *args, **kwargs):
    from django.conf import settings
    kwargs['location'] = settings.ASSETS_PREFIX
    return super(PrefixedStorage, self).__init__(*args, **kwargs)
