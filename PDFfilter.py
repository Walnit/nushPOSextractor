from pypdf import PdfReader, PdfWriter

try:
    reader = PdfReader("POS.pdf")
    print("POS.pdf found in root directory")
    print("Pages:", len(reader.pages))
except Exception as e:
    e.printStackTrace()
    print("Try placing POS as POS.pdf in same directory as the run location")

def isVertical(page):
    page = page.mediabox
    return page.right - page.left < page.top - page.bottom

pages = reader.pages
merger = PdfWriter()



for i in range(len(pages)):
    if not isVertical(pages[i]):
        merger.add_page(pages[i])

merger.write("merged.pdf")
merger.close()
