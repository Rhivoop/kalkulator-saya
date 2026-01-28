import streamlit as st

# Membuat judul aplikasi
st.title("Aplikasi Kalkulator Profit")

# Membuat input angka untuk user
modal = st.number_input("Masukkan Harga Modal (Rp)", value=0)
jual = st.number_input("Masukkan Harga Jual (Rp)", value=0)

# Logika perhitungan
if st.button("Hitung Keuntungan"):
    untung = jual - modal
    
    if modal > 0:
        persen = (untung / modal) * 100
    else:
        persen = 0

    # Menampilkan hasil
    st.success(f"Keuntungan Bersih: Rp {untung}")
    st.info(f"Persentase Profit: {persen}%")