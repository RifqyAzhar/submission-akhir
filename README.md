# Menyelesaikan Permasalahan Institusi Pendidikan (Jaya Jaya Institut)

## Business Understanding

**Jaya Jaya Institut** merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun demikian, institusi ini menghadapi permasalahan **tingginya jumlah mahasiswa yang melakukan dropout** (tidak menyelesaikan pendidikannya).

Tingginya angka dropout ini menjadi masalah besar bagi institusi pendidikan, karena itu Jaya Jaya Institut ingin dapat **mendeteksi secepat mungkin mahasiswa yang berpotensi melakukan dropout**, sehingga mahasiswa tersebut dapat diberikan bimbingan khusus sebelum benar-benar keluar dari perkuliahan.

### Permasalahan Bisnis

1. Seberapa besar tingkat dropout mahasiswa di Jaya Jaya Institut, dan faktor apa saja yang paling memengaruhinya?
2. Bagaimana cara membangun sebuah sistem yang dapat **memprediksi risiko dropout mahasiswa** berdasarkan data pribadi, finansial, dan akademiknya?
3. Rekomendasi tindakan (*action items*) apa yang bisa diambil oleh pihak manajemen untuk menekan angka dropout?

### Cakupan Proyek

1. **Data Understanding & Exploratory Data Analysis (EDA)** — memahami karakteristik data mahasiswa dan pola-pola yang berkaitan dengan dropout.
2. **Data Preparation** — menyiapkan data (feature/target split, train-test split, scaling) agar siap digunakan oleh model machine learning.
3. **Modeling & Evaluation** — melatih dan mengevaluasi model klasifikasi untuk memprediksi risiko dropout.
4. **Business Dashboard** — membuat dashboard visual untuk memonitor performa mahasiswa.
5. **Deployment (Prototype)** — membangun prototype aplikasi berbasis Streamlit agar model dapat langsung digunakan oleh pihak Jaya Jaya Institut, dan menghubungkannya dengan Streamlit Community Cloud.

### Persiapan

**Sumber data:** [Students' Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

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
- Pengaruh kondisi finansial (pembayaran UKT, status debitur, beasiswa) terhadap status mahasiswa
- Sebaran nilai & jumlah mata kuliah yang lulus di semester 1 & 2 per status
- Sebaran usia mahasiswa saat mendaftar

Dashboard ini dibangun menggunakan **Streamlit + Plotly** (`dashboard.py`) sehingga bisa langsung dijalankan secara lokal:

```bash
streamlit run dashboard.py
```

> **Link akses dashboard:** `(isi dengan link Streamlit Community Cloud / Looker Studio / Tableau Public Anda di sini setelah proses deploy)`

**Alternatif menggunakan Looker Studio / Tableau Public:**
Jika Anda ingin menggunakan Looker Studio atau Tableau Public (misalnya karena reviewer lebih familiar dengan tools tersebut), Anda dapat:
1. Mengunggah `data.csv` ke Google Sheets, lalu menghubungkannya sebagai data source di [Looker Studio](https://lookerstudio.google.com/).
2. Membuat chart berikut agar dashboard dianggap valid (tidak hanya tabel):
   - Pie/Bar chart distribusi `Status`
   - Bar chart `Status` vs `Tuition_fees_up_to_date`
   - Bar chart `Status` vs `Scholarship_holder`
   - Box/Bar chart rata-rata `Curricular_units_2nd_sem_grade` per `Status`
   - Histogram `Age_at_enrollment`
3. Set opsi *Share* menjadi "Anyone with the link can view" agar dapat diakses reviewer.

---

## Menjalankan Sistem Machine Learning (Prototype)

Prototype sistem machine learning dibangun menggunakan **Streamlit** (`app.py`). Sistem ini menerima input data seorang mahasiswa (data diri, finansial, dan performa akademik), lalu mengeluarkan prediksi apakah mahasiswa tersebut **berisiko Dropout** atau **Tidak**, beserta estimasi peluangnya.

### Cara menjalankan secara lokal

```bash
# 1. pastikan requirements.txt sudah terinstall
pip install -r requirements.txt

# 2. pastikan file model.pkl, scaler.pkl, dan feature_columns.pkl
#    berada satu folder dengan app.py (file ini dihasilkan dari notebook.ipynb)

# 3. jalankan aplikasi
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada alamat `http://localhost:8501`.

### Cara deploy ke Streamlit Community Cloud

1. Push seluruh folder proyek ini (termasuk `app.py`, `model.pkl`, `scaler.pkl`, `feature_columns.pkl`, `requirements.txt`) ke sebuah repository GitHub.
2. Buka [share.streamlit.io](https://share.streamlit.io/), login dengan akun GitHub Anda.
3. Klik **New app**, pilih repository & branch yang berisi proyek ini, lalu set **Main file path** menjadi `app.py`.
4. Klik **Deploy**. Streamlit Cloud akan otomatis meng-install `requirements.txt` dan menjalankan aplikasi.

> **Link akses prototype:** `(isi dengan link Streamlit Community Cloud Anda di sini setelah proses deploy, misalnya https://nama-app-anda.streamlit.app)`

---

## Conclusion

Berdasarkan proses *data understanding*, EDA, hingga *modeling* yang telah dilakukan, dapat disimpulkan:

1. Dari total **4.424 mahasiswa**, sekitar **32% (1.421 mahasiswa) berstatus Dropout** — sebuah angka yang cukup signifikan dan menegaskan urgensi masalah ini bagi Jaya Jaya Institut.
2. **Performa akademik di semester 1 dan 2** (khususnya jumlah mata kuliah yang berhasil disetujui/lulus dan rata-rata nilai) merupakan faktor **paling berpengaruh** terhadap kemungkinan dropout — semakin sedikit mata kuliah yang lulus, semakin besar risiko dropout.
3. **Kondisi finansial** juga berperan penting: mahasiswa yang **menunggak pembayaran UKT** atau **berstatus debitur** memiliki proporsi dropout yang jauh lebih tinggi, sementara mahasiswa **penerima beasiswa** cenderung memiliki risiko dropout yang lebih rendah.
4. Model **Logistic Regression** yang dilatih berhasil memprediksi risiko dropout dengan **akurasi ±87%** dan **ROC-AUC ±0.93**, serta dipilih sebagai model final karena memiliki *recall* yang baik pada kelas Dropout dan mudah diinterpretasikan oleh pihak non-teknis.
5. Model ini telah diimplementasikan dalam bentuk **prototype aplikasi Streamlit** (`app.py`) sehingga pihak Jaya Jaya Institut dapat langsung memanfaatkannya sebagai *early warning system*.

Dengan sistem ini, Jaya Jaya Institut diharapkan dapat mendeteksi mahasiswa berisiko dropout **lebih awal** (bahkan sejak akhir semester 1), sehingga bimbingan khusus dapat diberikan sebelum mahasiswa benar-benar keluar dari perkuliahan.

### Rekomendasi Action Items

1. **Bangun sistem monitoring akademik dini.** Gunakan prototype/model ini untuk melakukan scoring risiko dropout setiap akhir semester (terutama setelah semester 1), lalu tandai mahasiswa dengan peluang dropout tinggi (misalnya > 50%) untuk ditindaklanjuti oleh bagian akademik.
2. **Berikan program bimbingan akademik (akademik advisory) khusus** bagi mahasiswa yang jumlah mata kuliah lulusnya rendah atau nilainya di bawah rata-rata pada semester 1, karena performa akademik awal adalah prediktor terkuat dropout.
3. **Perkuat dukungan finansial**, misalnya program cicilan UKT atau bantuan dana darurat, bagi mahasiswa yang berstatus debitur atau menunggak pembayaran, mengingat kelompok ini memiliki risiko dropout yang jauh lebih tinggi.
4. **Perluas dan sosialisasikan program beasiswa**, karena data menunjukkan mahasiswa penerima beasiswa memiliki risiko dropout yang lebih rendah — beasiswa dapat menjadi salah satu bentuk intervensi preventif.
5. **Lakukan monitoring berkala melalui dashboard** yang telah dibuat, agar pihak manajemen dapat memantau tren dropout dari waktu ke waktu dan mengevaluasi efektivitas program-program intervensi yang telah dijalankan.
6. **Evaluasi & retrain model secara berkala** (misalnya setiap tahun ajaran baru) menggunakan data terbaru, agar model tetap relevan mengikuti perubahan karakteristik mahasiswa maupun kebijakan institusi.

---

## Struktur Berkas Proyek

```
├── notebook.ipynb          # Notebook lengkap: business understanding s.d. evaluation (sudah dijalankan)
├── data.csv                # Dataset mahasiswa Jaya Jaya Institut
├── app.py                  # Prototype sistem ML (Streamlit) untuk prediksi risiko dropout
├── dashboard.py            # Business dashboard (Streamlit + Plotly)
├── model.pkl               # Model Logistic Regression yang sudah dilatih
├── scaler.pkl              # StandardScaler yang sudah di-fit pada data training
├── feature_columns.pkl     # Daftar & urutan kolom fitur yang dipakai model
├── requirements.txt        # Daftar library yang dibutuhkan
└── README.md                # Dokumentasi proyek (berkas ini)
```
