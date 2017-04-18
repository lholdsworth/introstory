import os

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ['AKIAIAOE7IE5P6UEQA2A']
AWS_SECRET_ACCESS_KEY = os.environ['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']
AWS_STORAGE_BUCKET_NAME = os.environ['intro-story']
MEDIA_URL = 'http://%s.s3.amazonaws.com/assets/' % AWS_STORAGE_BUCKET_NAME

DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"