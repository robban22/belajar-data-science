print("Halo, saya memulai perjalanan menjadi Data Science / ML Enginer!")

nama = "Robban"
umur = 25
IPK = 3.75
Status_Mahasiswa = True
visi = "Menjadi Data Scientist / ML Enginer yang handal dan profesional"

# List
makanan_faforit = ["Nasi Goreng", "Sate", "Bakso", "Soto", "Rendang"]
# Tuple
ukuran_laptop = (1920, 1080)
#dictionary
orang = {
    "nama": nama,
    "umur": umur,
    "hobi" : ["Membaca", "Bermain Gitar", "Bermain Catur"],
    "cita_cita": "Menjadi Data Scientist / ML Enginer yang handal dan profesional"
}

#percabangan
#Buat program yang mengecek apakah umur Anda ≥ 18.
if umur >= 18:
    print("Anda sudah dewasa")
else:
    print("Anda belum dewasa")

#looping 1 sampai 10
for i in range(1, 11):
    print(i)

#fungsi menerima nama
def sapa(nama):
    return f"Halo {nama}, selamat belajar data science!"
print(sapa(nama))
