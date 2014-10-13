import os
import sys

from django.conf import settings

if __name__ == "__main__":

    if not os.environ.get("DJANGO_SETTINGS_MODULE"):
        print "DJANGO_SETTINGS_MODULE env variable not set, falling back to settings.local"
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
