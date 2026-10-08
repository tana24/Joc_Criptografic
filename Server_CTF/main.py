from flask import Flask, render_template, request, redirect, url_for
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import random
import binascii
app = Flask(__name__)
prime_list =[100000006109,123456766789,234235253279,753267236563,678827367227,112345645837,987654323753,325432114459,234654321283,234654321149]
# Pagina principală
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == '7682':
            return redirect(url_for('khai'))  
        else:
            message = "Nu-i bun"
            return render_template('index.html', message=message)

    return render_template('index.html', message='')

# Pagina pentru convertor ASCII
@app.route('/ascii_long', methods=['GET', 'POST'])
def ascii_long():
    text_to_number_result = ""
    number_to_text_result = ""
    if request.method == 'POST':
        # Conversie Text în Număr
        text = request.form.get('text')
        if text:
            text_bytes = text.encode('ascii')
            text_to_number_result = f"Echivalentul numeric: {bytes_to_long(text_bytes)}"
        
        # Conversie Număr în Text
        number = request.form.get('number')
        if number:
            try:
                number_int = int(number)
                number_to_text_result = f"Echivalentul text: {long_to_bytes(number_int).decode('ascii')}"
            except ValueError:
                number_to_text_result = "Te rog să introduci un număr valid."
            except UnicodeDecodeError:
                number_to_text_result = "Numărul introdus nu poate fi convertit în text ASCII."

    return render_template('ascii_long.html', 
                           text_to_number_result=text_to_number_result, 
                           number_to_text_result=number_to_text_result)

@app.route('/acerea', methods=['GET', 'POST'])
def rsa_encrypt():
    encrypted_message = ""
    if request.method == 'POST':
        try:
            # Preluăm valorile N și e de la utilizator
            N = int(request.form.get('N'))
            e = int(request.form.get('e'))
            print(N,e)
            # Mesajul de criptat
            message = 6000276099170587980
            # Convertim mesajul in bytes si apoi in numar
            encrypted_message = pow(message,e,N)

        except (ValueError, TypeError):
            encrypted_message = "Valorile N și e introduse nu sunt valide."

    return render_template('rsa_encrypt.html', encrypted_message=encrypted_message)

@app.route('/acere', methods=['GET', 'POST'])
def rsa_encrypt2():
    encrypted_message = ""
    if request.method == 'POST':
        try:
            # Preluăm valorile N și e de la utilizator
            N = int(request.form.get('N'))
            e = int(request.form.get('e'))

            # Mesajul de criptat
            message = 6000276099170587980
            # Convertim mesajul in bytes si apoi in numar
            encrypted_message = pow(message,e,N)

        except (ValueError, TypeError):
            encrypted_message = "Valorile N și e introduse nu sunt valide."

    return render_template('rsa_encrypt.html', encrypted_message=encrypted_message)
@app.route('/khai', methods=['GET', 'POST'])
def khai():
    if request.method == 'POST':
        raspuns_motivatie = request.form.get('motivatie')
        raspuns_pastarnac = request.form.get('pastarnac')
        
        # Comparăm răspunsurile convertite în litere mici
        if raspuns_motivatie.lower() == 'motivatiea' and raspuns_pastarnac.lower() == 'secretula':
            return redirect(url_for('subtine'))
        
    return render_template('khai.html')
@app.route("/random_2_primes")
def random_2_primes():
    # alege 2 elemente diferite aleator
    
    p, q = random.sample(prime_list, 2)
    while p==q:
        p, q = random.sample(prime_list, 2)
    return render_template("random_2_primes.html",p=p,q=q)
@app.route("/spargator")
def spargator():
    return render_template("spargator.html")
@app.route('/subtine')
def subtine():
    return """<h1>
Într-un colț uitat al unei universități prestigioase, profesorul Sokoevski, <br>
un geniu al criptografiei, își trăia viața în umbra mentorului său, profesorul Anton.<br>
Deși avea talent nativ, Sokoevski simțea că nu va putea niciodată să strălucească<br>
atât de puternic ca Anton, care deținuse mereu secretele celor mai complexe cifruri.<br><br>
Pe măsură ce anii treceau, invidia și ambiția s-au transformat în obsesie. <br>
Sokoevski a început să viseze la un cifru legendar, pe care Anton l-a dezvoltat și <br>
care era capabil să protejeze orice informație. Era o comoară a cunoștințelor, iar <br>
 Sokoevski voia să o aibă pentru sine. Gândurile lui întunecate au început să-l consume.<br><br>
Într-o noapte furtunoasă, când toată lumea dormea, Sokoevski s-a decis să-și pună planul <br>
în aplicare. A pătruns în biroul lui Anton, unde găsise cărți vechi și papirusuri pline de note, <br>
dar cel mai important, a descoperit jurnalul profesorului, plin de formule și idei despre cifruri. <br>
Cu fiecare pagină pe care o răsfoia, invidia lui creștea, transformându-se într-o furie devastatoare…<h1>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

