from aip import AipOcr
import os

filePath = 'C:/Users/August/Desktop/picture'

all_file_name= os.listdir(filePath)

""" 你的 APPID AK SK """
APP_ID = '16138850'
API_KEY = 'GyGryky94F8198qj6aebgkaK'
SECRET_KEY = 'B7wK89GL7sYgHbrGAXTOVRvGd2fsG6Qx'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


options = {}
options["detect_direction"] = "true"
# options["probability"] = "true"

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

for file_name in all_file_name:
    str = 'C:/Users/August/Desktop/picture/'+file_name
    image = get_file_content(str)
    """ 调用通用文字识别, 图片参数为本地图片 """
    result = client.basicAccurate(image,options)
    print(result)