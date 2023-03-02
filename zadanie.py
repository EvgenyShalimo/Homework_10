class Bred():
    def __init__(self,x):
        self.x = x

    def fool_bred(self):
        if self != 0:
            raise Exception('ЭТО НЕ 0!!!!!!!!!!')

zxc = Bred(1)
try:
    zxc.fool_bred()
except Exception:
    print('ЕТО НЕ 0!!!!!!!!!!!!!!!!!!!!!!!!!!')
#fs