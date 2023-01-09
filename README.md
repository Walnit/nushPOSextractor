# nushPOSextractor
Extractor for NUS High Programme of Studies (POS) from PDF to CSV.

## Usage instructions

1. Create a Python 3 virtual environment (i used python 3.11 but most versions >3.8 should work)
2. `pip install -r requirements.txt`
3. Download the POS of choice and save in same folder as scripts as "POS.pdf"
4. Run PDFFilter.py, will create merged.pdf
5. Open merged.pdf with mIcrOSoft WoRD and save it as table.docx in same folder
6. Run CSVFromWord.py, pos.csv should be generated
7. Profit

This repo includes pos.csv generated from POS for C2028

## How it works, in case this stops working

PDFFilter.py filters all horizontal pages as pages are horizontal if and only if they contain useful table data
We exploit miCrOSOft woRd'S ability to open PDFs to make the table into a pdf because pdf tables are impossible to manipulate
Then use CSVFromWord.py to deal with scuffed newlines and put it in CSV format