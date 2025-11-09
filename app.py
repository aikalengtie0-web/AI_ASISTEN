import streamlit as st
import pandas as pd
import re
from datetime import datetime

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="AI Asisten Kontak Pengguna", page_icon="🤖", layout="centered")

# --- Inisialisasi CSV ---
csv_file = "messages.csv"

# --- Navbar Pilihan Halaman ---
st.sidebar.markdown("📁 **Pilih Halaman**")
page = st.sidebar.selectbox("Menu", ["Form Kontak", "Halaman Admin"])

# --- Fungsi Validasi Email ---
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# --- Halaman Form Kontak ---
if page == "Form Kontak":
    st.title("🤖 AI Asisten Kontak Pengguna")
    st.subheader("Silakan isi formulir di bawah ini untuk menghubungi saya 👇")

    nama = st.text_input("🧑 Nama Lengkap")
    email = st.text_input("📧 Alamat Email")
    pesan = st.text_area("💬 Pesan Anda")

    if st.button("Kirim Pesan"):
        if not nama or not email or not pesan:
            st.warning("⚠️ Semua kolom harus diisi!")
        elif not valid_email(email):
            st.error("❌ Alamat email tidak valid! Harap isi dengan format yang benar (misalnya: nama@email.com).")
        else:
            data = pd.DataFrame([[datetime.now(), nama, email, pesan]], 
                                columns=["Waktu", "Nama", "Email", "Pesan"])
            data.to_csv(csv_file, mode='a', header=not pd.io.common.file_exists(csv_file), index=False)
            st.success("✅ Pesan berhasil dikirim! Terima kasih sudah menghubungi saya.")

    st.markdown("---")
    st.caption("Dibuat dengan berdasarkan keyakinan Aikal Eng Tie")

# --- Halaman Admin ---
elif page == "Halaman Admin":
    st.title("🤖 AI Asisten Kontak Pengguna")
    st.header("🛡️ Halaman Admin - Daftar Pesan Masuk")

    password = st.text_input("Masukkan password admin:", type="password")

    if password == "admin123":
        st.success("🔓 Akses diterima! Berikut daftar pesan masuk:")

        try:
            df = pd.read_csv(csv_file)
            st.dataframe(df)
        except FileNotFoundError:
            st.warning("Belum ada pesan yang masuk.")
    elif password:
        st.error("❌ Password salah!")

    st.markdown("---")
    st.caption("Dibuat dengan berdasarkan keyakinan Aikal Eng Tie")
