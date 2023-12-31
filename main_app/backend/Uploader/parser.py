from backend.Uploader.reader import ResumeReader
import backend.openapi
import openai
class ResumeParser:
    def __init__(self, file):
        self.file = file
        file = file.replace(' ','_')
        file = file.replace('(','')
        file = file.replace(')','')
        file = file.replace("'",'')
        file = file.replace('"','')


        self.file = 'Resumes/'+file
        self.reader = ResumeReader(self.file)
        self.text = self.reader.get_text()
        self.text = ' '.join(self.text)

    def get_info(text):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are are a resume reader, and you will respnd with only a score system, for each job classification, the output should be as follows:
                Full Name: [name]
                Email: [email]
                Phone: [phone]
                Address: [address]
                [category]: [score in percentage from 0.0 to 1.0] examples such as videography, photography, etc.
                for category rating don't include anything that isn't a number
                """},
                {"role": "user", "content": text.text}
            ]
        )

        response = completion.choices[0].message.content.strip()
        
        return response