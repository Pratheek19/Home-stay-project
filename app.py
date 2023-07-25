from flask import Flask , render_template

app = Flask(__name__)

Stays= [

{
'id': 1,
'title': 'Camp stays',
'location':'Madikeri',
'Number of stays' : 25 
},
{
'id': 2,
'title': 'Villa stays',
'location':'Madikeri',
'Number of stays' : 15 
},
{

'id': 3,
'title': 'Home stays',
'location':'Madikeri',
'Number of stays' : 125 
},
{
'id': 4,
'title': 'Activities',
'location':'Kodagu',
'Number of stays' : 15 
}

]

@app.route('/')
def hello_world():
    return "hello,world"

@app.route('/home')
def home():
    return render_template('homecopy.html', STAYS=Stays)


if __name__=='__main__':
    app.run(debug=True)