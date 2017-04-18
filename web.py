from flask import Flask, render_template, request
import yelp_script
import os
app = Flask(__name__)

@app.route("/")
def index():
	terms = request.values.get('terms')
	address = request.values.get('address')
	results = None
	if address: 
		results = yelp_script.get_results(terms, address)
	return render_template("index.html", results=results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)