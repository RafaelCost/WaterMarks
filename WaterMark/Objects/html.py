import codecs

def save_WaterMark(plot_name,watermark_image_path,size):
    base_ = '''
    <body>
    <div style="position: fixed;
    top: '''+str(size[0])+'''%; left: '''+str(size[0])+'''%;
    z-index:999999;">

    <img style = "opacity: 0.5;" width="200" src='''+watermark_image_path+'''>
    </div>
    '''
    f=codecs.open(plot_name, 'r',encoding="utf8")
    conteudo=f.read()
    conteudo = conteudo.replace('<body>', base_)

    with open(plot_name, 'w') as file:
        file.write(conteudo)