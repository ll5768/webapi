import dash
import dash_html_components as html
from flask import request, jsonify
import yfinance as yf

app = dash.Dash(__name__, meta_tags=[{"name":"viewport", "content":"width=device-width"}])

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
])

@app.server.route('/api/md/spot', methods=['GET'])
def api_get_spot():
    """get spot"""
    if 'ticker' in request.args:
        ticker_str = str(request.args['ticker'])
    else:
        return "Error: no ticker field provided. Please specify."
    if 'val_dt' in request.args:
        val_dt_str = str(request.args['val_dt'])
    else:
        return "Error: no val_dt field provided. Please specify."

    tickerData = yf.Ticker(ticker_str)
    data = tickerData.history(period='1d', start=val_dt_str, end=val_dt_str)
    return data.to_json()


if __name__ == "__main__":
    app.run_server(debug=True)
