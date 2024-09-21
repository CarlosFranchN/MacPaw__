from flask import Flask, render_template

app = Flask(__name__)

def wsgi_handler(environ, start_response):
    return app(environ, start_response)


@app.route("/")
def index():
    products = [
        {"link": "cleanmymac-x", "title": "CleanMyMac X"},
        {"link": "cleanmyphone", "title": "Clean My®Phone"},
        {"link": "moonlock", "title": "Moonlock"},
        {"link": "clearvpn", "title": "ClearVPN"},
        {"link": "cleanmypc", "title": "CleanMy®PC"},
        {"link": "setapp", "title": "Setapp"},
        {"link": "gemini", "title": "Gemini 2"},
        {"link": "the-unarchiver", "title": "The Unarchiver"},
        {"link": "wallpaper-wizard", "title": " Wallpaper Wizard2"},
        {"link": "encrypto", "title": "Encrypto"},
    ]

    review = [
        {"name": "Forbes", "id": "48f7e78b6ec2f2b8a52804145ddf5dba"},
        {"name": "MacStories", "id": "076595afcbe3e459fb1d508ca95eac4c"},
        {"name": "CultofMac", "id": "d9fc98f9ad609f61b2126daeecf7e99b"},
        {"name": "TechCrunch", "id": "348d8e02ce3f15de4ac82f9813949466"},
        {"name": "iDownloadBlog", "id": "6c83479971bf9d42f3a99ea0b4613a58"},
    ]

    context = {
        "review": review,
        "range_reviews": range(len(review)),  # Aqui você passa o range
    }

    cmmx_containers = [
        {
            "theme": "Limpeza",
            "title": "Libere seu espaço digital",
            "text": "O CleanMyMac X busca lixo em todos os cantos do macOS. Ele limpa arquivos desnecessários, como caches desatualizados, downloads incompletos, registros e traduções inúteis. Você pode remover toneladas de acúmulos escondidos no iTunes, Mail e Fotos, além de localizar gigabytes de arquivos ocultos. As ferramentas de limpeza do CleanMyMac eliminam o peso extra em segundos.",
            "link": "mac-cleanup",
            "action": "Limpar",
        },
        {
            "theme": "Velocidade",
            "title": "Faça mais em um Mac mais rápido",
            "text": "Para cada vez que o Mac engasgar, você pode contar com um arsenal de ferramentas de aceleração: libere a RAM, execute scripts de manutenção, e gerencie Itens de Início, Agentes Iniciais e Aplicativos Travados. Assim, você diminui a carga do sistema e ajusta o desempenho do Mac ao máximo. Quando a sua máquina é produtiva, você também produz mais.",
            "link": "mac-speedup",
            "action": "Acelerar",
        },
        {
            "theme": "Proteção",
            "title": "Alguém precisa proteger o seu Mac",
            "text": "Há vírus no Mac? Não no seu, se você o limpa com o CleanMyMac X. Sua tecnologia antimalware (o Mecanismo Moonlock) criada pela equipe da MacPaw, combate malware, adware, ransomware e todos os outros “wares” que existem para macOS. Ao encontrar algo suspeito, o app o apaga imediatamente. O banco de dados de malware é atualizado regularmente para que você sempre possa contar com os recursos de proteção do CleanMyMac X.",
            "link": "mac-protection",
            "action": "Proteger",
        },
        {
            "theme": "Gerenciamento de aplicativos",
            "title": "Tenha controle total sobre os seus apps",
            "text": "Para deixar o Mac em ordem, você dispõe da dupla dinâmica Desinstalador e Atualizador. O primeiro remove apps desnecessários por completo e o segundo atualiza automaticamente todo o software. Apps ruins vão embora e novos apps chegam sempre a tempo. Isso ajuda a evitar conflitos em apps e deixa o Mac sempre em dia.",
            "link": "mac-application-management",
            "action": "Gerenciar",
        },
    ]

    business_link = [
        {
            "link": "cleanmymac-for-business",
            "icon": "business.svg?id=79a1f47eacdfb7cba9035210be9ac1d9",
            "text": "CleanMyMac X para Empresas",
        },
        {
            "link": "educational-discount",
            "icon": "education.svg?id=11f6cba5e988cf25ec84cf7751151233",
            "text": "CleanMyMac X para Educação",
        },
    ]
    reviews_quotes = [
        {
            "especialista": "Forbes",
            "quote": "Uso semanalmente o CleanMyMac X no meu Mac mini com M2 Pro para garantir que tudo funcione bem, ficar de olho em softwares duvidosos e recuperar o espaço purgável em disco. Eu sei que poderia fazer algumas dessas coisas manualmente no Terminal, mas o processo é muito mais rápido via software e poupa tempo. O CleanMyMac X também é útil para desinstalar e atualizar softwares.",
            "author": "Mark Sparrow",
        },
        {
            "especialista": "MacStories",
            "quote": "Uso o CleanMyMac há muitos anos e continuo me impressionando a cada atualização. Sem dúvida, a versão deste ano é a melhor já feita. Altamente recomendado.",
            "author": "Bryan M. Wolfe",
        },
        {
            "especialista": "Cult of Mac",
            "quote": "O CleanMyMac X ajuda a remover arquivos desnecessários e identifica aquilo que está deixando o computador lento.",
            "author": "Romain Dilelt",
        },
        {
            "especialista": "Tech Crunch",
            "quote": "Seu Mac está em forma? Essa tarefa não precisa ser difícil. O CleanMyMac oferece todas as ferramentas que você precisa para garantir uma máquina sempre veloz e segura.",
            "author": "Killian Bell",
        },
        {
            "especialista": "iDownloadBlog",
            "quote": "Uso semanalmente o CleanMyMac X no meu Mac mini com M2 Pro para garantir que tudo funcione bem, ficar de olho em softwares duvidosos e recuperar o espaço purgável em disco. Eu sei que poderia fazer algumas dessas coisas manualmente no Terminal, mas o processo é muito mais rápido via software e poupa tempo. O CleanMyMac X também é útil para desinstalar e atualizar softwaresSe você já passou pela situação de ter um Mac quase cheio, confira o CleanMyMac X. Há anos, ele tem sido uma excelente forma de recuperar espaço com pouquíssimo esforço.",
            "author": "John Voorhees",
        },
    ]

    indo_info = [
        {
            "icon": '<svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M176 24c0-13.3-10.7-24-24-24s-24 10.7-24 24l0 40c-35.3 0-64 28.7-64 64l-40 0c-13.3 0-24 10.7-24 24s10.7 24 24 24l40 0 0 56-40 0c-13.3 0-24 10.7-24 24s10.7 24 24 24l40 0 0 56-40 0c-13.3 0-24 10.7-24 24s10.7 24 24 24l40 0c0 35.3 28.7 64 64 64l0 40c0 13.3 10.7 24 24 24s24-10.7 24-24l0-40 56 0 0 40c0 13.3 10.7 24 24 24s24-10.7 24-24l0-40 56 0 0 40c0 13.3 10.7 24 24 24s24-10.7 24-24l0-40c35.3 0 64-28.7 64-64l40 0c13.3 0 24-10.7 24-24s-10.7-24-24-24l-40 0 0-56 40 0c13.3 0 24-10.7 24-24s-10.7-24-24-24l-40 0 0-56 40 0c13.3 0 24-10.7 24-24s-10.7-24-24-24l-40 0c0-35.3-28.7-64-64-64l0-40c0-13.3-10.7-24-24-24s-24 10.7-24 24l0 40-56 0 0-40c0-13.3-10.7-24-24-24s-24 10.7-24 24l0 40-56 0 0-40zM160 128l192 0c17.7 0 32 14.3 32 32l0 192c0 17.7-14.3 32-32 32l-192 0c-17.7 0-32-14.3-32-32l0-192c0-17.7 14.3-32 32-32zm192 32l-192 0 0 192 192 0 0-192z"/></svg>',
            "title": "Requisitos do Sistema:",
            "content": "macOS 10.13 e superior, 210 MB",
        },
        {
            "icon": '<svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"/></svg>',
            "title": "Avaliação :",
            "content": "",
        },
        {
            "icon": '<svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M0 80L0 229.5c0 17 6.7 33.3 18.7 45.3l176 176c25 25 65.5 25 90.5 0L418.7 317.3c25-25 25-65.5 0-90.5l-176-176c-12-12-28.3-18.7-45.3-18.7L48 32C21.5 32 0 53.5 0 80zm112 32a32 32 0 1 1 0 64 32 32 0 1 1 0-64z"/></svg>',
            "title": "Preço:",
            "content": "a partir de $34.95",
        },
        {
            "icon": '<svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM216 336l24 0 0-64-24 0c-13.3 0-24-10.7-24-24s10.7-24 24-24l48 0c13.3 0 24 10.7 24 24l0 88 8 0c13.3 0 24 10.7 24 24s-10.7 24-24 24l-80 0c-13.3 0-24-10.7-24-24s10.7-24 24-24zm40-208a32 32 0 1 1 0 64 32 32 0 1 1 0-64z"/></svg>',
            "title": "Versão mais recente:",
            "content": "4.15.6, 7 agosto 2024",
        },
    ]

    footer_accordion_itens = [
        {
            "title": "Produtos",
            "list": [
                {"link": "https://macpaw.com/cleanmymac", "content": "CleanMyMac X"},
                {"link": "https://macpaw.com/cleanmyphone","content": "CleanMy®Phone"},
                {"link": "https://macpaw.com/moonlock", "content": "Moonlock"},
                {"link": "https://macpaw.com/clearvpn", "content": "ClearVPN"},
                {"link": "https://macpaw.com/cleanmypc", "content": "CleanMy® PC"},
                {"link": "https://setapp.com/", "content": "Setapp"},
                {"link": "https://macpaw.com/pt/gemini", "content": "Gemini 2"},
                {"link": "https://macpaw.com/the-unarchiver","content": "The Unarchiver"},
                {"link": "https://macpaw.com/encrypto", "content": "Encrypto"}
            ],
        },
        {
            "title": "Popular",
            "list": [
                {
                    "link": "https://macpaw.com/pt/how-to/fix-mac-running-slow",
                    "content": "Mac Lento",
                },
                {
                    "link": "https://macpaw.com/pt/how-to/speed-up-mac",
                    "content": "Acelere o Mac",
                },
                {
                    "link": "https://macpaw.com/pt/how-to/best-mac-cleaner-software",
                    "content": "Soluções para Limpeza do Mac",
                },
                {
                    "link": "https://macpaw.com/pt/how-to/clear-system-storage-mac",
                    "content": "ClearVPN",
                },
                {
                    "link": "https://macpaw.com/cleanmypc",
                    "content": "Reduza os Dados do Sistema",
                },
                {
                    "link": "https://macpaw.com/pt/how-to/clean-up-other-storage-on-mac",
                    "content": "Limpe o Armazenamento 'Outro'",
                },
                {
                    "link": "https://macpaw.com/pt/how-to/uninstall-apps-on-mac-os-x",
                    "content": "Desisntale Apps no Mac",
                },
                {
                    "link": "https://macpaw.com/pt/how-to/uninstall-apps-on-mac-os-x",
                    "content": "Limpe o Mac",
                },
                {
                    "link": "https://macpaw.com/pt/how-to/remove-viruses-malware-from-mac",
                    "content": "Remova Malware e Vírus",
                },
            ],
        },
        {
            "title": "Empresa",
            "list": [
                {"link": "https://macpaw.com/about", "content": "Sobre a MacPaw"},
                {
                    "link": "https://macpaw.com/cleanmymac/review",
                    "content": "Tutoriais da MacPaw",
                },
                {"link": "https://macpaw.com/pt/blog", "content": "Blog da MacPaw"},
                {
                    "link": "https://macpaw.com/affiliate",
                    "content": "Programa de Afiliação",
                },
                {
                    "link": "https://macpaw.com/reseller-offers",
                    "content": " Ofertas para Revenda",
                },
                {
                    "link": "https://macpaw.com/press",
                    "content": "Assessoria de Imprensa",
                },
                {"link": "https://macpaw.com/careers", "content": "Carreiras"},
                {"link": "https://macpaw.com/legal", "content": "Legal"},
            ],
        },
        {
            "title": "Suporte",
            "list": [
                {
                    "link": "https://my.macpaw.com/?svn=685397284.1725132023",
                    "content": "Conta",
                },
                {
                    "link": "https://macpaw.com/pt/support/contact",
                    "content": "Contatar Suporte",
                },
                {
                    "link": "https://macpaw.com/pt/support/cleanmymac/knowledgebase",
                    "content": "Base de Conhecimento",
                },
                {
                    "link": "https://macpaw.com/pt/support/license-retrieval",
                    "content": "Gerenciamento de Licenças",
                },
                {
                    "link": "https://macpaw.com/pt/support/cleanmymac/knowledgebase/discounts",
                    "content": "Cupons do CleanMyMac",
                },
                {
                    "link": "https://macpaw.com/pt/support/cleanmymac/knowledgebase/get-activation-number",
                    "content": "Número de Ativação",
                },
                {
                    "link": "https://macpaw.com/pt/support/cleanmymac/knowledgebase/uninstaller",
                    "content": "Desinstalação de Apps",
                },
                {
                    "link": "https://macpaw.com/pt/support/report-malware",
                    "content": "Enviar Malware CArlos",
                },
            ],
        },
    ]

    return render_template(
        "index.html",
        products=products,
        review=context,
        cmmx_containers=cmmx_containers,
        busines_links=business_link,
        review_btns=review,
        reviews_quotes=reviews_quotes,
        indo_info=indo_info,
        footer_accordion_itens=footer_accordion_itens,
    )


@app.route("/cookies")
def cookies():
    return render_template("cookies.html")


if __name__ == "__main__":
    app.run(debug=True)
