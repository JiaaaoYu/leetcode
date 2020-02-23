import datetime
import hmac
import hashlib
import base64

GMTFORMAT = '%a, %d %b %Y %H:%M:%S GMT'

def get_gmtdate():
   return datetime.datetime.utcnow().strftime(GMTFORMAT)

def authorization(method, date, canonicalizedheaders, canonicalizedresource, accesskey, secretkey):

   return "AWS" + " " + accesskey + ":" + signature(method, date, canonicalizedheaders, canonicalizedresource, secretkey)


def signature(method, date, canonicalizedheaders, canonicalizedresource, secretkey, md5="", content_type=""):

   payload = (method + "\n" +
              md5 + "\n" +
              content_type + "\n" +
              date + "\n" +
              canonicalizedheaders +
              canonicalizedresource)
    print payload
    h = hmac.new(secretkey,
                payload,
                hashlib.sha1
                )
    print h
    print h.digest()
    print base64.b64encode(h.digest())

   return base64.b64encode(h.digest())

#date='Fri, 21 Feb 2020 07:30:00 GMT'
date='20200221T060425Z'
#date='Fri, 21 Feb 2020 06:04:25 GMT'
ak='85f3c476709c43f09e6bfb0cdfe4c251'
sk='baf31cf1b5ce4d189e85ddd534b2e86b'
resource='/hotelmedia/yinweijie_test_1'

print(signature("PUT", date, "", resource, sk))