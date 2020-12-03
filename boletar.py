import json
import requests
from datetime import datetime

cpf_pagador = "43482163715"
cnpj_beneficiario = "32067312000109"

rotas = {
    "emissao_boleto": "https://apis.bancointer.com.br/openbanking/v1/certificado/boletos",
    "consulta_boleto": "",
    "baixa_pdf": "",
    "recupera_pdf": "",
}

now = datetime.now()
r = requests.post(
    rotas["emissao_boleto"],
    data=json.dumps({
        "pagador":{
            "cnpjCpf": cpf_pagador,
            "nome":"Nome do Pagador",
            "email":"",
            "telefone":"",
            "cep":"99999999",
            "numero":"00",
            "complemento":"",
            "bairro":"Bairro do Pagador",
            "cidade":"Cidade do Pagador",
            "uf":"MG",
            "endereco":"Logradouro do Pagador",
            "ddd":"",
            "tipoPessoa":"FISICA"
        },
        "seuNumero":"00000",
        "dataEmissao": now.strftime("%Y-%m-%d"),
        "dataLimite":"TRINTA",
        "dataVencimento":"2020-12-25",
        "mensagem":{
            "linha1":"mensagem na linha 1",
            "linha2":"mensagem na linha 2",
            "linha3":"mensagem na linha 3",
            "linha4":"mensagem na linha 4",
            "linha5":"mensagem na linha 5"
        },
        "desconto1":{
            "codigoDesconto":"NAOTEMDESCONTO",
            "taxa":0,
            "valor":0,
            "data":""
        },
        "desconto2":{
            "codigoDesconto":"NAOTEMDESCONTO",
            "taxa":0,
            "valor":0,
            "data":""
        },
        "desconto3":{
            "codigoDesconto":"NAOTEMDESCONTO",
            "taxa":0,
            "valor":0,
            "data":""
        },
        "valorNominal":100,
        "valorAbatimento":0,
        "multa":{
            "codigoMulta":"NAOTEMMULTA",
            "valor":0,
            "taxa":0
        },
        "mora":{
            "codigoMora":"ISENTO",
            "valor":0,
            "taxa":0
        },
        "cnpjCPFBeneficiario": cnpj_beneficiario,
        "numDiasAgenda":"TRINTA"
    }),
    headers={
        "x-inter-conta-corrente": "24737160",
        "content-type": "application/json",
    },
    cert=(
        '/path-to-file/certificado.crt',
        '/path-to-file/seudominio.key',
    )
)
print(r.status_code, r.text, r)
