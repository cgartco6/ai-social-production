from flask import Flask, request

app = Flask(__name__)

@app.route("/payment/webhook", methods=["POST"])
def payfast_webhook():
    data = request.form.to_dict()
    # verify signature here
    print("Payment Notification:", data)
    return "OK", 200
