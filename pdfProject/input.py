'''Creating input fields and frame to create target pdf for the application'''
import jinja2
import pdfkit
# import datetime
# from datetime import datetime
import random
name = "Manish"
age = 34
dob = "01/01/1990"
gen = random.choice(["male", "female"])
markdisA = random.choice(['Yes', 'No'])
markdisB = random.choice(['Yes', 'No'])
remark1 = "Remark1"
remark2 = "Remark2"
law1 = "Law1"
law2 = "Law2"
input_page1 = {'name': name, 'age': age, 'dob': dob, 'gen': gen, 'markdisA': markdisA, 'markdisB': markdisB,
               'remark1': remark1,
               'remark2': remark2,
               'law1': law1,
               'law2': law2}

template_loader = jinja2.FileSystemLoader('/Users/ca/API/pythonProject/pdfProject/templates')
template_env = jinja2.Environment(loader=template_loader)

output_text = template_env.get_template('page1.html').render(input_page1)
# print(output_text)

config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
pdfkit.from_string(output_text, 'page1.pdf', configuration=config)



