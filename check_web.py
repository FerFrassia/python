from requests import session

payload = {
    'action': 'login',
    'username': USERNAME,
    'password': PASSWORD
}

with session() as c:
    c.post('http://example.com/login.php', data=payload)
    response = c.get('http://example.com/protected_page.php')
    print(response.headers)
    print(response.text)