from flask import Flask, request, render_template, Markup
import numpy as np
import tensorflow as tf

app = Flask(__name__)

def predict(vec):
    x = tf.placeholder(tf.float32, shape=(None,54))
    y = tf.placeholder(tf.float32,shape=(None,3))
    with tf.Session() as sess:
        parameters={}
        sess.run(tf.global_variables_initializer())
        saver = tf.train.import_meta_graph('model_final.meta')
        saver.restore(sess,tf.train.latest_checkpoint('./'))
        parameters['w1'] = sess.run('w1:0')
        parameters['b1'] = sess.run('b1:0')
        parameters['w2'] = sess.run('w2:0')
        parameters['b2'] = sess.run('b2:0')
        parameters['w3'] = sess.run('w3:0')
        parameters['b3'] = sess.run('b3:0')
    input_relu = tf.add(tf.matmul(x,parameters['w1']),parameters['b1'])
    output_relu = tf.nn.relu(input_relu)
    hidden_output = tf.add(tf.matmul(output_relu,parameters['w2']),parameters['b2'])
    hidden_relu = tf.nn.relu(hidden_output)
    scores = tf.add(tf.matmul(hidden_relu,parameters['w3']),parameters['b3'])
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sc = sess.run(scores,feed_dict={x:vec})
        output = sess.run(tf.argmax(sc,1))
    return(output)

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
        d= {'A1Cresult_>7': 27,
             'A1Cresult_>8': 28,
             'A1Cresult_None': 29,
             'A1Cresult_Norm': 30,
             'admission_source_id_1': 20,
             'admission_source_id_2': 21,
             'admission_source_id_3': 22,
             'admission_source_id_4': 23,
             'admission_type_id_1': 13,
             'admission_type_id_2': 14,
             'admission_type_id_3': 15,
             'admission_type_id_4': 16,
             'age_[20-30)': 5,
             'age_[30-40)': 6,
             'age_[40-50)': 7,
             'age_[50-60)': 8,
             'age_[60-70)': 9,
             'age_[70-80)': 10,
             'age_[80-90)': 11,
             'age_[90-100)': 12,
             'change_0': 47,
             'change_1': 48,
             'diabetesMed_0': 49,
             'diabetesMed_1': 50,
             'diag_1_1': 51,
             'diag_1_2': 52,
             'diag_1_3': 53,
             'discharge_disposition_id_1': 17,
             'discharge_disposition_id_2': 18,
             'discharge_disposition_id_3': 19,
             'gender_Female': 3,
             'gender_Male': 4,
             'glipizide_Down': 35,
             'glipizide_No': 36,
             'glipizide_Steady': 37,
             'glipizide_Up': 38,
             'glyburide_Down': 39,
             'glyburide_No': 40,
             'glyburide_Steady': 41,
             'glyburide_Up': 42,
             'insulin_Down': 43,
             'insulin_No': 44,
             'insulin_Steady': 45,
             'insulin_Up': 46,
             'metformin_Down': 31,
             'metformin_No': 32,
             'metformin_Steady': 33,
             'metformin_Up': 34,
             'race_AfricanAmerican': 0,
             'race_Caucasian': 1,
             'race_Other': 2,
             'time_in_hospital_1': 24,
             'time_in_hospital_2': 25,
             'time_in_hospital_3': 26}
        """
        > colnames(df)
 [1] "race"                     "gender"                   "age"                      "admission_type_id"        "discharge_disposition_id" "admission_source_id"      "time_in_hospital"        
 [8] "A1Cresult"                "metformin"                "glipizide"                "glyburide"                "insulin"                  "change"                   "diabetesMed"             
[15] "readmitted"               "diag_1"     
        """
        #pkl_file = open('cat', 'rb')
        #index_dict = pickle.load(pkl_file)
        new_vector = np.zeros((1,54), dtype=np.int)

        try:
            new_vector[0][d[result['race']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['gender']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['age']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['admission_type_id']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['discharge_disposition_id']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['admission_source_id']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['time_in_hospital']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['A1Cresult']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['metformin']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['glipizide']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['glyburide']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['insulin']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['change']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['diabetesMed']]] = 1
        except:
            pass
        try:
            new_vector[0][d[result['diag_1']]] = 1
        except:
            pass


        #pkl_file = open('logmodel.pkl', 'rb')
        #logmodel = pickle.load(pkl_file)
        prediction = predict(new_vector)[0]
        str = ''
        if(prediction == 0):
            str = "Expected readmission within 30 days"
        if(prediction == 1):
            str = "Expected readmission after 30 days"
        if(prediction == 2):
            str = "No expected readmission"
        return render_template('results.html', prediction=str)

if __name__ == "__main__":
    app.run()
