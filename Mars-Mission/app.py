# Import Tools
# Use Flask to render a template
from flask import Flask, render_template, redirect, url_for

# Use PyMongo to interact with our Mongo database
from flask_pymongo import PyMongo

# Convert from Jupyter notebook to Python to use scraping code
import scraping

# Setup Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Set up scraping route
# Define it with def scrape()
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)
if __name__ == "__main__":
   app.run()