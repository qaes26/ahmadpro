# ahmad app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# الدالة is_prime لتحديد ما إذا كان الرقم أوليًا أم لا
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# المسار الجديد لصفحة الترحيب الافتراضية
@app.route('/')
def welcome():
    return render_template('welcome.html')

# المسار لفحص الأعداد الأولية (يستقبل GET و POST)
@app.route('/prime_checker', methods=['GET', 'POST'])
def prime_checker():
    result = None
    input_number = None

    if request.method == 'POST':
        try:
            input_number = int(request.form['number_to_check'])
            if is_prime(input_number):
                result = f"{input_number} is prime."
            else:
                result = f"{input_number} is not prime."
        except ValueError:
            result = "Invalid input. Please enter an integer."

    # هنا التأكد من أننا نعرض index.html مع النتائج
    return render_template('index.html', result=result, input_number=input_number)

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)