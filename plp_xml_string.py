# -*- coding: utf-8 -*-
import lxml
from lxml import etree
from xml.etree.ElementTree import XML, fromstring, tostring

def get_xml(cliente, endereco):
    xml = '<?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?>'
    xml += '<correioslog>'
    xml += '<tipo_arquivo>Postagem</tipo_arquivo>'
    xml += '<versao_arquivo>2.3</versao_arquivo>'
    xml += '<plp>' \
           '<id_plp/>' \
           '<valor_global/>'
    xml += '<mcu_unidade_postagem/><nome_unidade_postagem/>'
    xml += '<cartao_postagem>%s</cartao_postagem>' % \
           cliente.contratos[0].cartoesPostagem[0].numero

    xml += u'EMPRESA BRASILEIRA DE CORREIOS E TELÉGRAFOS – ECT SIGEP Web - ' \
           u'Manual de Implementação do Web Service 20/74</plp>'

    xml += '<remetente>'
    xml += '<numero_contrato>%s</numero_contrato>' % \
           cliente.contratos[0].contratoPK.numero

    xml += '<numero_diretoria>%s</numero_diretoria>' % \
           cliente.contratos[0].codigoDiretoria

    xml += '<codigo_administrativo>%s</codigo_administrativo>' % \
           cliente.contratos[0].cartoesPostagem[0].codigoAdministrativo

    xml += '<nome_remetente><![CDATA[%s]]></nome_remetente>' % cliente.nome
    xml += '<logradouro_remetente><![CDATA[%s]]> ' \
           '</logradouro_remetente>' % endereco.end

    xml += '<numero_remetente>2370</numero_remetente>'
    xml += '<complemento_remetente><![CDATA[%s]]></complemento_remetente>' % \
           endereco.complemento

    xml += '<bairro_remetente><![CDATA[%s]]></bairro_remetente>' % \
           endereco.bairro
    xml += '<cep_remetente><![CDATA[%s]]></cep_remetente>' % endereco.cep
    xml += '<cidade_remetente><![CDATA[%s]]></cidade_remetente>' % \
           endereco.cidade
    xml += '<uf_remetente>%s</uf_remetente>' % endereco.uf
    xml += '<telefone_remetente><![CDATA[6112345008]]></telefone_remetente>'
    xml += '<fax_remetente><![CDATA[]]></fax_remetente>'
    xml += '<email_remetente> <![CDATA[cli@mail.com.br]]> </email_remetente>'
    xml += '</remetente>' \
           '<forma_pagamento/>' \
           '<objeto_postal>'
    xml += '<numero_etiqueta>PH185560916BR</numero_etiqueta>'
    xml += '<codigo_objeto_cliente/>'
    xml += '<codigo_servico_postagem>41068</codigo_servico_postagem>'
    xml += '<cubagem>0,0000</cubagem>'
    xml += '<peso>200</peso>'
    xml += '<rt1/>' \
           '<rt2/>'
    xml += '<destinatario>'
    xml += '<nome_destinatario><![CDATA[Destino Ltda]]></nome_destinatario>'
    xml += '<telefone_destinatario><![CDATA[6212349644]]>' \
           '</telefone_destinatario>'

    xml += '<celular_destinatario><![CDATA[]]></celular_destinatario>'
    xml += '<email_destinatario><![CDATA[]]></email_destinatario>'
    xml += '<logradouro_destinatario><![CDATA[Avenida Central]]>' \
           '</logradouro_destinatario>'

    xml += '<complemento_destinatario><![CDATA[Qd: 102 A Lt: 04]]>' \
           '</complemento_destinatario>'

    xml += '<numero_end_destinatario>1065</numero_end_destinatario>'
    xml += '</destinatario>'

    xml += '<nacional>'
    xml += '<bairro_destinatario><![CDATA[Setor Industrial]]>' \
           '</bairro_destinatario>'
    xml += u'<cidade_destinatario><![CDATA[Goiânia]]></cidade_destinatario>'
    xml += '<uf_destinatario>GO</uf_destinatario>'
    xml += '<cep_destinatario> <![CDATA[74000100]]></cep_destinatario>'
    xml += '<codigo_usuario_postal/>'
    xml += '<centro_custo_cliente/>'
    xml += '<numero_nota_fiscal>102030</numero_nota_fiscal>'
    xml += '<serie_nota_fiscal/>' \
           '<valor_nota_fiscal/>' \
           '<natureza_nota_fiscal/>'
    xml += '<descricao_objeto><![CDATA[]]></descricao_objeto>'
    xml += '<valor_a_cobrar>0,0</valor_a_cobrar>'
    xml += '</nacional>'

    # O servico adicional 025 sempre deverá ser informado.
    xml += '<servico_adicional>'
    xml += '<codigo_servico_adicional>025</codigo_servico_adicional>'
    xml += '<codigo_servico_adicional>001</codigo_servico_adicional>'
    xml += '<codigo_servico_adicional>019</codigo_servico_adicional>'
    xml += '<valor_declarado>99,00</valor_declarado>'
    xml += '</servico_adicional>'
    xml += '<dimensao_objeto>'
    xml += '<tipo_objeto>002</tipo_objeto>'
    xml += '<dimensao_altura>20</dimensao_altura>'
    xml += '<dimensao_largura>30</dimensao_largura>'
    xml += '<dimensao_comprimento>38</dimensao_comprimento>'
    xml += '<dimensao_diametro>0</dimensao_diametro>'
    xml += '</dimensao_objeto>'
    xml += '<data_postagem_sara/>'
    xml += '<status_processamento>0</status_processamento>'
    xml += '<numero_comprovante_postagem/>'
    xml += '<valor_cobrado/>'
    xml += '</objeto_postal>' \
           '</correioslog>'

    return xml

xsd = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
elementFormDefault="qualified">
<xs:element name="versao_arquivo">
<xs:simpleType>
    <xs:restriction base="xs:decimal">
        <xs:enumeration value="2.3"/>
    </xs:restriction>
</xs:simpleType>
    </xs:element>
    <xs:element name="valor_nota_fiscal" type="xs:string"/>
    <xs:element name="valor_global" type="xs:string"/>
    <xs:element name="valor_declarado">
        <xs:simpleType>
            <xs:restriction base="xs:string"/>
        </xs:simpleType>
    </xs:element>
    <xs:element name="valor_cobrado" type="xs:string"/>
    <xs:element name="valor_a_cobrar">
        <xs:simpleType>
            <xs:restriction base="xs:string"/>
        </xs:simpleType>
    </xs:element>
    <xs:element name="uf_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="2"/>
                <xs:enumeration value="AC"/>
                <xs:enumeration value="AL"/>
                <xs:enumeration value="AP"/>
                <xs:enumeration value="AM"/>
                <xs:enumeration value="BA"/>
                <xs:enumeration value="CE"/>
                <xs:enumeration value="DF"/>
                <xs:enumeration value="ES"/>
                <xs:enumeration value="GO"/>
                <xs:enumeration value="MA"/>
                <xs:enumeration value="MT"/>
                <xs:enumeration value="MS"/>
                <xs:enumeration value="MG"/>
                <xs:enumeration value="PA"/>
                <xs:enumeration value="PB"/>
                <xs:enumeration value="PR"/>
                <xs:enumeration value="PE"/>
                <xs:enumeration value="PI"/>
                <xs:enumeration value="RJ"/>
                <xs:enumeration value="RN"/>
                <xs:enumeration value="RS"/>
                <xs:enumeration value="RO"/>
                <xs:enumeration value="RR"/>
                <xs:enumeration value="SC"/>
                <xs:enumeration value="SP"/>
                <xs:enumeration value="SE"/>
                <xs:enumeration value="TO"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="uf_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="2"/>
                <xs:enumeration value="AC"/>
                <xs:enumeration value="AL"/>
                <xs:enumeration value="AP"/>
                <xs:enumeration value="AM"/>
                <xs:enumeration value="BA"/>
                <xs:enumeration value="CE"/>
                <xs:enumeration value="DF"/>
                <xs:enumeration value="ES"/>
                <xs:enumeration value="GO"/>
                <xs:enumeration value="MA"/>
                <xs:enumeration value="MT"/>
                <xs:enumeration value="MS"/>
                <xs:enumeration value="MG"/>
                <xs:enumeration value="PA"/>
                <xs:enumeration value="PB"/>
                <xs:enumeration value="PR"/>
                <xs:enumeration value="PE"/>
                <xs:enumeration value="PI"/>
                <xs:enumeration value="RJ"/>
                <xs:enumeration value="RN"/>
                <xs:enumeration value="RS"/>
                <xs:enumeration value="RO"/>
                <xs:enumeration value="RR"/>
                <xs:enumeration value="SC"/>
                <xs:enumeration value="SP"/>
                <xs:enumeration value="SE"/>
                <xs:enumeration value="TO"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="tipo_arquivo">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="Postagem"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="telefone_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="telefone_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="24"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="status_processamento">
        <xs:simpleType>
            <xs:restriction base="xs:byte">
                <xs:enumeration value="0"/>
                <xs:enumeration value="1"/>
                <xs:enumeration value="2"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="servico_adicional">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="codigo_servico_adicional" maxOccurs="4"/>
                <xs:element ref="valor_declarado"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="serie_nota_fiscal">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="rt2">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="255"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="rt1">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="255"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="remetente">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="numero_contrato"/>
                <xs:element ref="numero_diretoria"/>
                <xs:element ref="codigo_administrativo"/>
                <xs:element ref="nome_remetente"/>
                <xs:element ref="logradouro_remetente"/>
                <xs:element ref="numero_remetente"/>
                <xs:element ref="complemento_remetente"/>
                <xs:element ref="bairro_remetente"/>
                <xs:element ref="cep_remetente"/>
                <xs:element ref="cidade_remetente"/>
                <xs:element ref="uf_remetente"/>
                <xs:element ref="telefone_remetente"/>
                <xs:element ref="fax_remetente"/>
                <xs:element ref="email_remetente"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="plp">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="id_plp"/>
                <xs:element ref="valor_global"/>
                <xs:element ref="mcu_unidade_postagem"/>
                <xs:element ref="nome_unidade_postagem"/>
                <xs:element ref="cartao_postagem"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="peso">
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:maxInclusive value="30000"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="objeto_postal">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="numero_etiqueta"/>
                <xs:element ref="codigo_objeto_cliente"/>
                <xs:element ref="codigo_servico_postagem"/>
                <xs:element ref="cubagem"/>
                <xs:element ref="peso"/>
                <xs:element ref="rt1"/>
                <xs:element ref="rt2"/>
                <xs:element ref="destinatario"/>
                <xs:element ref="nacional"/>
                <xs:element ref="servico_adicional"/>
                <xs:element ref="dimensao_objeto"/>
                <xs:element ref="data_postagem_sara"/>
                <xs:element ref="status_processamento"/>
                <xs:element ref="numero_comprovante_postagem"/>
                <xs:element ref="valor_cobrado"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="numero_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="18"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="numero_nota_fiscal">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="8"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="numero_etiqueta">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:minLength value="13"/>
                <xs:maxLength value="13"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="numero_end_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="18"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="numero_diretoria">
        <xs:simpleType>
            <xs:restriction base="xs:byte">
                <xs:enumeration value="75"/>
                <xs:enumeration value="72"/>
                <xs:enumeration value="74"/>
                <xs:enumeration value="70"/>
                <xs:enumeration value="68"/>
                <xs:enumeration value="64"/>
                <xs:enumeration value="65"/>
                <xs:enumeration value="26"/>
                <xs:enumeration value="60"/>
                <xs:enumeration value="50"/>
                <xs:enumeration value="36"/>
                <xs:enumeration value="34"/>
                <xs:enumeration value="32"/>
                <xs:enumeration value="30"/>
                <xs:enumeration value="28"/>
                <xs:enumeration value="24"/>
                <xs:enumeration value="22"/>
                <xs:enumeration value="20"/>
                <xs:enumeration value="18"/>
                <xs:enumeration value="16"/>
                <xs:enumeration value="14"/>
                <xs:enumeration value="12"/>
                <xs:enumeration value="10"/>
                <xs:enumeration value="08"/>
                <xs:enumeration value="05"/>
                <xs:enumeration value="06"/>
                <xs:enumeration value="04"/>
                <xs:enumeration value="03"/>
                <xs:enumeration value="01"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="numero_contrato">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="numero_comprovante_postagem" type="xs:string"/>
    <xs:element name="nome_unidade_postagem">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="30"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="nome_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="50"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="nome_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="50"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="natureza_nota_fiscal">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="nacional">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="bairro_destinatario"/>
                <xs:element ref="cidade_destinatario"/>
                <xs:element ref="uf_destinatario"/>
                <xs:element ref="cep_destinatario"/>
                <xs:element ref="codigo_usuario_postal"/>
                <xs:element ref="centro_custo_cliente"/>
                <xs:element ref="numero_nota_fiscal"/>
                <xs:element ref="serie_nota_fiscal"/>
                <xs:element ref="valor_nota_fiscal"/>
                <xs:element ref="natureza_nota_fiscal"/>
                <xs:element ref="descricao_objeto"/>
                <xs:element ref="valor_a_cobrar"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="mcu_unidade_postagem">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="8"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="logradouro_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="50"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="logradouro_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="50"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="id_plp">
        <xs:simpleType>
            <xs:restriction base="xs:string"/>
        </xs:simpleType>
    </xs:element>
    <xs:element name="forma_pagamento">
        <xs:simpleType>
            <xs:restriction base="xs:string">
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="fax_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="12"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="email_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="50"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="email_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="50"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="dimensao_objeto">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="tipo_objeto">
                    <xs:simpleType>
                        <xs:restriction base="xs:short">
                            <xs:enumeration value="001"/>
                            <xs:enumeration value="002"/>
                            <xs:enumeration value="003"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element ref="dimensao_altura"/>
                <xs:element ref="dimensao_largura"/>
                <xs:element ref="dimensao_comprimento"/>
                <xs:element ref="dimensao_diametro"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="dimensao_altura">
        <xs:simpleType>
            <xs:restriction base="xs:int">
                <xs:minInclusive value="2"/>
                <xs:maxInclusive value="105"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="dimensao_largura">
        <xs:simpleType>
            <xs:restriction base="xs:int">
                <xs:minInclusive value="11"/>
                <xs:maxInclusive value="105"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="dimensao_comprimento">
        <xs:simpleType>
            <xs:restriction base="xs:int">
                <xs:minInclusive value="16"/>
                <xs:maxInclusive value="105"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="dimensao_diametro">
        <xs:simpleType>
            <xs:restriction base="xs:int">
                <xs:minInclusive value="0"/>
                <xs:maxInclusive value="105"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="destinatario">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="nome_destinatario"/>
                <xs:element ref="telefone_destinatario"/>
                <xs:element ref="celular_destinatario"/>
                <xs:element ref="email_destinatario"/>
                <xs:element ref="logradouro_destinatario"/>
                <xs:element ref="complemento_destinatario"/>
                <xs:element ref="numero_end_destinatario"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="descricao_objeto">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="data_postagem_sara">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="8"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="cubagem">
        <xs:simpleType>
            <xs:restriction base="xs:string"/>
        </xs:simpleType>
    </xs:element>
    <xs:element name="correioslog">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="tipo_arquivo"/>
                <xs:element ref="versao_arquivo"/>
                <xs:element ref="plp" maxOccurs="1"/>
                <xs:element ref="remetente"/>
                <xs:element ref="forma_pagamento"/>
                <xs:element ref="objeto_postal" maxOccurs="1000"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="complemento_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="30"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="complemento_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="30"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="codigo_usuario_postal">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="codigo_servico_postagem">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="5"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="codigo_servico_adicional" type="xs:short"/>
    <xs:element name="codigo_objeto_cliente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="codigo_administrativo">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="9"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="cidade_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="30"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="cidade_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="30"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="cep_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="cep_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="centro_custo_cliente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="20"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="celular_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="12"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="cartao_postagem">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="10"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="bairro_remetente">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="30"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="bairro_destinatario">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:maxLength value="30"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
</xs:schema>"""

XSI = "http://www.w3.org/2001/XMLSchema-instance"
XS = '{http://www.w3.org/2001/XMLSchema}'


def validate_XML(xml):
    """Validate an XML file represented as string. Follow all schemaLocations.

    :param xml: XML represented as string.
    :type xml: str
    """
    tree = etree.XML(fromstring(xml))
    schema_tree = etree.XML(xsd)
    # Find all unique instances of 'xsi:schemaLocation="<namespace> <path-to-schema.xsd> ..."'
    schema_locations = set(tree.xpath("//*/@xsi:schemaLocation", namespaces={'xsi': XSI}))
    for schema_location in schema_locations:
        # Split namespaces and schema locations ; use strip to remove leading
        # and trailing whitespace.
        namespaces_locations = schema_location.strip().split()
        # Import all found namspace/schema location pairs
        for namespace, location in zip(*[iter(namespaces_locations)] * 2):
            xs_import = etree.Element(XS + "import")
            xs_import.attrib['namespace'] = namespace
            xs_import.attrib['schemaLocation'] = location
            schema_tree.append(xs_import)
    # Contstruct the schema
    schema = etree.XMLSchema(schema_tree)
    # Validate!
    res = schema.assertValid(tree)

    return res


