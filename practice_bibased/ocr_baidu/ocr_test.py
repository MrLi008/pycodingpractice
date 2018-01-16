# coding=utf8


from aip import AipOcr
import PythonMagick
import ghostscript
import PyPDF2
import traceback
import codecs
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
# chi
# print pdfmetrics.getRegisteredFontNames()

# register font

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
# pdfmetrics.registerFont(TTFont('msyh','msyh.ttf'))






APP_ID = '9330429'
API_KEY = 'FpWrhIUnyKWmQjXpnMjXaZkt'
SECRET_KEY = 'Gt5HsX9ziO3ynpGXFRdZY8N1MHAEhYTv'

#
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
options = {
    'detect_direction':True,
    'language_type': 'CHN_ENG',
}

import time
start = time.time()
result = aipOcr.accurate(open(u'D:/anguan/5555/image00002.JPG', 'rb').read(), options)
end = time.time()-start
#
# import time
# start = time.time()
# result = aipOcr.general(open(u'D:/anguan/5555/image00002.JPG', 'rb').read(), options)
# print result
def showComplexData(res, index=0):
    if isinstance(res, dict):
        for key,value in res.items():
            print index*3*'>',key,
            showComplexData(value, index+1)
    elif isinstance(res, list):
        for item in res:
            showComplexData(item, index+1)
    # elif isinstance(res, str):
    else :
        print index*'>',res


def saveComplexData(res, index=0, outstream=None):
    if isinstance(res, dict):
        for key,value in res.items():
            outstream.write( index*3*'>')
            # print key
            outstream.write(key)
            outstream.write('\n\r')
            saveComplexData(value, index+1, outstream)
    elif isinstance(res, list):
        for item in res:
            saveComplexData(item, index+1, outstream)
    # elif isinstance(res, str):
    else :
        outstream.write( index*u'>')
        # print res
        if isinstance(res, (int,float,long)):
            outstream.write(str(res))
        else:
            outstream.write(res)
        outstream.write(u'\n\r')
# showComplexData(result, 0)
# end = time.time()-start

# print end
#
# for r in result['words_result']:
#     print r['words']


pdffile = 'pdffile/test2.pdf'

def getimgfilefrompdf(pdffile):
    # with PyPDF2.PdfFileReader(pdffile) as f:
    f = PyPDF2.PdfFileReader(pdffile)
    pagenums = f.getNumPages()
    print f, pagenums

    # for page in range(pagenums):
    #     print 'read page: ', page
    #     # outfile = file(u'pdffile/result_'+str(page)+'.pdf','a+')
    #     # writer = PyPDF2.PdfFileWriter()
    #     # writer.addPage(f.getPage(page))
    #     # # with  as outstream:
    #     # writer.write(outfile)
    #     # # init image
    #     # img = PythonMagick.Image('result_'+str(page)+'.pdf')
    #
    #     # img.read(f.getPage(page))
    #     try:
    #         img = PythonMagick.Image(pdffile+'['+str(page)+']')
    #         img.density('300')
    #         img.magick('JPG')
    #         img.write('pdffile/sub/result_'+str(page)+'.jpg')
    #     except Exception as e:
    #         traceback.print_exc( e)

        # imgdata = PythonMagick.Image(pdffile+'_'+str(page)+'.jpg')
        # imgdata.sample('x1600')
        # imgdata.write(pdffile+str(page)+'.jpg')

        # img.write(pdffile + str(page) + '.jpg', 'rb')

    for page in range(pagenums):
        result = aipOcr.general(open('pdffile/sub/result_'+ str(page) + '.jpg', 'rb').read(), options)
        # result = aipOcr.general(img.read(),options)
        print pdffile, str(page),'*'*100
        with codecs.open('pdffile/sub/result_'+str(page)+'.txt', 'wb', 'utf-8') as outstream:
            saveComplexData( result, 0,outstream)
def setWordToPDF(pdfcanvas, left, top, text):
    # init
    # pdfcanvas.line(0,2,1*cm,2*cm)
    px = float(21)/2250
    py = float(30)/2700
    print left,left*cm*px,top,(30-top*py)*cm,cm
    pdfcanvas.drawString(left*cm*px, (30-top*py)*cm, text)
    # pdfcanvas.drawString(left/10,top/7,text)


def getpdffromimg(imgfile):
    #init
    pdfcanvas = canvas.Canvas(imgfile+'.pdf')
    pdfcanvas.setFont('STSong-Light',14)
    # pdfcanvas.rect(3000*cm, 3000*cm, 3000*cm,3000*cm,fill=1)
    result = aipOcr.accurate(open(imgfile, 'rb').read(), options)
    with codecs.open('imgfile/result_' + '.txt', 'wb',
                     'utf-8') as outstream:
        saveComplexData(result, 0, outstream)

    if not result.has_key(u'words_result'):
        print 'no word info list'
        return

    wordinfolist = result.get(u'words_result')
    for wordinfo in wordinfolist:
        location = wordinfo.get('location')
        if location in (None, ):
            continue
        top = location.get('top')
        left = location.get('left')
        text = wordinfo.get('words')
        if text not in ("", None):
            print text,top,left
            setWordToPDF(pdfcanvas, left,top, text)
        # pdfcanvas.showPage()
    pdfcanvas.showPage()
    pdfcanvas.save()

if __name__ == '__main__':
    # getimgfilefrompdf(pdffile)
    # pass
    # imgfile = 'imgfile/test2.jpg'
    # imgfile = 'imgfile/22.JPG'
    imgfile = 'imgfile/33.jpg'
    getpdffromimg(imgfile)


