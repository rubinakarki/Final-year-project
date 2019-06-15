from recognize import recognize
import matplotlib.pyplot as pyplt

file_name ="/home/rubina/finalYproject/soor/model/happy.jpeg"

result, resultArr, image = recognize(file_name)

label = ['angry','disgust','fear','happy','neutral','sad','surprise']    
# if label[result[0]]=='angry':
#     song =  Songs.objects.filter(angry__gt = )
# elif label[result[0]]=='disgust':
#     song =  Songs.objects.filter(disgust__gt = )
# elif label[result[0]]=='fear':
#     song =  Songs.objects.filter(fear__gt = )
# elif label[result[0]]=='happy':
#     song =  Songs.objects.filter(happy__gt = )
# elif label[result[0]]=='neutral':
#     song =  Songs.objects.filter(neutral__gt = )
# elif label[result[0]]=='sad':
#     song =  Songs.objects.filter(sad__gt = )
# else:
#      label[result[0]]=='surprise':
#     song =  SOngs.objects.filter(surprise__gt = 50)

    


# import ipdb; ipdb.set_trace()


