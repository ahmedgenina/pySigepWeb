# -*- coding: utf-8 -*-
from suds import client
import plp_xml_string

# Definindo url
url = "https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService" \
      "/AtendeCliente?wsdl"

print 'Conectando...'

# Instanciando um cliente
cliente = client.Client(url)

# Listar os metodos que o webservice utiliza
# print cliente

sgpkey = {
    'usuario': 'sigep',
    'senha': 'n5f9t8',
    'cod_admin': '08082650',
    'contrato': '9912208555',
    'cartao': '0057018901',
    'numero_servico': '40215',
    'cep_origem': '37503130',
    'cep_destino': '37503130',
    'tipo_destinatario': 'C',
    'cnpj': '34028316000103',
    'quant_etiquetas': int(1),
}

# Inicialização

# Verifica disponibilidade de servico
# verificaDisponibilidadeServico(codAdministrativo, numeroServico, cepOrigem, 
# cepDestino, usuario, senha)
disponibilidade = cliente.service.verificaDisponibilidadeServico(
    sgpkey['cod_admin'], sgpkey['numero_servico'],	sgpkey['cep_origem'],
    sgpkey['cep_destino'], sgpkey['usuario'], sgpkey['senha'])

# Solicitar dados do contrato/cartao
# buscaCliente(string idContrato, string idCartaoPostagem, string usuario,
# string senha)
busca_cliente = cliente.service.buscaCliente(sgpkey['contrato'],
                                             sgpkey['cartao'],
                                             sgpkey['usuario'],
                                             sgpkey['senha'])
sgpkey['id_servico'] = long(104707)
cliente_cnpj = busca_cliente.cnpj
year = busca_cliente.dataAtualizacao.year
contrato_list = busca_cliente.contratos
cod_client = contrato_list[0].codigoCliente

print busca_cliente.contratos[0].contratoPK.numero
print busca_cliente.contratos[0].cartoesPostagem[0].codigoAdministrativo
print busca_cliente.contratos[0].cartoesPostagem[0].numero
print busca_cliente.nome


# Consulta CEP
# consultaCEP(string cep)
cep = cliente.service.consultaCEP(sgpkey['cep_destino'])
# bairro = cep.bairro

#print cep

# Verificando status do cartao
# getStatusCartaoPostagem(string numeroCartaoPostagem, string usuario,
# string senha)
status = cliente.service.getStatusCartaoPostagem(sgpkey['cartao'],
                                                 sgpkey['usuario'],
                                                 sgpkey['senha'])

# Solicitar etiquetas por demanda
# solicitaEtiquetas(string tipoDestinatario, string identificador,
# long idServico, int qtdEtiquetas, string usuario, string senha)
solicit_etiq = cliente.service.solicitaEtiquetas(sgpkey['tipo_destinatario'],
                                                 sgpkey['cnpj'],
                                                 sgpkey['id_servico'],
                                                 sgpkey['quant_etiquetas'],
                                                 sgpkey['usuario'],
                                                 sgpkey['senha'])

etiquetas_sem_dig = solicit_etiq.split(',')
digito_verificador = cliente.service.geraDigitoVerificadorEtiquetas(
    etiquetas_sem_dig, sgpkey['usuario'], sgpkey['senha'])

etiqueta_com_digito = []

# Adiciona digito verificador no espaco em branco da etiqueta
for i in range(0, len(etiquetas_sem_dig)):
    aux = etiquetas_sem_dig[i].replace(' ', str(digito_verificador[i]))
    etiqueta_com_digito.append(aux)

# print etiqueta_com_digito

xml = plp_xml_string.get_xml(busca_cliente, cep)

print 'Validando xml'
print plp_xml_string.validate_XML(xml)


# Definindo url
url_calc = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL'

print 'Conectando webservice consulta prazo e preco'

# Instanciando um cliente
webservice_calc = client.Client(url_calc)

# print webservice_calc

# CalcPrecoPrazo(string nCdEmpresa, string sDsSenha, string nCdServico,
# string sCepOrigem, string sCepDestino, string nVlPeso, int nCdFormato,
# decimal nVlComprimento, decimal nVlAltura, decimal nVlLargura,
# decimal nVlDiametro, string sCdMaoPropria, decimal nVlValorDeclarado,
# string sCdAvisoRecebimento)

ret = webservice_calc.service.CalcPrecoPrazo(
    sgpkey['cod_admin'], sgpkey['senha'], sgpkey['numero_servico'],
    sgpkey['cep_origem'], sgpkey['cep_destino'], '1', 1, 100, 20, 20, 20,
    'S', 10, 'S')

print ret

print 'Consulta finalizada'