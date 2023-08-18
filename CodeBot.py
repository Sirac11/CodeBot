#Bu sistem basit programlar yapmak için kullanılabilir.
#Program sadece inglizce kullanılır.
#Oluşan çıktıların ChatGpt'den kaynaklı mesajları temizledikten sonra kullanabilirsiniz.


import openai

openai.api_key = "Api-Key"  # OpenAI API anahtarınızı buraya ekleyin

for i in range(0, 100):
    dosya_adı = input("\033[1;33mPlease enter the filename (example: file.py): \033[0m")
    dosya_icerigi = input("\033[1;33mPlease enter the file contents: \033[0m")
    
    messages = [
        {"role": "system", "content": "\033[1;34mCreating file...\033[0m"},
        {"role": "user", "content": dosya_icerigi}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    cevap_metni = response.choices[0].message["content"]

    with open(dosya_adı, "w") as dosya:
        dosya.write(cevap_metni)

    print(f"{dosya_adı} The program you want has been created.")

    karar = input("\033[1;31m!!!Press return if you want to continue, press 'e' if you want to Exit!!!\033[0m")

    if karar == 'e':
        break
        
