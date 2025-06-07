from fastapi import FastAPI, Form
import re

app = FastAPI()

ListErrorEmail = []
listErrorSenha = []
listErrorName = []

#validação de senha
def validar_senha(senha : str):
    if len(senha) < 7:
        listErrorSenha.append("A senha tem menos de 8 digitos!")
    
    if not re.search(r'[A-Z]', senha):
        listErrorSenha.append("A senha não tem letra maiúscula!")
        

    if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-]', senha):
        listErrorSenha.append("A senha não tem símbolos!")


    if not re.search(r'\d', senha):
        listErrorSenha.append("A senha não tem números!")

    return listErrorSenha


#validação de nome completo
def validar_nome(nome: str):
    if not re.search(r'\s', nome):
        listErrorName.append("O nome completo precisa ter nome e sobrenome")

    if not re.search(r'[A-Z]', nome):
        listErrorName.append("O nome completo não tem letra maiúscula!")

    return listErrorName

#validação de email
def validar_email(email: str):
    if not re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        ListErrorEmail.append("O email não é valido")

#a
@app.post("/cadastro")
def cadastro(fullname: str = Form(...), email: str = Form(...), user: str = Form(...), password: str = Form(...)):
    validar_senha(password)
    validar_nome(fullname)
    validar_email(email)
    
    if listErrorName:
        mensage = {f"O nome completo esta errado: {listErrorName.copy()}"}
        listErrorName.clear()
        return mensage
    elif ListErrorEmail:
        mensage = {f"A senha esta errada: {ListErrorEmail.copy()}"}
        ListErrorEmail.clear()
        return mensage
    elif listErrorSenha:
        mensage = {f"A senha esta errada: {listErrorSenha.copy()}"}
        listErrorSenha.clear()
        return mensage
        

