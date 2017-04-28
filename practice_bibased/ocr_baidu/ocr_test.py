# coding=utf8


from aip import AipOcr

APP_ID = '9330429'
API_KEY = 'FpWrhIUnyKWmQjXpnMjXaZkt'
SECRET_KEY = 'Gt5HsX9ziO3ynpGXFRdZY8N1MHAEhYTv'


aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

options = {
    'detect_direction':False,
    'language_type': 'CHN_ENG',
}


result = aipOcr.general(open('1.png', 'rb').read(), options)

for r in result['words_result']:
    print r['words']