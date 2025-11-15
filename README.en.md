# 🌐 AV2 Project — Computer Networks

Python Web Server + HTTP Analysis with Wireshark

[![Status](https://img.shields.io/badge/Status-In%20Development-orange)](#)
[![Course](https://img.shields.io/badge/Course-Computer%20Networks-blue)](#)
[![Stack](https://img.shields.io/badge/Stack-Python-lightyellow)](#)
[![Tool](https://img.shields.io/badge/Tool-Wireshark-cyan)](#)
[![Idioma: PT-BR](https://img.shields.io/badge/Linguagem-Português-green)](README.md)
[![Language: EN](https://img.shields.io/badge/Language-English-red)](README.en.md)

This repository contains the full implementation and documentation for the **AV2 (Assessment 2) of the Computer Networks course**, which includes:

✔ Building a **TCP Web Server in Python**  
✔ Implementing all logic using the **professor’s original starter skeleton**  
✔ Running browser tests and handling **404 Not Found**  
✔ Performing HTTP traffic analysis with **Wireshark**  
✔ Providing structured answers for the practical activity questions

---

## 🎯 Project Objective

The main goal of this assessment is to develop practical skills involving:

* ⭐ Programming with **TCP sockets**
* ⭐ Understanding how **HTTP requests** work
* ⭐ Manually constructing a **simple Web Server**
* ⭐ Inspecting and analyzing real HTTP traffic using **Wireshark**
* ⭐ Identifying headers, status codes, methods, IP addresses, and other HTTP events

This activity simulates, in a simplified manner, the behavior of a real web server and helps build a strong understanding of the **client → server → client** flow in the HTTP protocol.

---

## 🛠️ Technologies Used

* 🐍 **Python 3** — TCP server implementation
* 📡 **Sockets (AF_INET, SOCK_STREAM)**
* 🌍 **HTTP/1.1** (status codes 200 and 404)
* 🔍 **Wireshark** — packet capture and inspection
* 📄 **Basic HTML** file served by the server

---

## 📁 Project Folder Structure

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

## 🌍 Question 1 — Python Web Server

The server must:

✔ Create a TCP socket  
✔ Accept one request at a time  
✔ Read the HTTP request sent by the browser  
✔ Determine the requested file  
✔ Open and return its contents with header **HTTP/1.1 200 OK**  
✔ Handle nonexistent files with **HTTP/1.1 404 Not Found**  
✔ Follow *strictly* the professor’s starter skeleton  

### 📝 Note on the professor’s skeleton

This implementation follows **exactly** the structure provided in the activity.
Only the sections marked with **#Fill in start** and **#Fill in end** were completed, preserving the original didactic layout and logic.

### 📌 Files included

* **server.py** — full implementation
* **HelloWorld.html** — HTML file served by the web server
* **prints/** — screenshots used in the report

### ▶️ How to run the server

#### 1. Navigate to the directory

```bash
cd Projeto-AV2-Redes/questao1_server
```

#### 2. Start the server

```bash
python3 server.py
```

#### 3. Open in your browser:

```
http://127.0.0.1:6789/HelloWorld.html
```

#### 4. Test a nonexistent file:

```
http://127.0.0.1:6789/naoexiste.html
```

If implemented correctly, the server will return **404 Not Found**.

---

## 🔎 Question 2 — HTTP Lab with Wireshark

This part consists of a complete HTTP packet analysis using the URLs from the official course lab:

* `HTTP-wireshark-file1.html`
* `HTTP-wireshark-file2.html`

### 📌 Objectives analyzed:

* Identify HTTP versions
* Inspect accepted languages
* Determine source and destination IP addresses
* Analyze returned HTTP status codes
* Inspect `Last-Modified` headers
* Inspect caching behavior with `If-Modified-Since`
* Identify when the server returns **304 Not Modified**

All answers and screenshots are included in:

📄 **respostas_a_j.pdf**

---

## 🚀 Steps to Reproduce the Capture in Wireshark

1. Open Wireshark
2. Select the correct network interface
3. Apply the filter:

   ```
   http
   ```
4. Start the capture
5. In the browser, open:

   ```
   http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html
   ```
6. Stop the capture and analyze
7. Repeat for `HTTP-wireshark-file2.html`

---

## 📘 References

* KUROSE, James; ROSS, Keith. *Computer Networking: A Top-Down Approach*
* Python Documentation — **socket** module
* Wireshark — [https://www.wireshark.org/](https://www.wireshark.org/)
* Course material provided by the professor

---

## 👥 Contributors

* [Rafael Magno G.](https://github.com/rafaelmagnog)
* [Renato Alexandre](https://github.com/RenatoAlexandre06)

---
