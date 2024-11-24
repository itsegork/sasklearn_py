from flask import Flask, request
import openpyxl
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/save', methods=['POST'])
def save_to_excel():
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    wb = openpyxl.load_workbook('call.xlsx')
    ws = wb.active
    ws.append([name, phone, message])
    wb.save('call.xlsx')
    return 'Данные сохранены!', 200

if __name__ == '__main__':
    app.run(debug=True)
