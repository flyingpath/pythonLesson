import re

class InitialData():
    def normalizeBreak(self, text):
        windowBreakline = re.compile('\r\n')
        return windowBreakline.sub( '\n', text)

    def getbreakArray(self, text):
        breakline = re.compile('\n')
        multiSpace = re.compile(' +')
        return [ multiSpace.sub( ' ', each.strip()) for each in text.split('\n')]

    def getUseData(self, text):
        breakline = re.compile('\n')
        multiSpace = re.compile(' +')
        dotSpace = re.compile('\. ')
        return dotSpace.sub( '.', multiSpace.sub( ' ', breakline.sub( '. ', text ) ))

    def __init__(self, text):
        self.normal = self.normalizeBreak(text)
        self.breakArray = self.getbreakArray(self.normal)
        self.data = self.getUseData(self.normal)
texture = """right breast cancer s/p simple mastectomy, sentinel LN biopsy and implantation of a tissue expander on 2016/08/11, s/p second stage breast reconstruction surgery on 2016-12-08
a 225ml saline-filled prosthesis was implanted and filled up to 230ml

mild contracture
recommend compression of the prosthesis in prone position
more power on mannual massage
RTC for evaluation of effect of prosthesis massage"""

data = InitialData(texture)

print('aaa')