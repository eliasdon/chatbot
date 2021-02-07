from flask import Flask, render_template, request, jsonify
from assistant import check

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
    #     user_query = request.form['user_query']
    #     print(user_query)
    #     user_query = user_query.strip()
    #     result = check(user_query)
    #     return render_template('index.html', response=result, user_query=user_query)
    return render_template('index.html')


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    user_query = request.json
    #print(user_query)
    user_query = user_query['name']
    result = check(user_query)
    #print(result)
    return jsonify(result)




if __name__ == "__main__":
    app.run(debug=True)
