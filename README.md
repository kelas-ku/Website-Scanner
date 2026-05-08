# Website-Scanner

## 📖 Deskripsi
**Website Scanner Tools**  
Alat ini dibuat menggunakan bahasa pemrograman **Python**.  
Tujuannya adalah melakukan **pemindaian jaringan web dasar** tanpa melanggar aturan apa pun.

---

## ⚙️ Fungsi Alat
- **DNS Lookup** → mencari alamat IP dari sebuah domain.  
- **Reverse DNS** → mencari nama domain dari sebuah IP.  
- **Port Scanner** → mengecek port umum (21, 22, 80, 443) apakah terbuka atau tertutup.  
- **Ping Test** → mengecek apakah host/domain aktif dengan menggunakan ping.  

---

## 🎯 Tujuan Alat
- Memberikan informasi dasar jaringan dari sebuah domain.  
- Membantu pengguna melakukan diagnosis sederhana: apakah server aktif, port terbuka, dan apakah domain valid.  
- Menjadi latihan praktis untuk memahami modul Python yang berhubungan dengan jaringan dan sistem operasi.  
- Bisa dikembangkan menjadi **tools keamanan** atau **network utility** tingkat lanjut.  

---

## 📚 Materi Python yang Terlibat
Dalam script ini, ada beberapa materi Python yang digunakan:

- **Import Modul**
  - `import socket`, `import os` → mengimpor modul bawaan Python.  

- **Modul socket**
  - `socket.gethostbyname_ex()` → DNS Lookup.  
  - `socket.gethostbyaddr()` → Reverse DNS.  
  - `socket.connect_ex()` → cek port terbuka.  

- **Modul os**
  - `os.system("ping ...")` → menjalankan perintah ping sesuai sistem operasi.  
  - `os.name` → mendeteksi apakah Windows (`nt`) atau Linux/Mac (`posix`).  

- **Input & Output**
  - `input()` → menerima data dari user.  
  - `print()` → menampilkan hasil ke layar.  

- **Percabangan**
  - `if-elif-else` → menentukan menu yang dipilih user dan menjalankan fungsi sesuai pilihan.  

- **Looping**
  - `for` → digunakan untuk mengecek port satu per satu dalam daftar.  

- **Exception Handling**
  - `try-except` → menangani error jika domain/IP tidak valid.  

- **String Formatting**
  - `f"{variable}"` → menampilkan teks dengan variabel di dalamnya.  
  - Digunakan juga untuk menambahkan warna terminal dengan kode ANSI.  

---

# Perintah di Linux/MacOS:
```
# Clone repository dari GitHub
git clone https://github.com/kelas-ku/Website-Scanner.git

# Masuk ke folder project
cd Website-Scanner

# Jalankan script dengan Python 3
python3 scanner.py
```
## ✨ Catatan
Alat ini masih sederhana, namun bisa dikembangkan lebih lanjut dengan fitur tambahan seperti:
- **Whois Lookup**  
- **Traceroute**  
- **GeoIP Lookup**  
- **SSL Certificate Info**
