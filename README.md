# Menyelesaikan Permasalahan Institusi Pendidikan (Jaya Jaya Institut)

## Business Understanding

**Jaya Jaya Institut** merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun demikian, institusi ini menghadapi permasalahan **tingginya jumlah mahasiswa yang melakukan dropout** (tidak menyelesaikan pendidikannya).

Tingginya angka dropout ini menjadi masalah besar bagi institusi pendidikan, karena itu Jaya Jaya Institut ingin dapat **mendeteksi secepat mungkin mahasiswa yang berpotensi melakukan dropout**, sehingga mahasiswa tersebut dapat diberikan bimbingan khusus sebelum benar-benar keluar dari perkuliahan.

### Permasalahan Bisnis

1. Seberapa besar tingkat dropout mahasiswa di Jaya Jaya Institut, dan faktor apa saja yang paling memengaruhinya?
2. Bagaimana cara membangun sebuah model machine learning yang dapat **memprediksi status akhir mahasiswa** (Dropout / Enrolled / Graduate) berdasarkan data pribadi, finansial, dan akademiknya?
3. Rekomendasi tindakan (*action items*) apa yang bisa diambil oleh pihak manajemen untuk menekan angka dropout?

### Cakupan Proyek

1. Data Understanding & Exploratory Data Analysis (EDA), memahami karakteristik data mahasiswa dan pola-pola yang berkaitan dengan status mahasiswa.
2. Data Preparation, melakukan label encoding pada target, train-test split, dan feature scaling agar data siap digunakan oleh model machine learning.
3. Modeling & Evaluation, melatih dan mengevaluasi model klasifikasi (Random Forest) untuk memprediksi status mahasiswa (Dropout / Enrolled / Graduate).
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

Prototype sistem machine learning dibangun menggunakan **Streamlit** (app.py), memanfaatkan model rf_model.pkl dan scaler.pkl yang telah dilatih pada notebook.ipynb. Sistem ini menerima input data seorang mahasiswa (data diri, finansial, dan performa akademik), lalu mengeluarkan prediksi status mahasiswa tersebut: **Dropout**, **Enrolled**, atau **Graduate**.

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

Berdasarkan proses *data understanding*, EDA, hingga *modeling* yang telah dilakukan, dapat disimpulkan:

1. Dari total **4.424 mahasiswa**, sekitar **32% (1.421 mahasiswa) berstatus Dropout**, ~50% (2.209 mahasiswa) **Graduate**, dan ~18% (794 mahasiswa) masih **Enrolled** — angka dropout ini cukup signifikan dan menegaskan urgensi masalah bagi Jaya Jaya Institut.
2. **Performa akademik di semester 1 dan 2** (khususnya jumlah mata kuliah yang berhasil disetujui/lulus dan rata-rata nilai) merupakan **faktor paling berpengaruh** terhadap status akhir mahasiswa, diikuti oleh **status pembayaran UKT**.
3. Model **Random Forest Classifier** (n_estimators=200, max_depth=10, min_samples_split=10) berhasil memprediksi status mahasiswa (Dropout/Enrolled/Graduate) dengan **akurasi 76%**. Model ini cukup kuat dalam mendeteksi mahasiswa **Dropout** (precision 0.84, recall 0.74) dan **Graduate** (recall 0.95), meskipun masih kurang optimal dalam mengenali kelas **Enrolled** (recall 0.28) karena sifatnya yang transisional dan jumlah datanya paling sedikit.
4. Model ini telah disimpan (rf_model.pkl beserta scaler.pkl) dan diimplementasikan dalam bentuk **prototype aplikasi Streamlit**, sehingga pihak Jaya Jaya Institut dapat langsung memanfaatkannya sebagai *early warning system*.

Dengan sistem ini, Jaya Jaya Institut diharapkan dapat mendeteksi mahasiswa berisiko dropout **lebih awal** (bahkan sejak akhir semester 1), sehingga bimbingan khusus dapat diberikan sebelum mahasiswa benar-benar keluar dari perkuliahan.

### Rekomendasi Action Items

1. **Bangun sistem monitoring akademik dini.** Gunakan prototype/model ini untuk melakukan scoring status mahasiswa setiap akhir semester (terutama setelah semester 1), lalu tandai mahasiswa dengan prediksi **Dropout** untuk ditindaklanjuti oleh bagian akademik.
2. **Berikan program bimbingan akademik (academic advisory) khusus** bagi mahasiswa dengan jumlah mata kuliah lulus rendah atau nilai di bawah rata-rata pada semester 1, karena performa akademik awal adalah prediktor terkuat status dropout.
3. **Perkuat dukungan finansial**, misalnya program cicilan UKT atau bantuan dana darurat, bagi mahasiswa yang menunggak pembayaran, mengingat status pembayaran UKT merupakan salah satu faktor penting yang memengaruhi risiko dropout.
4. **Perluas dan sosialisasikan program beasiswa** sebagai salah satu bentuk intervensi preventif bagi mahasiswa yang berisiko dropout.
5. **Berikan perhatian khusus pada mahasiswa berstatus Enrolled** yang menunjukkan pola akademik menyerupai mahasiswa Dropout (nilai rendah, sedikit mata kuliah lulus), karena model menunjukkan kelas ini paling sulit dibedakan dan berpotensi menjadi dropout berikutnya jika tidak ditangani.
6. **Lakukan monitoring berkala melalui dashboard** yang telah dibuat di Looker Studio, agar pihak manajemen dapat memantau tren dropout dari waktu ke waktu dan mengevaluasi efektivitas program-program intervensi yang telah dijalankan.
7. **Evaluasi & retrain model secara berkala** (misalnya setiap tahun ajaran baru) menggunakan data terbaru, agar model tetap relevan mengikuti perubahan karakteristik mahasiswa maupun kebijakan institusi.

---