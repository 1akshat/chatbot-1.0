from flask import Flask, render_template, request
from bot import bot
import time, datetime, json, os

app = Flask(__name__)

bot_obj = bot.Bot()

@app.route("/", methods=['GET'])
def api():
    if request.method == 'GET':
        try:
            query = request.args.get('q')
            response = bot_obj.get_response(query)
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            return json.dumps({
                     'status': 'success',
                     'query' : query ,
                     'response': response,
                     'timestamp': timestamp
                });
        except Exception as e:
            return '{ "status" : "error" }'


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
