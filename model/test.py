from recognize import recognize
import matplotlib.pyplot as pyplt

file_name ="/home/rubina/finalYproject/soor/model/face.jpg"

result, resultArr, image = recognize(file_name)
# import ipdb; ipdb.set_trace()
print(result)

