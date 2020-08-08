dict1={}
def read_file(file_name):
    f=open(file_name)
    for eachline in f:
        eachline=eachline.strip()
        (chinese,english)=eachline.split(' ',1)
        dict1[chinese]=english
    f.close()

def dictation():
    for each in dict1:
        print(each)
        a=str(input('根据中文输入英文单词:'))
        while dict1[each]!=a:
            a=str(input('重新输入英文单词:'))

read_file('dictation.txt')
dictation()
print('听写结束!')
    
