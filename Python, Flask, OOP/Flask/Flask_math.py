from flask import Flask, request, render_template, url_for, redirect

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def get_n():
    if request.method == 'POST':
        n = int(request.form['n'])
        print(n)
        a = n**2
        b = n**n
        c = 1
        if n in (0, 1):
            pass
        else:
            for i in range (2, n+1):
                c = c * i
        return render_template('index_x2.html', a=a, b=b, c=c)
    else:
        return render_template('index-x1.html')

app.run(debug=True)