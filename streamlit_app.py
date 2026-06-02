import streamlit as st
import math

# ============================================
# CSS BACKGROUND PINK
# ============================================
st.markdown("""
    <style>
    /* Background Utama - Pink */
    .stApp {
        background-color: #FFE4E1;
    }
    
    /* Background Sidebar - Pink Lebih Gelap */
    [data-testid="stSidebar"] {
        background-color: #FFD1DC;
    }
    
    /* Warna Teks Utama */
    p, div, span, label {
        color: #8B4557 !important;
    }
    
    /* Warna Heading */
    h1, h2, h3, h4, h5, h6 {
        color: #DB7093 !important;
    }
    
    /* Button */
    .stButton > button {
        background-color: #DB7093;
        color: white;
    }
    .stButton > button:hover {
        background-color: #C76085;
    }
    
    /* Input Fields */
    .stTextInput > div > div > input {
        background-color: #FFF0F5;
        border: 1px solid #DB7093;
    }
    
    /* Selectbox */
    .stSelectbox > div > div > div {
        background-color: #FFF0F5;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #FFD1DC;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# ============================================
# FUNGSI PERHITUNGAN
# ============================================

#WEB PENGHITUNG KADAR ANALIT PADA GRAVIMETRI DAN TITRIMETRI
#PERHITUNGAN KADAR AIR DAN ABU
def perhitungan_kadar_air_abu(bobot_analit, bobot_sampel):
    kadar_analit = bobot_analit / bobot_sampel * 100
    return kadar_analit


#PERHITUNGAN KADAR B/B
def perhitungan_kadar_bperb(faktor_gravi, bobot_analit, bobot_sampel):
    kadar_analit = faktor_gravi * (bobot_analit / bobot_sampel) * 100
    return kadar_analit


#PERHITUNGAN KADAR B/V
def perhitungan_kadar_bperv(faktor_gravi, bobot_analit, vol_sampel):
    kadar_analit = faktor_gravi * (bobot_analit / vol_sampel) * 100
    return kadar_analit


#STANDARISASI ASAM BASA
def standarisasi_asam_basa(bobot_primer, fp, vol_titran, berat_ekivalen):
    normalitas = (bobot_primer / (fp * vol_titran * berat_ekivalen))
    return normalitas


#PERHITUNGAN KADAR ASAM ASETAT DALAM CUKA 
def kadar_asam_asetat(volume_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = volume_titran * Normalitas * berat_ekivalen * fk * fp * 100 / volume_sampel
    return kadar_persen


#PENETAPAN KADAR Na2CO3 DALAM WARDER
def kadar_Na2CO3(b, a, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = 2 * (b-a) * Normalitas * berat_ekivalen * fk * fp * 100 / volume_sampel
    return kadar_persen 


#PENETAPAN KADAR NaOH DALAM WARDER 
def kadar_NaOH(a, b, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = ((2*a)-b) * Normalitas* berat_ekivalen * fk * fp * 100 / volume_sampel
    return kadar_persen


#STANDARISASI LARUTAN KMnO4 
def standarisasi_KMnO4(bobot_primer, fp, vol_titran, berat_ekivalen):
    normalitas = bobot_primer / (fp * vol_titran * berat_ekivalen)
    return normalitas


#PENETAPAN KADAR BESI 
def kadar_besi(volume_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = volume_titran * Normalitas * berat_ekivalen * fk * fp * 100 / volume_sampel
    return kadar_persen


#STANDARISASI LARUTAN TIOSULFAT 
def standarisasi_tio(bobot_primer, fp, vol_titran, berat_ekivalen):
    normalitas = bobot_primer / (fp * vol_titran * berat_ekivalen)
    return normalitas 


#PENETAPAN KADAR KLOR IODOMETRI 
def kadar_klor(volume_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = volume_titran * Normalitas * berat_ekivalen * fk * fp * 100 / volume_sampel 
    return kadar_persen 


#PENETAPAN KADAR KLOR ARGENTOMETRI
def kadar_klor(volume_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = volume_titran * Normalitas * berat_ekivalen * fk * fp * 100 / volume_sampel 
    return kadar_persen 


#STANDARISASI LARUTAN EDTA
def standarisasi_edta(bobot_primer, fp, vol_titran, BM):
    molaritas = bobot_primer / (fp * vol_titran * BM)
    return molaritas 


#PENETAPAN KESADAHAN JUMLAH DALAM SAMPEL AIR KOMPLEKSOMETRI EDTA 
def kadar_kesadahan(volume_titran, Molaritas, BM, volume_sampel):
    kadar_ppm = volume_titran * Molaritas * BM / volume_sampel
    return kadar_ppm 


# ============================================
# MENU NAVIGASI
# ============================================

menu = st.sidebar.selectbox(
    label = "PILIH MENU",
    options = ["Beranda", "Gravimetri", "Titrimetri", "Bahaya Bahan Kimia", "Latihan Soal", "Tentang Aplikasi"])
        

if menu == "Beranda":
    st.markdown("<h1 style='text-align: center; color: #DB7093;'>SELAMAT DATANG</h1>", unsafe_allow_html=True)
    left, mid, right = st.columns(3)
    with mid:   
        st.markdown('---')
        st.markdown('<div style="text-align: center;">Kalkulator Kimia Analitik. Dibuat untuk membantu perhitungan dalam Kimia Analitik</div>', unsafe_allow_html=True)
        st.markdown('---')
        st.markdown('<h2 style="color: #DB7093; ">DIBUAT OLEH:</h2>', unsafe_allow_html=True)
        st.write('KELOMPOK 4 (1B - ANALISIS KIMIA)')
        st.write('''
    1. Allysa Desvita Almasya R.   (2560566)
    2. Bagas Nanang Suryana        (2560595)
    3. Ezwan Pradhana Deriz        (2560621) 
    4. M. Fathurahman              (2560242) 
    5. Reva Dwi Nurhalika          (2560275)
    ''')
        st.markdown('---')
    

elif menu == "Gravimetri":
    st.write("INI GRAVIMETRI WOY")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kadar Air", "Kadar Abu", "Kadar Sulfat", "Kadar Besi", "Kadar Ba"])
    with tab1:
        st.write("Kadar Air")
        # Input bobot analit dengan 4 angka belakang koma
        bobot_analit = st.number_input(
            "Masukkan bobot analit (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BA1"
        )
        
        # Input bobot sampel dengan 4 angka belakang koma
        bobot_sampel = st.number_input(
            "Masukkan bobot sampel (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BS1"
        )

        st.write(f"Bobot analit: = {bobot_analit:.4f}", "g") 
        st.write(f"Bobot sampel: = {bobot_sampel:.4f}", "g")
        
        if st.button("Hitung Kadar", key="T1"):
            kadar_analit = perhitungan_kadar_air_abu(bobot_analit, bobot_sampel)
            st.write("Kadar Air = ", round(kadar_analit, 4))
            st.success(f"Kadar Air adalah {kadar_analit:.2f}%")
            
    with tab2:
        st.write("Kadar Abu")
        # Input bobot analit dengan 4 angka belakang koma
        bobot_analit = st.number_input(
            "Masukkan bobot analit (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BA2"
        )
        
        # Input bobot sampel dengan 4 angka belakang koma
        bobot_sampel = st.number_input(
            "Masukkan bobot sampel (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BS2"
        )

        st.write(f"Bobot analit: = {bobot_analit:.4f}", "g") 
        st.write(f"Bobot sampel: = {bobot_sampel:.4f}", "g")
        
        if st.button("Hitung Kadar", key="T2"):
            kadar_analit = perhitungan_kadar_air_abu(bobot_analit, bobot_sampel)
            st.write("Kadar Abu = ", round(kadar_analit, 4))
            st.success(f"Kadar Abu adalah {kadar_analit:.2f}%")
    with tab3:
        st.write("Kadar Sulfat")
        fg = {
            "Ar Sulfat / Mr Barium Sulfat": 96/233,
            "2 Ar Besi / Mr Besi (iii) Oksida": 112/160,
            "Ar Barium / Mr Barium Kromat": 137/253
        }
        selected_fg = st.selectbox(
            "Pilih Faktor Gravimetri", list(fg.keys()), key="S3")
        faktor_gravi = fg[selected_fg]
        st.write(f"Faktor Gravimetri = {faktor_gravi:.4f}")
        
        # Input bobot analit dengan 4 angka belakang koma
        bobot_analit = st.number_input(
            "Masukkan bobot analit (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BA3"
        )
        
        # Input bobot sampel dengan 4 angka belakang koma
        bobot_sampel = st.number_input(
            "Masukkan bobot sampel (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BS3"
        )

        st.write(f"Bobot analit: = {bobot_analit:.4f}", "g") 
        st.write(f"Bobot sampel: = {bobot_sampel:.4f}", "g")
        
        if st.button("Hitung Kadar", key="T3"):
            kadar_analit = perhitungan_kadar_bperb(faktor_gravi, bobot_analit, bobot_sampel)
            st.write(f"Kadar Sulfat = {kadar_analit:.2f}", "%")
            st.success(f"Kadar Sulfat adalah {kadar_analit:.2f}%")
            
    with tab4:
        st.write("Kadar Besi")
        fg = {
        "Ar Sulfat / Mr Barium Sulfat": 96/233,
        "2 Ar Besi / Mr Besi (iii) Oksida": 112/160,
        "Ar Barium / Mr Barium Kromat": 137/253
        }
        selected_fg = st.selectbox(
            "Pilih Faktor Gravimetri", list(fg.keys()), key = ("S4"))
        faktor_gravi = fg[selected_fg]
        st.write(f"Faktor Gravimetri = {faktor_gravi:.4f}")
        
        bobot_analit = st.number_input(
            "Masukkan bobot analit (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BA4"
        )
        bobot_sampel = st.number_input(
            "Masukkan bobot sampel (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BS4"
        )
        st.write(f"Bobot analit: = {bobot_analit:.4f}", "g") 
        st.write(f"Bobot sampel: = {bobot_sampel:.4f}", "g")
        
        if st.button("Hitung Kadar", key = "T4"):
            kadar_analit = perhitungan_kadar_bperb(faktor_gravi, bobot_analit, bobot_sampel)
            st.write(f"Kadar Besi = {kadar_analit:.2f}", "%")
            st.success(f"Kadar Besi adalah {kadar_analit:.2f}%")
            
    with tab5:
        st.write("Kadar Ba")
        fg = {
        "Ar Sulfat / Mr Barium Sulfat": 96/233,
        "2 Ar Besi / Mr Besi (iii) Oksida": 112/160,
        "Ar Barium / Mr Barium Kromat": 137/253
        }
        selected_fg = st.selectbox(
            "Pilih Faktor Gravimetri", list(fg.keys()), key = ("S5"))
        faktor_gravi = fg[selected_fg]
        st.write(f"Faktor Gravimetri = {faktor_gravi:.4f}")
        
        bobot_analit = st.number_input(
            "Masukkan bobot analit (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BA4"
        )
        bobot_sampel = st.number_input(
            "Masukkan bobot sampel (g): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="BS4"
        )
        st.write(f"Bobot analit: = {bobot_analit:.4f}", "g") 
        st.write(f"Volume sampel: = {vol_sampel:.4f}", "mL")
        
        if st.button("Hitung Kadar", key = "T5"):
            kadar_analit = perhitungan_kadar_bperv(faktor_gravi, bobot_analit, vol_sampel):
            st.write(f"Kadar Ba = {kadar_analit:.2f}", "b/v")
            st.success(f"Kadar Ba adalah {kadar_analit:.2f}b/v")
        

elif menu == "Titrimetri":
    tab6, tab7, tab8, tab9 = st.tabs(["Standarisasi", "Penetapan Kadar", "Kompleksometri", "Custom"])
    with tab6:
        st.write("Ini Standarisasi")
        be = {
        "berat_ekivalen Asam Oksalat": 63,
        "berat_ekivalen Boraks": 190,
        "berat_ekivalen Kalium Dikromat": 49,
        }
        selected_be = st.selectbox(
            "Pilih Berat Ekivalen", list(be.keys()))
        berat_ekivalen = be[selected_be]
        st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
        
        bobot_primer = st.number_input("Masukkan bobot baku primer (mg): ")
        fp =  st.number_input("Masukkan faktor pengali: ") 
        vol_titran =  st.number_input("Masukkan volume titran (mL): ")
        st.write("Bobot baku primer: ", bobot_primer, "mg")
        st.write("Faktor pengenceran: ", fp)
        st.write("Volume titran: ", round(vol_titran, 2), "mL")
        if st.button("Hitung Normalitas", key = "T1"):
            normalitas = standarisasi_asam_basa(bobot_primer, fp, vol_titran, berat_ekivalen)
            st.write("Normalitas = ", round(normalitas, 4))
            st.success(f"Normalitas adalah {round(normalitas, 4)} mgrek/mL")
        
    with tab7:
        st.write("Ini Penetapan Kadar")
    with tab8:
        st.write("Ini Kompleksometri")
    with tab9:
        st.write("Ini Custom")
    st.write("INI TITRIMETRI WOY")
    
    
    
    

elif menu == "Bahaya Kimia":
    st.write("INI BAHAYA BAHAN KIMIA WOY")

elif menu == "Latihan Soal":
    st.write("INI LATSOL WOY")





    

