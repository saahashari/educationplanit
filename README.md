
<h2 style="text-align: center;"> <u>Project Title - Education PlanIt: "Discover Your Future Today"</u></h2> <br>

<h3 style= "text-align: left;"><i><u>Project Background</u></i></h3> <br>
Automated Educational Consulting is an innovative career exploration tool tailored to students who aren’t sure on what to do in the future. Through inputting sentences or phrases upon your strengths, habits, and interests, x helps students identify potential careers. By making career exploration fun and relevant, we help young students make their correct choices from now on to be successful in their future careers.

Born out of an invigorating brainstorming session at the esteemed Google Palm2 API Hackathon hosted by Carnegie Mellon University, Automated Educational Consulting stands as a testament to innovative thought and collaborative spirit. Notably, we've enriched the model by training it on our own meticulously curated dataset, ensuring that its insights are tailored and relevant. Our dedicated team has harnessed the power of Google's avant-garde Palm2 API to envision a tool that could potentially revolutionize how middle schoolers approach their career paths.<br>
<h3 style="text-align: left"><i><u>Project Description</u></i></h3><br>
Automated Educational Consulting is a dynamic model designed to gauge students' current interests. Utilizing the capabilities of the Google Palm2 API, our model interprets inputs—whether they're bullet points, sentences, or paragraphs—into a skill set that the LLM can comprehend. For enhanced accuracy, we've aggregated matching qualities from various online sources for 21 distinct job titles and have trained the Palm2 API using Makersuite. Our primary aim is to offer users a detailed guide, providing step-by-step recommendations on courses to pursue at their universities and suggesting the most suitable universities based on their school rankings.<br><br>
Our project is in its developmental phase and has not reached its final form. We aspire to offer seamless access to all free online courses, allowing students to easily tap into valuable resources like Harvard's acclaimed CS50 course, a favorite among many programmers. To keep our users at the forefront of educational opportunities, we're committed to monthly updates that encompass the newest free courses available. We understand the weight of our recommendations and are deeply aware of their potential impact on our users' futures.

<h3 style="text-align: left;"><i><u>Code And Explanation</u></i></h3><br>
<h5><u>SNIPPET 1</u></h5>
<div style="border: 2px solid #000; padding: 10px;"><code>pip install google-generativeai</code></div>
<br>Here we are invoking the generative AI interface provided by google.<br>
<br>
<h5><u>SNIPPET 2</u></h5>
<div style="border: 2px solid#000; padding: 10px;"><code>import google.generativeai as palm<br>API_KEY = 'AIzaSyDKbnLMFZ3I1H2iXcBMsYpe31IIu4BM4aM'<br>
palm.configure(api_key = API_KEY)<br>
from flask import Flask, jsonify, request, render_template</code></div>
<br>The installed package is imported using the import command. The API key is used to authenticate the program and also to use the training model that we require. We use the flask as it is the main class in the flask web framework. It is used to create an instance of the web application.<br>
<br>
<h5><u>SNIPPET 3</u><h5>
<div style="border: 2px solid#000; padding 10px;">
<pre>
<code>
def findJD(jobroles):
    JD = []
    for i in jobroles:
        prompt = f"Can you briefly explain in three lines what {i} is to a middle schooler? Please use an example if it is hard to explain"
        completion = palm.generate_text(
            model=model_id,
            prompt=prompt,
            temperature=0.99, 
            max_output_tokens=800,
        )
        result = completion.result
        JD.append(result)
    return JD
</code>
</pre>

The above function takes a list of <i>jobroles</i> as parameters. For each job role the funtion generates a prompt, a three line string that asks ti explain what a jobrole is. The set parameters of <i>temperature</i> and <i>max_output_tokens</i> limits the randomness of the output and the length generated text. The reult obtained is stored in </i><b>result</b></i> and is appended to a list <b>JD</b><br>
<br>
<h5><u>SNIPPET 4</u></h5>
<div style="border: 2px solid#000; padding 10px;">
<pre>
<code># Suggest top 5 courses for the particular job role
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
        result_mod = result.replace('*', '')
        result_mod = result_mod.replace(f'Top 5 College Courses for {i}s', '')
        courses.append(result_mod)
        courses = [x.strip(' ') for x in courses]
    return courses
</code>
</pre>

The above code generates a list of courses for the prescribed job role. The <i>findcourses</i> function recieves jobroles as parameter and iterates over each each item in the jobrole list. <i>palm_generate_text</i> generates using the Palm API and the values are passed to the identifiers. The result is then retrieved from the text generating model and the '*' is replaced using the <i>result.replace</i> command. The modified result is then appended to the courses list and is passed to the caller function through the <i>return(courses)</i>.<br>
<br>
<h5><u>SNIPPET 5</u></h5><br>
<div style="border: 2px solid#000; padding 10px">
<pre>
<code># Find top 3 schools for the particular job role and also suggest which degree programs would help
# every i element in colleges list correspond to the i job role. Output Format - College | Degree
# In a single i element, use \n to separate college | degree combinations for every i role.
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
        result_mod = result.replace('*', '')
        result_mod = result_mod.replace('[', '')
        result_mod = result_mod.replace(']', '')
        result_mod = result_mod.replace('College|Degree', '')
        result_mod = result_mod.replace('College | Degree', '') # resorted to this hard-coding after trying numerous times to clean strings efficiently
        colleges.append(result_mod)
        colleges = [x.strip(' ') for x in colleges]
    return colleges
</code>
</pre>
</div>
<br>
This function receives the <i>jobrole</i> parameter and associates it with the top 3 schools and courses that preferably lands you the job role. The receives parameter is iterated and then stored in the predefined empty array <i>colleges</i>[]. The prompt is then send to the AI model which then returns and stores in the identifier. As in the previous code snippets, the <i>temperature</i> and <i>max
output_tokens</i> limits the generaterd output. The result is then passed using the <i>return(colleges)</i> function. <br>
<br>
<h5><u>SNIPPET 6</h5></u>
<div style="border: 2px solid#000; padding 10px">
<pre>
<code>def findsalaryrange(jobroles):
    salaryranges = []
    for i in jobroles:
        prompt = f'Output format should be $Salary Range, and numbers should not be shortened. Do not add any title, including the job role. Can you give me a single base salary range (median) for the {i} role? Just list these out as a starred list only.'
        completion = palm.generate_text(
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
</code>
</pre>

</div>
<br>
This function receives the job roles as the parameter and is used to associate expected salary range for each job role mentioned. An empty list <i>salary_range</i> is created and is iterated in order to attain the required specification. The function to invoke the AI model is used and the returned values are stored in the identifier. The obtained result in the identifiers is then cleaned using the <i>replace</i>functions and finally appended to the list. The entire function finally returns the <i>salaryrange</i>anytime being invoked.<br>
<br>
<h5><u>SNIPPET 7</u><h5>
<div style="border: 2px solid#000; padding 10px"><pre>
<code>def findjobroles(what_karthik_gives_me):
    prompt = what_karthik_gives_me + ''' Output format should be a starred list. Find me the perfect job role. Just list the top 5 job roles alone, and nothing else.'''
    completion = palm.generate_text(
        model=model_id,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
    )
    result = completion.result
    result_mod = result.replace('*', '')
    jobroles = result_mod.split('\n')
    jobroles = [x.strip(' ') for x in jobroles]
    JDlist = findJD(jobroles)
    courselist = findcourses(jobroles)
    collegeslist = findcolleges(jobroles)  # every i element in colleges list correspond to the i job role. Output Format - College | Degree\n In a single i element, use \n to separate college | degree combinations for every i role. Other lists except jobroles follow the same format.
    salarylist = findsalaryrange(jobroles)  # every i element corresponds to i job role, pretty straightforward
    print(jobroles)
    print(JDlist)
    print(courselist)
    print(collegeslist)
    print(salarylist)
</code>
</pre>

Here, the function receives the dynamic input from the user. The prompt is the passed to the generative AI and the resulting being stored in the identifiers. After cleaning the output the result is split into a list of jobs. Each obtained jobrole is used as parameters to invoke the functions <i>findJD</i>, <i>findcourses</i>, <i>fincollages</i> and <i>findsalaryrange</i>. The values returned from these functions are stored and printed respectively in seperate lists or arrays, namely: <i>JDlist</i>, <i>courselist</i>, <i>collagelist</i> and <i>salarylist</i>.
<br>
<br>
<h5><u>SNIPPET 8(USER INTERFACE)</h5></u>

<br>The code for our user interface (UI) has been provided, which contains a Bootstrap CSS framework. Let's break everything down step-by-step. To begin with, we declare the document as an 'HTML' document in the English language. In the Head Section, we use the <i>title</i>, <i>link</i>, and <i>script</i> tags to establish the contents of the UI, such as the title, as well as a reference the included Bootstrap Stylesheet. Also, we use the <i>intergrity</i> and <i>crossorigin</i> tags to ensure the authenticity of the file. In the Body Section, we first use <i>container text-center</i> as a container for our generated content and <i>row text-center</i> to display a heading. Next, we create a form called 'interest-form' that contains an input field for the user to detail their personal and professional interets. This is followed by a submit button coded as <i>button type="submit"</i> with a Bootstrap button of class <i>class="btn btn-primary</i> and the generated response is stored in an empty container <i>div id="response"</i>. We follow this up with a jQuery, which is JavaScript Library, that handles a AJAX Request to generate a table of specifc Job Roles based on the user's response. When handling an AJAX Request in this case, we bind our specific function to a document ready request, <i>$(document).ready(function())</i>, to ensure our DOM is loaded before executing or running. This is followed up by a Form Submission Handler that triggers the ID <i>interest-form</i> upon successful user input submission. Our code then handles an AJAX Request that specifies an endpoint, <i>/findjobroles</i>, for the request to be sent as well as data from the request to be sent to the server and serialized for submission. The <i>success: function(response)</i> is an AJAX Success Callback that defines what happens if the AJAX Request is successfull received and executed. <br><br> This will generate an HTML-based table that contains associated values in the Header Rows of <i>Job Role</i>, <i>JD</i>, <i>Courses</i>, <i>Colleges</i>, and <i>Salary</i>, which are all appended to the table. This is then followed by the for loop function <i>for(var i = 0; i < response.jobroles.length; i++)</i>, which essentially works to generate and append text values in each of the specific header rows to the constructed table. This table is then added to the HTML Element with ID <i>#response</i>; it should be noted that the previous responses of the table are emptied before adding the newly generated responses or result. Finally, in the event that an AJAX Request cannot be handled or encounters an error, we created an error callback function that logs the message, "Error Occurred" and displays an error message through the HTML Element with ID <i>#response</i>.<br><br>
This index template is referenced in the main. 
<br>
<div style="border: 2px solid #000; padding: 10px">
<pre>
@app.route('/')
def index():
    return 'Hello World!'
</pre>
<pre>
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
</pre>
<pre>
if __name__ == '__main__':
    app.run(debug=True)
</pre>

</div>


<br>
<br>
<h5><u>SNIPPET 9(Online Web Resource)</h5></u>
<br>This provided snippet acts as a web scraper and draws information on the available online courses that would furnish the individual for his career. These resources can be used by the individual as a foundation for the career.
<div style="border: 2px solid #000; padding: 10px">
    <pre>
def findonlineresources(jobroles):
    resources = []
    for i in jobroles:
        prompt = f"Can you share a list of free resources I can use to be {i}? Just list out the top 5 resources with links if possible and without any description or anything else. The output format should be a starred list with no titles."
        completion = palm.generate_text(model=model_id, prompt=prompt, max_output_tokens=800)
        result = completion.result
        result = result.replace('*', '')
        resources.append(result)
    return resources
    </pre>
</div>

<h3 style="text-align: left;"><i><u>Results and Output</u></i></h3><br>
The output has been presented in the images provided in the section. As per the interests of the user, the interface provides the course of action that the user can stick to in order to achieve it. From a future point of view, this can be further worked on by training with more availablity of the data. The product has been made public using the AWS, and the provided link <b><i><u>http://3.144.159.94:8000/</u></i></b> can be used to access it.  
<br>
<h5><b><u>Comparing Results from Similar Platforms</u></b></h5>
<br>Education PlanIt has been trained as a career guidance tool and we have compared the exact same prompts in similar platforms. This particular prompt has been used  in Google Bard, ChatGPT and Education PlanIt, as a test to compare our LLM responses to that of the others. <br><b>"I like art, design and drawing. I also like history and jeopardy. What are my career options and which colleges should I opt for to achieve it? Also what would be my average annual return on these career options?"</b>.<br> The results are compared below.<br>

<h5>Bard Result</h5>
<img src="images/bardResult.jpeg" alt="Bard Result">

<h5>GPT Result</h5>
<img src="images/gptResult.png" alt="GPT Result">

<h5>Education PlanIt Platform Result</h5>
<img src="images/platformResult.png" alt="Platform Result">


<h3 style="text-align: left;"><i><u>Results and Output</u></i></h3><br>
The output has been presented in the images provided in the section. As per the interests of the user, the interface provides the course of action that the user can stick to in order to achieve it. From a future point of view, this can be further worked on by training with more availability of the data. To install the required packages & libraries that we used for our project, you can write the command <b><code>pip install -r requirements.txt</code></b> . <br><br>

To run the code locally, please use <b><code>python hackathoneducation.py</code></b><b>

This site is alternatively hosted on AWS EC2. 









