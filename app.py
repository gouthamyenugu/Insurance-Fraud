from flask import Flask,render_template,request  # here we are importing class from package

import pickle

app = Flask(__name__)  # here we are creating the instance

with open('grid_search_results.pkl', 'rb') as file:
    best_model, best_params, best_score = pickle.load(file)


@app.route('/') 
def hello():    
    return render_template('home.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():

   if request.method == 'POST':
        # Collect data from form
        incident_severity = int(request.form.get('incident_severity'))
        authorities_contacted = int(request.form.get('authorities_contacted'))
        insured_hobbies = int(request.form.get('insured_hobbies'))
        property_claim = float(request.form.get('property_claim'))
        total_claim_amount = float(request.form.get('total_claim_amount'))
        vehicle_claim = float(request.form.get('vehicle_claim'))

        pred1 = best_model.predict([[incident_severity,authorities_contacted,insured_hobbies,float(property_claim),float(total_claim_amount),float(vehicle_claim)]])
        print(pred1)
        return render_template('result1.html',pred = int(round(pred1[0])))
   
   
   else:
       return render_template('predict.html')
   



    
        

if __name__=='__main__':
    app.run()