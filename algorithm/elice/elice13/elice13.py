
def shootOut(str) :
    temp_arr = str.split(":")
    a = int(temp_arr[0])
    b = int(temp_arr[1])
    if a >= 0 and b >=0 and a+1 >= b and a <= b+1:
        return True
    else:
        return False



def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    input_str = input()
    print(shootOut(input_str))

if __name__ == "__main__":
    main()
