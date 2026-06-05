def handler(request, response):
    cookie = request.headers.get('cookie', '')
    if 'session=' in cookie:
        response.status_code = 200
        response.body = b'{"user":"ok"}'
    else:
        response.status_code = 401
        response.body = b'{"error":"unauthorized"}'
