# -*- coding: cp1252 -*-
import sqlite3
import os
class dao():

    def __init__(self):
        pass

    def criandoBanco(self):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE post (
                idPost TEXT NOT NULL PRIMARY KEY,
                texto VARCHAR(500) NOT NULL,
                criado_em DATE NOT NULL,
                idSentimento INTEGER NOT NULL
                );            
        """)

        cursor.execute("""
            CREATE TABLE comentario (
                idComentario TEXT NOT NULL PRIMARY KEY,
                idUsuario TEXT NOT NULL,
                texto VARCHAR(500) NOT NULL,
                criado_em DATE NOT NULL,
                idSentimento INTEGER NOT NULL,
                FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario)
                );
        """)

        cursor.execute("""
            CREATE TABLE post_comentario (
                idPost TEXT NOT NULL,
                idComentario TEXT NOT NULL,
                FOREIGN KEY(idPost) REFERENCES post(idPost),
                FOREIGN KEY(idComentario) REFERENCES comentario(idComentario)
                );
        """)
        
        cursor.execute("""
            CREATE TABLE usuario (
                idUsuario TEXT NOT NULL PRIMARY KEY,
                nome TEXT NOT NULL,
                genero TEXT,
                data DATE,
                Educacao TEXT
                );
        """)
        
        cursor.execute("""
            CREATE TABLE curtidasPost (
                idPost TEXT NOT NULL,
                idUsuario TEXT NOT NULL,            
                FOREIGN KEY(idPost) REFERENCES post(idPost),
                FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario)
                );
        """)

        cursor.execute("""
            CREATE TABLE sentimento (
                idSentimento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL
                );
        """)
        print 'Tabela post criada com sucesso.'
        conexao.close()

    def inserirPost(self, idPost, mensagem, data):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    INSERT INTO post(idPost, texto, criado_em, idSentimento)
                    VALUES (?,?,?,?)
                    """, (idPost, mensagem, data, 1))
                
            conexao.commit()

        except:
            print 'Erro inserirPost.'

        conexao.close()

    def inserirUsuario(self, idUsuario, nome, sexoUsuario, aniversarioUsuario, educacaoUsuario):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')
        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    INSERT INTO usuario(idUsuario, nome, genero, data, Educacao)
                    VALUES (?,?,?,?,?)
                    """, (idUsuario, nome, sexoUsuario, aniversarioUsuario, educacaoUsuario))
                
            conexao.commit()

        except:
            print 'Erro inserirUsuario.'

        conexao.close()

    def inserirComentario(self, idComentario, idUsuario, texto, criado_em):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')
        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    INSERT INTO comentario(idComentario, idUsuario, texto, criado_em, idSentimento)
                    VALUES (?,?,?,?,?)
                    """, (idComentario, idUsuario, texto, criado_em, 1))
                
            conexao.commit()

        except:
            print 'Erro inserirComentario.'

        conexao.close()

    def inserirCurtidasPost(self, idPost, idUsuario):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    INSERT INTO curtidasPost(idPost, idUsuario)
                    VALUES (?,?)
                    """, (idPost, idUsuario))
                
            conexao.commit()

        except:
            print 'Erro inserirCurtidasPost.'

        conexao.close()

    def inserirPostComentario(self, idPost, idComentario):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    INSERT INTO post_comentario(idPost, idComentario)
                    VALUES (?,?)
                    """, (idPost, idComentario))
                
            conexao.commit()
            
        except:
            print 'Erro inserirPostComentario.'

        conexao.close()

    def postExiste(self, idPost):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    SELECT *
                    FROM post
                    WHERE idPost = ?
                    """, (idPost,))
            
            if cursor.fetchone() == None:
                return False
            else:
                return True

        except:
            print 'Erro postExiste.'

        conexao.close()

    def usuarioExiste(self, idUsuario):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    SELECT *
                    FROM usuario
                    WHERE idUsuario = ?
                    """, (idUsuario,))
            
            if cursor.fetchone() == None:
                return False
            else:
                return True

        except:
            print 'Erro usuarioExiste.'

        conexao.close()

    def curtidasPostExiste(self, idPost, idUsuario):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    SELECT *
                    FROM curtidasPost
                    WHERE idPost = ?
                    AND idUsuario = ?
                    """, (idPost, idUsuario,))
            
            if cursor.fetchone() == None:
                return False
            else:
                return True

        except:
            print 'Erro curtidasPostExiste.'

        conexao.close()

    def comentarioExiste(self, idComentario):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    SELECT *
                    FROM comentario
                    WHERE idComentario = ?
                    """, (idComentario,))
            
            if cursor.fetchone() == None:
                return False
            else:
                return True

        except:
            print 'Erro comentarioExiste.'

        conexao.close()

    def postComentarioExiste(self, idPost, idComentario):
        conexao = sqlite3.connect(os.getcwd()+'//banco//dwEstelita.sqlite')

        try:
            cursor = conexao.cursor()
            
            cursor.execute("""
                    SELECT *
                    FROM post_comentario
                    WHERE idPost = ?
                    AND idComentario = ?
                    """, (idPost, idComentario,))
            
            if cursor.fetchone() == None:
                return False
            else:
                return True

        except:
            print 'Erro postComentarioExiste.'

        conexao.close()
    
##d = dao()
##
##d.criandoBanco()
##
##d.inserirUsuario('1','Teste')
##
##print d.usuarioExiste('1')
