from flask import Flask, request, render_template

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def get_code():
    if request.method == "POST":
        code = request.form['code']
        code_list = list(code)
        if (len(code) == 6) and (code_list[2] == "-"):
            return 'Kod poprawny'
        else:
            return 'Kod niepoprawny'
    else:
        return render_template('index_x3.html')




app.run(debug=True)