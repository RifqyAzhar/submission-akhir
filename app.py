import os
import streamlit as st
import pandas as pd
import joblib

# 1. Load model dan scaler 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

@st.cache_resource
def load_artifacts():
    model = joblib.load(os.path.join(MODEL_DIR, "rf_model.pkl"))
    scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
    return model, scaler

try:
    model, scaler = load_artifacts()
except FileNotFoundError as e:
    st.error(f"Gagal memuat model. Pastikan file `rf_model.pkl` dan `scaler.pkl` ada di dalam folder `model/`.\n\nDetail error: {e}")
    st.stop()

# 2. Pengaturan halaman
st.set_page_config(page_title="Prediksi Dropout Mahasiswa", page_icon="🎓", layout="wide")

st.title("🎓 Prediksi Risiko Dropout Mahasiswa")
st.markdown(
    """
    Aplikasi ini membantu **Jaya Jaya Institut** memprediksi apakah seorang
    mahasiswa berpotensi **Dropout** atau **Tidak Dropout**, berdasarkan data
    pribadi, finansial, dan performa akademiknya.

    Silakan isi data mahasiswa pada form di bawah ini, lalu klik tombol
    **Prediksi**.
    """
)

st.divider()

# 3. Form input data mahasiswa
with st.form("prediction_form"):

    st.subheader("1. Data Diri Mahasiswa")
    col1, col2, col3 = st.columns(3)
    with col1:
        marital_status = st.selectbox(
            "Status Pernikahan (kode 1-6, 1 = Single)", options=list(range(1, 7)), index=0
        )
        gender = st.selectbox("Jenis Kelamin", options=[("Perempuan", 0), ("Laki-laki", 1)],
                               format_func=lambda x: x[0])[1]
        age = st.number_input("Usia saat Mendaftar", min_value=17, max_value=70, value=20)
    with col2:
        displaced = st.selectbox("Mahasiswa Perantauan (Displaced)?", [("Tidak", 0), ("Ya", 1)],
                                  format_func=lambda x: x[0])[1]
        international = st.selectbox("Mahasiswa Internasional?", [("Tidak", 0), ("Ya", 1)],
                                      format_func=lambda x: x[0])[1]
        special_needs = st.selectbox("Kebutuhan Khusus (Educational Special Needs)?",
                                      [("Tidak", 0), ("Ya", 1)], format_func=lambda x: x[0])[1]
    with col3:
        nationality = st.number_input("Kode Kewarganegaraan (Nacionality)", min_value=1, value=1)
        application_mode = st.number_input("Kode Jalur Pendaftaran (Application Mode)", min_value=1, value=17)
        application_order = st.number_input("Urutan Pilihan Pendaftaran (Application Order)", min_value=0, value=1)

    st.subheader("2. Data Pendaftaran & Latar Belakang Keluarga")
    col1, col2, col3 = st.columns(3)
    with col1:
        course = st.number_input("Kode Program Studi (Course)", min_value=1, value=9238)
        attendance = st.selectbox("Waktu Kuliah", [("Pagi/Siang (Daytime)", 1), ("Malam (Evening)", 0)],
                                   format_func=lambda x: x[0])[1]
        previous_qualification = st.number_input("Kode Kualifikasi Sebelumnya", min_value=1, value=1)
    with col2:
        previous_qualification_grade = st.number_input("Nilai Kualifikasi Sebelumnya (0-200)",
                                                         min_value=0.0, max_value=200.0, value=133.0)
        admission_grade = st.number_input("Nilai Penerimaan / Admission Grade (0-200)",
                                           min_value=0.0, max_value=200.0, value=127.0)
    with col3:
        mothers_qualification = st.number_input("Kode Kualifikasi Ibu", min_value=1, value=19)
        fathers_qualification = st.number_input("Kode Kualifikasi Ayah", min_value=1, value=19)
        mothers_occupation = st.number_input("Kode Pekerjaan Ibu", min_value=0, value=5)
        fathers_occupation = st.number_input("Kode Pekerjaan Ayah", min_value=0, value=7)

    st.subheader("3. Kondisi Finansial")
    col1, col2, col3 = st.columns(3)
    with col1:
        debtor = st.selectbox("Status Debitur (punya tunggakan)?", [("Tidak", 0), ("Ya", 1)],
                               format_func=lambda x: x[0])[1]
    with col2:
        tuition_fees = st.selectbox("Pembayaran UKT Lancar (Tuition fees up to date)?",
                                     [("Ya, Lancar", 1), ("Tidak/Menunggak", 0)], format_func=lambda x: x[0])[1]
    with col3:
        scholarship = st.selectbox("Penerima Beasiswa?", [("Tidak", 0), ("Ya", 1)],
                                    format_func=lambda x: x[0])[1]

    st.subheader("4. Performa Akademik Semester 1")
    col1, col2, col3 = st.columns(3)
    with col1:
        cu1_credited = st.number_input("Mata Kuliah Diakui (Credited) - Sem 1", min_value=0, value=0)
        cu1_enrolled = st.number_input("Mata Kuliah Diambil (Enrolled) - Sem 1", min_value=0, value=6)
    with col2:
        cu1_evaluations = st.number_input("Jumlah Evaluasi/Ujian - Sem 1", min_value=0, value=8)
        cu1_approved = st.number_input("Mata Kuliah Lulus (Approved) - Sem 1", min_value=0, value=5)
    with col3:
        cu1_grade = st.number_input("Rata-rata Nilai - Sem 1 (0-20)", min_value=0.0, max_value=20.0, value=12.0)
        cu1_without_eval = st.number_input("Mata Kuliah Tanpa Evaluasi - Sem 1", min_value=0, value=0)

    st.subheader("5. Performa Akademik Semester 2")
    col1, col2, col3 = st.columns(3)
    with col1:
        cu2_credited = st.number_input("Mata Kuliah Diakui (Credited) - Sem 2", min_value=0, value=0)
        cu2_enrolled = st.number_input("Mata Kuliah Diambil (Enrolled) - Sem 2", min_value=0, value=6)
    with col2:
        cu2_evaluations = st.number_input("Jumlah Evaluasi/Ujian - Sem 2", min_value=0, value=8)
        cu2_approved = st.number_input("Mata Kuliah Lulus (Approved) - Sem 2", min_value=0, value=5)
    with col3:
        cu2_grade = st.number_input("Rata-rata Nilai - Sem 2 (0-20)", min_value=0.0, max_value=20.0, value=12.0)
        cu2_without_eval = st.number_input("Mata Kuliah Tanpa Evaluasi - Sem 2", min_value=0, value=0)

    st.subheader("6. Kondisi Makroekonomi saat Mendaftar")
    col1, col2, col3 = st.columns(3)
    with col1:
        unemployment_rate = st.number_input("Tingkat Pengangguran (%)", value=11.1)
    with col2:
        inflation_rate = st.number_input("Tingkat Inflasi (%)", value=1.4)
    with col3:
        gdp = st.number_input("GDP", value=0.3)

    submitted = st.form_submit_button("🔍 Prediksi", use_container_width=True)

# 4. Proses prediksi ketika tombol ditekan
if submitted:
    input_dict = {
        "Marital_status": marital_status,
        "Application_mode": application_mode,
        "Application_order": application_order,
        "Course": course,
        "Daytime_evening_attendance": attendance,
        "Previous_qualification": previous_qualification,
        "Previous_qualification_grade": previous_qualification_grade,
        "Nacionality": nationality,
        "Mothers_qualification": mothers_qualification,
        "Fathers_qualification": fathers_qualification,
        "Mothers_occupation": mothers_occupation,
        "Fathers_occupation": fathers_occupation,
        "Admission_grade": admission_grade,
        "Displaced": displaced,
        "Educational_special_needs": special_needs,
        "Debtor": debtor,
        "Tuition_fees_up_to_date": tuition_fees,
        "Gender": gender,
        "Scholarship_holder": scholarship,
        "Age_at_enrollment": age,
        "International": international,
        "Curricular_units_1st_sem_credited": cu1_credited,
        "Curricular_units_1st_sem_enrolled": cu1_enrolled,
        "Curricular_units_1st_sem_evaluations": cu1_evaluations,
        "Curricular_units_1st_sem_approved": cu1_approved,
        "Curricular_units_1st_sem_grade": cu1_grade,
        "Curricular_units_1st_sem_without_evaluations": cu1_without_eval,
        "Curricular_units_2nd_sem_credited": cu2_credited,
        "Curricular_units_2nd_sem_enrolled": cu2_enrolled,
        "Curricular_units_2nd_sem_evaluations": cu2_evaluations,
        "Curricular_units_2nd_sem_approved": cu2_approved,
        "Curricular_units_2nd_sem_grade": cu2_grade,
        "Curricular_units_2nd_sem_without_evaluations": cu2_without_eval,
        "Unemployment_rate": unemployment_rate,
        "Inflation_rate": inflation_rate,
        "GDP": gdp,
    }

    # Jadikan DataFrame
    input_df = pd.DataFrame([input_dict])

    # Mengurutkan kolom secara otomatis mengambil dari memori Random Forest
    if hasattr(model, 'feature_names_in_'):
        expected_cols = model.feature_names_in_
        for col in expected_cols:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[expected_cols]

    # Scaling & Prediksi
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    
    probability_dropout = model.predict_proba(input_scaled)[0][0]

    st.divider()
    st.subheader("Hasil Prediksi")

    # Ubah logika, Jika hasil prediksi adalah 0 (Dropout)
    if prediction == 0:
        st.error(f"Mahasiswa ini **BERISIKO DROPOUT** (peluang: {probability_dropout*100:.1f}%)")
        st.markdown(
            "**Rekomendasi:** segera hubungi mahasiswa untuk sesi bimbingan/konseling, "
            "cek kendala akademik maupun finansial yang dihadapi."
        )
    else:
        st.success(f"Mahasiswa ini **TIDAK BERISIKO DROPOUT** (peluang dropout: {probability_dropout*100:.1f}%)")
        st.markdown("Tetap pantau performa mahasiswa secara berkala.")

    st.progress(min(int(probability_dropout * 100), 100))