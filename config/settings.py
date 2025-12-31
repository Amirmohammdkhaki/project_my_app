from pathlib import Path

# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# امنیت
SECRET_KEY = 'django-insecure-xxxxxx'
DEBUG = True
ALLOWED_HOSTS = ["*"]   # در حالت توسعه همه درخواست‌ها مجازند

# اپلیکیشن‌ها
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # اپ‌های پروژه
    'accounts',
    'pages',

    # crispy forms + bootstrap
    'crispy_forms',
    'crispy_bootstrap4',
]

# میان‌افزارها
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# قالب‌ها
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # پوشه templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# دیتابیس (هماهنگ با docker-compose.yml)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',          # همان POSTGRES_DB
        'USER': 'myuser',        # همان POSTGRES_USER
        'PASSWORD': 'mypassword',# همان POSTGRES_PASSWORD
        'HOST': 'db',            # نام سرویس در docker-compose.yml
        'PORT': 5432,
    }
}

# اعتبارسنجی پسورد
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# زبان و زمان
LANGUAGE_CODE = 'fa'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# فایل‌های استاتیک (CSS/JS)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]   # جایی که خودت css/js می‌ذاری
STATIC_ROOT = BASE_DIR / "staticfiles"     # جایی که collectstatic می‌ریزه

# مدیریت کش فایل‌های استاتیک
if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# فایل‌های مدیا (آپلود کاربر)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# کلید پیش‌فرض
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# مدل کاربر سفارشی
AUTH_USER_MODEL = 'accounts.CustomUser'

# مسیرهای ورود و خروج
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"