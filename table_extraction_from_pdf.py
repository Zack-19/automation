# -*- coding: utf-8 -*-
"""table extraction from pdf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cHIzqsYbSy7wieiAMe0vp-22gioEbG33
"""

!pip install tk
!pip install ghostscript
!pip  install camelot-py

!pip install Ghostscript
import camelot
tables = camelot.read_pdf('target.pdf',pages='4',flavor='stream')

tables
tables.export('target.csv',f='csv',compress=True)
#tables[0].to_csv('target.csv')