from jinja2 import Template
import sys
import csv
from matplotlib import pyplot as plt

HISTOTEMP= """
<!DOCTYPE html>
<html lang='en'>
    <head>
        <title>Course Data </title>
    </head>
    <body>
        <h1> Course Details </h1>
    <table>
      <tr>
          <th> Average Marks </th>
          <th> Maximum Marks </th>
      </tr>
          <tr>
            <td>{{averg}}</td>
            <td> {{maxi}}</td>
          </tr>
      </table>
        <img src="image.png" alt="123456">
      </body>
      </html>

"""

ERRORTEM="""
<!DOCTYPE html>
<html lang='en'>
<head>
    <title>Something went wrong</title>
    </head>
    <body>
    <h1> Wrong Inputs</h1>
    <p> Something went wrong</p>
    </body>
    </html>
"""
TEMPLATE = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <title>Student Details</h1>
    </head>
    <body>
    <h1>Student Details</h1>
    <table>
        <thead>
            <tr>
              <th>Student ID</th>
              <th>Course ID </th>
              <th>Marks</th>
            </tr>
            {% for i in ans %}
                <tr>
                    <td>{{i[0]}}</td>
                    <td>{{i[1]}}</td>
                    <td>{{i[2]}}</td>
                </tr>
                {% endfor %}
                <tr>
                    <td></td>
                    <td> Total Marks</td>

                    <td>{{toral}}<td>
        </thead>
      </table>
<body>

</body>
</html>

"""
def main():
    file = open('data.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)


    if sys.argv[1] == '-s' :
        student_id =  sys.argv[2]
        ans = []
        total = 0
        for i in rows:
            if i[0] == student_id:
                ans.append(i)
        print(ans)
        if len(ans) == 0:
            template = Template(ERRORTEM)
            content = template.render()
            """my_file = open('output.html' ,'w') 
               my_file.write(content)"""
        else:
          for i in ans:
              total = total + int(i[2])
          template = Template(TEMPLATE)
          content = template.render(ans = ans , total=total)
          """my_file = open('output.html' ,'w') 
               my_file.write(content)"""
    elif sys.argv[1] == '-c':
        ans = []
        course_id = (" "+sys.argv[2])
        for i in rows:
            if i[1] == Template(ERRORTEM):
                ans.append(i)
        if len(ans) == 0:
          template = Template(ERRORTEM)
          content = template.render()
        
    else:
        template = Template(ERRORTEM)
        content = template.render()
    print(content)
    my_file = open('output.html',"w")
    my_file.write(content)
    my_file.close()
if __name__== '_main_':
  main ()
