import openai

# Função para interagir com o modelo de linguagem
def interagir_com_modelo(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        log_level="info"
    )
    return response.choices[0].text.strip()

def conversa_interativa():
    print("Bem-vindo! Você pode começar a fazer perguntas ou digitar 'sair' para encerrar.")

    while True:
        pergunta = input("Usuário: ")

        if pergunta.lower() == "sair":
            print("Até logo!")
            break

        prompt = f"Usuário: {pergunta}\nModelo:"
        resposta = interagir_com_modelo(prompt)
        print("Modelo:", resposta)

# Executar a conversa interativa
conversa_interativa()
