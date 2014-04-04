import unittest
import pickle
from timetable_trial import parseTimetable
from dwnld import download
import codecs

class ParseTimetableTest(unittest.TestCase):
    #def __init__(self, test):
    #    self.filename = 'sevastop_prospect-A1.html'
    
    def testParsing(self):
        files = ['1','2','3','1o','2o']
        for file_ in files:
            if file_[-1] == 'o':
                a = 'cp1251'
            else:
                a = 'utf-8'
            with codecs.open('test/' + file_+'.htm', encoding=a) as f:
                actRes = parseTimetable(f)
            expRes = pickle.load(open('test/' + file_+'.p', "r"))
            self.failUnless(actRes == expRes, 'Fail on the file ' + file_)

    def testDownload(self):
        local = "test/4.htm"
        url = 'http://www.mosgortrans.ru/rasp/1/2188303/45140/3689/index.html'
        actRes = download(url)
        with codecs.open(local, encoding='utf-8') as f:
          for line1,line2,i in zip(f,actRes,range(len(actRes))):
            self.failUnless(line1.strip() == line2.strip(), "Failed in line no " + str(i))
                 

if __name__ == '__main__':
    unittest.main()
        
