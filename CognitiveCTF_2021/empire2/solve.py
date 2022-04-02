import zlib
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import base64_decode, URLSafeTimedSerializer

# secret_key = 'CognitiveCTF{your_flag_is_in_another_castle12345678}'
# cookie = '.eJwljktqAzEQRO-idRZqfVveGnIC70VL3e0MTjygmQkE47tbJpuCKnjFe5iqQ7Yvc9rHIR-mLmxOhjH2QEk1gi2WFRUYHQF5gQTsLcSWWyELBUFsD-LUCrvcMGEIhblFYSTKhZuVDNopRnrf-dITWbadXcqKuRHNgMjUYxNxEkDRTJFjk_Fv42ft29C6rze5z8HRFGSUrN1HVOsiRO0KwiScQkOH2Fyyk2Mat7pJH7JP8Lxe78u-_Mr58vlY9q1S_ZH6tx6j6jddq7jsEQI9zfMFufVV2A.YSCnrA.Aw1LrMfUpsuUsrnV26ocW28bupk'
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
session = FlaskSessionCookieManager.decode(secret_key, cookie)
print(session)