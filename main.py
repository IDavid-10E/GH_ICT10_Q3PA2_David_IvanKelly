from pyscript import display, document

def students_classification(e):
    document.getElementById('result').innerHTML = ''

    classification = float(document.getElementById('number1').value)

    if classification >= 95:
        display('Bergamo 1', target='result')
    elif 91 <= classification <= 94:
        display('Bergamo 2', target='result')
    elif 86 <= classification <= 90:
        display('Bergamo 3', target='result')
    elif 75 <= classification <= 85:
        display('Perugia 1', target='result')
    elif 65 <= classification <= 74:
        display('Perugia 2', target='result')
