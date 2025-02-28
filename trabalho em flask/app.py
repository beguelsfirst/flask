from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        "name": "Seu Nome",
        "bio": "Desenvolvedor apaixonado por tecnologia e inovação.",
        "email": "seuemail@example.com",
        "phone": "+55 11 99999-9999"
    }
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
