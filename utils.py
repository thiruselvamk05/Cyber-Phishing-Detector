# utils.py
import validators
import requests
import socket
import ssl
from urllib.parse import urlparse

def is_url_valid(url):
    return validators.url(url)

def resolve_dns(url):
    try:
        domain = urlparse(url).netloc
        socket.gethostbyname(domain)
        return True
    except:
        return False

def check_http_response(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code in [200, 301, 302]
    except:
        return False

def check_https_certificate(url):
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname
        port = parsed.port or 443
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.getpeercert()
        return True
    except:
        return False

