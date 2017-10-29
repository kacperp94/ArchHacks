from flask import Flask, render_template, Markup
import numpy as np
#import tensorflow

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('hackathon.html')

def main():
    return "Welcome!"


@app.route('/results', methods=['POST', 'GET'])
def get_delay():
    if request.method == 'POST':
        result = request.form

        # Prepare the feature vector for prediction

        """
        > colnames(df)
 [1] "race"                     "gender"                   "age"                      "admission_type_id"        "discharge_disposition_id" "admission_source_id"      "time_in_hospital"        
 [8] "A1Cresult"                "metformin"                "glipizide"                "glyburide"                "insulin"                  "change"                   "diabetesMed"             
[15] "readmitted"               "diag_1"     
        """
        #pkl_file = open('cat', 'rb')
        #index_dict = pickle.load(pkl_file)
        new_vector = [0] * 15

        try:
            new_vector[0] = (result['race'])
        except:
            pass
        try:
            new_vector[1] = (result['gender'])
        except:
            pass
        try:
            new_vector[2] = (result['age'])
        except:
            pass
        try:
            new_vector[3] = result['admission_type_id']
        except:
            pass
        try:
            new_vector[4] = result['discharge_disposition_id']
        except:
            pass
        try:
            new_vector[5] = result['admission_source_id']
        except:
            pass
        try:
            new_vector[6] = result['time_in_hospital']
        except:
            pass
        try:
            new_vector[7] = result['A1Cresult']
        except:
            pass
        try:
            new_vector[8] = result['metformin']
        except:
            pass
        try:
            new_vector[9] = result['glipizide']
        except:
            pass
        try:
            new_vector[10] = result['glyburide']
        except:
            pass
        try:
            new_vector[11] = result['insulin']
        except:
            pass
        try:
            new_vector[12] = result['change']
        except:
            pass
        try:
            new_vector[13] = result['diabetesMed']
        except:
            pass
        try:
            new_vector[14] = result['diag_1']
        except:
            pass


        #pkl_file = open('logmodel.pkl', 'rb')
        #logmodel = pickle.load(pkl_file)
        prediction = logmodel.predict(new_vector)

        return render_template('results.html', prediction=prediction)

if __name__ == "__main__":
    app.run()
