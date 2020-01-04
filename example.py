import easyust #导入模块
cproject = easyust.cproject('example.ust','example.ini') #转码工程，并获取临时文件路径
print('输入文件：', cproject[0]) #打印输入文件路径
print('临时文件：', cproject[1]) #打印临时文件路径
print('曲速：', easyust.rtempo(cproject[1])) #获取曲速
print('工程名：', easyust.rpname(cproject[1])) #获取工程名
print('音源：', easyust.rdb(cproject[1])) #获取音源
print('输出：', easyust.rof(cproject[1])) #获取输出文件路径
print('缓存：', easyust.rcache(cproject[1])) #获取工程缓存文件夹
print('wavtool：', easyust.rwt(cproject[1])) #获取工程wavtool
print('resamper：', easyust.rres(cproject[1])) #获取工程resamper
#print('Flags：', easyust.rflags(cproject[1])) #获取工程flags（部分工程没有，禁用）
print('音符个数：', easyust.rnallnote(cproject[1])) #获取音符个数
print('音符列表：', easyust.rallnote(cproject[1])) #获取音符列表，可传入for循环
print('在第一个音符下：') #第一个音符就是#0000
print('长度：', easyust.rlength(cproject[1],'#0000')) #获取音符长度
print('歌词：', easyust.rlyric(cproject[1],'#0000')) #获取歌词
NoteNum = easyust.rNoteNum(cproject[1],'#0000') #获取音符号，并存到变量内
print('音符号：', NoteNum) #打印音符号
print('音符：', easyust.getnote(NoteNum)) #音符号转音符