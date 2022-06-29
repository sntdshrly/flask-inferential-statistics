from asyncio.windows_events import NULL
from flask import Flask, render_template, url_for, redirect, request, jsonify
import math
import statistics
from scipy.stats import norm
from scipy import stats
import numpy as np
import scipy
# python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose (write this on your command prompt)

app = Flask(__name__)
app.config["SECRET_KEY"] = ""


@app.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """
    return render_template('index.html')

@app.route('/index_two', methods=['GET'])
def index_two():
    """ Displays the index page accessible at '/' """
    return render_template('index_two.html')


@app.route('/operation_result', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""

    result = None

    # request.form looks for: html tags with matching "name= "
    operation = request.form['operation']
    inputAll = []

    try:
        if operation == "val1":
            input1 = float(request.form['Input1'])
            result = norm.ppf(((1-input1)/2)+input1)
            inputAll.append(input1)

        elif operation == "val2":
            input2 = float(request.form['Input2'])
            input2b = int(request.form['Input2b'])
            df = input2b-1
            result = scipy.stats.t.ppf(((1-input2)/2), df)
            inputAll.append(input2)
            inputAll.append(input2b)

        elif operation == "val3":
            input3 = float(request.form['Input3'])
            radioButt = str(request.form['radioButt'])
            if radioButt == "left tail" or radioButt == "right tail":
                Zc = norm.ppf(input3)
            elif radioButt == "two tail":
                Zc = norm.ppf(input3/2)
            result = Zc
            inputAll.append(input3)
            inputAll.append(radioButt)

        elif operation == "val4":
            input4 = float(request.form['Input4'])
            input4b = int(request.form['Input4b'])
            df = input4b - 1
            chiKanan = (1-input4)/2
            chiKiri = (1+input4)/2
            X2 = []
            X2.append(scipy.stats.chi2.ppf(chiKiri, df))
            X2.append(scipy.stats.chi2.ppf(chiKanan, df))
            result = X2
            inputAll.append(input4)
            inputAll.append(input4b)

        elif operation == "val5":
            input5 = float(request.form['Input5'])
            input5b = float(request.form['Input5b'])
            result = (input5 + input5b) / 2
            inputAll.append(input5)
            inputAll.append(input5b)

        elif operation == "val6":
            input6 = float(request.form['Input6'])
            Zc = norm.ppf(((1-input6)/2)+input6)
            input6b = float(request.form['Input6b'])
            input6c = float(request.form['Input6c'])
            result = []
            result.append((Zc * input6b / input6c)**2)
            result.append(math.ceil((Zc * input6b / input6c)**2))
            inputAll.append(input6)
            inputAll.append(input6b)
            inputAll.append(input6c)

        elif operation == "val7":
            p = float(request.form['Input7'])
            q = 1-p
            c = float(request.form['Input7b'])
            Zc = norm.ppf(((1-c)/2)+c)
            E = float(request.form['Input7c'])
            result = []
            result.append(p * q * (Zc/E)**2)
            result.append(math.ceil(p * q * (Zc/E)**2))
            inputAll.append(p)
            inputAll.append(c)
            inputAll.append(E)

        elif operation == "val8":
            x = float(request.form['Input8'])
            c = float(request.form['Input8b'])
            sigma = float(request.form['Input8c'])
            n = int(request.form['Input8d'])
            Zc = norm.ppf(((1-c)/2)+c)
            marginErrorKiri = x - Zc * sigma / math.sqrt(n)
            marginErrorKanan = x + Zc * sigma / math.sqrt(n)
            result = []
            result.append(marginErrorKiri)
            result.append(marginErrorKanan)
            inputAll.append(x)
            inputAll.append(c)
            inputAll.append(sigma)
            inputAll.append(n)

        elif operation == "val9":
            x = float(request.form['Input9'])
            c = float(request.form['Input9b'])
            s = float(request.form['Input9c'])
            n = int(request.form['Input9d'])
            Zc = norm.ppf(((1-c)/2)+c)
            df = n - 1
            tc = scipy.stats.t.ppf(((1-c)/2), df)
            tc = tc * -1
            marginErrorKiri = x - tc * s / math.sqrt(n)
            marginErrorKanan = x + tc * s / math.sqrt(n)
            result = []
            result.append(marginErrorKiri)
            result.append(marginErrorKanan)
            inputAll.append(x)
            inputAll.append(c)
            inputAll.append(s)
            inputAll.append(n)

        elif operation == "val10":
            n = float(request.form['Input10'])
            s = float(request.form['Input10b'])
            c = float(request.form['Input10c'])
            df = n-1
            chiKanan = (1-c)/2
            chiKiri = (1+c)/2
            X2L = scipy.stats.chi2.ppf(chiKiri, df)
            X2R = scipy.stats.chi2.ppf(chiKanan, df)
            radioButt2 = str(request.form['radioButt2'])
            if radioButt2 == "variance":
                X2RIGHT = (n-1)*(s**2)/X2R
                X2LEFT = (n-1)*(s**2)/X2L
            elif radioButt2 == "standard deviation":
                X2RIGHT = math.sqrt((n-1)*(s**2)/X2R)
                X2LEFT = math.sqrt((n-1)*(s**2)/X2L)
            result = []
            result.append(X2RIGHT)
            result.append(X2LEFT)
            inputAll.append(n)
            inputAll.append(s)
            inputAll.append(c)
            inputAll.append(radioButt2)

        elif operation == "val11":
            n = int(request.form['Input11'])
            x = float(request.form['Input11b'])
            c = float(request.form['Input11c'])
            p = x/n
            q = 1 - p
            Zc = norm.ppf(((1-c)/2)+c)
            peluangKanan = p + Zc * math.sqrt((p*q)/n)
            peluangKiri = p - Zc * math.sqrt((p*q)/n)
            result = []
            result.append(peluangKiri)
            result.append(peluangKanan)
            inputAll.append(n)
            inputAll.append(x)
            inputAll.append(c)

        elif operation == "val12":
            radioButt3 = str(request.form['radioButt3'])
            c = float(request.form['Input12'])
            n = int(request.form['Input12b'])
            s = float(request.form['Input12c'])
            if (radioButt3 == 'normal'):
                Zc = norm.ppf(((1-c)/2)+c)
                marginError = Zc * s / math.sqrt(n)
            elif (radioButt3 == 'student'):
                df = n - 1
                tc = scipy.stats.t.ppf(((1-c)/2), df)
                marginError = tc * s / math.sqrt(n)
            result = marginError
            inputAll.append(c)
            inputAll.append(n)
            inputAll.append(s)

        elif operation == "val13":
            alfa = float(request.form['Input13'])
            n = int(request.form['Input13b'])
            df = n-1
            tc = stats.t.ppf(alfa,df)

            result = tc
            inputAll.append(alfa)
            inputAll.append(n)

        elif operation == "val14":
            alfa = float(request.form['Input14'])
            n = int(request.form['Input14b'])
            df = n-1
            t_kiri = stats.t.ppf((alfa/2),df) # Daerah Penolakan / t-Score
            t_kanan = stats.t.ppf((1-(alfa/2)),df)
            result = []
            result.append(t_kiri)
            result.append(t_kanan)
            inputAll.append(alfa)
            inputAll.append(n)

        return render_template(
            'index.html',
            operation=operation,
            result=result,
            calculation_success=True,
            inputAll=inputAll
        )

    except ValueError:
        return render_template(
            'index.html',
            calculation_success=False,
            error="Cannot perform numeric operations with provided input"
        )

@app.route('/operation_result_two', methods=['POST'])
def operation_result_two():
    """Route where we send calculator form input"""

    result = None

    # request.form looks for: html tags with matching "name= "
    operation = request.form['operation']
    inputAll = []

    try:
        if operation == "val1":
            alfa = float(request.form['Input1'])
            H0 = str(request.form['Input1b'])
            Ha = str(request.form['Input1c'])
            z = float(request.form['Input1d'])
            tail = str(request.form['radioButt'])
            if tail == 'left tail' or tail == 'right tail':
                z0 = norm.ppf(alfa) # Daerah Penolakan / Z-Score
            elif tail == 'two tail':
                z0 = norm.ppf(alfa/2) # Daerah Penolakan / Z-Score

            if z >= 0:
                A = 1-norm.cdf(z,0,1) # Peluang Kumulatif
            elif z < 0:
                A = norm.cdf(z,0,1) # Peluang Kumulatif

            if tail == 'two tail':
                p = 2 * A
                if p <= alfa :
                    statement = "reject H0"
                elif p > alfa :
                    statement = "failed to reject H0"
            elif tail == 'left tail' or tail == 'right tail':
                p = A
                if p <= alfa :
                    statement = "reject H0"
                elif p > alfa :
                    statement = "failed to reject H0"

            result = []
            result.append(z0)
            result.append(z)
            result.append(p)
            result.append(statement)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
        
        elif operation == "val2":
            alfa = float(request.form['Input2'])
            H0 = str(request.form['Input2b'])
            Ha = str(request.form['Input2c'])
            x_bar = float(request.form['Input2d'])
            mu = float(request.form['Input2e'])
            sigma = float(request.form['Input2f'])
            n = int(request.form['Input2g'])
            z = ( x_bar - mu ) / ( sigma / math.sqrt(n))
            tail = str(request.form['radioButt2'])
            if tail == 'left tail' or tail == 'right tail':
                z0 = norm.ppf(alfa) # Daerah Penolakan / Z-Score
            elif tail == 'two tail':
                z0 = norm.ppf(alfa/2) # Daerah Penolakan / Z-Score

            if z >= 0:
                A = 1-norm.cdf(z,0,1) # Peluang Kumulatif
            elif z < 0:
                A = norm.cdf(z,0,1) # Peluang Kumulatif

            if tail == 'two tail':
                p = 2 * A
                if p <= alfa :
                    statement = "reject H0"
                elif p > alfa :
                    statement = "failed to reject H0"
            elif tail == 'left tail' or tail == 'right tail':
                p = A
                if p <= alfa :
                    statement = "reject H0"
                elif p > alfa :
                    statement = "failed to reject H0"

            result = []
            result.append(z0)
            result.append(z)
            result.append(p)
            result.append(statement)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)

        elif operation == "val3":
            alfa = float(request.form['Input3'])
            H0 = str(request.form['Input3b'])
            Ha = str(request.form['Input3c'])
            t = float(request.form['Input3d'])
            n = int(request.form['Input3e'])
            tail = str(request.form['radioButt3'])
            df = n-1
            if tail == 'left tail':
                t0 = stats.t.ppf(alfa,df) # Daerah Penolakan / t-Score
                if t >= t0 :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"                
            elif tail == 'right tail':
                t0 = (stats.t.ppf((1-alfa),df)) # Daerah Penolakan / t-Score
                if t <= t0 :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"

            result = []
            result.append(t0)
            result.append(t)
            result.append(statement)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
            inputAll.append(n)

        elif operation == "val4":
            alfa = float(request.form['Input4'])
            H0 = str(request.form['Input4b'])
            Ha = str(request.form['Input4c'])
            t = float(request.form['Input4d'])
            n = int(request.form['Input4e'])
            tail = str(request.form['radioButt4'])
            df = n-1
            t0_kiri = stats.t.ppf((alfa/2),df) # Daerah Penolakan / t-Score
            t0_kanan = (stats.t.ppf((1-(alfa/2)),df)) # Daerah Penolakan / t-Score
            if t >= t0_kiri and t <= t0_kanan :
                statement = "failed to reject H0"
            else:
                statement = "reject H0"
            result = []
            result.append(t0_kiri)
            result.append(t)
            result.append(statement)
            result.append(t0_kanan)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
            inputAll.append(n)

        elif operation == "val5":
            alfa = float(request.form['Input5'])
            H0 = str(request.form['Input5b'])
            Ha = str(request.form['Input5c'])
            n = int(request.form['Input5d'])
            x_bar = float(request.form['Input5e'])
            mu = float(request.form['Input5f'])
            s = float(request.form['Input5g'])
            tail = str(request.form['radioButt5'])
            df = n-1
            t = ( x_bar - mu ) / ( s / math.sqrt(n))
            if tail == 'left tail':
                t0 = stats.t.ppf(alfa,df) # Daerah Penolakan / t-Score
                if t >= t0 :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"                
            elif tail == 'right tail':
                t0 = (stats.t.ppf((1-alfa),df)) # Daerah Penolakan / t-Score
                if t <= t0 :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"

            result = []
            result.append(t0)
            result.append(t)
            result.append(statement)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
            inputAll.append(n)

        elif operation == "val6":
            alfa = float(request.form['Input6'])
            H0 = str(request.form['Input6b'])
            Ha = str(request.form['Input6c'])
            n = int(request.form['Input6d'])
            x_bar = float(request.form['Input6e'])
            mu = float(request.form['Input6f'])
            s = float(request.form['Input6g'])
            tail = str(request.form['radioButt6'])
            df = n-1
            t = ( x_bar - mu ) / ( s / math.sqrt(n))
            t0_kiri = stats.t.ppf((alfa/2),df) # Daerah Penolakan / t-Score
            t0_kanan = (stats.t.ppf((1-(alfa/2)),df)) # Daerah Penolakan / t-Score
            if t >= t0_kiri and t <= t0_kanan :
                statement = "failed to reject H0"
            else:
                statement = "reject H0"

            result = []
            result.append(t0_kiri)
            result.append(t)
            result.append(statement)
            result.append(t0_kanan)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
            inputAll.append(n)

        elif operation == "val7":
            alfa = float(request.form['Input7'])
            H0 = str(request.form['Input7b'])
            Ha = str(request.form['Input7c'])
            n = int(request.form['Input7d'])
            tail = str(request.form['radioButt7'])
            if str(request.form['Input7e'])  == "-999":
                p_topi = float(request.form['Input7f'])
                p = float(request.form['Input7g'])
                z = ( p_topi - p ) / math.sqrt(p * (1-p) / n)
            else:
                z = float(request.form['Input7e'])

            if tail == 'left tail':
                z0 = norm.ppf(alfa) # Daerah Penolakan / t-Score
                if z >= z0 :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"
            elif tail == 'right tail':
                z0 = norm.ppf(1-alfa) # Daerah Penolakan / t-Score
                if z <= z0 :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"

            result = []
            result.append(z0)
            result.append(z)
            result.append(statement)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
            inputAll.append(n)

        elif operation == "val8":
            alfa = float(request.form['Input8'])
            H0 = str(request.form['Input8b'])
            Ha = str(request.form['Input8c'])
            n = int(request.form['Input8d'])
            tail = str(request.form['radioButt8'])
            if str(request.form['Input8e'])  == "-999":
                p_topi = float(request.form['Input8f'])
                p = float(request.form['Input8g'])
                z = ( p_topi - p ) / math.sqrt(p * (1-p) / n)
            else:
                z = float(request.form['Input8e'])

            if tail == 'two tail':
                z0_kiri = norm.ppf((alfa/2)) # Daerah Penolakan / t-Score
                z0_kanan = norm.ppf((1-(alfa/2))) # Daerah Penolakan / t-Score
                if z >= z0_kiri and z <= z0_kanan :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"

            result = []
            result.append(z0_kiri)
            result.append(z0_kanan)
            result.append(z)
            result.append(statement)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
            inputAll.append(n)

        elif operation == "val9":
            alfa = float(request.form['Input9'])
            H0 = str(request.form['Input9b'])
            Ha = str(request.form['Input9c'])
            n = int(request.form['Input9d'])
            tail = str(request.form['radioButt9'])
            df = n-1
            chi0 = scipy.stats.chi2.ppf(alfa, df) # Daerah Penolakan / t-Score
            if str(request.form['Input9e'])  == "-999":
                s = float(request.form['Input9f'])
                var = float(request.form['Input9g'])
                if str(request.form['radioButt10'])  == "variance":
                    chi = ( n - 1 ) * s / var
                elif str(request.form['radioButt10'])  == "standard deviation":
                    chi = ( n - 1 ) * s**2 / var**2
            else:
                chi = float(request.form['Input9e'])

            if tail == 'left tail':
                if chi >= chi0 :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"
            elif tail == 'right tail':
                if chi <= chi0 :
                    statement = "failed to reject H0"
                else:
                    statement = "reject H0"

            result = []
            result.append(chi0)
            result.append(chi)
            result.append(statement)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
            inputAll.append(n)

        elif operation == "val10":
            alfa = float(request.form['Input10'])
            H0 = str(request.form['Input10b'])
            Ha = str(request.form['Input10c'])
            n = int(request.form['Input10d'])
            tail = str(request.form['radioButt11'])
            df = n-1
            chi0_kiri = scipy.stats.chi2.ppf(alfa/2, df) # Daerah Penolakan / t-Score
            chi0_kanan = scipy.stats.chi2.ppf(1-(alfa/2), df) # Daerah Penolakan / t-Score
            if str(request.form['Input10e'])  == "-999":
                s = float(request.form['Input10f'])
                var = float(request.form['Input10g'])
                if str(request.form['radioButt12'])  == "variance":
                    chi = ( n - 1 ) * s / var
                elif str(request.form['radioButt12'])  == "standard deviation":
                    chi = ( n - 1 ) * s**2 / var**2
            else:
                chi = float(request.form['Input10e'])

        if tail == 'two tail':
            if chi >= chi0_kiri and chi <= chi0_kanan :
                statement = "failed to reject H0"
            else:
                statement = "reject H0"

            result = []
            result.append(chi0_kiri)
            result.append(chi)
            result.append(statement)
            result.append(chi0_kanan)
            inputAll.append(alfa)
            inputAll.append(H0)
            inputAll.append(Ha)
            inputAll.append(tail)
            inputAll.append(n)

        return render_template(
            'index_two.html',
            operation=operation,
            result=result,
            calculation_success=True,
            inputAll=inputAll
        )

    except ValueError:
        return render_template(
            'index_two.html',
            calculation_success=False,
            error="Cannot perform numeric operations with provided input"
        ) 


if __name__ == "__main__":
   app.run(debug=True, port=5001, threaded=True)
    # app.run(host='0.0.0.0', debug=True, port=80)