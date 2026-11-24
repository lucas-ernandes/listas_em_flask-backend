from flask import render_template, request, redirect, url_for, flash

from model.usuario import Usuario

def login():
    return render_template('login.html')