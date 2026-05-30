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



#STANDARISASI ASAM BASA
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


bobot_primer = st.number_input("Masukkan bobot baku primer (mg)")
fp =  st.number_input("Masukkan faktor pengali") 
vol_titran =  st.number_input("Masukkan volume titran (mL)")
be = {
    "BE Asam Oksalat": 63,
    "BE Boraks": 190,
    "BE Kalium Dikromat": 49,
}
selected_be = st.selectbox(
    "Pilih Berat Ekivalen", list(be.keys()))
BE = be[selected_be]
st.write("Berat Ekivalen = ", BE, "mg/mgrek")

if st.button("Hitung Normalitas", key = "H1"):
    normalitas = standarisasi_asam_basa(bobot_primer, fp, vol_titran, BE)
    st.write("Normalitas = ", round(normalitas, 4))
    st.success(f"Normalitas adalah {round(normalitas, 4)} mgrek/mL")
