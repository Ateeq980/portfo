from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(Flask)


@app.route('/')
def hello_world(username=None, post_id=None):
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n {email}, {subject}, {message}')

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         name = data['name']
#         email = data['email']
#         subject = data['subject']
#         message  = data['message']
#         file = database.write(f'\n {name}, {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/about.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

# @app.route('/about.html')
# def about():
#     return render_template('./about.html')
#     return

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blog'
#
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'This is my dog'
