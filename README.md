[read me](https://github.com/GnuriaN/format-README)

```commandline
python manage.py collectstatic
```

wsgi.py
```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rzsgymn.settings')

application = get_wsgi_application()
```
