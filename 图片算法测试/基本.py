#coding=utf-8
with open('001.txt', 'w', encoding="gbk") as f:
    for i in range(10):
        s = '{"610100000000011001", "01", "1", "黑A12345", "2", "01", "A", "K33", "http://193.169.100.238:8099/ftp/pic/%s.jpg", },' % i
        print(s)
        f.write(s+'\n')
