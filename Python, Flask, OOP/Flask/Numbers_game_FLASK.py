from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def imagine_number():
    """Get imaginary number from user from 1 to 1000.
    checking exception
    :rtype: int
    :return: user number as int
    """

    if request.method == 'POST':
        while True:
            try:
                img_number = int(request.form['number'])
                if img_number < 1 or img_number > 1000:
                    return 'Give number from 1 to 1000!' + render_template('index.html')
                break
            except ValueError:
                return 'Please set a integer!' + render_template('index.html')
                break
        quess = 500
        return render_template('index_2.html', quess=quess)
    else:
        return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def show_number():
    """Guessing number, which user choose in imagine_number().
    User choose if computer guess number or not
    """

    if request.method == 'POST':
        if request.form['text'] == "Too many":
            quess = request.form['qu']
            max = int(quess)
            min = request.form['min']
            print(min)
            if min == "":
                min = 0
            else:
                min = int(min)
            quess = int(((max - min) / 2) + min)
            return render_template('index_2.html', quess=quess, max=max)

        elif request.form['text'] == 'Not enough':
            quess = request.form['qu']
            min = int(quess)
            max = request.form['max']
            print(max)
            if max == "":
                max = 1000
            else:
                max = int(max)
            quess = int(((max - min) / 2) + min)
            return render_template('index_2.html', quess=quess, min=min)

        elif request.form['text'] == 'Guess it':
            string = 'I won!!!'
            return render_template('index_3.html', string=string)
    else:
        return render_template('index_2.html')


app.run(debug=True)