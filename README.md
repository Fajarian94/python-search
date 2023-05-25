# python-search
Sequential search adalah metode pencarian elemen pada indeks dengan cara berurutan yang melibatkan setiap elemen yang ada di dalam list hingga elemen yang dicari sampai ketemu atau sampai akhir list
Binary search adalah metode pencarian yang hanya berlaku untuk list yang  diurutkan dalam urutan menaik. Metode ini membagi daftar menjadi dua bagian dan memeriksa apakah elemen yang akan dicari ada di sisi kiri atau  kanan list. jika elemen yang dicari lebih besar dari nilai tengah maka hanya setengah kanan yang diperiksa,sebaliknya jika elemen yang dicari adalah lebih kecil dari nilai tengah maka hanya setengah kiri yang diperiksa.

# Percobaan 10
Pada Percobaan 10 untuk mencari indeks rotasi terkecil dalam suatu array yang telah diputar. Di dalam loop, dihitung nilai tengah (mid) dengan membagi jumlah low dan high lalu dibagi 2 kemudian melakukan pengecekan apakah nilai mid lebih besar dari high, jika iya indeks rotasi terkecil ada di kanan, maka low diupdate menjadi mid+1,jika sudah ketemu hasilnya akan disimpan di variabel rotation_index. kemudian dipanggil menggunakan print

# Percobaan 11
temukan elemen yang paling sering  dalam  array yang diurutkan. Fungsi ini menggunakan algoritma pencarian biner untuk menemukan elemen yang paling umum. Dalam setiap iterasi, fungsi menghitung jumlah kemunculan elemen tengah saat ini dan memperbarui variabel max_count dan most_frequent jika  lebih besar dari yang sebelumnya. Fungsi juga mencari elemen yang memiliki tampilan yang sama di sisi kiri dan kanan elemen tengah. Proses pencarian berlanjut, membatasi area pencarian ke kiri atau ke kanan, tergantung pada  jumlah kemunculan dan hasil 1 perbandingan. Pencarian berhenti ketika tidak ada elemen lain yang cocok dengan elemen tengah. Ketika fungsi berakhir, ia mengembalikan elemen array yang paling sering. Dalam contoh ini, elemen array yang paling sering  [2, 2, 2, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8] adalah 8. Nilai ini kemudian dicetak menggunakan membuat pernyataan cetak.

# Percobaan 12
pencarian biner untuk menemukan nilai target dalam  daftar data yang diurutkan. Inisialisasi variabel rendah dengan  0 sebagai indeks awal daftar dan tinggi dengan  len(data) - 1 sebagai indeks akhir. Sedangkan nilai rendah kurang dari atau sama dengan tertinggi, lakukan langkah berikut: Hitung indeks rata-rata tengah  menggunakan rumus (tinggi rendah) // 2. Jika nilai  indeks rata-rata sama dengan nilai target, kembalikan  indeks di tengah tempat target ditemukan. Jika nilai di tengah indeks kurang dari nilai target, perbarui nilai rendah ke tengah dengan 1 untuk mendapatkan yang teratas dari daftar lainnya. Jika nilai di tengah indeks  lebih besar dari nilai target, perbarui pertengahan ke 1 untuk mendapatkan bagian bawah  daftar. Jika nilai target tidak ditemukan dalam daftar, kembalikan -1 untuk menunjukkan bahwa itu tidak ditemukan. . Dalam contoh yang ditampilkan, program meminta pengguna memasukkan nama untuk mencari dari daftar ['Alice', 'Bob', 'Charlie', 'Emma', 'Frank', 'George']. Fungsi binary_search kemudian dipanggil dengan daftar dan nama objek sebagai argumen. Jika indeks yang dikembalikan bukan -1, itu berarti nama itu ditemukan dan program mencetak indeks tempat nama itu ditemukan. Jika indeks yang dikembalikan adalah -1, program akan mencetak pesan  bahwa nama  tidak dapat ditemukan.
