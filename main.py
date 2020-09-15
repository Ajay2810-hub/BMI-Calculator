from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def welcome():
    bmi = False
    w = '0'
    h = '0'
    status = ''
    if request.method == "POST":
       weight = request.form.get('weight')
       height = request.form.get('height')
       try:
          weight = int(weight)
          height = int(height)
          
          w = weight
          h = height
          height = height/100
          
          bmi = weight/(height**2)

          if bmi > 40.0 or bmi < 16.0:
             bmi = "Nan"
          elif bmi >= 16.0 and bmi <= 18.5:
             status = 'Underweight'
          elif bmi > 18.5 and bmi <= 28.0:
             status = 'Normal'
          elif bmi > 28.0 and bmi <= 40.0:
             status = 'Overweight'
          if len(str(bmi)) > 4:
             bmi = str(bmi)[:5]
          
       except Exception as e:
          print(e)

    text = status.lower()

    return render_template('index.html', bmi=bmi, height=h, weight=w, status=status, text=text)
    
