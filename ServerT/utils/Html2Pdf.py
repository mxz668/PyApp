import requests
import bs4
import pdfkit
import wkhtmltopdf


url = 'https://weread.qq.com/web/reader/ff032ea071e06ef4ff0f844kc1632f5021fc16a5320f3dc'
path_wk = r'D:\Python\wkhtmltox\bin\wkhtmltopdf.exe' #安装位置
config = pdfkit.configuration(wkhtmltopdf = path_wk)
pdfkit.from_url(url, 'wx.pdf', configuration=config)

# pdfkit.from_file('test.html', 'out.pdf')
# pdfkit.from_string('Hello!', 'out.pdf')

