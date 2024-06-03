import os
from pathlib import Path
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url
# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '188.166.144.19',
    '8000-jesseross00-cleandesign-p60uhvpp848.ws-eu114.gitpod.io',
    'cleandesignuk.uk',
    'cleandesignuk.com',
    'localhost',
    '127.0.0.1',
    'cleandesignuk.uk:8000',
    '127.0.0.1:8000',
    
]

CSRF_TRUSTED_ORIGINS = [
    'http://188.166.144.19',
    'http://8000-jesseross00-cleandesign-p60uhvpp848.ws-eu114.gitpod.io',
    'http://cleandesignuk.uk',
    'http://cleandesignuk.com',
    'http://cleandesignuk.uk:8000'
    # You can add HTTPS versions as well if applicable
    'https://188.166.168.22',
    'https://8000-jesseross00-cleandesign-p60uhvpp848.ws-eu114.gitpod.io',
    'https://cleandesignuk.uk',
    'https://cleandesignuk.com',
    'https://127.0.0.1:8000'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_ckeditor_5',
    'corsheaders',
    'cloudinary',
    'cloudinary_storage',
    'home',  # add this
    'blog',  # add this
    'about',  # add this
    'project_gallery',  # add this
    'packages_services',  # add this
    'contact',  # add this

]





cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

#CORS_ALLOWED_ORIGINS = [
#    'https://8000-jesseross00-cleandesign-p60uhvpp848.ws-eu114.gitpod.io',
#    'https://gitpod.io',
#    'https://cleandesignuk.uk',
#    'https://cleandesignuk.com',
#    'http://127.0.0.1:8000',
#    'https://8000-jesseross00-cleandesign-p60uhvpp848.ws-eu114.gitpod.io'
#    ]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',  # This should be near the top
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
#   'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',  # This should be near the bottom
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this if your base.html is in a global templates directory
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

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),  # Read database name from environment variables
        'USER': os.getenv('DB_USER'),  # Read database user from environment variables
        'PASSWORD': os.getenv('DB_PASSWORD'),  # Read database password from environment variables
        'HOST': os.getenv('DB_HOST'),  # Read database host from environment variables
        'PORT': os.getenv('DB_PORT'),  # Read database port from environment variables
        'OPTIONS': {
            'sslmode': os.getenv('DB_SSLMODE'),  # This is required for Digital Ocean's managed databases
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}


CACHE_MIDDLEWARE_ALIAS = 'default'  # Uses the default cache defined earlier
CACHE_MIDDLEWARE_SECONDS = 600      # Cache each page for 600 seconds (10 minutes)
CACHE_MIDDLEWARE_KEY_PREFIX = ''    # A prefix that should be unique to this site


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files (uploads)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'


CKEDITOR_5_CUSTOM_CSS = {
    'default': [
        '/static/django_ckeditor_5/ckeditor/ckeditor5.css',
    ],
}

CKEDITOR_5_CUSTOM_JS = {
    'default': [
        '/static/django_ckeditor_5/ckeditor/ckeditor5.js',
    ],
}

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 360,
        'width': '100%',
        'extraPlugins': ','.join([
            'codesnippet',
            'image2',
        ]),
    },
}




# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Simplifies static file handling
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# For caching support
WHITENOISE_MAX_AGE = 31536000  # One year in seconds