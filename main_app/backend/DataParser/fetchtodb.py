import sqlite3
con = sqlite3.connect("data.db")
cur = con.cursor()
import openai
# import openapi
# openapi.__init__()

class Fetcher:
    def __init__(self, *args,) -> None:
        pass
    def add_skill(skills):
        # make a temporary list of skills
        temp = []
        for skill in skills:
            temp.append(skill)
        # convert to string while keeping commas
        temp = ','.join(temp)

        # make a string of skills in the database in one line

        skills_in_db = ''
        for skill in Fetcher.get_skills():
            skills_in_db += skill[1]
       

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """ you are a system that compares two lists and only ouputs the needed data in a comma seperated format and nothing else, you need to make sure that your only output is in the following format: skill1,skill2,skill3 meaning that they are comma seperated and no spaces between them, avoid using filler words like 'sure here it is' i want you to only show me the result in a comma seperated format and nothing else, if there is existing skills, dont output them, only output the needed skills to add, and if there are no skills to add then output 'nothing to add' avoid using extra words and keep it simple, your output will be parsed and needs to be in the correct format that i tell you"""},
                
                {"role": "user", "content": """check if the folllowing skills """+temp+""" are in """ +skills_in_db+""+""" if not, output only the skills that are not there in the following format: skill1,skill2,skill3 meaning that they are comma seperated and no spaces between them, avoid using filler words like 'sure here it is' i want you to only show me the result in a comma seperated format and nothing else"""}
            ]
        )
        response = completion.choices[0].message.content.strip()
        # check if "nothing" is in the response
        if "nothing" in response:
            return
        elif "," in response:
            skills_to_add = response.split(',')
            for skill in skills_to_add:
                cur.execute("INSERT INTO skill (skill_name) VALUES (?)", (skill,))
                con.commit()

    def get_skills():
        cur.execute('select * from skill')
        return cur.fetchall()