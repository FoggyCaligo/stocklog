from fileManager import FileManager

class Main:
    def __init__(self):
        self.fm = FileManager()
        self.cmd = ''
        self.isWrite = True
    
    def main(self):
        print('write: w')
        print('write record: w -> stockCode price quantity')
        print('history : h')
        print('history search : h -> y.m.d+-y.m.d y.m.d    (empty == current)')
        print('ㅡㅡstock Recorderㅡㅡ')
        while(self.cmd != 'exit'):
            self.cmd = input()


    def test(self):
        print('write: w')
        print('write record: w -> stockCode price quantity')
        print('history : h')
        print('history search : h -> y.m.d+-y.m.d y.m.d    (empty == current)')
        print('ㅡㅡstock Recorder : test.ver ㅡㅡ')
        while(self.cmd != 'exit'):
            self.cmd = input()
            if(self.cmd == 'h'):
                self.isWrite=False
            elif(self.cmd == 'w'):
                self.isWrite=True
            elif(self.cmd=='exit'):
                break
            else:
                if(self.isWrite):
                    try:
                        self.fm.record(self.cmd)
                    except:
                        print('failed. please try again.')
                else:
                    try:
                        print(self.fm.get_data(self.cmd))
                        # self.show_data(self.cmd)
                    except:
                        print('failed. please try again.')
    def show_data(self,input):
        pass



main = Main()
main.test()
