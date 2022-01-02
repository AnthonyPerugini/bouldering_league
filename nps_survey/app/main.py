from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/send-survey', methods=['POST'])
def send_survey():
   pass

@app.route('/get-scores', methods=['GET'])
def get_scores():

   scores = {"score_list": []}

   return scores
