# cliinformationretrievaldemo-2217051082
UAS Temu Kembali Informasi 2026 UNILA

Tema: Cari kata kunci umum (tidak spesialisasi)

Gantikan 
folder_path = 'D:/UASTKI/documents'


di dalam 


folder_path = 'D:/UASTKI/documents'
docs = []
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        doc = file.read()
        docs.append(doc)

ke direktori dimana folder documents berada di clone/salinan yang telah diunduh

Presentasi: https://drive.google.com/file/d/1YnbYs4YXkzYd_wo20YJER0PdWsRToTk3/view?usp=sharing
