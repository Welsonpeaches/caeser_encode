import os


os.system('cls')



print('''
   ##################################################
   #                                                #
   #         caesar_encode          by : Welson     #
   #                                                #
   ##################################################

''')


def encode():
    print('Starting encode')
    print('输入你想要输入的明文' )
    txt = input(">>")
    print('请输入移动位数')
    offset = int(input(">>"))


    #考虑用户用的是字符串
    result = ""

    for t in txt:
        n = ord(t)
        n = n + offset
        t2 = chr(n)
        result = result + t2
   
    print(f'加密后的字符是 {result}')

def decode():
    print('Starting decode')
    print('输入你要解密的密文' )
    cipher = input('>>')
    print("请输入秘钥.")
    key = int(input('>'))
    
    plain = ""

    
    for c in cipher:
        n = ord(c)
        n = n - key
        p = chr(n)
        plain += p

    print(f'解密后的明文是：{plain}')





    


running = True
while running:
    print('1.Encode      2.decode    3.Exit')
    sel = input(">>")
    if sel == '1':
        encode()
    elif sel == '2':
        decode()
    elif sel == '3':
        print("Thank you for use this app!")
        running = False
    else:
        print('请做出正确的选择。 ')
        
    
