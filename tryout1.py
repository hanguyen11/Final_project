from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

# Display the form
@app.route("/")
def mainpage():
    return render_template("design.html")

@app.route("/feedback")
def feedbackform():
    return render_template("Final_project.html")

@app.route("/feedbackform", methods=["POST"])
def gather_feedback():
    form_data = request.form
    # Print out all the form data in the terminal
    print(form_data)

    curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/routes \
    -F priority=0 \
    -F description='Sample route' \
    -F expression='match_recipient(".*@YOUR_DOMAIN_NAME")' \
    -F action='forward("http://myhost.com/messages/")' \
    -F action='stop()'

    return "Thank you!"









app.run(debug=True)
