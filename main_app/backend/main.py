from Uploader.parser import ResumeParser
import openapi

openapi.__init__()

a = ResumeParser('CV.pdf')
print(a.get_info())

