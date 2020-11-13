SECRET_KEY = '1%^$!=rwey6_w$p)=txsh964jsaoyu4mja)w$8ikx08@ifmbas'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['139.59.71.156']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'engineers_tech',
        'USER': 'rohit',
        'PASSWORD':'jamshedpur',
        'HOST':'localhost',
        # 'PORT': '',
    }
}

EMAIL_USE_TLS = True
Email_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'bharatengineering789@gmail.com'
EMAIL_HOST_PASSWORD = 'Bharat@123'
EMAIL_PORT = 587