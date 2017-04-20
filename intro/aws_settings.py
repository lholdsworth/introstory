import os

# AWS_QUERYSTRING_AUTH = False
# AWS_ACCESS_KEY_ID = os.environ['AKIAIAOE7IE5P6UEQA2A']
# AWS_SECRET_ACCESS_KEY = os.environ['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']
# AWS_STORAGE_BUCKET_NAME = os.environ['intro-story']
# MEDIA_URL = 'http://%s.s3.amazonaws.com/assets/' % AWS_STORAGE_BUCKET_NAME

# DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"


AWS_STORAGE_BUCKET_NAME = 'intro-story'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'