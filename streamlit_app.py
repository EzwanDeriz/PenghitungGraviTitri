import streamlit as st
import math
from streamlit_option_menu import option_menu

# ============================================
# FUNGSI PERHITUNGAN
# ============================================
st.markdown("""
    <style>
    /* Background Utama - Warm Beige */
    .stApp {
        background-color: #EFECE2;
    }
    
    /* Background Sidebar - Olive Green Gray */
    [data-testid="stSidebar"] {
        background-color: #8A9A86;
    }
    
    /* Warna Teks Utama - Matte Black */
    p, div, span, label {
        color: #374151 !important;
    }
    
    /* Warna Heading - Matte Black */
    h1, h2, h3, h4, h5, h6 {
        color: #374151 !important;
    }
    
    /* Button - Terracotta Red (Tombol Aksi) */
    .stButton > button {
        background-color: #C2593F;
        color: white;
    }
    .stButton > button:hover {
        background-color: #A84832;
    }
    
    /* Input Fields - Classic Gray (Tombol Angka) */
    .stTextInput > div > div > input {
        background-color: #D1D5DB;
        border: 1px solid #8A9A86;
        color: #374151;
    }
    
    /* Selectbox - Classic Gray */
    .stSelectbox > div > div > div {
        background-color: #D1D5DB;
        color: #374151;
    }
    
    /* Number Input - Classic Gray */
    .stNumberInput > div > div > div > input {
        background-color: #D1D5DB;
        border: 1px solid #8A9A86;
        color: #374151;
    }
    
    /* Tabs - Olive Green Gray Background */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #D1D5DB;
    }
    
    /* Radio Buttons & Checkboxes - Matte Black */
    .stRadio > div > label {
        color: #374151 !important;
    }
    
    /* Slider - Terracotta Red */
    .stSlider [data-baseweb="slider"] {
        color: #C2593F;
    }
    
    /* Dividers / Garis Batas - Classic Gray */
    hr {
        border-color: #D1D5DB !important;
    }
    
    /* Metrics - Terracotta Red */
    [data-testid="stMetricValue"] {
        color: #C2593F !important;
    }
    
    /* Expander - Classic Gray */
    .streamlit-expanderHeader {
        color: #374151 !important;
        background-color: #D1D5DB;
    }
    
    /* Tables - Classic Gray Border */
    .stDataFrame {
        border: 1px solid #D1D5DB;
    }
    
    /* Success/Error/Info Messages */
    .stSuccess {
        background-color: #DCFEEC;
        color: #065F46;
    }
    .stError {
        background-color: #FEE2E2;
        color: #991B1B;
    }
    .stWarning {
        background-color: #FEF3C7;
        color: #92400E;
    }
    .stInfo {
        background-color: #E0E7FF;
        color: #3730A3;
    }
    
    /* Markdown Link - Terracotta Red */
    a {
        color: #C2593F;
    }
    
    /* Sidebar Text Color - Warm Beige */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #EFECE2 !important;
    }
    
    /* Container styling */
    div[data-testid="stVerticalBlock"] {
        background-color: #EFECE2;
    }
    
    /* Header di Sidebar */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #EFECE2 !important;
    }
    
    /* Selection highlight */
    ::selection {
        background-color: #C2593F;
        color: white;
    }
    </style>
    """, 
    unsafe_allow_html=True
)






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


#PERHITUNGAN KADAR PERSEN 
def kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = vol_titran * Normalitas * berat_ekivalen * fk * fp * 100 / volume_sampel
    return kadar_persen


#PENETAPAN KADAR Na2CO3 DALAM WARDER
def kadar_Na2CO3(b, a, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = (b-a) * 2 * Normalitas * berat_ekivalen * fk * fp * 100 / volume_sampel
    return kadar_persen


#PENETAPAN KADAR NaOH DALAM WARDER 
def kadar_NaOH(a, b, Normalitas, berat_ekivalen, fk, fp, volume_sampel):
    kadar_persen = ((2*a)-b) * Normalitas* berat_ekivalen * fk * fp * 100 / volume_sampel
    return kadar_persen


#STANDARISASI LARUTAN KMnO4 
def standarisasi_KMnO4(bobot_primer, fp, vol_titran, berat_ekivalen):
    normalitas = bobot_primer / (fp * vol_titran * berat_ekivalen)
    return normalitas


#STANDARISASI LARUTAN TIOSULFAT 
def standarisasi_tio(bobot_primer, fp, vol_titran, berat_ekivalen):
    normalitas = bobot_primer / (fp * vol_titran * berat_ekivalen)
    return normalitas 

#STANDARISASI LARUTAN EDTA
def standarisasi_edta(bobot_primer, fp, vol_titran, berat_molekul):
    molaritas = bobot_primer / (fp * vol_titran * berat_molekul)
    return molaritas 


#PENETAPAN KESADAHAN JUMLAH DALAM SAMPEL AIR KOMPLEKSOMETRI EDTA 
def kadar_kesadahan(volume_titran, Molaritas, berat_molekul, volume_sampel):
    kadar_ppm = volume_titran * Molaritas * berat_molekul / volume_sampel
    return kadar_ppm 


# ============================================
# MENU NAVIGASI
# ============================================

with st.sidebar:
    menu = option_menu(
        menu_title = "Menu",
        options = ["Beranda", 
            "Gravimetri", 
            "Titrimetri",
            "Bahaya Bahan Kimia",
            "Latihan Soal",
            "Tentang Aplikasi"],
        icons = ["house-door", "calculator", "calculator", "calculator", "calculator", "exclamation-circle"],
        styles = {
        "icon": {"font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "blue"}}
    )
        

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
    4. Muhammad Fathurrahman       (2560681) 
    5. Reva Dwi Nurhalika          (2560750)
    ''')
        st.markdown('---')
    

elif menu == "Gravimetri":
    st.write("INI GRAVIMETRI WOY")
    tab1, tab2, tab3, tab4, tab5, tabX = st.tabs(["Kadar Air", "Kadar Abu", "Kadar Sulfat", "Kadar Besi", "Kadar Ba", "Custom"])
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
            kadar_analit =  perhitungan_kadar_air_abu(bobot_analit, bobot_sampel)
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
            key="BA5"
        )
        vol_sampel = st.number_input(
            "Masukkan volume sampel (mL): ",
            min_value=0.0,
            step=0.0001,
            format="%.2f",
            key="VS1"
        )
        st.write(f"Bobot analit: = {bobot_analit:.4f}", "g") 
        st.write(f"Volume sampel: = {vol_sampel:.2f}", "mL")
        
        if st.button("Hitung Kadar", key = "T5"):
            kadar_analit = perhitungan_kadar_bperv(faktor_gravi, bobot_analit, vol_sampel)
            st.write(f"Kadar Ba = {kadar_analit:.2f}", "b/v")
            st.success(f"Kadar Ba adalah {kadar_analit:.2f}b/v")
            
    with tabX:
        tabQ, tabR =  st.tabs(["Kadar B/B", "Kadar B/v"])
        with tabQ:
            faktor_gravimetri = st.number_input(
                "Masukkan faktor gravimetri: ",
                 min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="FGX"
            )
            st.write(f"Faktor Gravimetri = {faktor_gravimetri:.4f}")
            bobot_analit = st.number_input(
                "Masukkan bobot analit (g): ",
                min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="BAX"
            )
            bobot_sampel = st.number_input(
                "Masukkan bobot sampel (g): ",
                min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="BSX"
            )
            st.write(f"Bobot analit: = {bobot_analit:.4f}", "g") 
            st.write(f"Bobot sampel: = {bobot_sampel:.4f}", "g")
            
            if st.button("Hitung Kadar", key = "TX"):
                kadar_analit = perhitungan_kadar_bperb(faktor_gravimetri, bobot_analit, bobot_sampel)
                st.write(f"Kadar Besi = {kadar_analit:.2f}", "%")
                st.success(f"Kadar Besi adalah {kadar_analit:.2f}%")
                
        with tabR:
            faktor_gravimetri = st.number_input(
                "Masukkan faktor gravimetri: ",
                min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="FGR"
            )
            st.write(f"Faktor Gravimetri = {faktor_gravimetri:.4f}")
            bobot_analit = st.number_input(
                "Masukkan bobot analit (g): ",
                min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="BAR"
            )
            vol_sampel = st.number_input(
                "Masukkan volume sampel (mL): ",
                min_value=0.0,
                step=0.0001,
                format="%.2f",
                key="VSR"
            )
            st.write(f"Bobot analit: = {bobot_analit:.4f}", "g") 
            st.write(f"Volume sampel: = {vol_sampel:.2f}", "mL")
             
            if st.button("Hitung Kadar", key = "TR"):
                kadar_analit = perhitungan_kadar_bperv(faktor_gravimetri, bobot_analit, vol_sampel)
                st.write(f"Kadar Ba = {kadar_analit:.2f}", "b/v")
                st.success(f"Kadar Ba adalah {kadar_analit:.2f}b/v")
            
        
        
        

elif menu == "Titrimetri":
    tab6, tab7, tab8, tab9 = st.tabs(["Standarisasi", "Penetapan Kadar", "Kompleksometri", "Custom"])
    with tab6:
        st.write("Ini Standarisasi")
        be = {
        "Berat ekivalen Asam Oksalat": 63,
        "Berat ekivalen Boraks": 190,
        "Berat ekivalen Kalium Dikromat": 49,
        "Berat ekivalen Asam Asetat": 60,
        "Berat ekivalen Natrium Karbonat": 53,
        "Berat ekivalen Besi": 56,
        "Berat ekivalen Kalium Dikromat": 49,
        "Berat ekivalen Klorida": 37.5,
        }
        selected_be = st.selectbox(
            "Pilih Berat Ekivalen", list(be.keys()), key = ("VT6"))
        berat_ekivalen = be[selected_be]
        st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
        
        bobot_primer = st.number_input("Masukkan bobot baku primer (mg): ")
        fp =  st.number_input("Masukkan faktor pengali/pengenceran: ") 
        vol_titran =  st.number_input("Masukkan volume titran (mL): ")
        st.write("Bobot baku primer: ", bobot_primer, "mg")
        st.write("Faktor pengali/pengenceran: ", fp)
        st.write("Volume titran: ", round(vol_titran, 2), "mL")
        if st.button("Hitung Normalitas", key = "T1"):
            normalitas = standarisasi_asam_basa(bobot_primer, fp, vol_titran, berat_ekivalen)
            st.write("Normalitas = ", round(normalitas, 4))
            st.success(f"Normalitas adalah {round(normalitas, 4)} mgrek/mL")
        
    with tab7:
        st.write("Ini Penetapan Kadar")
        tab10, tab11, tab12, tab13 = st.tabs(["Kadar Asetat", "Kadar NaOH dan Na2CO3", "Kadar Besi", "Kadar Klor"])
        with tab10:
            be = {
            "Berat ekivalen Asam Oksalat": 63,
            "Berat ekivalen Boraks": 190,
            "Berat ekivalen Kalium Dikromat": 49,
            "Berat ekivalen Asam Asetat": 60,
            "Berat ekivalen Natrium Karbonat": 53,
            "Berat ekivalen Besi": 56,
            "Berat ekivalen Kalium Dikromat": 49,
            "Berat ekivalen Klorida": 37.5,
            "Berat ekivalen Natrium Hidroksida": 40,
            }
            selected_be = st.selectbox(
                "Pilih Berat Ekivalen", list(be.keys()), key = ("BE10"))
            berat_ekivalen = be[selected_be]
            st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
        
            Normalitas = st.number_input(
            "Masukkan normalitas titran (N): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="N10"
        )
            fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FP10")) 
            fk = 0.001
            vol_titran =  st.number_input("Masukkan volume titran (mL): ", key = ("VT10"))
            volume_sampel = st.number_input("Masukkan volume titrat (mL): ", key = ("VS10"))
            st.write("Normalitas titran: ", Normalitas, "N")
            st.write("Faktor pengali/pengenceran: ", fp)
            st.write("Faktor Konversi: ", fk)
            st.write("Volume titran: ", round(vol_titran, 2), "mL")
            st.write("Volume titrat: ", round(volume_sampel, 2), "mL")
            
            if st.button("Hitung Kadar", key = "T10"):
                kadar_persen = kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                st.write("Kadar Persen = ", round(kadar_persen, 2), "%")
                st.success(f"Kadar Persen adalah {round(kadar_persen, 2)} %")
        with tab11:
            st.write("Kadar NaOH dan Na2CO3")
            tabA, tabB = st.tabs (["Kadar NaOH", "Kadar Na2CO3"])
            with tabA:
                be = {
                "Berat ekivalen Asam Oksalat": 63,
                "Berat ekivalen Boraks": 190,
                "Berat ekivalen Kalium Dikromat": 49,
                "Berat ekivalen Asam Asetat": 60,
                "Berat ekivalen Natrium Karbonat": 53,
                "Berat ekivalen Besi": 56,
                "Berat ekivalen Kalium Dikromat": 49,
                "Berat ekivalen Klorida": 37.5,
                "Berat ekivalen Natrium Hidroksida": 40,
                }
             
                selected_be = st.selectbox(
                    "Pilih Berat Ekivalen", list(be.keys()), key = ("BEA"))
                berat_ekivalen = be[selected_be]
                st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
            
                Normalitas = st.number_input(
                "Masukkan normalitas titran (N): ",
                min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="NA"
            )
                fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FPA")) 
                fk = 0.001
                a = st.number_input("Masukkan volume awal: (mL) ", key = ("AA")) 
                b = st.number_input("Masukkan volume akhir: (mL) ", key = ("BA")) 
                volume_sampel = st.number_input("Masukkan volume titrat (mL): ", key = ("VSA"))
                st.write("Normalitas titran: ", Normalitas, "mg")
                st.write("Volume Awal: ", a, "mL")
                st.write("Volume Akhir: ", b, "mL")
                st.write("Faktor pengali/pengenceran: ", fp)
                st.write("Faktor Konversi: ", fk)
                st.write("Volume titrat: ", volume_sampel, "ml")
                
                if st.button("Hitung Kadar", key = "TA"):
                    kadar_persen = kadar_NaOH(a, b, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                    st.write("Kadar Persen NaOH = ", round(kadar_persen, 2))
                    st.success(f"Kadar Persen NaOH adalah {round(kadar_persen, 2)} %")
                
            with tabB:
                be = {
                "Berat ekivalen Asam Oksalat": 63,
                "Berat ekivalen Boraks": 190,
                "Berat ekivalen Kalium Dikromat": 49,
                "Berat ekivalen Asam Asetat": 60,
                "Berat ekivalen Natrium Karbonat": 53,
                "Berat ekivalen Besi": 56,
                "Berat ekivalen Kalium Dikromat": 49,
                "Berat ekivalen Klorida": 37.5,
                "Berat ekivalen Natrium Hidroksida": 40,
                }
                selected_be = st.selectbox(
                    "Pilih Berat Ekivalen", list(be.keys()), key = ("BEB"))
                berat_ekivalen = be[selected_be]
                st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
            
                Normalitas = st.number_input(
                "Masukkan normalitas titran (N): ",
                min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="NB"
            )
                fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FPB")) 
                fk = 0.001
                a = st.number_input("Masukkan volume awal: (mL) ", key = ("AB")) 
                b = st.number_input("Masukkan volume akhir: (mL) ", key = ("BB")) 
                volume_sampel = st.number_input("Masukkan volume titrat (mL): ", key = ("VSB"))
                st.write("Normalitas titran: ", Normalitas, "N")
                st.write("Volume Awal: ", a, "mL")
                st.write("Volume Akhir: ", b, "mL") 
                st.write("Faktor pengali/pengenceran: ", fp)
                st.write("Faktor Konversi: ", fk)
                st.write("Volume titrat: ", volume_sampel, "mL")
                
                if st.button("Hitung Kadar", key = "TB"):
                    kadar_persen = kadar_Na2CO3(b, a, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                    st.write("Kadar Persen Na2CO3 = ", round(kadar_persen, 2))
                    st.success(f"Kadar Persen Na2CO3 adalah {round(kadar_persen, 2)} %")

        with tab12:
            be = {
            "Berat ekivalen Asam Oksalat": 63,
            "Berat ekivalen Boraks": 190,
            "Berat ekivalen Kalium Dikromat": 49,
            "Berat ekivalen Asam Asetat": 60,
            "Berat ekivalen Natrium Karbonat": 53,
            "Berat ekivalen Besi": 56,
            "Berat ekivalen Kalium Dikromat": 49,
            "Berat ekivalen Klorida": 37.5,
            "Berat ekivalen Natrium Hidroksida": 40,
            }
            selected_be = st.selectbox(
                "Pilih Berat Ekivalen", list(be.keys()), key = ("BE12"))
            berat_ekivalen = be[selected_be]
            st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
        
            Normalitas = st.number_input(
            "Masukkan normalitas titran (N): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="N12"
        )
            fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FP12")) 
            fk = 0.001
            vol_titran =  st.number_input("Masukkan volume titran (mL): ", key = ("VT12"))
            volume_sampel = st.number_input("Masukkan volume titrat (mL): ", key = ("VS12"))
            st.write("Normalitas titran: ", Normalitas, "N")
            st.write("Faktor pengali/pengenceran: ", fp)
            st.write("Faktor Konversi: ", fk)
            st.write("Volume titran: ", round(vol_titran, 2), "mL")
            
            if st.button("Hitung Kadar", key = "T12"):
                kadar_persen = kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                st.write("Kadar Persen = ", round(kadar_persen, 2))
                st.success(f"Kadar Persen adalah {round(kadar_persen, 2)} %")
                
        with tab13:
            be = {
            "Berat ekivalen Asam Oksalat": 63,
            "Berat ekivalen Boraks": 190,
            "Berat ekivalen Kalium Dikromat": 49,
            "Berat ekivalen Asam Asetat": 60,
            "Berat ekivalen Natrium Karbonat": 53,
            "Berat ekivalen Besi": 56,
            "Berat ekivalen Kalium Dikromat": 49,
            "Berat ekivalen Klorida": 37.5,
            "Berat ekivalen Natrium Hidroksida": 40,
            }
            selected_be = st.selectbox(
                "Pilih Berat Ekivalen", list(be.keys()), key = ("BE13"))
            berat_ekivalen = be[selected_be]
            st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
        
            Normalitas = st.number_input(
            "Masukkan normalitas titran (N): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="N13"
        )
            fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FP13")) 
            fk = 0.001
            vol_titran =  st.number_input("Masukkan volume titran (mL): ", key = ("VT13"))
            volume_sampel = st.number_input("Masukkan volume titrat (mL): ", key = ("VS13"))
            st.write("Normalitas titran: ", Normalitas, "N")
            st.write("Faktor pengali/pengenceran: ", fp)
            st.write("Faktor Konversi: ", fk)
            st.write("Volume titran: ", round(vol_titran, 2), "mL")
            
            if st.button("Hitung Kadar", key = "T13"):
                kadar_persen = kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                st.write("Kadar Persen = ", round(kadar_persen, 2))
                st.success(f"Kadar Persen adalah {round(kadar_persen, 2)} %")    
    with tab8:
        st.write("Ini Kompleksometri")
        tabC, tabD = st.tabs (["Standarisasi EDTA", "Penetapan Kesadahan"])
        with tabC:
            bm = {"Berat Molekul Kalsium Karbonat": 100,}
            selected_bm = st.selectbox(
                "Pilih Berat Molekul", list(bm.keys()), key = ("BMC"))
            berat_molekul = bm[selected_bm]
            st.write("Berat Molekul = ", berat_molekul, "mg/mmol")
                
            bobot_primer = st.number_input("Masukkan bobot baku primer (mg): ", key = ("BPC"))
            fp =  st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FPC")) 
            vol_titran =  st.number_input("Masukkan volume titran (mL): ", key = ("MC"))
            st.write("Bobot baku primer: ", bobot_primer, "mg")
            st.write("Faktor pengali/pengenceran: ", fp)
            st.write("Volume titran: ", round(vol_titran, 2), "mL")
            if st.button("Hitung Molaritas", key = "TC"):
                molaritas = standarisasi_edta(bobot_primer, fp, vol_titran, berat_molekul)
                st.write("Molaritas = ", round(molaritas, 4))
                st.success(f"Molaritas adalah {round(molaritas, 4)} mmol/mL")
        
        with tabD:
            bm = {"Berat Molekul Kalsium Karbonat": 100,}
            selected_bm = st.selectbox(
                "Pilih Berat Molekul", list(bm.keys()), key = ("BMD"))
            berat_molekul = bm[selected_bm]
            st.write("Berat Molekul = ", berat_molekul, "mg/mmol")
        
            Molaritas = st.number_input(
            "Masukkan molaritas titran (mg/mmol): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="MD"
        )
            fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FPD")) 
            volume_titran =  st.number_input("Masukkan volume titran (mL): ", key = ("VTD"))
            volume_sampel = st.number_input("Masukkan volume titrat (L): ", key = ("VSD"))
            st.write("Molaritas titran: ", Molaritas, "mg/mmol")
            st.write("Faktor pengali/pengenceran: ", fp)
            st.write("Volume titran: ", round(volume_titran, 2), "mL")
            st.write("Volume titrat: ", round(volume_sampel, 2), "L")
                     
            if st.button("Hitung Kadar", key = "TD"):
                kadar_kesadahan = kadar_kesadahan(volume_titran, Molaritas, berat_molekul, volume_sampel)
                st.write("Kadar Kesadahan = ", round(kadar_kesadahan, 2))
                st.success(f"Kadar Kesadahan adalah {round(kadar_kesadahan, 2)} mg/L")
        
    with tab9:
        st.write("Ini Custom")
        tabE, tabF= st.tabs (["Standarisasi ", "Penetapan Kadar"])
        with tabE:
            berat_ekivalen = st.number_input("Masukkan berat ekivalen (mg/mgrek): ",key = ("BEE"))
            st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
            bobot_primer = st.number_input("Masukkan bobot baku primer (mg): ",key = ("BPE"))
            fp =  st.number_input("Masukkan faktor pengali/pengenceran: ",key = ("FPE")) 
            vol_titran =  st.number_input("Masukkan volume titran (mL): ",key = ("VTE"))
            st.write("Bobot baku primer: ", bobot_primer, "mg")
            st.write("Faktor pengali/pengenceran: ", fp)
            st.write("Volume titran: ", round(vol_titran, 2), "mL")
            if st.button("Hitung Normalitas", key = "NE"):
                normalitas = standarisasi_asam_basa(bobot_primer, fp, vol_titran, berat_ekivalen)
                st.write("Normalitas = ", round(normalitas, 4))
                st.success(f"Normalitas adalah {round(normalitas, 4)} mgrek/mL")

        with tabF:
            berat_ekivalen = st.number_input("Masukkan berat ekivalen (mg/mgrek): ",key = ("BEF"))
            st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
            Normalitas = st.number_input(
            "Masukkan normalitas titran (N): ",
            min_value=0.0,
            step=0.0001,
            format="%.4f",
            key="NF"
        )
            fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FPF")) 
            fk = 0.001
            vol_titran =  st.number_input("Masukkan volume titran (mL): ", key = ("VTF"))
            volume_sampel = st.number_input("Masukkan volume titrat (mL): ", key = ("VSF"))
            st.write("Normalitas titran: ", Normalitas, "N")
            st.write("Faktor pengali/pengenceran: ", fp)
            st.write("Faktor Konversi: ", fk)
            st.write("Volume titran: ", round(vol_titran, 2), "mL")
            
            if st.button("Hitung Kadar", key = "TF"):
                kadar_persen = kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                st.write("Kadar Persen = ", round(kadar_persen, 2))
                st.success(f"Kadar Persen adalah {round(kadar_persen, 2)} %")
    
    
    
    

elif menu == "Bahaya Bahan Kimia":
    st.set_page_config(
        page_title="Aplikasi Simbol Hazard Kimia",
        page_icon="🧪",
        layout="centered"
    )
    
    # CSS styling
    st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            color: #8A9A86;
            margin-bottom: 10px;
        }
        .hazard-card {
            background-color: #EFECE2;
            border-left: 5px solid #8A9A86;
            border-radius: 8px;
            padding: 16px 20px;
            margin-bottom: 16px;
        }
        .section-label {
            font-size: 1rem;
            font-weight: bold;
            color: #8A9A86;
            margin-bottom: 4px;
        }
        .badge {
            display: inline-block;
            background-color: #EFECE2;
            color: #8A9A86;
            border-radius: 12px;
            padding: 3px 12px;
            margin: 3px;
            font-size: 0.9rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Data hazard
    hazards = {
        "Korosif": {
            "emoji": "🧪",
            "color": "#e74c3c",
            "desc": "Menyebabkan kerusakan serius pada kulit dan/atau mata. Dapat merusak logam.",
            "examples": ["Asam Sulfat (H₂SO₄)", "Natrium Hidroksida (NaOH)", "Amonium Nitrat", "Hidrogen Klorida (HCl)"]
        },
        "Mudah Meledak": {
            "emoji": "💥",
            "color": "#c0392b",
            "desc": "Sangat tidak stabil secara termal, dapat meledak atau bereaksi secara eksplosif.",
            "examples": ["TNT (Trinitrotoluena)", "Nitroglycerin", "Peroksida Hidrogen (konsentrat)", "Azida Natrium"]
        },
        "Mudah Terbakar": {
            "emoji": "🔥",
            "color": "#e67e22",
            "desc": "Mudah terbakar di udara pada suhu normal. Menyala saat terkena percikan api.",
            "examples": ["Etanol", "Bensin", "Aseton", "Toluene"]
        },
        "Beracun": {
            "emoji": "☠️",
            "color": "#8e44ad",
            "desc": "Fatal jika tertelan, terhirup atau bersentuhan dengan kulit. Sangat beracun.",
            "examples": ["Sianida (CN⁻)", "Stricnin", "Ricin", "Tembaga Sulfat"]
        },
        "Berbahaya Kesehatan": {
            "emoji": "⚠️",
            "color": "#d35400",
            "desc": "Mungkin menyebabkan kanker, mutasi genetik, atau kerusakan reproduksi.",
            "examples": ["Benzena", "Formaldehida", "Asbes", "Timbal"]
        },
        "Berbahaya Lingkungan": {
            "emoji": "🌊",
            "color": "#1abc9c",
            "desc": "Sangat beracun bagi kehidupan air. Berbahaya bagi lingkungan.",
            "examples": ["Merkuri", "PCB (Poliklorinasi Bifenil)", "DDT", "Organofosfat"]
        },
        "Oksidator": {
            "emoji": "🧯",
            "color": "#f39c12",
            "desc": "Mungkin menyebabkan atau memperkuat jalanan. Melepaskan oksigen.",
            "examples": ["Kalium Permanganat (KMnO₄)", "Natrium Nitrat (NaNO₃)", "Hidrogen Peroksida", "Amonium Perklorat"]
        },
        "Gas Tekan": {
            "emoji": "💨",
            "color": "#2980b9",
            "desc": "Gas di bawah tekanan. Dapat meledak jika dipanaskan.",
            "examples": ["Oksigen (O₂)", "Nitrogen (N₂)", "Karbon Dioksida (CO₂)", "Hidrogen (H₂)"]
        }
    }
    
    # Session state untuk navigasi
    if "page" not in st.session_state:
        # Langsung ke menu hazard, menu utama dihapus
        st.session_state.page = "hazard_menu"
    if "selected_hazard" not in st.session_state:
        st.session_state.selected_hazard = None
    
    def go_to(page, hazard=None):
        st.session_state.page = page
        st.session_state.selected_hazard = hazard
    
    # ───────────────────────────────
    # HALAMAN: MENU HAZARD (Halaman Awal)
    # ───────────────────────────────
    if st.session_state.page == "hazard_menu":
        st.markdown('<div class="main-title">📋 PILIH SIMBOL HAZARD</div>', unsafe_allow_html=True)
        st.markdown("---")
    
        cols = st.columns(2)
        for i, (name, data) in enumerate(hazards.items()):
            with cols[i % 2]:
                if st.button(f"{data['emoji']} {name}", use_container_width=True, key=f"btn_{name}"):
                    go_to("hazard_detail", name)
                    st.rerun()
    
        st.markdown("---")
        st.caption("Aplikasi edukasi simbol bahaya bahan kimia berdasarkan standar GHS (Globally Harmonized System).")
    
    # ───────────────────────────────
    # HALAMAN: DETAIL HAZARD
    # ───────────────────────────────
    elif st.session_state.page == "hazard_detail":
        name = st.session_state.selected_hazard
        data = hazards[name]
    
        st.markdown(f"<h2 style='color:{data['color']}'>{data['emoji']} {name}</h2>", unsafe_allow_html=True)
        st.caption("Simbol Hazard Kimia GHS")
        st.markdown("---")
    
    
        st.markdown('<div class="section-label">1️⃣ PENJELASAN BAHAYA</div>', unsafe_allow_html=True)
        st.write(data["desc"])
    
        st.markdown('<br><div class="section-label">2️⃣ CONTOH BAHAN KIMIA</div>', unsafe_allow_html=True)
        for ex in data["examples"]:
            st.markdown(f'<span class="badge">• {ex}</span>', unsafe_allow_html=True)
    
        st.markdown('</div>', unsafe_allow_html=True)
    
        st.markdown("---")
        if st.button("⬅️ Kembali ke Daftar Simbol", use_container_width=True):
            go_to("hazard_menu")
            st.rerun() 
         
elif menu == "Latihan Soal":
    st.write("LATIHAN SOAL")
    st.write("Sebuah sampel tepung terigu ditimbang untuk dianalisis kadar abunya menggunakan cawan porselen. Berdasarkan penimbangan diperoleh data sebagai berikut:")

elif menu == "Tentang Aplikasi":
    st.write("Ini Informasi Mengenai Aplikasi")





    

