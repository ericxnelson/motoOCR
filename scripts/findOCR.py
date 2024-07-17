#!/usr/bin/python3
from paddleocr import PaddleOCR,draw_ocr
import sys
import exif
from exiftool import ExifToolHelper

sourcefile = sys.argv[1]

ocr = PaddleOCR(use_angle_cls=True, lang='en', warmup=True, use_gpu=True, ocr_version='PP-OCRv3', structure_version='PP-StructureV3', mode='structure', show_log=True) # need to run only once to download and load model into memory

result = ocr.ocr(sourcefile, cls=True)

def writeExif(data,file):
    with ExifToolHelper() as et:
        et.set_tags(
        [file],
        tags={"Keywords": data}
    )

if result[0]:
    for idx in range(len(result)):
        res = result[idx]
    result = result[0]
    txts = [line[1][0] for line in result]
    
    for txt in txts:
        print(txt)
        if txt:
            writeExif(txts,sourcefile)
