from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mysql123!@localhost/mytestdb'

db = SQLAlchemy(app)

class Requerimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))

with app.app_context():
    # Crie as tabelas no banco de dados
    db.create_all()

@app.route('/requerimento', methods=['GET', 'POST'])
def requerimento():
    if request.method == 'POST':
        nome = request.form['nome']
        requerimento = Requerimento(nome=nome)
        db.session.add(requerimento)
        db.session.commit()
        return redirect('/')
    else:
        requerimentos = Requerimento.query.all()
        return render_template('index.html', requerimentos=requerimentos)

if __name__ == '__main__':
    app.run(debug=True)

 

