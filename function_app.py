import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="CompoundCalculator")
def compound_calculator(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing compound interest calculation.')

    try:
        req_body = req.get_json()
        principal = float(req_body.get('principal'))
        rate = float(req_body.get('rate'))
        time = float(req_body.get('time'))
        n = float(req_body.get('n'))

        amount = principal * (1 + (rate / (100 * n))) ** (n * time)
        result = round(amount, 2)

        return func.HttpResponse(
            json.dumps({"compound_interest": result}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=400
        )
