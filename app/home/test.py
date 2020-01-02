import os
model_list=['udnie.ckpt-done','cubist.ckpt-done'] #模型名称
model_src='C:/Users/19145/Desktop/学习/实训/风格迁移/fast-neural-style-tensorflow-master/model/' #模型地址
model_file=model_src+model_list[1]
image_file='C:\\Users\\19145\\Desktop\\文件\\图片\\lyj.JPG' #原图地址
image_name= 'mayuantao_2' #风格图名字ed
imaged_file='C:\\Users\\19145\\Desktop\\文件\\图片/'#图片保存地址
cmd='python C:/Users/19145/Desktop/学习/实训/风格迁移/fast-neural-style-tensorflow-master\\eval.py --model_file '+model_file+' --image_file '+image_file+' --image_name '+image_name+' --imaged_file '+imaged_file
os.system(cmd)
