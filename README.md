# motoOCR

This repo has a dockerfile to manage dependencies and has a few scripts to detect words/numbers using OCR and tag the image metadata "Keywords" field with results if any are found

- scripts/test.py
  - process file manually and save a result image with boxed results

- scripts/findOCR.py
  - process image as sys.argv[1] and tag it with any found strings

- scripts/processDir.sh
  - iterate through all jpg files in a directory and tag with any results found
