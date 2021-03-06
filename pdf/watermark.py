import PyPDF2

template = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
writer = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  writer.addPage(page)

  with open('watermarked.pdf', 'wb') as output:
    writer.write(output)