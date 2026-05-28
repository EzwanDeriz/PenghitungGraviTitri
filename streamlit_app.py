import streamlit as st
import math 

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

with st.sidebar:
    selected = option_menu(
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


#WEB PENGHITUNG KADAR ANALIT PADA GRAVIMETRI DAN TITRIMETRI
#PERHITUNGAN KADAR AIR DALAM TEPUNG
def perhitungan_kadar_air_tepung(bobot_analit, bobot_sampel):
    kadar_analit = bobot_analit / bobot_sampel * 100
    return kadar_analit 


#PERHITUNGAN KADAR ABU DALAM TEPUNG
def perhitungan_kadar_abu_tepung(bobot_analit, bobot_sampel):
    kadar_analit = bobot_analit / bobot_sampel * 100
    return kadar_analit


#PERHITUNGAN KADAR SULFAT DALAM GARAM GLAUBER
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



#STANDARISASI NaOH
def standarisasi_asam_basa(bobot_primer, fp, vol_titran, BE):
    normalitas = bobot_primer / (fp * vol_titran * BE)
    return normalitas


#STANDARISASI HCL 
def standarisasi_asam_basa(bobot_primer, fp, vol_titran, BE):
    normalitas = bobot_primer / (fp * vol_titran * BE)
    return normalitas 


#PERHITUNGAN KADAR ASAM ASETAT DALAM CUKA 
def kadar_asam_asetat(volume_titran, Normalitas, BE, fk, fp, volume_sampel):
    kadar_persen = volume_titran * Normalitas * BE * fk * fp * 100 / volume_sampel
    return kadar_persen


#PENETAPAN KADAR Na2CO3 DALAM WARDER
def kadar_Na2CO3(b, a, Normaitas, BE, fk, fp, volume_sampel):
    kadar_persen = 2 * (b-a) * Normalitas * BE * fk * fp * 100 / volume_sampel
    return kadar_persen 


#PENETAPAN KADAR NaOH DALAM WARDER 
def kadar_NaOH(a, b, Normalitas, BE, fk, fp, volume_sampel):
    kadar_persen = ((2*a)-b) * Normalitas* BE * fk * fp * 100 / volume_sampel
    return kadar_persen


#STANDARISASI LARUTAN KMnO4 
def standarisasi_KMnO4(bobot_primer, fp, vol_titran, BE):
    normalitas = bobot_primer / (fp * vol_titran * BE)
    return normalitas


#PENETAPAN KADAR BESI 
def kadar_besi(volume_titran, Normalitas, BE, fk, fp, volume_sampel):
    kadar_persen = volume_titran * Normalitas * BE * fk * fp * 100 / volume_sampel
    return kadar_persen


#STANDARISASI LARUTAN TIOSULFAT 
def standarisasi_tio(bobot_primer, fp, vol_titran, BE):
    normalitas = bobot_primer / (fp * vol_titran * BE)
    return normalitas 


#PENETAPAN KADAR KLOR IODOMETRI 
def kadar_klor(volume_titran, Normalitas, BE, fk, fp, volume_sampel):
    kadar_persen = volume_titran * Normalitas * BE * fk * fp * 100 / volume_sampel 
    return kadar_persen 


#PENETAPAN KADAR KLOR ARGENTOMETRI
def kadar_klor(volume_titran, Normalitas, BE, fk, fp, volume_sampel):
    kadar_persen = volume_titran * Normalitas * BE * fk * fp * 100 / volume_sampel 
    return kadar_persen 


#STANDARISASI LARUTAN EDTA
def standarisasi_edta(bobot_primer, fp, vol_titran, BM):
    molaritas = bobot_primer / (fp * vol_titran * BM)
    return molaritas 


#PENETAPAN KESADAHAN JUMLAH DALAM SAMPEL AIR KOMPLEKSOMETRI EDTA 
def kadar_kesadahan(volume_titran, Molaritas, BM, volume_sampel):
    kadar_ppm = volume_titran * Molaritas * BM / volume_sampel
    return kadar_ppm 


bobot_analit = st.number_input("Masukkan bobot analit (g): ")
bobot_sampel = st.number_input("Masukkan bobot sampel (g): ")
BM_analit = st.number_input("Masukkan BM Analit (g/mol): ")
BM_sampel = st.number_input("Masukkan BM sampel (g/mol): ")
faktor_gravi = BM_analit / BM_sampel
perbandingan_bobot = bobot_analit / bobot_sampel
st.write("Bobot analit: ", bobot_analit, "g") 
st.write("Bobot sampel: ", bobot_sampel, "g")
st.write("Faktor Gravimetri: ", faktor_gravi)


