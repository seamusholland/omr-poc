import os
from pdf2image import convert_from_path
import subprocess

def main():
    process('simple')
    process('complex')
    process('expressions')


def process(folder:  str) -> str:
    #what 
    print("Processing " + folder + " examples.")

    for root, dirs, files in os.walk('./samples/' + folder + '/'):
        for file in files:
            if file[-4:] == '.png':
                subprocess.run(['bash', 'E:/Coding/Transpose/audiveris/build/distributions/Audiveris/bin/Audiveris', 
                '-batch', '-export', '-output', 'E:/Coding/Transpose/OMR-POC/output/' + folder + '/', os.path.join(root, file)])



# single use method that converts existing .pdf files to .png
def pdf_to_png():
    convert_folder('simple')
    convert_folder('complex')
    convert_folder('expressions')
        

def convert_folder(folder: str):
    for root, dirs, files in os.walk('./samples/' + folder + '/'):
        for file in files:
            # convert
            print("Here is da file: " + file)
            png_version = convert_from_path(os.path.join(root, file))

            counter = -1

            if len(png_version) > 1:
                counter = counter + 1 

            # and save
            for page in png_version:
                if counter > -1:
                    page.save(os.path.join(root, file)[:-4] + str(counter) + '.png', 'PNG')

                    counter = counter + 1
                
                else:
                    page.save(os.path.join(root, file)[:-4] + '.png', 'PNG')
