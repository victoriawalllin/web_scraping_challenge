from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.store_inventory
produce = db.produce


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    mars_data = client.db.collection.find_one()

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrapper():

    mars_scraper_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    client.db.collection.update({}, mars_scraper_data, upsert=True)
   
    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
