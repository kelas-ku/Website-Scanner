# Website-Scanner

WEBSITE SCANNER TOOLS
Alat ini saya buat menggunakan full bahasa pemrograman python, yang dimana alat ini hanya
bertujuan unutk melakukan pemindaian jaringan web dasar tanpa melanggar aturan sedikit pun.

# Fungsi Alat Ini:

• DNS Lookup : mencari alamt IP dari sebuah domain

• Reverse DNS : mencari nama domain dari sebuah IP

• Port Scanner : mengecek port umum seperti : (21, 22, 80, 443) apakah port-port tesebut
terbuka atau tertutup

• Ping Test : mengecek apakah host/domain aktif dengan menggunakan ping

# Tujuan Alat Ini:

• Memberikan informasi dasar jaringan dari sebuah domain

• membantu pengguna melakukan diagnosis sederhana: apakah server aktif, port terbuka, dan
apakah domain valid

• Menjadi latihan praktis untuk memahami module Python yang berhubungan dengan
jaringan dan sistem operasi

• Bisa dikembangkan menjadi tools keamananm network utility tingkat lanjut
Materi Python yang Terlibat:
Dalam script ini, ada beberapa materi Python yang digunakan:

• Import modul import socket, import os → mengimpor modul bawaan Python.

• Modul socket

• socket.gethostbyname_ex() : DNS Lookup.

• socket.gethostbyaddr() : Reverse DNS.

• socket.connect_ex() : cek port terbuka.

• Modul os

• os.system("ping ...") : menjalankan perintah ping sesuai sistem operasi.

• os.name → mendeteksi apakah Windows (nt) atau Linux/Mac (posix).

• Input & Output

• input() : menerima data dari user.

• print() : menampilkan hasil ke layar.

• Percabangan if-elif-else Menentukan menu yang dipilih user dan menjalankan fungsi sesuai
pilihan.

• Looping for Digunakan untuk mengecek port satu per satu dalam daftar.

• Exception Handling

• try-except : menangani error jika domain/IP tidak valid.

• String formatting

• f"{variable}" : menampilkan teks dengan variabel di dalamnya.

• Digunakan juga untuk menambahkan warna terminal dengan kode ANSI.
