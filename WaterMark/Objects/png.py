from PIL import Image

def save_WaterMark(input_image_path,
                                watermark_image_path,
                                position):
    output_image_path = input_image_path
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    size = width*0.15, height*0.15
     

    
    img = watermark.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item != (0, 0, 0, 0):
            newData.append((item[0],item[1],item[2],128))
        else:
            newData.append((255, 255, 255, 0))

    watermark.putdata(newData)
    watermark.thumbnail(size)  
    
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)