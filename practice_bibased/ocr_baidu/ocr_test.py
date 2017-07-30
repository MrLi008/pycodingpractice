# coding=utf8


from aip import AipOcr
import PythonMagick
import PyPDF2
from PIL import Image
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
    for page in range(pagenums):
        img.read(pdffile+('[%s]'%page))
        # img.read(f.getPage(page))
        # img = Image.open(pdffile+'['+str(page)+']')
        img.density('300')
        img.write(pdffile+'_'+str(page)+'.jpg')
        # imgdata = PythonMagick.Image(pdffile+'_'+str(page)+'.jpg')
        # imgdata.sample('x1600')
        # imgdata.write(pdffile+str(page)+'.jpg')

        # img.write(pdffile + str(page) + '.jpg', 'rb')

        result = aipOcr.general(open(pdffile + '_'+ str(page) + '.jpg', 'rb').read(), options)
        print pdffile, str(page),'*'*100
        for res in result.keys():
            print result[res]


if __name__ == '__main__':
    getimgfilefrompdf(pdffile)
    # pass


