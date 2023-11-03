from flask import Flask, request, jsonify, render_template

from Controllers import ControllerCreditCard, ControllerPaymentPlan
from Models.CreditCard import CreditCard

from datetime import date

view = Flask(__name__)

#Main window - menu
@view.route("/")
def home():
    return render_template("index.html")

#Window to insert a new credit card
@view.route("/view/create-credit-card")
def view_new_credit_card():
    return render_template("create-credit-card.html")

#Window to delete a credit card
@view.route("/view/delete-credit-card")
def view_delete_credit_card():
    return render_template("delete-credit-card.html")

#Window to simulate a purchase
@view.route("/view/simulate-purchase")
def view_simulate_purchase():
    return render_template("simulate-purchase.html")

#Window to insert a payment plan
@view.route("/view/payment-plan")
def view_payment_plan():
    return render_template("payment-plan.html")

#Window to get the total payment in a specified range of months
@view.route("/view/view-payments")
def view_payments():
    return render_template("view-payments.html")


#inserts the credit card in the database
@view.route('/view/insert/credit-card')
def view_insert_credit_card():
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

        result: str = f"Tarjeta de credito {search_credit_card.card_number} guardada exitosamente!"
        return result
    except Exception as err:
        return str(err)


# Simulates a purchase and shows the monthly payment, the total interest and the suggested planned saving.
@view.route('/view/simulate/purchase')
def view_show_purchase():
    try:
        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        payments = int(request.args["payments"])

        search_credit_card = ControllerCreditCard.search_by_card_id(card_number)

        monthly_amount = CreditCard.calc_monthly_payment(search_credit_card, purchase_amount, payments)
        total_interest = CreditCard.calc_total_interest(search_credit_card, purchase_amount, payments)

        planned_saving = CreditCard.calc_planned_saving(search_credit_card, monthly_amount, purchase_amount)

        result: str = f"""
        Pago mensual: ${monthly_amount}... \n
        Interés total a pagar: ${total_interest}... \n
        
        Te sugerimos ahorrar por {planned_saving} meses para realizar la misma compra de contado.
        """

        return result

    except Exception as err:
        return str(err)


#Inserts a payment plan in the database
@view.route('/view/insert/payment-plan')
def insert_payment_plan():
    try:
        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        purchase_date = date.fromisoformat(request.args["purchase_date"])
        payments = int(request.args["payments"])

        ControllerPaymentPlan.insert_payment_plan(card_number, purchase_amount, purchase_date, payments)

        result: str = "Plan de amortización guardado exitosamente en la base de datos."

        return result

    except Exception as err:
        return str(err)

# Shows the total payment outstanding in a given interval of months
@view.route("/view/calc/payments")
def calc_payments():
    try:
        inintial_date = request.args["initial_date"]
        final_date = request.args["final_date"]

        total = ControllerPaymentPlan.calc_total_payment_in_x_interval(date.fromisoformat(inintial_date), date.fromisoformat(final_date)    )

        result: str = f"El total a pagar desde {inintial_date} hasta {final_date} es: ${total}"

        return result

    except Exception as err:
        return str(err)


@view.route("/view/delete/credit-card")
def delete_credit_card():
    try:
        card_number = request.args["card_number"]
        ControllerCreditCard.delete_credit_card(card_number)

        result: str = f"Se eliminó exitosamente la tarjeta de crédito con número: {card_number}"

        return result

    except Exception as err:
        return str(err)


if __name__=='__main__':
   view.run( debug=True )
