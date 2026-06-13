import json
import base64

def handler(request, response):
    try:
        body = json.loads(request.body.decode('utf-8'))
        email = body.get('email')
        password = body.get('password')

        # TODO: valódi ellenőrzés (adatbázis + hashelt jelszó)
        if email == 'domcso007@gmail.com' and password == '20130523':
            token = base64.b64encode(f'user:{email}'.encode()).decode()
            # HTTP-only süti beállítása
            response.headers['Set-Cookie'] = f'session={token}; Path=/; HttpOnly; Secure; SameSite=Lax'
            response.status_code = 200
            response.body = json.dumps({ 'ok': True }).encode('utf-8')
        else:
            response.status_code = 401
            response.body = json.dumps({ 'error': 'Invalid credentials' }).encode('utf-8')
    except Exception:
        response.status_code = 500
        response.body = json.dumps({ 'error': 'Server error' }).encode('utf-8')
