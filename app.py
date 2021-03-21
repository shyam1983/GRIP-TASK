from flask import Flask, render_template, request, redirect 

from instamojo_wrapper import Instamojo

API_KEY = "test_f3173039bed8d231e4385779f1b"

AUTH_TOKEN = "test_76bc2679e848fe26cb60a54b23c"

api = Instamojo(api_key=API_KEY , auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('front.html')
   
@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

   
@app.route('/pay',methods=['POST','GET'])
def pay():
    if request.method == 'POST':
        name = request.form.get('name')
        purpose = request.form.get('purpose')
        email = request.form.get('email')
        amount = request.form.get('amount')
        
        response = api.payment_request_create(
        amount=amount,
        purpose=purpose,
        buyer_name=name,
        send_email=True,
        email=email,
        redirect_url="http://localhost:5000/success"
        )
        return redirect(response['payment_request']['longurl'])
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)