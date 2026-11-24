class PasienPoliDalam:

    # Class Attribute
    rumah_sakit = "RS Kurnia Serang"
    poli = "Poli Penyakit Dalam"

    # Constructor
    def __init__(self, nama, umur, keluhan):
        self.nama = nama
        self.umur = umur
        self.keluhan = keluhan

    # Method perkenalan
    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}.")
        print(f"Umur saya {self.umur} tahun.")
        print(f"Keluhan saya adalah {self.keluhan}.")

    # Method percakapan
    def berbicara(self, lawan_bicara, kalimat):
        print(f"{self.nama}: {kalimat}")


# Membuat Object
budi = PasienPoliDalam(
    "Budi", 35, "Nyeri ulu hati dan perut terasa perih sejak kemarin"
)

sari = PasienPoliDalam(
    "Sari", 28, "Sering merasa lemas, pusing, dan agak mual"
)


# Memulai Percakapan
print("====================================")
print(" PERCAKAPAN PASIEN DI POLI DALAM")
print("====================================")
print("Rumah Sakit:", PasienPoliDalam.rumah_sakit)
print("Ruangan:", PasienPoliDalam.poli)
print()

print("--- PERKENALAN ---")
budi.perkenalan()
print()
sari.perkenalan()

print()
print("--- PERCAKAPAN ---")

budi.berbicara("Sari",
    "Permisi, apakah kursi di sebelah sini kosong? Saya juga antre di Poli Dalam.")

sari.berbicara("Budi",
    "Silakan, kosong kok. Kebetulan saya juga sedang menunggu giliran periksa.")

budi.berbicara("Sari",
    "Sudah lama menunggunya? Antrean hari ini lumayan ramai ya.")

sari.berbicara("Budi",
    "Baru sekitar lima belas menit. Kalau boleh tahu, keluhan yang dirasakan apa?")

budi.berbicara("Sari",
    "Ulu hati saya nyeri dan perih, sepertinya asam lambung naik. "
    "Kalau kamu sendiri bagaimana?")

sari.berbicara("Budi",
    "Saya akhir-akhir ini sering merasa lemas, pusing, dan agak mual.")

budi.berbicara("Sari",
    "Wah, memang harus segera dicek dokter supaya dapat penanganan yang tepat.")

sari.berbicara("Budi",
    "Betul, tadi di depan saya juga sudah cek tekanan darah sebelum menunggu di sini.")

budi.berbicara("Sari",
    "Sama, tadi perawat sudah mengukur tensi dan berat badan saya juga.")

sari.berbicara("Budi",
    "Semoga nanti proses pemeriksaannya berjalan lancar ya.")

print()
print("--- PROSES PEMERIKSAAN ---")

budi.berbicara("Sari",
    "Oh, nomor antrean saya sudah dipanggil perawat. "
    "Saya masuk ke ruang dokter dulu ya.")

sari.berbicara("Budi",
    "Iya, silakan. Semoga tidak ada masalah yang serius.")

budi.berbicara("Sari",
    "Terima kasih. Dokter menyarankan saya menjaga pola makan "
    "dan memberikan resep obat lambung.")

sari.berbicara("Budi",
    "Syukurlah kalau sudah jelas penyebabnya. Sekarang giliran nama saya yang dipanggil.")

budi.berbicara("Sari",
    "Silakan masuk, semoga hasil pemeriksaannya baik.")

sari.berbicara("Budi",
    "Terima kasih. Dokter sudah memeriksa kondisi saya dan "
    "menganjurkan untuk cek darah di laboratorium.")

print()
print("--- PENUTUP ---")

budi.berbicara("Sari",
    "Semoga hasil cek lab-nya bagus ya dan kondisi kamu cepat pulih.")

sari.berbicara("Budi",
    "Aamiin, terima kasih banyak. Kamu juga jangan sampai telat makan lagi ya.")

budi.berbicara("Sari",
    "Siap, pasti saya jaga. Saya mau ke bagian farmasi dulu untuk menebus obat.")

sari.berbicara("Budi",
    "Baik, senang bisa mengobrol sambil menunggu tadi. Hati-hati di jalan!")

budi.berbicara("Sari",
    "Senang juga berkenalan denganmu. Lekas sembuh dan sampai jumpa!")

print()
print("====================================")
print("PERCAKAPAN SELESAI")
print("Kedua pasien selesai menjalani proses pemeriksaan.")
print("====================================")
print("Proses perkenalan selesai.")



OUTPUT;
PERCAKAPAN PASIEN DI POLI DALAM

====================================
 PERCAKAPAN PASIEN DI POLI DALAM
====================================
Rumah Sakit: RS Kurnia Serang
Ruangan: Poli Penyakit Dalam

--- PERKENALAN ---
Halo, nama saya Budi.
Umur saya 35 tahun.
Keluhan saya adalah Nyeri ulu hati dan perut terasa perih sejak kemarin.

Halo, nama saya Sari.
Umur saya 28 tahun.
Keluhan saya adalah Sering merasa lemas, pusing, dan agak mual.

--- PERCAKAPAN ---
Budi: Permisi, apakah kursi di sebelah sini kosong? Saya juga antre di Poli Dalam.
Sari: Silakan, kosong kok. Kebetulan saya juga sedang menunggu giliran periksa.
Budi: Sudah lama menunggunya? Antrean hari ini lumayan ramai ya.
Sari: Baru sekitar lima belas menit. Kalau boleh tahu, keluhan yang dirasakan apa?
Budi: Ulu hati saya nyeri dan perih, sepertinya asam lambung naik. Kalau kamu sendiri bagaimana?
Sari: Saya akhir-akhir ini sering merasa lemas, pusing, dan agak mual.
Budi: Wah, memang harus segera dicek dokter supaya dapat penanganan yang tepat.
Sari: Betul, tadi di depan saya juga sudah cek tekanan darah sebelum menunggu di sini.
Budi: Sama, tadi perawat sudah mengukur tensi dan berat badan saya juga.
Sari: Semoga nanti proses pemeriksaannya berjalan lancar ya.

--- PROSES PEMERIKSAAN ---
Budi: Oh, nomor antrean saya sudah dipanggil perawat. Saya masuk ke ruang dokter dulu ya.
Sari: Iya, silakan. Semoga tidak ada masalah yang serius.
Budi: Terima kasih. Dokter menyarankan saya menjaga pola makan dan memberikan resep obat lambung.
Sari: Syukurlah kalau sudah jelas penyebabnya. Sekarang giliran nama saya yang dipanggil.
Budi: Silakan masuk, semoga hasil pemeriksaannya baik.
Sari: Terima kasih. Dokter sudah memeriksa kondisi saya dan menganjurkan untuk cek darah di laboratorium.

--- PENUTUP ---
Budi: Semoga hasil cek lab-nya bagus ya dan kondisi kamu cepat pulih.
Sari: Aamiin, terima kasih banyak. Kamu juga jangan sampai telat makan lagi ya.
Budi: Siap, pasti saya jaga. Saya mau ke bagian farmasi dulu untuk menebus obat.
Sari: Baik, senang bisa mengobrol sambil menunggu tadi. Hati-hati di jalan!
Budi: Senang juga berkenalan denganmu. Lekas sembuh dan sampai jumpa!

====================================
PERCAKAPAN SELESAI
Kedua pasien selesai menjalani proses pemeriksaan.
====================================
Proses perkenalan selesai.