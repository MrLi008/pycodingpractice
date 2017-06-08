# coding=utf8


from aip import AipOcr
import PythonMagick
import PyPDF2
import os




APP_ID = '9330429'
API_KEY = 'FpWrhIUnyKWmQjXpnMjXaZkt'
SECRET_KEY = 'Gt5HsX9ziO3ynpGXFRdZY8N1MHAEhYTv'


aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

options = {
    'detect_direction':False,
    'language_type': 'CHN_ENG',
}

import time
start = time.time()
# result = aipOcr.general(open(u'D:/anguan/5555/image00002.JPG', 'rb').read(), options)
end = time.time()-start

# print end
#
# for r in result['words_result']:
#     print r['words']


pdffile = 'pdffile/test.pdf'

def getimgfilefrompdf(pdffile):
    # with PyPDF2.PdfFileReader(pdffile) as f:
    f = PyPDF2.PdfFileReader(pdffile)
    print f
    pagenums = f.getNumPages()

    # init image
    img = PythonMagick.Image()
    img.density('300')
    for page in range(pagenums):
        img.read(pdffile+('[%s]'%page))
        imgdata = PythonMagick.Image(img)
        imgdata.sample('x1600')
        imgdata.write(pdffile+str(page)+'.jpg')

        # img.write(pdffile + str(page) + '.jpg', 'rb')

        result = aipOcr.general(open(pdffile + str(page) + '.jpg', 'rb').read(), options)
        print pdffile, str(page),'*'*100
        for res in result.keys():
            print result[res]


if __name__ == '__main__':
    getimgfilefrompdf(pdffile)
    # pass


