# from PIL import ImageColor
# print(ImageColor.getcolor('red','RGBA'))
# print(ImageColor.getcolor('RED','RGBA'))
# print(ImageColor.getcolor('Black','RGBA'))
# print(ImageColor.getcolor('chocolate','RGBA'))
# print(ImageColor.getcolor('CornflowerBlue','RGBA')

# from PIL import Image
# catIm = Image.open('zophie.png')
# im = Image.new('RGBA',(100,200),'purple')
# im.save('purpleImage1.png')
# im2 = Image.new('RGBA',(20,20),)
# im2.save('transparentImage1.png')


# from PIL import Image
# catIm = Image.open('zophie.png')
# croppedIm = catIm.crop((335,345,565,560))
# croppedIm.save('cropped.png')

# from PIL import Image
# catIm = Image.open('zophie.png')
# catCopyIm = catIm.copy()
# faceIm = catIm.crop((335,345,565,560))
# catCopyIm.paste(faceIm,(0,0))
# catCopyIm.paste(faceIm,(400,500))
# catCopyIm.save('pasted.png')

# from PIL import Image
# catIm = Image.open('zophie.png')
# catCopyIm = catIm.copy()
# faceIm = catIm.crop((335,345,565,560))
# facewidth,faceheight = faceIm.size
# newIm = Image.new('RGBA',(1000,1000))
# newWidth,newHeight = newIm.size
# for i in range(newWidth//facewidth):
#     for j in range(newHeight//faceheight):
#         newIm.paste(faceIm,(i*facewidth,j*faceheight))
# newIm.save('dupli-cat.png')

# from PIL import Image
# catIm = Image.open('zophie.png')
# width,height = catIm.size
# quartersizeIm = catIm.resize((int(width/2),int(height/2)))
# quartersizeIm.save('quartersized.png')
# svelteIm = catIm.resize((width,height+300))
# svelteIm.save('svelte.png')

# from PIL import Image
# catIm = Image.open('zophie.png')
# # catIm.rotate(90).save('rotated90.png')
# # catIm.rotate(180).save('rotated180.png')
# # catIm.rotate(270).save('rotated270.png')
# # catIm.rotate(6).save('rotate6.png')
# # catIm.rotate(6,expand=True).save('rotate6_expanded.png')
# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal.png')
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical.png')

# from PIL import Image
# im = Image.new('RGBA',(100,100))
# for x in range(50):
#     for y in range(100):
#         im.putpixel((x,y),(210,210,210))
# from PIL import ImageColor
# for x in range(50,100):
#     for y in range(100):
#         im.putpixel((x,y),ImageColor.getcolor('darkgray','RGBA'))
# im.save('putPixel.png')


# from PIL import Image
# import os
# from pathlib import Path

# im1 = Image.open('catlogo.png')
# width,height = im1.size
# index = width/height

# if index > 1:
#     index = 1/index

# size = [width,height]
# num = 0
# if height == max(width,height) :
#     num = 1
# if size[num] > 300:
#     size[num] = 300
#     size[1-num] = int(size[num]*index)

# im1 = im1.resize((size[0],size[1]))
# print('resizing catlogo.png')

# filenames = os.listdir(Path.cwd()/'program')
# pathsrc  = Path.cwd()/'program'
# pathde = Path.cwd()/'marks'
# for filename in filenames:
#     im = Image.open(pathsrc/filename)
#     im.paste(im1,(0,0),im1)
#     im.save(pathde/('marked_'+filename))

# from PIL import Image,ImageDraw
# im = Image.new('RGBA',(200,200),'white')
# draw = ImageDraw.Draw(im)

# draw.line([(0,0),(199,0),(199,199),(0,199),(0,0)],fill='black')
# draw.rectangle((20,30,60,60),fill='blue')
# draw.ellipse((120,30,160,60),fill='red')
# draw.polygon(((57,87),(79,62),(94,85),(120,90),(103,103)),fill='brown')

# for i in range(100,200,10):
#     draw.line([(i,0),(200,i)],fill='green')

# im.save('drawing.png')

from PIL import ImageFont,Image,ImageDraw
import os
im = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(im)
draw.text((20,150),'Hello',fill='purple')
fontsFolder = 'C:\Windows\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder,'arial.ttf'),32)
draw.text((100,150),'Howdy',fill='gray',font=arialFont)
im.save('text.png')
