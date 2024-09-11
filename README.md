Nama : Olav Dendy Christian Manullang
NPM : 2306230590
Kelas : PBP A

SOAL

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
Mengetahui bahwa: 
main = direktori aplikasi
rumai_kedai = direktori project

1. Membuat sebuah proyek Django baru bernama snowpy yang sebelumnya berada di direktori utama snowpy dan terhubung ke direktori github
2. Membuat direktori aplikasi bernama main
3. Mendaftarkan aplikasi main ke dalam proyek snowpy
4. Membuat model di dalam models.py dalam aplikasi main dengan nama class Product, fungsi model adalah untuk menyimpan script database
5. Membuat direktori templates di dalam direktori main. Di dalam direktori templates akan terdapat template (main.html) yang berguna untuk menampilkan data program snowpy
6. Membuat sebuah fungsi di dalam views.py yang terdapat di dalam direktori aplikasi main untuk dikembalikan ke dalam sebuah template html
7. Routing URL aplikasi main dengan cara membuat urls.py di dalam direktori aplikasi main untuk mengatur rute URL yang terkait dengan aplikasi main. urls.py pada aplikasi main digunakan untuk memetakan fungsi yang telah dibuat pada views.py
8. Routing URL proyek snowpy menambahkan rute URL dalam urls.py proyek untuk menghubungkannya ke tampilan main
9. Deployment ke PWS

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
1. Membuat request dari internet -> webserver environment -> run django -> extract argument from request -> diteruskan ke views.py <-> views akan mencari data terkait di models.py -> mengembalikan data ke dalam template html untuk ditampilkan ke pada user atas respon dari request.

Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git digunakan untuk beberapa hal, seperti:
1. Pengelolaan Repositori: Git digunakan untuk menyimpan dan mengelola repositori, baik di komputer lokal maupun di layanan server seperti GitHub.
2. Pelacakan Perubahan Kode: Setiap perubahan pada kode sumber direkam dalam riwayat revisi, memungkinkan pengembang untuk melacak semua modifikasi. Setiap kali perubahan disimpan (disebut commit), Git mencatat versi terbaru proyek beserta informasi tentang siapa yang membuat perubahan, kapan dilakukan, dan penjelasan perubahan tersebut.
3. Kolaborasi Tim: Git memfasilitasi kerja sama antar pengembang pada proyek yang sama. Setiap pengembang dapat bekerja secara independen pada salinan lokal proyek, melakukan perubahan, dan kemudian menggabungkan hasilnya ke repositori utama.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
1. Mudah Dipelajari: Django relatif mudah dipahami, terutama bagi pemula.
2. Struktur yang Jelas: Django menawarkan arsitektur yang terstruktur dengan baik, memudahkan pengembang untuk mengikuti alur kerja yang sistematis.
3. Pendekatan MVT: Django menggunakan pendekatan Model-View-Template (MVT) yang populer dalam pengembangan perangkat lunak. Memahami MVT membantu pemula mengerti pentingnya pemisahan tanggung jawab dalam aplikasi, yang sangat penting dalam proyek skala besar.
4. Digunakan Secara Luas: Django telah diadopsi oleh banyak perusahaan besar dan digunakan dalam proyek berskala industri, seperti Instagram, Pinterest, dan Mozilla, yang menunjukkan popularitasnya di dunia industri.

Mengapa model pada Django disebut sebagai ORM?
Model dalam Django dikenal sebagai ORM (Object-Relational Mapping) karena berperan sebagai lapisan yang menghubungkan objek dalam kode Python dengan tabel dalam basis data relasional. Dengan ORM, pengembang dapat mengelola data menggunakan konsep objek di Python tanpa perlu menulis SQL secara manual untuk berinteraksi dengan basis data.