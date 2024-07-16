
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        serial_numbers = request.form.get("serial-numbers")
        attachment_names = request.form.get("attachment-names")

        # Sample data for testing purposes
        serial_numbers = "SN12345, SN67890"
        attachment_names = "Attachment1, Attachment2"

        # AI prompt and response generation
        prompt = "Provide information related to the following serial numbers: {}, and attachment names: {}".format(serial_numbers, attachment_names)
        response = "AI Response: Serial numbers: {}, Attachment names: {}".format(serial_numbers, attachment_names)

        return jsonify({"response": response})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
