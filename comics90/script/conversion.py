import glob
import fitz
import os
#文件夹下所有JPG文件转化成一个PDF文件到一个文件夹
def AllJpg2OnePdf(dir_path,pdf_path,pdf_name):
    rename_list = [str(i) for i in range(1,10)]
    doc = fitz.open()
    jpg_path_list = sorted(glob.glob(dir_path+ "\\*.jpg"))
    for jpg_path in jpg_path_list:
        imgdoc = fitz.open(jpg_path)
        img_byte = imgdoc.convertToPDF()
        img_pdf = fitz.open("pdf",img_byte)
        doc.insertPDF(img_pdf)
    doc.save(pdf_path + '\\{}.pdf'.format(pdf_name))
    doc.close()

#一个指定JPG转换成一个pdf
def OneJpg2OnePdf(jpg_path,pdf_path,pdf_name):
    imgdoc = fitz.open(jpg_path)
    img_byte = imgdoc.convetToPdf()
    img_pdf = fitz.open("pdf", img_byte)
    img_pdf.save(pdf_path + '\\{}.pdf'.format(pdf_name))
    img_pdf.close()

#将文件夹中所有JPG转换成同名PDF
def AllJpg2AllPdf(dir_path,pdf_path):
    jpg_path_list = sorted(glob.glob(dir_path+ "\\*.jpg"))
    for jpg_path in jpg_path_list:
        pdf_name = os.os.path.basename(jpg_path).replace('jpg', 'pdf')
        OneJpg2OnePdf(jpg_path,pdf_path,pdf_name)

#将文件夹中所有PDF加入到一个PDF中
def AllPDF2OnePDF(dir_path,newpdf_path,pdf_name):
    pdf_list = sorted(glob.glob(dir_path+ "\\*.pdf"))
    doc = fitz.open()
    for pdf_path in pdf_list:
        one_pdf = fitz.open(pdf_path)
        doc.insertPDF(one_pdf)
    doc.save(newpdf_path + '\\{}.pdf'.format(pdf_name))
    doc.close()

if __name__ == '__main__':
    base_path = 'D:\\manhuaspider\\终将成为你'
    chap_list = glob.glob(base_path + '\\'+'**')
    for chap_path in chap_list:
        pdf_name = os.path.basename(chap_path)
        AllJpg2OnePdf(chap_path,base_path,pdf_name)