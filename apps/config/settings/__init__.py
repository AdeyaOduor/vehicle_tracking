from .base import *

try:
    from .local import *
except ImportError:
    pass

# Determine environment and load appropriate settings
import os
if os.environ.get('DJANGO_ENV') == 'production':
    from .production import *
else:
    from .development import *