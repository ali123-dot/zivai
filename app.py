import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def gpt_ile_icerik_uret(konu):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Youtube videosu için etkileyici başlık, açıklama ve etiketler oluştur. Konu: {konu}",
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

st.title("YouTube İçerik Önerici - GPT Destekli")

konu = st.text_input("İçerik konusunu yazınız:")

if konu:
    with st.spinner("Öneriler hazırlanıyor..."):
        içerik = gpt_ile_icerik_uret(konu)
    st.markdown("### Önerilen İçerik")
    st.write(içerik)
    
