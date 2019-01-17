from PIL import Image
import os

fold_name = 'input folder name'   # the folder that contains all images
file_name = 'output file name'    # the filename of the output PDF file
path = os.getcwd() + '\\' + fold_name + '\\'
file_list = os.listdir(path)
pdf_name = file_name + '.pdf'

pic_name = []
im_list = []

index = 0
for name in file_list:
    # rename each image
    old_name = path + name
    new_name = path + file_name + '.' + str(index).zfill(3) + '.jpg'
    os.rename(old_name, new_name)
    index += 1

    pic_name.append(new_name)

print('Rename finished.')

im1 = Image.open(pic_name[0])
pic_name.pop(0)

for i in pic_name:
    img = Image.open(i)
    im_list.append(Image.open(i))

# merge all images
im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)

print('Merge finished.')