#Meme word dictionary
meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "BRB": "Singkatan dari 'Be Right Back', artinya sebentar lagi kembali",
            "OMG": "Singkatan dari 'Oh My God', ungkapan keterkejutan atau heran",
            "ROFL":  "tanggapan terhadap lelucon",
            "SHEESH":  "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah"
            }

word = input("Ketikkan kata yang tidak kalian Mengerti!").upper()

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("Word Found! Meaning:", meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("Word not found!")
