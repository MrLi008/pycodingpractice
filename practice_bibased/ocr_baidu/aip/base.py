# -*- coding: utf-8 -*-

"""
    AipBase
"""
import hmac
import json
import hashlib
import http
import datetime
import base64
import time
from urllib import urlencode
from urllib import quote
from urlparse import urlparse

class AipBase:
    """
        AipBase
    """

    __accessTokenUrl = 'https://aip.baidubce.com/oauth/2.0/token'

    __scopes = set([
        'vis-ocr_ocr',
        'vis-ocr_bankcard',
        'vis-faceattribute_faceattribute',
        'nlp_wordseg',
        'nlp_simnet',
        'nlp_wordemb',
        'nlp_comtag',
        'nlp_wordpos',
        'nlp_dnnlm_cn',
        'vis-antiporn_antiporn_v2',
        'audio_voice_assistant_get',
        'audio_tts_post',
        'vis-faceverify_faceverify',
    ])

    def __init__(self, appId, apiKey, secretKey):
        """
            AipBase(appId, apiKey, secretKey)
        """

        self._appId = appId.strip()
        self._apiKey = apiKey.strip()
        self._secretKey = secretKey.strip()
        self._authObj = {}
        self._isCloudUser = None

    def _request(self, url, data):
        """
            self._request('', {})
        """

        authObj = self._auth()
        headers = self._getAuthHeaders('POST', url)
        params = self._getParams(authObj)

        response = http.post(url, data=data, params=params, headers=headers)
        obj = self._proccessResult(response)

        if not self._isCloudUser and obj.get('error_code', '') == 110:
            authObj = self._auth(True)
            params = self._getParams(authObj)
            response = http.post(url, data=data, params=params, headers=headers)
            obj = self._proccessResult(response)

        return obj

    def _proccessResult(self, content):
        """
            formate result
        """

        return json.loads(content) or {}

    def _auth(self, refresh=False):
        """
            api access auth
        """
        
        if len(self._apiKey) == 32 or self._isCloudUser == True:
            self._isCloudUser = True
            return

        #未过期
        if not refresh:
            tm = self._authObj.get('time', 0) + int(self._authObj.get('expires_in', 0)) - 30
            if tm > int(time.time()):
                return self._authObj

        obj = json.loads(http.get(self.__accessTokenUrl, params={
            'grant_type': 'client_credentials',
            'client_id': self._apiKey,
            'client_secret': self._secretKey,
        }))

        self._isCloudUser = not self._isPermission(obj)
        obj['time'] = int(time.time())
        self._authObj = obj

        return obj

    def _isPermission(self, authObj):
        """
            check whether permission
        """

        scopes = authObj.get('scope', False) 
        if scopes == False:
            return False

        intersection = self.__scopes.intersection(set(scopes.split(' ')))

        return not not intersection

    def _getParams(self, authObj):
        """
            api request http url params
        """

        params = {}

        if self._isCloudUser == False:
            params['access_token'] = authObj['access_token']

        return params

    def _getAuthHeaders(self, method, url):
        """
            api request http headers
        """
        if self._isCloudUser == False:
            return {}

        # UTC timestamp
        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        urlResult = urlparse(url)
        host = urlResult.hostname
        path = urlResult.path
        version, expire, signatureHeaders = '1', '1800', 'host'

        # 1 Generate SigningKey
        val = "bce-auth-v%s/%s/%s/%s" % (version, self._apiKey, timestamp, expire)
        signingKey = hmac.new(self._secretKey, val, hashlib.sha256).hexdigest().encode('utf-8')

        # 2 Generate CanonicalRequest
        # 2.1 Genrate CanonicalURI
        canonicalUri = quote(path)
        # 2.2 Generate CanonicalURI: not used here
        # 2.3 Generate CanonicalHeaders: only include host here
        canonicalHeaders = 'host:%s' % quote(host).strip()
        # 2.4 Generate CanonicalRequest
        canonicalRequest = '%s\n%s\n\n%s' % (method.upper(), canonicalUri, canonicalHeaders)

        # 3 Generate Final Signature 
        signature = hmac.new(signingKey, canonicalRequest, hashlib.sha256).hexdigest()
        authorization = 'bce-auth-v%s/%s/%s/%s/%s/%s' % (version, self._apiKey, timestamp, expire, signatureHeaders, signature)

        return {
            'Host': host,
            'x-bce-date': timestamp,
            'accept': '*/*',
            'authorization': authorization,
        }
