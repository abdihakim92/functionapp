import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="CompoundCalculator")
def CompoundCalculator(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        principal = req_body.get('principal')
        rate = req_body.get('rate')
        time = req_body.get('time')
        n = req_body.get('n')
        amount = principal * (1 + rate / n) ** (n * time)
    except Exception as e:
        logging.error(f"Exception occurred: {str(e)}")
        return func.HttpResponse("Error occurred in compound calculation",status_code=400)
    else:
        return func.HttpResponse(f"The answer is {amount}")