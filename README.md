

<h2 style="text-align: center;"> <u>Project Title: Automated Educational Consultant: "Discover Your Future Today"</u></h2> <br>

<h3 style= "text-align: left;"><i><u>Project Background</u></i></h3> <br>
Automated Educational Consulting is an innovative career exploration tool tailored to students who aren’t sure on what to do in the future. Through inputting sentences or phrases upon your strengths, habits, and interests, x helps students identify potential careers. By making career exploration fun and relevant, we help young students make their correct choices from now on to be successful in their future careers.

Born out of an invigorating brainstorming session at the esteemed Google Palm2 API Hackathon hosted by Carnegie Mellon University, Automated Educational Consulting stands as a testament to innovative thought and collaborative spirit. Notably, we've enriched the model by training it on our own meticulously curated dataset, ensuring that its insights are tailored and relevant. Our dedicated team has harnessed the power of Google's avant-garde Palm2 API to envision a tool that could potentially revolutionize how middle schoolers approach their career paths.<br>
<h3 style="text-align: left"><i><u>Project Description</u></i></h3><br>
Automated Educational Consulting is a dynamic model designed to gauge students' current interests. Utilizing the capabilities of the Google Palm2 API, our model interprets inputs—whether they're bullet points, sentences, or paragraphs—into a skill set that the LLM can comprehend. For enhanced accuracy, we've aggregated matching qualities from various online sources for 21 distinct job titles and have trained the Palm2 API using Makersuite. Our primary aim is to offer users a detailed guide, providing step-by-step recommendations on courses to pursue at their universities and suggesting the most suitable universities based on their school rankings.<br>
Our project is in its developmental phase and has not reached its final form. We aspire to offer seamless access to all free online courses, allowing students to easily tap into valuable resources like Harvard's acclaimed CS50 course, a favorite among many programmers. To keep our users at the forefront of educational opportunities, we're committed to monthly updates that encompass the newest free courses available. We understand the weight of our recommendations and are deeply aware of their potential impact on our users' futures.

<h3 style="text-align: left;"><i><u>Code And Explanation</u></i></h3><br>
<div style="border: 2px solid #000; padding: 10px;"><code>pip install google-generativeai</code></div>
<br>Here we are invoking the generative AI interface provided by google.<br>
<br>
<div style="border: 2px solid#000; padding: 10px;"><code>import google.generativeai as palm<br>API_KEY = 'AIzaSyDKbnLMFZ3I1H2iXcBMsYpe31IIu4BM4aM'<br>
palm.configure(api_key = API_KEY)</code></div>
<br>The installed package is imported using the import command. The API key is used to authenticate the program and also to use the training model that we require.<br>
<br>
<div style="border: 2px solid#000; padding 10px;"><code>def findJD(jobroles):<br>JD = []<br>
for i in jobroles:<br> prompt = f"Can you briefly explain in three lines what {i} is to a middle schooler? Please use an example if it is hard to explain"<br>completion=palm.generate_text(<br>model=model_id,<br>prompt=prompt,<br>temperature=0.99,<br> max_output_tokens=800,<br>)<br>result = completion.result<br>JD.append(result)<br>return JD<br>
</code></div>


<h2>Requirements (required) </h2><br>
<h2>Recommended modules (optional)</h2> <br>
<h2>Installation (required, unless a separate INSTALL.md is provided) </h2><br>
<h2>Code and explanation</h2> <br>
<h2>Configuration (required) </h2><br>
<h2>Troubleshooting & FAQ (optional)</h2> <br>
<h2>Issues our team face</h2> <br>
<h2>Contacts </h2><br>
<h2>Acknowledgement </h2><br>
