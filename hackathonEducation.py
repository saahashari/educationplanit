import google.generativeai as palm
API_KEY = 'AIzaSyDKbnLMFZ3I1H2iXcBMsYpe31IIu4BM4aM'
palm.configure(api_key = API_KEY)
import re
from flask import Flask, jsonify, request, render_template, render_template_string

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
    completion = palm.generate_text(
      model=model_id,
      prompt=prompt,
      temperature=0.99,
      max_output_tokens=800,
    )
    result = completion.result
    # Assuming the result comes in a list format, separated by new lines
    # First, we remove the asterisk and split by new lines
    courses_list = result.replace('*', '').split('\n')
    # Then we strip whitespace and filter out empty strings
    courses_list = [course.strip() for course in courses_list if course.strip()]
    # Join the courses with a comma
    courses_joined = ', '.join(courses_list)
    courses.append(courses_joined)
  return courses

def findcolleges(jobroles):
  colleges = []
  for i in jobroles:
    prompt = f'Output format should be College|Degree. Do not add any title like College|Degree. No numbered list too. Can you give me the top 3 schools for the {i} role? Also, give me which undergrad degree program to go for? Just list these out as a starred list only.'
    completion = palm.generate_text(
    model=model_id,
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
    )
    result = completion.result
    # Split the result into lines and strip whitespace
    lines = [line.strip() for line in result.split('\n') if line.strip()]
    # Create a new list to hold the formatted colleges and degrees
    formatted_colleges = []
    for line in lines:
      # Assuming the format is 'College - Degree', we replace ' - ' with '|'
      formatted_line = line.replace(' - ', '|')
      formatted_colleges.append(formatted_line)
    # Join the formatted colleges with commas
    colleges_string = ', '.join(formatted_colleges)
    colleges.append(colleges_string)
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

def clean_text(text):
    # Remove \n and \r characters
    text = text.replace('\n', ' ').replace('\r', ' ')
    # Remove special characters you consider unnecessary
    # Add or remove characters in the regex as needed
    text = re.sub(r'[;*#]', '', text)
    # Additional stripping to remove potential double spaces
    text = re.sub(' +', ' ', text).strip()
    return text

@app.route('/')
def index():
    return render_template('index.html')  # Your input form page

@app.route('/findjobroles', methods=['POST'])
def get_job_roles():
    interests = request.form['interests'] + 'Exclude any headers like top 5 job roles and explanations.'
    job_roles_data = findjobroles(interests)
    
    # Generate list of lists for the table
    job_roles_data['jobroles'] = [clean_text(role) for role in job_roles_data['jobroles']]
    job_roles_data['JD'] = [clean_text(jd) for jd in job_roles_data['JD']]
    job_roles_data['courses'] = [clean_text(course) for course in job_roles_data['courses']]
    job_roles_data['colleges'] = [clean_text(college) for college in job_roles_data['colleges']]
    job_roles_data['salary'] = [clean_text(salary) for salary in job_roles_data['salary']]
    
    # Here we should return a JSON response because the frontend is expecting it
    return jsonify(job_roles_data)

if __name__ == '__main__':
    app.run(debug=True)

