'''
64의 길이를 반으로 계속 반으로 자르기 떄문에 
2의 배수 즉 2진수의 성격을 띔
여기서 쓰인 갯수는 해당 숫자를 2진수로 치환한 후 1의 
'''

print "{0:b}".format(37)
print "{0:b}".format(23)
print str("{0:b}".format(23)).count("1")
print str("{0:b}".format(32)).count("1")
print str("{0:b}".format(64)).count("1")
print str("{0:b}".format(48)).count("1")
