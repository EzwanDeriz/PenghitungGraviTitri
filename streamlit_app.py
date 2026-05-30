import streamlit as st
import math

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

#WEB PENGHITUNG KADAR ANALIT PADA GRAVIMETRI DAN TITRIMETRI
#PERHITUNGAN KADAR AIR DALAM TEPUNG
def perhitungan_kadar_air_tepung(bobot_analit, bobot_sampel):
    kadar_analit = bobot_analit / bobot_sampel * 100
    return kadar_analit 


#PERHITUNGAN KADAR ABU DALAM TEPUNG
def perhitungan_kadar_abu_tepung(bobot_analit, bobot_sampel):
    kadar_analit = bobot_analit / bobot_sampel * 100
    return kadar_analit


#PERHITUNGAN KADAR SULFAT DALAM GARAM GLAUberat_ekivalenR
def perhitungan_kadar_sulfat_glauber(faktor_gravi, bobot_analit, bobot_sampel):
    kadar_analit = faktor_gravi * (bobot_analit / bobot_sampel) * 100
    return kadar_analit


#PERHITUNGAN KADAR BESI DALAM GARAM BESI
def perhitungan_kadar_besi(faktor_gravi, bobot_analit, bobot_sampel):
    kadar_analit = faktor_gravi * (bobot_analit / bobot_sampel) * 100
    return kadar_analit


#PERHITUNGAN KADAR BARIUM SEBAGAI BaCrO4
def perhitungan_kadar_barium(faktor_gravi, bobot_analit, vol_sampel):
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


with st.sidebar:
        menu = {
            "Beranda",
            "Gravimetri",
            "Titrimetri", 
            "Bahaya Bahan Kimia",
            "Latihan Soal",
            "Tentang Aplikasi"
        }
    selected_menu = st.selectbox(
        "Pilih Menu", list(fg.keys()))
        

if selected == "Beranda":
    st.write("SELAMAT DATANG WOY")

elif selected == "Gravimetri":
    st.write("INI GRAVIMETRI WOY")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kadar Air", "Kadar Abu", "Kadar Sulfat", "Kadar Besi", "Kadar Ba"])
    with tab1:
        st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
    with tab2:
        st.dataframe({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with tab3:
        st.checkbox("Show gridlines")
    with tab4:
        st.write("Bansos")
        fg = {
        "Ar Sulfat / Mr Barium Sulfat": 96/233,
        "2 Ar Besi / Mr Besi (iii) Oksida": 112/160,
        "Ar Barium / Mr Barium Kromat": 137/253
        }
        selected_fg = st.selectbox(
            "Pilih Faktor Gravimetri", list(fg.keys()))
        faktor_gravi = fg[selected_fg]
        st.write("Faktor Gravimetri = ", round(faktor_gravi, 4))
        
        bobot_analit = st.number_input("Masukkan bobot analit (g): ")
        bobot_sampel = st.number_input("Masukkan bobot sampel (g): ")
        st.write("Bobot analit: ", round(bobot_analit, 4), "g") 
        st.write("Bobot sampel: ", round(bobot_sampel, 4), "g")
        
        if st.button("Hitung Kadar", key = "T1"):
            kadar_analit = perhitungan_kadar_besi(faktor_gravi, bobot_analit, bobot_sampel)
            st.write("Kadar Besi = ", round(kadar_analit, 4))
            st.success(f"Kadar Besi adalah {kadar_analit:.2f}%")

    
    with tab5:
        st.write("Bansosss")
        

elif selected == "Titrimetri":
    st.write("INI TITRIMETRI WOY")
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
    st.write("Bobot baku primer: ", round(bobot_primer, 4), "mg")
    st.write("Faktor pengenceran: ", fp)
    st.write("Volume titran: ", round(vol_titran, 2), "mL")
    
    
    if st.button("Hitung Normalitas", key = "G1"):
        normalitas = standarisasi_asam_basa(bobot_primer, fp, vol_titran, berat_ekivalen)
        st.write("Normalitas = ", round(normalitas, 4))

elif selected == "Bahaya Kimia":
    st.write("INI BAHAYA BAHAN KIMIA WOY")

elif selected == "Latihan Soal":
    st.write("INI LATSOL WOY")






    st.success(f"Normalitas adalah {round(normalitas, 4)} mgrek/mL")

