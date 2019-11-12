# -*- coding: utf-8 -*-
class Closer:
    '''with 문에서 close 메소드를 사용하여 객체를 자동으로 닫는 컨텍스트
    관리자입니다.'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        print("__enter__")
        return self.obj # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        print("__exit__")
        try:
           self.obj.close()
        except AttributeError: # 객체를 닫을 수 없는 경우입니다.
           print('Not closable.')
           return True # 예외가 성공적으로 처리되었습니다.


if __name__ == '__main__':
    import os
    now_path = os.path.dirname(os.path.realpath(__file__))
    with Closer(open(os.path.join(now_path, "01.py"))) as f:
        print(f)
