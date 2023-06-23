from Uploader.reader import ResumeReader
import api

api.__init__()

class ResumeParser:
    def __init__(self, file):
        self.file = 'Resumes/'+file
        self.reader = ResumeReader(self.file)
        self.text = self.reader.get_text()
        self.text = ' '.join(self.text)

    def get_info(text):
        # completion = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system", "content": """You are are a resume reader, and you will respnd with only a score system, for each job classification, the output should be as follows:
        #         Full Name: [name]
        #         Email: [email]
        #         Phone: [phone]
        #         Address: [address]
        #         [category]: [score in percentage from 0.0 to 1.0] examples such as videography, photography, etc.
        #         for category rating don't include anything that isn't a number
        #         """},
        #         {"role": "user", "content": text.text}
        #     ]
        # )

        # response = completion.choices[0].message.content.strip()
        response="""Full Name: Zardasht Mudur
                Email: ZardashtKaya@gmail.com
                Phone: +964 (751) 101-4123
                Address: N/A
                Content Creation: 1.0 
                Photography: 0.75
                Graphic Design: 0.90"""
        
    
        return response