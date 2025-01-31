from flask import Flask, render_template, jsonify
app=Flask(__name__, static_folder='static')
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bangalore,India',
    'salary':'Rs.10,00,000'
  },
  {
    'id':2,
    'title':'Data Engineer',
    'location':'Bangalore,India',
    'salary':'Rs.12,00,000'
  },
  {
    'id':3,
    'title':'Software Engineer',
    'location':'Bangalore,India',
    'salary':'Rs.7,00,000'
  },{
    'id':4,
    'title':'Full Stack Developer',
    'location':'Delhi,India',
    'salary':'Rs.8,00,000'
  }
]
@app.route("/")
def hello_world():
   return render_template('home.html',jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
 