from flask import Flask, render_template, request 
from wtforms import Form, TextAreaField, validators
import __keyword_finder_init__
from __keyword_finder_init__ import matching_keywords

app = Flask(__name__)

class CompareForm(Form):
    resume_ = TextAreaField('', [validators.DataRequired()])
    job_posting_ = TextAreaField('', [validators.DataRequired()])
    
@app.route('/')
def index():
    form = CompareForm(request.form)
    return render_template('first_page.html', form=form)
   

@app.route('/result', methods=['POST'])
def find_words():
    form = CompareForm(request.form)
    if request.method == 'POST' and form.validate():
        resume=request.form['resume_']
        job_posting=request.form['job_posting_']
        output = matching_keywords(job_posting, resume)
        return render_template('result.html', output=output)
    return render_template('first_page.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    