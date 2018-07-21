import random,string
def rand_str(num,length=8):
    f=open("youhuiquan.txt",'w')#以写的方式打开文件
    for i in range(num):
        chars=string.ascii_letters+string.digits
        s=[random.choice(chars)for i in range(length)]
        #上述类似写为
        #s=[]
        #for i in range(length)
        #s.append(random.choice(chars))
        f.write('{0}\n'.format(''.join(s)))
    f.close
if __name__=='__main__':
    rand_str(200)
