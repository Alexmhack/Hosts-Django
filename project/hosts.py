from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'blog', settings.ROOT_URLCONF, name='blog'),
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'(?!www).*', 'project.hostsconf.urls', name='wildcard'),
)
