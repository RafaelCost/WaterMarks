from .Objects import html, png

def _png_mark(name_file, watermark_image_path, position):
    html.save_WaterMark(name_file,watermark_image_path, position)
    
def _html_mark(name_file, watermark_image_path, position):
    png.save_WaterMark(name_file,watermark_image_path, position)

def set_WaterMark(name_file, mark, position):
    tipo = name_file.split('.')[-1]
    if tipo == 'png':
        _png_mark(name_file, mark, position)
        
    elif tipo == 'html':
        _html_mark(name_file, mark, position)