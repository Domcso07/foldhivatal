def handler(request, response):
    response.headers['Set-Cookie'] = 'session=; Path=/; HttpOnly; Secure; Max-Age=0; SameSite=Lax'
    response.status_code = 200
    response.body = b'{"ok":true}'
