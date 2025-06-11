from fastapi import FastAPI, Form, Depends
from sqlalchemy.orm import Session
import re
from database import Base, engine, SessionLocal
from model import Usuario
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou use ["http://127.0.0.1:5500"] para mais segurança
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

Base.metadata.create_all(bind=engine)



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
    else:
        db = SessionLocal()

        novo_usuario = Usuario(
            email = email,
            password_hash = password,
            fullname = fullname,
            user = user
        )

        email_existente = db.query(Usuario).filter(Usuario.email == email).first()

        if email_existente:
            return {f"Email já existente. Tente fazer o login!"}

        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        db.close()


@app.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    db = SessionLocal()

    usuario = db.query(Usuario).filter(Usuario.email == email).first()

    if not usuario:
        db.close()
        return{f"Dados errados, ou conta inexistente "}
    if usuario.password_hash != password:
        db.close()
        return {"erro": "Senha incorreta"}
    else:
        db.close()
