# url_checker.py
from utils import is_url_valid, resolve_dns, check_http_response, check_https_certificate
from urllib.parse import urlparse

def analyze_url_wrapper(url):
    if not is_url_valid(url):
        return {"phishing": True, "reason": "Invalid URL"}

    if not resolve_dns(url):
        return {"phishing": True, "reason": "Suspicious: unreachable"}

    if not check_http_response(url):
        return {"phishing": True, "reason": "Suspicious: no HTTP response"}

    parsed = urlparse(url)
    scheme = parsed.scheme.lower()

    if scheme == "https":
        if check_https_certificate(url):
            return {"phishing": False, "reason": "Secure (HTTPS with valid certificate)"}
        else:
            return {"phishing": True, "reason": "Invalid SSL certificate"}
    elif scheme == "http":
        return {"phishing": False, "reason": "Insecure (HTTP but reachable)"}

    return {"phishing": True, "reason": "Unknown URL scheme"}

