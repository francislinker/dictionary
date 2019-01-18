import pymysql

db = pymysql.connect('localhost','root','123456','dict',charset='utf8')

cursor = db.cursor()

ins = 'insert into words(word,interpret) values(%s,%s)'
i = 1
with open ('dict.txt','r') as f:
    while True:
        oneLine = f.readline()#读一行，得到一个字符串
        if not oneLine:
            break
        word = oneLine.split()[0]
        interpret = ' '.join(oneLine.split()[1:])#切割后整合
        cursor.execute(ins,[word,interpret])
        db.commit()
        print('第%d条存入成功' % i)
        i += 1

cursor.close()
db.close()