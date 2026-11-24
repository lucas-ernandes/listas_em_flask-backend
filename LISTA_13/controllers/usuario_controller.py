from flask import render_template, request, redirect, url_for, flash

from model.usuario import Usuario

def novo():
    return render_template('cadastro.html')

def salvar():
    data = request.form
    
    usuario = Usuario(data=data)
    
    if usuario.validate():
        
        if usuario.save():
            flash('Usuario cadastrado com sucesso!', 'success')
            return redirect(url_for('usuario_novo'))
    
        else:
            flash('Não foi possivel cadastrar o usuario. Tente novamente!', 'danger')
    
    else:
        for erro in usuario.errors:
            flash(erro, 'danger')

    return render_template('cadastro.html')