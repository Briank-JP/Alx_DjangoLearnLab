SECURE_SSL_REDIRECT:	Redirects all HTTP requests to HTTPS.
SECURE_HSTS_SECONDS:	Enforces HTTPS-only access for one year.
SECURE_HSTS_INCLUDE_SUBDOMAINS:	Ensures all subdomains follow HTTPS policy.
SECURE_HSTS_PRELOAD:	Enables site for preloading in browsers' HSTS list.
SESSION_COOKIE_SECURE:	Prevents session hijacking by enforcing HTTPS-only cookies.
CSRF_COOKIE_SECURE:	Protects CSRF tokens from being stolen over HTTP.
X_FRAME_OPTIONS = "DENY":	Prevents clickjacking by blocking iframe embedding.
SECURE_CONTENT_TYPE_NOSNIFF:	Blocks MIME-type sniffing to prevent content injection.
SECURE_BROWSER_XSS_FILTER:	Enables built-in XSS protection in browsers.
SECURE_REFERRER_POLICY:	Restricts referrer information sent across different websites.