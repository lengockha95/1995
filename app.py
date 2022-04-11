from flask import Flask
import cloudscraper
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/getmail')

def getmail():
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

    mail = scraper.post("https://mob2.temp-mail.org/mailbox").text
    return mail

@app.route("/readmail/<token>")

def a(token):

    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

    tk = f"{token}"

    headers = {
        'Authorization': tk

    }

    mailboxx = scraper.get("https://mob2.temp-mail.org/messages",headers=headers).text
    return mailboxx


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')