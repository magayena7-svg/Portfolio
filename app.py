import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SIM - Mega Waena Futsal", layout="wide", page_icon="⚽")

st.title("⚽ Sistem Informasi Manajemen - Mega Waena Futsal")
st.caption("Proyek Akhir Mata Kuliah: Analisis & Desain Proses Bisnis | Isak Bunai - Universitas Ottow Geisler")

# 1. Menyiapkan Data Statis (Mockup untuk Presentasi)
data_futsal = {
    'Nama': ['Isak', 'Dyson', 'Anas', 'Budi', 'Candra'],
    'Status': ['Aktif', 'Aktif', 'Tertunda', 'Aktif', 'Tertunda'],
    'Total Iuran': [50000, 50000, 0, 50000, 0]
}
df = pd.DataFrame(data_futsal)

# 2. Sidebar Menu
menu = st.sidebar.selectbox("Pilih Menu", ["1. Alur Proses & Stakeholder", "2. Form Pendaftaran", "3. Laporan Keuangan"])

if menu == "1. Alur Proses & Stakeholder":
    st.header("📑 Desain & Analisis Sistem")
    
    # BAGIAN STAKEHOLDER (Penting untuk Nilai Kuliah!)
    st.subheader("👥 Identifikasi Stakeholder")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.info("**Admin (Isak)**\n\nBertugas menginput data dan memvalidasi pembayaran.")
    with col_b:
        st.success("**Pemain (Tim)**\n\nMemberikan data diri dan memantau transparansi kas.")
    with col_c:
        st.warning("**Manajer**\n\nMenggunakan laporan untuk rencana turnamen.")

    st.divider()

    # BAGIAN ALUR PROSES
    st.subheader("🔄 Alur Proses Bisnis Digital")
    st.write("Sistem ini mengubah pencatatan manual menjadi digital dengan alur:")
    st.code("Input Form -> Validasi Sistem -> Visualisasi Real-time -> Export Laporan")
    st.image("https://img.icons8.com/illustrations/external-tulpahn-outline-color-tulpahn/100/external-business-process-business-management-tulpahn-outline-color-tulpahn.png", width=100)

elif menu == "2. Form Pendaftaran":
    st.header("📝 Input Data Pemain Baru")
    st.write("Gunakan formulir ini untuk mendaftarkan pemain ke dalam sistem database.")
    with st.form("daftar"):
        nama = st.text_input("Nama Lengkap Pemain")
        posisi = st.selectbox("Posisi Utama", ["Pivot", "Anchor", "Ala", "Kiper"])
        nominal = st.number_input("Iuran Awal (Rp)", min_value=0, step=5000)
        submit = st.form_submit_button("Simpan ke Sistem")
        if submit:
            st.success(f"Proses Bisnis Berhasil: Pemain {nama} telah terdaftar!")
            st.balloons()

elif menu == "3. Laporan Keuangan":
    st.header("📈 Dashboard Monitoring & Output")
    
    # Ringkasan Cepat (Metrics)
    col1, col2, col3 = st.columns(3)
    total_kas = df['Total Iuran'].sum()
    col1.metric("Total Saldo Kas Tim", f"Rp {total_kas:,}")
    col2.metric("Pemain Terdaftar", len(df))
    col3.metric("Status Bayar", "60%", delta="Aktif")

    # Visualisasi
    st.subheader("📊 Visualisasi Status Pembayaran")
    fig = px.pie(df, names='Status', values='Total Iuran', 
                 hole=0.4, # Membuat grafik jadi donut chart agar lebih modern
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

    # Tabel Data
    st.subheader("📋 Detail Data Transaksi")
    st.dataframe(df, use_container_width=True)

    # Fitur Export (ETL)
    st.divider()
    st.subheader("📥 Export Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Laporan Resmi (CSV)",
        data=csv,
        file_name='laporan_futsal_waena.csv',
        mime='text/csv',
    )