# Menyelesaikan Permasalahan Institusi Pendidikan (Jaya Jaya Institut)

## Business Understanding

**Jaya Jaya Institut** merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun demikian, institusi ini menghadapi permasalahan **tingginya jumlah mahasiswa yang melakukan dropout** (tidak menyelesaikan pendidikannya).

Tingginya angka dropout ini menjadi masalah besar bagi institusi pendidikan, karena itu Jaya Jaya Institut ingin dapat **mendeteksi secepat mungkin mahasiswa yang berpotensi melakukan dropout**, sehingga mahasiswa tersebut dapat diberikan bimbingan khusus sebelum benar-benar keluar dari perkuliahan.

### Permasalahan Bisnis

1. Seberapa besar tingkat dropout mahasiswa di Jaya Jaya Institut, dan faktor apa saja yang paling memengaruhinya?
2. Bagaimana karakteristik umum mahasiswa yang cenderung mengalami dropout dibandingkan mahasiswa yang berhasil lulus (graduate)?
3. Bagaimana cara membangun sebuah model machine learning yang dapat memprediksi apakah seorang mahasiswa akan Dropout atau Graduate, berdasarkan data pribadi, finansial, dan akademiknya?
4. Rekomendasi tindakan (*action items*) apa yang bisa diambil oleh pihak manajemen untuk menekan angka dropout?

### Cakupan Proyek

1. Data Understanding & Exploratory Data Analysis (EDA), memahami karakteristik data mahasiswa dan pola-pola yang berkaitan dengan status mahasiswa.
2. Data Preparation, melakukan filtering data sehingga hanya mahasiswa berstatus Dropout dan Graduate yang digunakan untuk pemodelan (mahasiswa Enrolled dipisahkan karena belum memiliki label akhir), membuat target biner (1 = Dropout, 0 = Graduate), train-test split, dan feature scaling.
3. Modeling & Evaluation, melatih dan mengevaluasi model klasifikasi (Random Forest) untuk memprediksi status mahasiswa (Dropout vs Graduate), lalu menggunakan model tersebut untuk memprediksi risiko dropout pada mahasiswa yang masih berstatus Enrolled.
4. Business Dashboard, membuat dashboard visual (Looker Studio) untuk memonitor performa dan risiko dropout mahasiswa.
5. Deployment (Prototype), membangun prototype aplikasi berbasis Streamlit agar model dapat langsung digunakan oleh pihak Jaya Jaya Institut, dan menghubungkannya dengan Streamlit Community Cloud.

### Persiapan

**Sumber data:** [Students' Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

**Python version:** `3.11.9`

**Setup environment:**

```bash
# 1. (opsional) buat virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. install seluruh library yang dibutuhkan
pip install -r requirements.txt

# 3. jalankan notebook untuk melihat keseluruhan analisis
jupyter notebook notebook.ipynb
```

---

## Business Dashboard

Dashboard dibuat untuk membantu Jaya Jaya Institut memonitor performa mahasiswa secara keseluruhan, meliputi:
- Jumlah & proporsi mahasiswa berdasarkan status (Dropout / Enrolled / Graduate)
- Pengaruh kondisi finansial (pembayaran UKT) dan beasiswa terhadap status mahasiswa
- Sebaran nilai (grade) semester 1 & 2 per status
- Distribusi status berdasarkan kelompok usia mahasiswa

Dashboard ini dibuat menggunakan **Looker Studio**:

🔗 **Link Dashboard:** [https://datastudio.google.com/reporting/19eed07e-e3ac-4eb1-a5d5-da7bf7f4885a](https://datastudio.google.com/reporting/19eed07e-e3ac-4eb1-a5d5-da7bf7f4885a)

---

## Menjalankan Sistem Machine Learning (Prototype)

Prototype sistem machine learning dibangun menggunakan Streamlit (app.py), memanfaatkan model rf_model.pkl dan scaler.pkl yang telah dilatih pada notebook.ipynb. Model ini dilatih khusus menggunakan data mahasiswa yang berstatus Dropout & Graduate (mahasiswa Enrolled tidak dilibatkan dalam training karena belum memiliki label akhir), sehingga sistem ini cocok digunakan untuk memprediksi mahasiswa yang masih aktif kuliah. Sistem menerima input data seorang mahasiswa (data diri, finansial, dan performa akademik), lalu mengeluarkan prediksi: Dropout atau Graduate, beserta estimasi peluang dropout-nya.

### Cara menjalankan secara lokal

```bash
# 1. pastikan requirements.txt sudah terinstall
pip install -r requirements.txt

# 2. pastikan file model/rf_model.pkl dan model/scaler.pkl
#    berada satu folder dengan app.py (file ini dihasilkan dari notebook.ipynb)

# 3. jalankan aplikasi
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada alamat `http://localhost:8501`.

🔗 **Link Prototype:** [https://dashboard-prediksi-dropout-mahasiswa.streamlit.app/](https://dashboard-prediksi-dropout-mahasiswa.streamlit.app/)

---

## Conclusion

Berdasarkan proses data understanding, EDA, hingga modeling yang telah dilakukan, dapat disimpulkan:

1. Dari total 4.424 mahasisw, sekitar 32% (1.421 mahasiswa) berstatus Dropout, ~50% (2.209 mahasiswa) Graduate, dan ~18% (794 mahasiswa) masih Enrolled — angka dropout ini cukup signifikan dan menegaskan urgensi masalah bagi Jaya Jaya Institut.

2. Karakteristik umum mahasiswa yang cenderung Dropout (dibandingkan mahasiswa yang Graduate) adalah sebagai berikut:

   | Karakteristik | Dropout | Graduate |
   |---|---|---|
   | Usia saat mendaftar (rata-rata) | 26.1 tahun | 21.8 tahun |
   | Rata-rata nilai semester 1 | 7.26 | 12.64 |
   | Rata-rata nilai semester 2 | 5.90 | 12.70 |
   | Rata-rata jumlah mata kuliah lulus semester 1 | 2.55 | 6.23 |
   | Rata-rata jumlah mata kuliah lulus semester 2 | 1.94 | 6.18 |
   | Proporsi berstatus debitur (punya tunggakan) | 22.0% | 4.6% |
   | Proporsi pembayaran UKT lancar | 67.8% | 98.7% |
   | Proporsi penerima beasiswa | 9.4% | 38.0% |
   | Proporsi laki-laki | 49.3% | 24.8% |

   Singkatnya, mahasiswa yang cenderung dropout umumnya mendaftar di usia yang lebih tua, memiliki performa akademik yang jauh lebih rendah sejak semester 1 (nilai maupun jumlah mata kuliah yang lulus), berada pada kondisi finansial yang lebih rentan (lebih banyak yang berstatus debitur/menunggak UKT), jarang menerima beasiswa, dan proporsi lebih tinggi dibanding mahasiswa yang graduate.

3. Performa akademik di semester 1 dan 2 (jumlah mata kuliah yang lulus/approved dan rata-rata nilai) merupakan faktor paling berpengaruh terhadap risiko dropout, diikuti oleh status pembayaran UKT.

4. Sesuai dengan tujuan sistem yang ingin dibangun, proses pemodelan difokuskan hanya pada mahasiswa berstatus Dropout dan Graduate — mahasiswa berstatus Enrolled dikeluarkan dari proses training karena belum memiliki label/hasil akhir (Dropout atau Graduate), dan sebagai gantinya dipisahkan untuk digunakan sebagai data prediksi di masa mendatang. Target biner yang digunakan: 1 = Dropout, 0 = Graduate.

5. Dengan pendekatan yang telah diperbaiki ini, model **Random Forest Classifier** (n_estimators=200, max_depth=10, min_samples_split=10) berhasil mencapai akurasi 92%, dengan precision 0.91 dan recall 0.87 untuk kelas Dropout — meningkat signifikan dibandingkan pendekatan sebelumnya yang menyertakan ketiga kelas sekaligus (akurasi 76%).

6. Model kemudian digunakan untuk memprediksi risiko dropout pada 794 mahasiswa yang masih berstatus Enrolled, dan hasilnya menunjukkan sekitar 356 mahasiswa (44,8%) berisiko dropout — kelompok inilah yang perlu menjadi prioritas intervensi oleh pihak akademik.

7. Model ini telah disimpan (rf_model.pkl beserta scaler.pkl) dan diimplementasikan dalam bentuk prototype aplikasi Streamlit, sehingga pihak Jaya Jaya Institut dapat langsung memanfaatkannya sebagai *early warning system*.

### Rekomendasi Action Items

1. Bangun sistem monitoring akademik dini. Gunakan prototype/model ini untuk melakukan scoring risiko dropout pada mahasiswa yang masih Enrolled setiap akhir semester (terutama setelah semester 1), lalu tandai mahasiswa dengan peluang dropout tinggi (misalnya > 50%) untuk ditindaklanjuti oleh bagian akademik. Sebagai referensi awal, dari 794 mahasiswa Enrolled saat ini, sekitar 356 di antaranya sudah terdeteksi berisiko tinggi.
2. Berikan program bimbingan akademik (academic advisory) khusus bagi mahasiswa dengan jumlah mata kuliah lulus rendah atau nilai jauh di bawah rata-rata pada semester 1 (di bawah nilai 8-9), karena performa akademik awal adalah karakteristik & prediktor terkuat risiko dropout.
3. Perkuat dukungan finansial, misalnya program cicilan UKT atau bantuan dana darurat, khususnya bagi mahasiswa yang berstatus debitur atau menunggak pembayaran, mengingat proporsi debitur pada kelompok dropout 5x lebih tinggi dibanding kelompok graduate.
4. Perluas dan sosialisasikan program beasiswa, karena data menunjukkan mahasiswa penerima beasiswa jauh lebih jarang mengalami dropout — beasiswa dapat menjadi salah satu bentuk intervensi preventif yang efektif.
5. Berikan perhatian khusus pada mahasiswa yang mendaftar di usia lebih tua (di atas 25 tahun), karena kelompok ini secara historis menunjukkan tingkat dropout yang lebih tinggi, kemungkinan karena tantangan membagi waktu antara kuliah dengan pekerjaan/tanggung jawab lain.
6. Lakukan monitoring berkala melalui dashboard yang telah dibuat di Looker Studio, agar pihak manajemen dapat memantau tren dropout dari waktu ke waktu dan mengevaluasi efektivitas program-program intervensi yang telah dijalankan.
7. Evaluasi & retrain model secara berkala (misalnya setiap tahun ajaran baru) menggunakan data terbaru — termasuk data mahasiswa Enrolled yang sudah memiliki hasil akhir — agar model tetap relevan mengikuti perubahan karakteristik mahasiswa maupun kebijakan institusi.

---