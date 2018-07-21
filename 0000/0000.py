from PIL import Image#PIL是优秀的图像处理框架
from PIL import ImageFont#imagefont 模块定义了相同名称的类，即imagefont类，这个类的实例存储bitmap字体，用于imageDraw类的text（）方法
from PIL import ImageDraw#ImageDraw模块提供了图像对象的简单2D绘制。用户可以使用这个模块创建新的图像，注释或润饰已存在图像，为web应用实时产生各种图形。

def white_to_transparent(img):
    img=img.convert('RGBA')#返回一个转换后的图像副本
    datas=img.getdata()
    newData=[]
    for item in datas:#循坏语句
        if item[0]==255 and item[1]==255:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)#赋给图片新的像素数据
    return img

if __name__=="__main__":
    p1_name="b.png"
    p2_name="a.png"
    #打开两张png图片，注意为当前路径
    p1_image=Image.open(p1_name)
    p2_image=Image.open(p2_name)
    p2_transparent=white_to_transparent(p2_image)
    p1_image.paste(p2_transparent,(0,0),p2_transparent)#将一张图粘贴到另一张图上，将p2_transparent粘贴到p1_image上，复制p2_transparent时是从（0，0）左上角开始的

    # user_font=ImageFont.truetype("./yahei.TTF",32)
    draw=ImageDraw.Draw(p1_image)#在p1_image上绘制文字、图像
    draw.text((152,8),u'12')
    p1_image.save("final.png","PNG")
