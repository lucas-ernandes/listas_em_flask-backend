from flask import render_template, request, redirect, url_for, flash, session

from model.usuario import Usuario

def inicio():
    return render_template('index.html')

def _iniciar_sessao(usuario):
    session.clear()
    
    if isinstance(usuario, Usuario):
        usuario = Usuario.get_by_username(usuario.data['username'])
    
    session['usuario_id'] = usuario['id_usuario']
    session['username'] = usuario['username']
    

def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')
    
    if request.method == 'POST':
        data = request.form
    
        usuario = Usuario(data=data)
    
        if usuario.validate():
            if usuario.save():
                _iniciar_sessao(usuario)
                flash('Usuario cadastrado com sucesso!', 'success')
                return redirect(url_for('inicio'))
        
            else:
                flash('Não foi possivel cadastrar o usuario. Tente novamente!', 'danger')
    
        else:
            for erro in usuario.errors:
                flash(erro, 'danger')

        return render_template('cadastro.html')
    
    
def login():
    if request.method == 'POST':
        usuario = Usuario.autenticar(
            request.form.get('username'),
            request.form.get('password'),
        )
        
        if usuario is None:
            flash('Nome ou senha incorretos.', 'error')
        else:
            _iniciar_sessao(usuario)
            return redirect(url_for('inicio'))
        
    return render_template('login.html')

def logout():
    session.clear()
    return redirect(url_for('login'))