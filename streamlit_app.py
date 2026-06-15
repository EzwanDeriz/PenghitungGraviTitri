import streamlit as st
import math
from streamlit_option_menu import option_menu
#Kode Style CSS untuk WEB
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

#Fungsi-Fungsi Kalkulator
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
#STANDARISASI
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
#STANDARISASI LARUTAN EDTA
def standarisasi_edta(bobot_primer, fp, vol_titran, berat_molekul):
    molaritas = bobot_primer / (fp * vol_titran * berat_molekul)
    return molaritas 
#PENETAPAN KESADAHAN JUMLAH DALAM SAMPEL AIR KOMPLEKSOMETRI EDTA 
def kadar_kesadahan(volume_titran, Molaritas, berat_molekul, volume_sampel):
    kadar_ppm = volume_titran * Molaritas * berat_molekul / volume_sampel
    return kadar_ppm 
# MENU NAVIGASI
with st.sidebar:
    menu = option_menu(
        menu_title = "Menu",
        options = ["Beranda", 
            "Gravimetri", 
            "Titrimetri",
            "Latihan Soal"],
        icons = ["house-door", "calculator", "calculator", "pencil"],
        styles = {
        "icon": {"font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "blue"}}
    )
 #MENU BERANDA       
if menu == "Beranda":
    st.markdown("<h1 style='text-align: center; color: #DB7093;'>KALKULATOR KIMIA ANALITIK</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h1 style='text-align: center; color: #DB7093;'>OLEH KELOMPOK 4</h1>", unsafe_allow_html=True)
    ki, te, kn = st.columns(3)
    with te:
        st.image("video_gif/merangkul.gif")
    left, mid, right = st.columns(3)
    with mid:   
        st.markdown('---')
        st.markdown('<div style="text-align: center;">Kalkulator Kimia Analitik. Dibuat untuk membantu perhitungan Analisis Gravimetri dan Analisis Titrimetri</div>', unsafe_allow_html=True)
        st.markdown('---')
        st.markdown('<h2 style="color: #DB7093; ">Cara Penggunaan Kalkulator:</h2>', unsafe_allow_html=True)
        st.markdown('---')
    st.markdown('<h3 style="color: #DB7093; ">Prosedur Penggunaan Kalkulator Gravimetri</h3>', unsafe_allow_html=True)
    st.markdown("""
        1. Akses Menu Gravimetri
          *Buka* halaman *web lab*. *Klik* tanda panah di pojok kiri atas pada tampilan awal.
          *Pilih dan klik* menu *Gravimetri*.
        2. Prosedur Berdasarkan Pilihan Opsi Analisis Silakan ikuti instruksi di bawah ini sesuai dengan jenis analisis yang Anda butuhkan:""")
    st.markdown(""" 
        *Opsi A: Perhitungan Kadar Air / Kadar Abu*
        1. *Masukkan* data bobot analit (gram) yang telah diketahui ke dalam kolom yang tersedia.
        2. *Masukkan* data bobot sampel (gram) yang telah diketahui.
        3. *Klik* tombol *Hitung Kadar* untuk memproses data.
        4. *Catat* hasil perhitungan yang muncul pada layar. 
        """)
    st.markdown("""
        *Opsi B: Perhitungan Kadar Sulfat / Kadar Besi / Kadar Ba*
        1. *Pilih* opsi faktor gravimetri yang sesuai dengan kebutuhan analisis Anda.
        2. *Masukkan* data bobot analit (gram) yang telah diketahui.
        3. *Masukkan* data bobot sampel (gram) yang telah diketahui.
        4. *Klik* tombol *Hitung Kadar* untuk memproses data.
        5. *Catat* hasil perhitungan yang muncul pada layar.
        """)
    st.markdown("""
        *Opsi C: Menu Custom (Kadar b/b atau Kadar b/v)**
        1. *Pilih* salah satu menu yang diinginkan: *Kadar b/b* atau *Kadar b/v*
        2. *Masukkan* nilai faktor gravimetri secara manual pada kolom yang disediakan.
        3. *Input* data bobot analit (gram).
        4. *Input* data bobot sampel (gram).
        5. *Klik* tombol *Hitung Kadar* untuk melihat hasil analisis.
        6. *Catat* hasil perhitungan yang muncul pada layar.
        """)
    
    st.markdown('---')
    st.markdown('<h3 style="color: #DB7093; ">Prosedur Penggunaan Kalkulator Titrimetri</h3>', unsafe_allow_html=True)
    st.markdown("""
        Prosedur Penggunaan Kalkulator Titrimetri
        1. Akses Menu Titrimetri
            *Buka halaman web lab*.
            *Klik* tanda panah di pojok kiri atas pada tampilan awal untuk membuka menu samping.
            *Pilih dan klik* menu *Titrimetri*.
         2. Prosedur Berdasarkan Pilihan Opsi Analisis
            Silakan ikuti instruksi di bawah ini sesuai dengan jenis menu titrimetri yang akan Anda gunakan:
        """)
    st.markdown("""
        *Opsi A: Menu Standardisasi*
        1. *Pilih* jenis larutan standar atau zat penstandardisasi pada kolom pilihan (data Berat Ekuivalen/BE akan muncul secara otomatis).
        2. *Masukkan* data bobot baku primer dalam satuan miligram (mg).
        3. *Masukkan* data faktor pengali atau faktor pengenceran sesuai dengan kebutuhan analisis.
        4. *Masukkan* data volume titran dalam satuan mililiter (mL).
        5. *Klik tombol Hitung Normalitas* untuk memproses data.
        6. *Catat* hasil perhitungan normalitas yang keluar pada layar.
        """)
    st.markdown("""
        *Opsi B: Menu Penetapan Kadar (Kadar Asetat, Kadar NaOH & Na2CO3, Kadar Besi, atau Kadar Klor)*
        *(Langkah-langkah di bawah ini berlaku sama untuk keempat jenis kadar tersebut)*
        1. *Pilih* jenis larutan kadar atau zat kadar pada kolom pilihan (data Berat Ekuivalen/BE akan muncul secara otomatis).
        2. *Masukkan* data Normalitas titran (N) yang telah diketahui.
        3. *Masukkan* data faktor pengali atau faktor pengenceran sesuai kebutuhan.
        4. *Masukkan* data volume titran (mL) hasil titrasi. *catatan: Pada penentuan kadar NaOH dan Na2CO3, volume akhir adalah volume total tanpa pengurangan volume awal)
        5. *Klik* tombol *Hitung Kadar* untuk memproses data.
        6. *Catat* hasil kadar akhir yang ditampilkan pada layar.
        """)
    st.markdown("""
        *Opsi C: Menu Kompleksometri (Standardisasi EDTA atau Penetapan Kesadahan)*
        *(Langkah-langkah di bawah ini berlaku sama untuk kedua menu kompleksometri)*
        1. *Pilih* berat molekul kalsium karbonat (CaCO3) pada kolom pilihan (data berat molekul akan muncul secara otomatis).
        2. *Masukkan* data bobot baku primer dalam satuan miligram (mg).
        3. *Masukkan* data faktor pengali atau faktor pengenceran sesuai kebutuhan.
        4. *Masukkan* data volume titran dalam satuan mililiter (mL).
        5. *Klik* tombol *Hitung Normalitas* untuk memproses data.
        6. *Catat* hasil perhitungan yang keluar pada layar.
        """)
    st.markdown("""
        *Opsi D: Menu Custom*
        Pilih salah satu dari 2 sub-menu *Custom* yang tersedia, lalu ikuti langkahnya:
        *Jika memilih Sub-Menu Standardisasi (Custom):*
        1. Masukkan nilai berat ekuivalen (mg/mgrek) secara manual pada kolom yang tersedia.
        2. Masukkandata bobot baku primer (mg).
        3. *Masukkan* data faktor pengali atau faktor pengenceran.
        4. *Masukkan* data volume titran (mL).
        5. *Klik* tombol *Hitung Normalitas* dan catat hasilnya.
        """)
    st.markdown("""
        *Jika memilih Sub-Menu Penetapan Kadar (Custom):*
        1. *Masukkan* nilai berat ekuivalen (mg/mgrek) secara manual.
        2. *Masukkan* data normalitas titran (N).
        3. *Masukkan* data faktor pengali atau faktor pengenceran.
        4. *Masukkan* data volume titran (mL) *Simplo*.
        5. *Masukkan* data volume titran (mL) *Duplo*.
        6. *Klik tombol Hitung Kadar* dan catat hasilnya.
        """)
#MENU GRAVIMETRI
elif menu == "Gravimetri":
    st.markdown("<h1 style='text-align: center; color: #DB7093;'>KALKULATOR ANALISIS GRAVIMETRI</h1>", unsafe_allow_html=True)
    st.markdown("---")
    kiri, tengah, kanan = st.columns(3)
    with tengah:
        st.image("video_gif/Gravimetri.gif")
    st.markdown("---")
    tab1, tab2, tab3, tab4, tab5, tabX = st.tabs(["Kadar Air", "Kadar Abu", "Kadar Sulfat", "Kadar Besi", "Kadar Ba", "Custom"])
    with tab1:
        st.image("gambar_gambar/air.jpeg")
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
            st.write(f"Kadar Air = {kadar_analit:.2f}%")
            st.success(f"Kadar Air adalah {kadar_analit:.2f}%")
            
    with tab2:
        st.image("gambar_gambar/kadar abu.jpeg")
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
            st.write(f"Kadar Abu = {kadar_analit:.2f}%")
            st.success(f"Kadar Abu adalah {kadar_analit:.2f}%")
    with tab3:
        st.image("gambar_gambar/sulfat.jpeg")
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
        st.image("gambar_gambar/fe.jpeg")
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
        st.image("gambar_gambar/ba.jpeg")
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
        st.markdown("---")
        tabQ, tabR =  st.tabs(["Kadar B/B", "Kadar B/v"])
        with tabQ:
            st.image("gambar_gambar/bperb.jpeg")
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
                st.write(f"Kadar b/b = {kadar_analit:.2f}", "%")
                st.success(f"Kadar b/b adalah {kadar_analit:.2f}%")
                
        with tabR:
            st.image("gambar_gambar/custom bperv.jpeg")
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
                st.write(f"Kadar b/v = {kadar_analit:.2f}", "b/v")
                st.success(f"Kadar b/v adalah {kadar_analit:.2f}b/v")
            
#MENU TITRIMETRI
elif menu == "Titrimetri":
    st.markdown("<h1 style='text-align: center; color: #DB7093;'>KALKULATOR ANALISIS TITRIMETRI</h1>", unsafe_allow_html=True)
    st.markdown("---")
    kir, teng, kan = st.columns(3)
    with teng:
        st.image("video_gif/Titrimetri.gif")
    st.markdown("---")
    tab6, tab7, tab8, tab9 = st.tabs(["Standarisasi", "Penetapan Kadar", "Kompleksometri", "Custom"])
    with tab6:
        st.image("gambar_gambar/standarisasi.jpeg")
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
        st.write(f"Berat Ekivalen = {berat_ekivalen:.0f}mg/mgrek")
        
        bobot_primer = st.number_input("Masukkan bobot baku primer (mg): ")
        fp =  st.number_input("Masukkan faktor pengali/pengenceran: ") 
        vol_titran =  st.number_input("Masukkan volume titran (mL): ")
        st.write(f"Bobot baku primer: {bobot_primer:.2f}mg")
        st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
        st.write(f"Volume titran: {vol_titran:.2f}mL")
        if st.button("Hitung Normalitas", key = "T1"):
            normalitas = standarisasi_asam_basa(bobot_primer, fp, vol_titran, berat_ekivalen)
            st.write(f"Normalitas = {normalitas:.4f}mgrek/mL")
            st.success(f"Normalitas adalah {normalitas:.4f}mgrek/mL")
        
    with tab7:
        st.markdown("---")
        tab10, tab11, tab12, tab13 = st.tabs(["Kadar Asetat", "Kadar NaOH dan Na2CO3", "Kadar Besi", "Kadar Klor"])
        with tab10:
            st.image("gambar_gambar/ch3cooh.jpeg")
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
            st.write(f"Berat Ekivalen = {berat_ekivalen:.0f}mg/mgrek")
        
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
            st.write(f"Normalitas titran: {Normalitas:.4f}N")
            st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
            st.write(f"Faktor Konversi: {fk:.2f}")
            st.write(f"Volume titran: {vol_titran:.2f}mL")
            st.write(f"Volume titrat: {volume_sampel:.2f}mL")
            
            if st.button("Hitung Kadar", key = "T10"):
                kadar_persen = kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                st.write(f"Kadar Persen =  {kadar_persen:.2f}%")
                st.success(f"Kadar Persen adalah {kadar_persen:.2f}%")
        with tab11:
            st.write("Kadar NaOH dan Na2CO3")
            tabA, tabB = st.tabs (["Kadar NaOH", "Kadar Na2CO3"])
            with tabA:
                st.image("gambar_gambar/naoh.jpeg")
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
                st.write(f"Berat Ekivalen = {berat_ekivalen:.0f}mg/mgrek")
            
                Normalitas = st.number_input(
                "Masukkan normalitas titran (N): ",
                min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="NA"
            )
                fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FPA")) 
                fk = 0.001
                a = st.number_input("Masukkan volume awal (a): (mL) ", key = ("AA")) 
                b = st.number_input("Masukkan volume akhir(b): (mL) ", key = ("BA")) 
                volume_sampel = st.number_input("Masukkan volume titrat (mL): ", key = ("VSA"))
                st.write(f"Normalitas titran: {Normalitas:.4f}mg")
                st.write(f"Volume Awal: {a:.2f}mL")
                st.write(f"Volume Akhir: {b:.2f}mL")
                st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
                st.write(f"Faktor Konversi: {fk:.2f}")
                st.write(f"Volume titrat: {volume_sampel:.2f}ml")
                
                if st.button("Hitung Kadar", key = "TA"):
                    kadar_persen = kadar_NaOH(a, b, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                    st.write(f"Kadar Persen NaOH = {kadar_persen:.2f}%")
                    st.success(f"Kadar Persen NaOH adalah {kadar_persen:.2f}%")
                
            with tabB:
                st.image("gambar_gambar/na2co3.jpeg")
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
                st.write(f"Berat Ekivalen = {berat_ekivalen:.0f}mg/mgrek")
            
                Normalitas = st.number_input(
                "Masukkan normalitas titran (N): ",
                min_value=0.0,
                step=0.0001,
                format="%.4f",
                key="NB"
            )
                fp = st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FPB")) 
                fk = 0.001
                a = st.number_input("Masukkan volume awal (a): (mL) ", key = ("AB")) 
                b = st.number_input("Masukkan volume akhir (b): (mL) ", key = ("BB")) 
                volume_sampel = st.number_input("Masukkan volume titrat (mL): ", key = ("VSB"))
                st.write(f"Normalitas titran: {Normalitas:.2f}N")
                st.write(f"Volume Awal: {a:.2f}mL")
                st.write(f"Volume Akhir: {b:.2f}mL") 
                st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
                st.write(f"Faktor Konversi: {fk:.2f}")
                st.write(f"Volume titrat: {volume_sampel:.2f}mL")
                
                if st.button("Hitung Kadar", key = "TB"):
                    kadar_persen = kadar_Na2CO3(b, a, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                    st.write(f"Kadar Persen Na2CO3 = {kadar_persen:.2f}%")
                    st.success(f"Kadar Persen Na2CO3 adalah {kadar_persen:.2f}%")

        with tab12:
            st.image("gambar_gambar/fe bperv.jpeg")
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
            st.write(f"Berat Ekivalen = {berat_ekivalen:.0f}mg/mgrek")
        
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
            st.write(f"Normalitas titran: {Normalitas:.2f}N")
            st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
            st.write(f"Faktor Konversi: {fk:.2f}")
            st.write(f"Volume titran: {volume_sampel:.2f}mL")
            
            if st.button("Hitung Kadar", key = "T12"):
                kadar_persen = kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                st.write(f"Kadar Persen = {kadar_persen:.2f}%")
                st.success(f"Kadar Persen adalah {kadar_persen:.2f}%")
                
        with tab13:
            st.image("gambar_gambar/cl.jpeg")
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
            st.write(f"Berat Ekivalen = {berat_ekivalen:.0F}mg/mgrek")
        
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
            st.write(f"Normalitas titran: {Normalitas:.4f}N")
            st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
            st.write(f"Faktor Konversi: {fk:.2f}")
            st.write(f"Volume titran: {vol_titran:.2f}mL")
            
            if st.button("Hitung Kadar", key = "T13"):
                kadar_persen = kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                st.write(f"Kadar Persen = {kadar_persen:.2f}%")
                st.success(f"Kadar Persen adalah {kadar_persen:.2f}%")    
    with tab8:
        st.markdown("---")
        tabC, tabD = st.tabs (["Standarisasi EDTA", "Penetapan Kesadahan"])
        with tabC:
            bm = {"Berat Molekul Kalsium Karbonat": 100,}
            selected_bm = st.selectbox(
                "Pilih Berat Molekul", list(bm.keys()), key = ("BMC"))
            berat_molekul = bm[selected_bm]
            st.write(f"Berat Molekul = {berat_molekul:.0f}mg/mmol")
                
            bobot_primer = st.number_input("Masukkan bobot baku primer (mg): ", key = ("BPC"))
            fp =  st.number_input("Masukkan faktor pengali/pengenceran: ", key = ("FPC")) 
            vol_titran =  st.number_input("Masukkan volume titran (mL): ", key = ("MC"))
            st.write(f"Bobot baku primer: {bobot_primer:.2f}mg")
            st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
            st.write(f"Volume titran: {vol_titran:.2f}mL")
            if st.button("Hitung Molaritas", key = "TC"):
                molaritas = standarisasi_edta(bobot_primer, fp, vol_titran, berat_molekul)
                st.write(f"Molaritas = {molaritas:.4f}mmol/mL")
                st.success(f"Molaritas adalah {molaritas:.4f}mmol/mL")
        
        with tabD:
            bm = {"Berat Molekul Kalsium Karbonat": 100,}
            selected_bm = st.selectbox(
                "Pilih Berat Molekul", list(bm.keys()), key = ("BMD"))
            berat_molekul = bm[selected_bm]
            st.write(f"Berat Molekul = {berat_molekul:.0f}mg/mmol")
        
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
            st.write(f"Molaritas titran: {Molaritas:.0f}mg/mmol")
            st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
            st.write(f"Volume titran: {volume_titran:.2f}mL")
            st.write(f"Volume titrat: {volume_sampel:.2f}L")
                     
            if st.button("Hitung Kadar", key = "TD"):
                kadar_kesadahan = kadar_kesadahan(volume_titran, Molaritas, berat_molekul, volume_sampel)
                st.write(f"Kadar Kesadahan = {kadar_kesadahan:.2f}mg/L")
                st.success(f"Kadar Kesadahan adalah {kadar_kesadahan:.2f}mg/L")
        
    with tab9:
        st.markdown("---")
        tabE, tabF= st.tabs (["Standarisasi ", "Penetapan Kadar"])
        with tabE:
            berat_ekivalen = st.number_input("Masukkan berat ekivalen (mg/mgrek): ",key = ("BEE"))
            st.write("Berat Ekivalen = ", berat_ekivalen, "mg/mgrek")
            bobot_primer = st.number_input("Masukkan bobot baku primer (mg): ",key = ("BPE"))
            fp =  st.number_input("Masukkan faktor pengali/pengenceran: ",key = ("FPE")) 
            vol_titran =  st.number_input("Masukkan volume titran (mL): ",key = ("VTE"))
            st.write(f"Bobot baku primer: {bobot_primer:.2f}mg")
            st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
            st.write(f"Volume titran: {vol_titran:.2f}mL")
            if st.button("Hitung Normalitas", key = "NE"):
                normalitas = standarisasi_asam_basa(bobot_primer, fp, vol_titran, berat_ekivalen)
                st.write(f"Normalitas = {normalitas:.4f}mgrek/mL")
                st.success(f"Normalitas adalah {normalitas:.4f}mgrek/mL")

        with tabF:
            berat_ekivalen = st.number_input("Masukkan berat ekivalen (mg/mgrek): ",key = ("BEF"))
            st.write(f"Berat Ekivalen = {berat_ekivalen:.4f}mg/mgrek")
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
            st.write(f"Normalitas titran: {Normalitas:.4f}N")
            st.write(f"Faktor pengali/pengenceran: {fp:.2f}")
            st.write(f"Faktor Konversi: {fk:.2f}")
            st.write(f"Volume titran: {vol_titran:.2f}mL")
            
            if st.button("Hitung Kadar", key = "TF"):
                kadar_persen = kadar_persen(vol_titran, Normalitas, berat_ekivalen, fk, fp, volume_sampel)
                st.write(f"Kadar Persen = {kadar_persen:.2f}%")
                st.success(f"Kadar Persen adalah {kadar_persen:.2f}%")
    
#MENU LATIHAN SOAL
elif menu == "Latihan Soal":
    st.set_page_config(
        page_title="Latihan Soal Analisis Gravimetri dan Analisis Titrimetri",
        page_icon="✏️",
        layout="centered"
    )
    
    # CSS Styling Latihan Soal
    st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            color: #8A9A86;
            margin-bottom: 10px;
        }
        .question-card {
            background-color: #EFECE2;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .explanation {
            background-color: #d4edda;
            border-left: 5px solid #28a745;
            border-radius: 8px;
            padding: 16px;
            margin-top: 16px;
        }
        .result-correct {
            background-color: #d4edda;
            color: #155724;
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
        }
        .result-wrong {
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
        }
        .score-card {
            background-color: #EFECE2;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin: 20px 0;
        }
        div.stButton > button {
            background-color: #8A9A86;
            color: white;
        }
        div.stButton > button:hover {
            background-color: #6d7a66;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Data soal
    questions = [
        {
            "question": "Sebuah sampel tepung terigu ditimbang untuk dianalisis kadar abunya menggunakan cawan porselen. Berdasarkan penimbangan diperoleh data sebagai berikut: <br> - Bobot cawan porselen kosong (W0) = 21,4530 g. <br> - Bobot cawan + sampel sebelum dipanaskan (W1) = 24,4530 g. <br>- ⁠Bobot cawan + abu setelah pemijaran hingga bobot tetap (W2) = 21,4680 g. <br> Berapakah persentase kadar abu dalam sampel tepung terigu tersebut?",
            "options": ["0,45%", "0,50%", "0,61%", "1,50%"],
            "answer": 1,
            "explanation": "% Kadar Abu = (W abu / W sampel) x 100% = (0,0150 g / 3,0000 g) x 100% = 0,50%"
        },
        {
            "question": "Sebanyak 25 mL sampel larutan garam barium diendapkan secara homogeneous-precipitation menggunakan kalium kromat (K2CrO4) dan urea. Setelah melalui proses penyaringan, pencucian, dan pengeringan dalam oven pada suhu 110°C, diperoleh endapan barium kromat (BaCrO4) dengan bobot tetap sebesar 0,5066 g. Berapakah kadar Barium dalam sampel tersebut?",
            "options": ["0,27% (b/v)", "1,10% (b/v)", "2,03% (b/v)", "5,50% (b/v)"],
            "answer": 1,
            "explanation": "% Kadar Ba = BA Ba / BM BaCrO4 x bobot endapan yang diperoleh g / volume sampel mL x 100% = 137 (g/mol) / 253 (g/mol) x 0,2746 g / 25 mL x 100%"
        },
        {
            "question": "Seorang analis akan menstadarisasi larutan KMnO4 0,1N menggunakan asam Oksalat (C2H2O4. 2H2O) sebanyak 0,315 g asam Oksalat dihidrat ditimbang, yang dilarutkan dalam air. Kemudian di pipet 25 mL ke erlenmeyer dan di tambah asam sulfat encer, dipanaskan hingga 70°C. Larutan tersebut kemudian dititrasi dengan KMn04 hingga tercapai titik akhir. berwarna merah muda yang stabil, sebanyak 25,10 mL. Hitunglah Normalitas KMnO4?",
            "options": ["0,0498 N", "0,0150 N", " 0,0973 N", "0,1004N"],
            "answer": 0,
            "explanation": "Normalitas KMnO4 = Massa Oksalat (g) / (BE x Volume KMnO4 (L)) = 0,07875 / (63 x 0,02510 L) ≈ 0,0498 N"
        },
        {
            "question": "Dalam sebuah analisis campuran NaOH dan Na2CO3 menggunakan metode Warder, sebanyak 25 mL sampel dititrasi dengan larutan standar HCl 0,1000 N. Pada titrasi tahap pertama dengan indikator fenolftalein (pp), warna merah muda tepat hilang setelah menghabiskan 15,00 mL asam (dianggap sebagai a). Ke dalam larutan yang sama kemudian ditambahkan indikator sindur metil (SM), dan titrasi dilanjutkan tanpa mengenolkan buret hingga warna berubah menjadi merah jingga yang konstan pada volume total buret 25,00 mL (dianggap sebagai b). Berapakah kadar NaOH dan Na2CO3 berturut-turut dalam satuan %(b/v)?",
            "options": ["0,07% b/v NaOH dan 0,42% b/v Na2CO3", "0,04% b/v NaOH dan 0,53% b/v Na2CO3", "0,08% b/v NaOH dan 0,42% b/v Na2CO3", "0,02% b/v NaOH dan 0,21% b/v Na2CO3"],
            "answer": 2,
            "explanation": "Kadar NaOH % (b/v) = (5,00 mL x 0,1000 N x 40) / (25 mL x 1000) x 100% = 0,08% <br> Kadar Na2CO3 % (b/v) = (20,00 mL x 0,1000 N x 53) / (25 mL x 1000) x 100% = 0,424% ≈ 0,42%"
        },
        {
            "question": "Sebanyak 25,00 mL sampel larutan garam besi(II) dipipet ke dalam Erlenmeyer, lalu ditambahkan asam sulfat 4N secukupnya. Larutan tersebut kemudian dititrasi dengan larutan standar KMnO4 0,0980N dalam kondisi dingin hingga muncul warna merah muda seulas yang persisten. Jika volume KMnO4 yang habis terbaca pada buret adalah 18,50 mL, berapakah kadar besi (Fe) dalam sampel tersebut dalam satuan %(b/v)?",
            "options": ["0,0810% b/v", "0,2025% b/v", "0,8100% b/v", "0,4050% b/v"],
            "answer": 3,
            "explanation": "% Fe = (V KMnO4 x N KMnO4 x BE Fe) / Volume sampel (mL)  x 0,001(g/mg) x 100% (b/v)"
        }
    ]
    
    # Session State
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "selected_answer" not in st.session_state:
        st.session_state.selected_answer = None
    if "quiz_finished" not in st.session_state:
        st.session_state.quiz_finished = False
    
    def reset_quiz():
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected_answer = None
        st.session_state.quiz_finished = False
    
    def check_answer(selected_idx):
        st.session_state.selected_answer = selected_idx
        st.session_state.answered = True
        
        if selected_idx == questions[st.session_state.current_question]["answer"]:
            st.session_state.score += 1
    
    def next_question():
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
            st.session_state.answered = False
            st.session_state.selected_answer = None
        else:
            st.session_state.quiz_finished = True
    
    # TAMPILAN UTAMA LATIHAN SOAL
    st.markdown('<div class="main-title">✏️ LATIHAN SOAL ANALISIS GRAVIMETRI DAN TITRIMETRI</div>', unsafe_allow_html=True)
    if st.session_state.quiz_finished:
        # Halaman Hasil Akhir
        st.markdown("---")
        
        score_percentage = (st.session_state.score / len(questions)) * 100
        
        st.markdown(f"""
        <div class="score-card">
            <h2 style="color: #8A9A86;">Hasil Latihan</h2>
            <h1 style="font-size: 3rem; color: #8A9A86;">{st.session_state.score} / {len(questions)}</h1>
            <p style="font-size: 1.2rem;">Skor: {score_percentage:.0f}%</p>
        </div>
        """, unsafe_allow_html=True)
        
        if score_percentage >= 80:
            st.success("🎉 luar biasa! Anda memahami dengan baik materi Analisis Gravimetri dan Titrimetri!")
        elif score_percentage >= 50:
            st.warning("📚 Cukup baik, tapi ada beberapa yang perlu dipelajari lagi!")
        else:
            st.error("💪 Semangat! Anda perlu belajar lebih lagi!")
        
        st.markdown("---")
        
        if st.button("🔄 Ulangi Latihan", use_container_width=True):
            reset_quiz()
            st.rerun()
    
    else:
        # Tampilan Soal
        current_idx = st.session_state.current_question
        q = questions[current_idx]
        
        st.markdown(f"**Soal {current_idx + 1} dari {len(questions)}**", unsafe_allow_html=True)
        st.progress((current_idx + 1) / len(questions))
        
        # Card Pertanyaan
        st.markdown(f"""
        <div class="question-card">
            <h3 style="color: #333; margin-bottom: 15px;">{q["question"]}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Opsi Jawaban
        for i, option in enumerate(q["options"]):
            if st.button(option, key=f"option_{current_idx}_{i}", use_container_width=True):
                check_answer(i)
                st.rerun()
        
        # Penjelasan (setelah menjawab)
        if st.session_state.answered:
            selected_idx = st.session_state.selected_answer
            correct_idx = q["answer"]
            
            if selected_idx == correct_idx:
                st.markdown(f"""
                <div class="result-correct">
                    ✅ <strong>Benar!</strong> Jawaban Anda benar.
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-wrong">
                    ❌ <strong>Salah!</strong> Jawaban yang benar adalah: {q["options"][correct_idx]}
                </div>
                """, unsafe_allow_html=True)
            
            # Penjelasan Jawaban
            st.markdown(f"""
            <div class="explanation">
                <strong>📝 Penjelasan:</strong><br>
                {q["explanation"]}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            if st.button("➡️ Soal Berikutnya", use_container_width=True):
                next_question()
                st.rerun()
    
    st.markdown("---")




    

