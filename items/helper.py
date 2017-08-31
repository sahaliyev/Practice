from PIL import Image

def resize(image_path, slider_image_path, new_width,new_height):
    image = Image.open(image_path)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    image.save(slider_image_path)

#def rsize(image_path,thumb_image_path, new_width,new_height):
    #image = Image.open(image_path)
    #image = image.resize((new_width, new_height), Image.ANTIALIAS)
    #image.save(thumb_image_path)
