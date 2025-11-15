# 🌐 Projeto AV2 — Redes de Computadores

Servidor Web em Python + Análise HTTP com Wireshark

[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)](#)
[![Disciplina](https://img.shields.io/badge/Disciplina-Redes%20de%20Computadores-blue)](#)
[![Stack](https://img.shields.io/badge/Stack-Python-lightyellow)](#)
[![Ferramenta](https://img.shields.io/badge/Ferramenta-Wireshark-cyan)](#)
[![Idioma: PT-BR](https://img.shields.io/badge/Idioma-PT--BR-green)](README.md)
[![Language: EN](https://img.shields.io/badge/Language-English-red)](README.en.md)

Este repositório contém a implementação e documentação completas da **AV2 de Redes de Computadores**, que envolve:

✔ Construção de um **Servidor Web TCP em Python**  
✔ Implementação baseada no **esqueleto inicial do professor**  
✔ Testes com navegador e tratamento de erro **404 Not Found**  
✔ Análise de tráfego HTTP utilizando **Wireshark**  
✔ Respostas estruturadas para as questões propostas na atividade

---

## 🎯 Objetivo do Projeto

O objetivo principal desta avaliação é desenvolver habilidades práticas de:

* ⭐ Programação com **sockets TCP**
* ⭐ Entendimento do funcionamento de **requisições HTTP**
* ⭐ Construção manual de um **servidor Web simples**
* ⭐ Interpretação e análise de tráfego real usando **Wireshark**
* ⭐ Identificação de cabeçalhos, códigos de status, IPs, métodos e eventos HTTP

A atividade simula, de forma simplificada, o funcionamento de um servidor real, permitindo compreender de maneira sólida o fluxo **cliente → servidor → cliente** no protocolo HTTP.

---

## 🛠️ Tecnologias Utilizadas

* 🐍 **Python 3** — implementação do servidor TCP
* 📡 **Sockets (AF_INET, SOCK_STREAM)**
* 🌍 **HTTP/1.1** (status 200 e 404)
* 🔍 **Wireshark** — captura e análise de pacotes
* 📄 **HTML básico** para página servida

---

## 📁 Estrutura de Pastas do Projeto

```bash
📂 Projeto-AV2-Redes
├── 📁 questao1_server
│   ├── server.py
│   ├── HelloWorld.html
│   └── 📁 prints
│       ├── servidor_iniciado.png
│       ├── teste_200.png
│       └── teste_404.png
│
├── 📁 questao2_wireshark
│   ├── respostas_a_j.pdf
│   ├── captura_file1.pcap
│   ├── captura_file2.pcap
│   └── 📁 prints
│       ├── req_1_get.png
│       ├── resp_1_200.png
│       ├── req_2_get.png
│       └── resp_2_304.png
│
└── README.md
```

---

## 🌍 Questão 1 — Servidor Web em Python

O servidor deve:

✔ Criar socket TCP  
✔ Aceitar uma única requisição por vez  
✔ Ler a requisição HTTP enviada pelo navegador  
✔ Determinar o arquivo solicitado  
✔ Abrir e retornar o conteúdo com cabeçalho **HTTP/1.1 200 OK**  
✔ Tratar arquivos inexistentes com **HTTP/1.1 404 Not Found**  
✔ Seguir *estritamente* o esqueleto fornecido pelo professor  

### 📝 Nota sobre o esqueleto do professor

A implementação segue **exatamente** a estrutura disponibilizada na atividade,
preenchendo somente os trechos delimitados por **#Fill in start** e **#Fill in end**,
mantendo a lógica e formato originais conforme o propósito didático do exercício.

### 📌 Arquivos envolvidos

* **server.py** — implementação completa
* **HelloWorld.html** — arquivo HTML servido pelo servidor
* **prints/** — evidências para o relatório

### ▶️ Como executar o servidor

#### 1. Acesse o diretório

```bash
cd Projeto-AV2-Redes/questao1_server
```

#### 2. Execute o servidor

```bash
python3 server.py
```

#### 3. Acesse no navegador:

```
http://127.0.0.1:6789/HelloWorld.html
```

#### 4. Teste um arquivo inexistente:

```
http://127.0.0.1:6789/naoexiste.html
```

Se o servidor estiver correto, retornará **404 Not Found**.

---

## 🔎 Questão 2 — Laboratório HTTP com Wireshark

Nesta etapa, foi realizada uma análise completa do tráfego HTTP a partir das URLs do laboratório oficial:

* `HTTP-wireshark-file1.html`
* `HTTP-wireshark-file2.html`

### 📌 Objetivos analisados:

* Identificar versões do HTTP
* Verificar linguagens aceitas pelo navegador
* Determinar IP de origem e destino
* Analisar códigos de status retornados
* Observar cabeçalho `Last-Modified`
* Verificar comportamento do cache com `If-Modified-Since`
* Identificar quando ocorre `304 Not Modified`

Todos os resultados e evidências estão no arquivo:

📄 **respostas_a_j.pdf**

---

## 🚀 Passos para Reproduzir a Captura no Wireshark

1. Abra o Wireshark
2. Selecione a interface correta
3. Aplique o filtro:

   ```
   http
   ```
4. Inicie a captura
5. No navegador, acesse:

   ```
   http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html
   ```
6. Pare a captura e analise
7. Repita com `HTTP-wireshark-file2.html`

---

## 📘 Referências

* KUROSE, James; ROSS, Keith. *Redes de Computadores e a Internet*
* Documentação Python — Módulo **socket**
* Wireshark — [https://www.wireshark.org/](https://www.wireshark.org/)
* Material fornecido pelo professor

---

## 👥 Contribuidores

* [Rafael Magno G.](https://github.com/rafaelmagnog)
* [Renato Alexandre](https://github.com/RenatoAlexandre06)

---

