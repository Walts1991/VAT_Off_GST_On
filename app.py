from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_tax(value):
    # Remove 20% VAT
    vat_removed_value = value / 1.20
    vat_amount = value - vat_removed_value
    
    # Add 5% GST
    gst_amount = vat_removed_value * 0.05
    final_value = value + gst_amount

    return {
        'original_value': value,
        'vat_removed_value': vat_removed_value,
        'vat_amount': vat_amount,
        'gst_amount': gst_amount,
        'final_value': final_value
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = float(request.form['value'])
        result = calculate_tax(user_input)
        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
