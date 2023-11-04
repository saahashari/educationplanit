import google.generativeai as palm
API_KEY = 'AIzaSyDKbnLMFZ3I1H2iXcBMsYpe31IIu4BM4aM'
palm.configure(api_key = API_KEY)
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
model_id = "models/text-bison-001"

def findJD(jobroles):
  JD = []
  for i in jobroles:
    prompt = f"Can you briefly explain in three lines what {i} is to a middle schooler? Please use an example if it is hard to explain"
    completion=palm.generate_text(
      model=model_id,
      prompt=prompt,
      temperature=0.99,
      max_output_tokens=800,
    )
    result = completion.result
    JD.append(result)
  return JD

def findcourses(jobroles):
  courses = []
  for i in jobroles:
    prompt = f'Can you briefly explain what courses do I need to take in college to become {i}? Just list out top 5 courses names as a starred list only. Do not add any title'
    completion=palm.generate_text(
    model=model_id,
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
    )
    result = completion.result
    result_mod = result.replace('*', '')
    result_mod = result_mod.replace(f'Top 5 College Courses for {i}s', '')
    courses.append(result_mod)
  courses = [x.strip(' ') for x in courses]
  return courses

def findcolleges(jobroles):
  colleges = []
  for i in jobroles:
    prompt = f'Output format should be College|Degree. Do not add any title like College|Degree. No numbered list too. Can you give me the top 3 schools for the {i} role? Also, give me which undergrad degree program to go for? Just list these out as a starred list only.'
    completion=palm.generate_text(
    model=model_id,
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
    )
    result = completion.result
    result_mod = result.replace('*', '')
    result_mod = result_mod.replace('[', '')
    result_mod = result_mod.replace(']', '')
    result_mod = result_mod.replace('College|Degree', '')
    result_mod = result_mod.replace('College | Degree', '') #resorted to this hard-coding after trying numerous times to clean strings efficiently
    colleges.append(result_mod)
  colleges = [x.strip(' ') for x in colleges]
  return colleges

def findsalaryrange(jobroles):
  salaryranges = []
  for i in jobroles:
    prompt = f'Output format should be $Salary Range, and numbers should not be shortened. Do not add any title, including the job role. Can you give me a single base salary range (median) for the {i} role? Just list these out as a starred list only.'
    completion=palm.generate_text(
    model=model_id,
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
    )
    result = completion.result
    result_mod = result.replace('*', '')
    result_mod = result_mod.replace('\\', '')
    salaryranges.append(result_mod)
  salaryranges = [x.strip(' ') for x in salaryranges]
  return salaryranges

def findjobroles(interests):
  prompt = interests + ''' Output format should be a starred list. Find me the perfect job role. Just list the top 5 job roles alone, and nothing else.'''
  completion=palm.generate_text(
      model=model_id,
      prompt=prompt,
      temperature=0.99,
      max_output_tokens=800,
  )
  result = completion.result
  result_mod = result.replace('*', '')
  jobroles = result_mod.split('\n')
  jobroles = [x.strip(' ') for x in jobroles]
  return {
        "jobroles": jobroles,
        "JD": findJD(jobroles),
        "courses": findcourses(jobroles),
        "colleges": findcolleges(jobroles),
        "salary": findsalaryrange(jobroles),
    }
@app.route('/')
def index():
    return render_template('index.html')  # Your input form page

@app.route('/findjobroles', methods=['POST'])
def get_job_roles():
    interests = request.form['interests']
    job_roles_data = findjobroles(interests)
    output = ""
    for key, values in job_roles_data.items():
        output += key + "; "
        for value in values:
            output += value + " "
        output += " "
    return output

if __name__ == '__main__':
    app.run(debug=True)

