import json, urllib
from pprint import pprint
from criando_banco import dao

d = dao()

token = 'CAACEdEose0cBAEnwRZBPCWrWQ7ilLpDCT6SFfYZBC3ZBwvtOlOZBrMTVUrbFcUGUnlgz26Mpz8K3Wh3h75Xtcbr1mJddJxyB4WSuSNPCvDVfj3NwupPvd59YhkG5Yt6xV41NV9Gs9csLYc0npoASOjtO2GI3EMAzXByVmrcUbykrL59wZB8lfnNZCmsP20BC7HnDZCpuU9yNgHNZBaIvKYeo'

def pegarDadosUsuario(idUser):
    idUser = str(idUser)
    
    url = 'https://graph.facebook.com/v2.3/' + idUser + '?access_token='+token

    resp = urllib.urlopen(url).read()

    dados = json.loads(resp.decode('utf-8'))

    print dados

    idUser = dados['id']
    
    nomeCompleto = dados['name']

    if 'gender' in dados.keys():
        sexo = dados['gender']
    else:
        sexo = None

    if 'birthday' in dados.keys():
        aniversario = dados['birthday']
    else:
        aniversario = None

    if 'education' in dados.keys():
        education = ['education'][len(dados['education'])-1]['type']
    else:
        education = None
    
    return (idUser, nomeCompleto, sexo, aniversario, education)


ids_pages = ['320033178143669','656041921137604','1447067488906490','1431849273799074','233680560160631','241341586064569','803005986480403','253946268141958','1464043183838725','1623122437904948','706728776102230']

print 'Iniciando...'

for page in ids_pages:
    url_post = 'https://graph.facebook.com/' + page + '/posts?access_token=' + token

    resposta_post = urllib.urlopen(url_post).read()

    dados_post = json.loads(resposta_post)

    if 'error' not in dados_post.keys():

        if len(dados_post['data']) > 0:
            nomePage = dados_post['data'][0]['from']['name']
            
            print 'Page = ' + nomePage
            for dado in dados_post['data']:        
                idPost = dado['id']
##                if 'message' in dado.keys():
##                    if d.postExiste(idPost) == False:
##                        texto = dado['message']
##                        criado_em = dado['created_time'][0:10]
##                        print 'Post Novo: ' + idPost
##                        d.inserirPost(idPost,texto,criado_em)
                if 'likes' in dado.keys():
                    likes = dado['likes']['data']
                    for like in likes:
                        dadosUsuario = pegarDadosUsuario(like['id'])
                        print dadosUsuario
##                        idUsuario = dadosUsuario[0]
##                        nomeUsuario = dadosUsuario[1]
##                        sexoUsuario = dadosUsuario[2]
##                        aniversarioUsuario = dadosUsuario[3]
##                        educacaoUsuario = dadosUsuario[4]
##                        if d.usuarioExiste(idUsuario) == False:
##                            d.inserirUsuario(idUsuario, nomeUsuario, sexoUsuario, aniversarioUsuario, educacaoUsuario)
##                            print 'Usuario Novo: ' + idUsuario
##                            if d.curtidasPostExiste(dado['id'], idUsuario) == False:
##                                d.inserirCurtidasPost(dado['id'], idUsuario)
##                                print 'Curtida Novo'
                if 'comments' in dado.keys():
                    comments = dado['comments']['data']
                    for comment in comments:
                        idComentario = comment['id']
                        texto = comment['message']
                        criado_em = comment['created_time'][0:10]
                        dadosUsuario = pegarDadosUsuario(comment['from']['id'])
                        print dadosUsuario
##                        idUsuario = dadosUsuario[0]
##                        nomeUsuario = dadosUsuario[1]
##                        sexoUsuario = dadosUsuario[2]
##                        aniversarioUsuario = dadosUsuario[3]
##                        educacaoUsuario = dadosUsuario[4]
##                        if d.usuarioExiste(idUsuario) == False:
##                            d.inserirUsuario(idUsuario, nomeUsuario, sexoUsuario, aniversarioUsuario, educacaoUsuario)
##                            print 'Usuario Comentario Novo: ' + idUsuario
##                        if d.comentarioExiste(idComentario) == False:
##                            d.inserirComentario(idComentario, idUsuario, texto, criado_em)
##                            print 'Comentario Novo: ' + idComentario
##                        if d.postComentarioExiste(idPost, idComentario) == False:
##                            d.inserirPostComentario(idPost, idComentario)
##                            print 'post Comentario Novo: ' + idPost
    else:        
        print 'code: ' + str(dados_post['error']['code']) + '\nMessage: ' + dados_post['error']['message'] + '\nType: ' + dados_post['error']['type']
        
        break
print 'Terminado.'
