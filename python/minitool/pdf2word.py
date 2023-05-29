from pdf2docx import Converter
import os

def main():
    a='C:\\Users\\LENOVO\\Desktop\\1\\附件'
    p,f=os.path.split(a)

    os.chdir(p)
    pdf_file = f
    name,end=os.path.splitext(pdf_file)
    docx_file = '{}.docx'.format(name)

    # convert pdf to docx
    cv = Converter(pdf_file)
    cv.convert(docx_file) # 默认参数start=0, end=None
    cv.close()
    print("Finished")

if __name__ == "__main__":
    main()
