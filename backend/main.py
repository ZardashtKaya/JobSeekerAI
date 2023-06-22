from parser import ResumeParser
import api
api.__init__()

a = ResumeParser('CV.pdf')
print(a.get_info())
