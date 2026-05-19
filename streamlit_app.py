import streamlit as st

st.title("🎈 Bismillah Lesgow ")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

#WEB PENGHITUNG KADAR ANALIT PADA GRAVIMETRI DAN TITRIMETRI
"""GRAVIMETRI"""
#PERHITUNGAN KADAR AIR DALAM TEPUNG
def perhitungan_kadar_air_tepung(bobot_analit, bobot_sampel):
    kadar_analit = bobot_analit / bobot_sampel * 100
    return kadar_analit 


#PERHITUNGAN KADAR ABU DALAM TEPUNG
def perhitungan_kadar_abu_tepung(bobot_analit, bobot_sampel):
    kadar_analit = bobot_analit / bobot_sampel * 100
    return kadar_analit


#PERHITUNGAN KADAR SULFAT DALAM GARAM GLAUBER
def perhitungan_kadar_sulfat_glauber(faktor_gravi, perbandingan_bobot):
    kadar_analit = faktor_gravi * perbandingan_bobot * 100
    return kadar_analit


#PERHITUNGAN KADAR BESI DALAM GARAM BESI
def perhitungan_kadar_besi(faktor_gravi, perbandingan_bobot):
    kadar_analit = faktor_gravi * perbandingan_bobot * 100
    return kadar_analit


#PERHITUNGAN KADAR BARIUM SEBAGAI BaCrO4
def perhitungan_kadar_barium(faktor_gravi, bobotpervolume):
    kadar_analit = faktor_gravi * bobotpervolume * 100
    return kadar_analit 


"""TITRIMETRI"""
#STANDARISASI NaOH
def standarisasi_asam_basa(bobot_primer, pembagi):
    normalitas = bobot_primer / pembagi
    return normalitas


#STANDARISASI HCL 
def standarisasi_asam_basa(bobot_primer, pembagi):
    normalitas = bobot_primer / pembagi
    return normalitas 


#PERHITUNGAN KADAR ASAM ASETAT DALAM CUKA 
def kadar_asam_asetat(volume_titran, N_NaOH, BE, fk, fp, volume_sampel):
    kadar_persen = volume_titran * N_NaOH * BE * fk * fp * 100 / volume_sampel
    return kadar_persen


#PENETAPAN KADAR Na2CO3 DALAM WARDER
def kadar_Na2CO3(b, a, N_HCL, BE, fk, fp, volume_sampel):
    kadar_persen = 2 * (b-a) * N_HCL * BE * fk * fp * 100 / volume_sampel
    return kadar_persen 


#PENETAPAN KADAR NaOH DALAM WARDER 
def kadar_NaOH(a, b, N_HCL, BE, fk, fp, volume_sampel):
    kadar_persen = ((2*a)-b) * N_HCL* BE * fk * fp * 100 / volume_sampel
    return kadar_persen


#STANDARISASI LARUTAN KMnO4 
def standarisasi_KMnO4(bobot_primer, pembagi):
    normalitas = bobot_primer / pembagi
    return normalitas


#PENETAPAN KADAR BESI 
def kadar_besi(volume_titran, N_KMnO4, BE, fk, fp, volume_sampel):
    kadar_persen = volume_titran * N_KMnO4 * BE * fk * fp * 100 / volume_sampel
    return kadar_persen


#STANDARISASI LARUTAN TIOSULFAT 
def standarisasi_tio(bobot_primer, pembagi):
    normalitas = bobot_primer / pembagi 
    return normalitas 


#PENETAPAN KADAR KLOR IODOMETRI 
def kadar_klor(volume_titran, N_tio, BE, fk, fp, volume_sampel):
    kadar_persen = volume_titran * N_tio * BE * fk * fp * 100 / volume_sampel 
    return kadar_persen 


#PENETAPAN KADAR KLOR ARGENTOMETRI
def kadar_klor(volume_titran, N_tio, BE, fk, fp, volume_sampel):
    kadar_persen = volume_titran * N_tio * BE * fk * fp * 100 / volume_sampel 
    return kadar_persen 


#STANDARISASI LARUTAN EDTA
def standarisasi_edta(bobot_primer, pembagi):
    molaritas = bobot_primer / pembagi
    return molaritas 


#PENETAPAN KESADAHAN JUMLAH DALAM SAMPEL AIR KOMPLEKSOMETRI EDTA 
def kadar_kesadahan(volume_titran, M_EDTA, BM, volume_sampel):
    kadar_ppm = volume_titran * M_EDTA * BM / volume_sampel
    return kadar_ppm 


"""VARIABEL GRAVIMETRI"""
bobot_analit = float(input("Masukkan bobot analit (g): "))
bobot_sampel = float(input("Masukkan bobot sampel (g): ")) 
BM_analit = float(input("Masukkan BM Analit (g/mol): "))
BM_sampel = float(input("Masukkan BM sampel (g/mol): "))
faktor_gravi = BM_analit / BM_sampel
perbandingan_bobot = bobot_analit / bobot_sampel
st.write("Bobot analit: ", bobot_analit, "g") 
st.write("Bobot sampel: ", bobot_sampel, "g")
st.write("Faktor Gravimetri: ", faktor_gravi)


