def hexdump(src,length=16):
    '''16进制导出函数'''
    result=[]
    digits=4 if isinstance(src,str) else 2
    for i in range(0,len(src),length):
        s=src[i:i+length]
        print("s:",s)
        # %0*X: %X 16进制转换 0靠右对齐 * 占长度=digits
        hexa=" ".join(["%0*X" %(digits,ord(x)) for x in s])# %X:格式化无符号十六进制数（大写）
        print("hexa:",hexa)
        print([(digits,ord(x)) for x in s])
        text=''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        print("text:",text)
        result.append("%04X   %-*s  %s"%(i,length*(digits+1),hexa,text))
        print('\n'.join(result))

if __name__ == '__main__':
    src="abcgds34$#sdffsd"
    hexdump(src)