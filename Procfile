web: gunicorn notesapp.wsgi -- log-file -
gunicorn app.wsgi:application -w 2 -b :8000 --timeout 120