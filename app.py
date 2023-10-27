from flask import Flask, request, jsonify, render_template

from Controllers import ControllerCreditCard, ControllerPaymentPlan
from Models.CreditCard import CreditCard

from datetime import date

app = Flask(__name__)

#Main window
@app.route("/")
def home():
    return render_template("index.html")

#/api/search/credit-card?card_number=123123
@app.route("/api/search/credit-card")
def search_credit_card():
    try:
        card_number = request.args["card_number"]

        searched_credit_card = ControllerCreditCard.search_by_card_id(card_number)

        return {
            "status": "ok",
            "message": "credit card searched succesfully",
            "searched credit card": searched_credit_card
        }

    except Exception as err:
        return {"status": "error",
                "message": "Request could not be completed",
                "error": str(err)}


#/api/card/new?card_number=123123&owner_id=13124&owner_name=ola&bank_name=ola&due_date=2028-09-12&franchise=ola&payment_day=09&monthly_fee=12000&interest_rate=3

@app.route('/api/card/new')
def insert_credit_card():
    try:
        card_number = request.args["card_number"]
        owner_id = request.args["owner_id"]
        owner_name = request.args["owner_name"]
        bank_name = request.args["bank_name"]
        due_date = date.fromisoformat(request.args["due_date"])
        franchise = request.args["franchise"]
        payment_day = int(request.args["payment_day"])
        monthly_fee = float(request.args["monthly_fee"])
        interest_rate = float(request.args["interest_rate"])

        credit_card = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day,
                                 monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card)

        search_credit_card = ControllerCreditCard.search_by_card_id(card_number)

        return {"status": "ok",
                "message": "Credit card created succesfully",
                "credit card": search_credit_card}
    except Exception as err:
        return {"status": "error",
                "message": "Request could not be completed",
                "error": str(err)}

#/api/simulate/purchase?card_number=123123&purchase_amount=50000&payments=24
@app.route('/api/simulate/purchase')
def simulate_purchase():

    try:
        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        payments = int(request.args["payments"])

        search_credit_card = ControllerCreditCard.search_by_card_id(card_number)

        monthly_amount = CreditCard.calc_monthly_payment(search_credit_card, purchase_amount, payments)
        total_interest = CreditCard.calc_total_interest(search_credit_card, purchase_amount, payments)

        return {"status": "ok", "monthly_payment": f"{monthly_amount}", "total_interest": f"{total_interest}"}

    except Exception as err:
        return {"status": "error",
                "message": "Request could not be completed",
                "error": str(err)}

#/api/simulate/saving?card_number=123123&purchase_amount=50000&payments=24
@app.route('/api/simulate/saving')
def simulate_planned_saving():
    """
    The function for planned saving receives a credit card and get the interest rate from that credit card
    """

    try:

        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        payments = int(request.args["payments"])

        search_credit_card = ControllerCreditCard.search_by_card_id(card_number)

        monthly_amount = CreditCard.calc_monthly_payment(search_credit_card, purchase_amount, payments)
        planned_saving = CreditCard.calc_planned_saving(search_credit_card, monthly_amount, purchase_amount)

        return {"status": "ok",
                "months": planned_saving}

    except Exception as err:
        return {"status": "error",
                "message": "Request could not be completed",
                "error": str(err)}

#/api/purchase/new?card_number=123123&purchase_amount=200000&&payments=36&purchase_date=2023-09-11
@app.route('/api/purchase/new')
def simulate_payment_plan():
    try:
        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        purchase_date = date.fromisoformat(request.args["purchase_date"])
        payments = int(request.args["payments"])

        ControllerPaymentPlan.insert_payment_plan(card_number, purchase_amount, purchase_date, payments)

        return {"status": "ok"}

    except Exception as err:
        return {"status": "error",
                "message": "Request could not be completed",
                "error": str(err)}


if __name__=='__main__':
   app.run( debug=True )
