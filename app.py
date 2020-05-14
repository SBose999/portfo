from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        with open("database.csv", 'a') as file:
            field_name = ['email', 'subject', 'message']
            writer = csv.DictWriter(file, fieldnames=field_name)
            writer.writerow(data)

        return redirect('thank_you.html')
    else:
        return 'something went wrong'


if __name__ == '__main__':
    app.run()
