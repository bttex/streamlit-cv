from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV Digital | Bruno Teixeira"
PAGE_ICON = ":wave:"
NAME = {
    "Português": "Bruno Teixeira",
    "English": "Bruno Teixeira"
}
DESCRIPTION = {
    "Português": "Analista de dados, auxiliando empresas no suporte à tomada de decisões baseada em dados.",
    "English": "Data Analyst, helping companies with data-driven decision making."
}
EMAIL = "itbttex@icloud.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/bruno-teixeira-6b543a201/",
    "GitHub": "https://github.com/bttex",
}
PROJECTS = {
    "🏆 Weather App - Checando o clima através de API": "https://github.com/bttex/weather-app",
    "🏆 Telegram Bot - Um bot que faz webscraping e captura informações de servidores": "https://github.com/bttex/telegrambot",
    "🏆 Discord Bot - Bot para agendamento de mensagens personalizadas": "https://github.com/bttex/Discord-bot",
}

EXPERIENCE = {
    "Português": """
- ✔️ Cursando Ciência de Dados na Universidade Descomplica - Ago/2024 - Presente
- ✔️ 5 Anos de experiência na área de dados
- ✔️ Grande experiência prática e conhecimento em Python, Excel e SQL
- ✔️ Boa compreensão dos princípios estatísticos e suas respectivas aplicações
- ✔️ Excelente jogador de equipe e demonstra forte senso de proatividade.
    """,
    "English": """
- ✔️ Studying Data Science at Descomplica University - Aug/2024 - Present
- ✔️ 5 years of experience in the data field
- ✔️ Extensive practical experience with Python, Excel, and SQL
- ✔️ Good understanding of statistical principles and their applications
- ✔️ Excellent team player with strong proactive skills.
    """
}

HARD_SKILLS = {
    "Português": """
- 👩‍💻 Programação: Python (Scikit-learn, Pandas, Streamlit), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel
- 🗄️ Databases: Postgres, MySQL, MS SQL Server
    """,
    "English": """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Streamlit), SQL, VBA
- 📊 Data Visualization: PowerBi, MS Excel
- 🗄️ Databases: Postgres, MySQL, MS SQL Server
    """
}

WORK_HISTORY = {
    "Português": [
        ("🚧 Analista de Dados Jr | Vertex Digital", "01/2023 - Presente", """
- ► Geração de R$5000 em economia de custos anuais ao implementar um novo processo de ETL, reduzindo recursos gastos.
- ► Criação de novos processos de ETL e automações para melhorias em tempo real de relatórios e dashboards.
- ► Criação de novos projetos em Streamlit e manutenção e criação de banco de dados SQL Server.
- ► Criação de relatórios e dashboards em Power BI e Excel.
        """),
        ("🚧 Analista de BI | MP Advogados", "11/2021 - 12/2022", """
- ► Apuração de resultados da companhia
- ► Participação em reuniões com a equipe, discutindo novos processos para melhorar a eficiência e a qualidade do serviço.
- ► Criação de novos relatórios em Excel/Power BI
        """),
        ("🚧 Assistente Técnico em BI | Eletromecânica do Maranhão", "01/2021 - 10/2021", """
- ► Auxílio aos gestores em processos de tomada de decisão, produzindo relatórios diários sobre títulos para recomendar ações corretivas e melhorias.
- ► Desenvolvimento e implementação de processos para aumentar a eficiência de áreas como: manutenção e mecânica.
- ► Geração de pacotes de relatórios para análises de desempenho do Negócio.
        """),
    ],
    "English": [
        ("🚧 Data Analyst Jr | Vertex Digital", "01/2023 - Present", """
- ► Generated R$5000 in annual cost savings by implementing a new ETL process, reducing resource usage.
- ► Created new ETL processes and automations for real-time improvements to reports and dashboards.
- ► Developed new Streamlit projects and maintained SQL Server databases.
- ► Created reports and dashboards in Power BI and Excel.
        """),
        ("🚧 BI Analyst | MP Advogados", "11/2021 - 12/2022", """
- ► Company performance results tracking
- ► Participated in team meetings to discuss new processes to improve efficiency and service quality.
- ► Created new reports in Excel/Power BI
        """),
        ("🚧 BI Technical Assistant | Eletromecânica do Maranhão", "01/2021 - 10/2021", """
- ► Assisted managers in decision-making processes, producing daily reports on titles to recommend corrective actions and improvements.
- ► Developed and implemented processes to improve efficiency in areas like maintenance and mechanics.
- ► Generated report packages for business performance analysis.
        """),
    ],
}

# --- LANGUAGE SELECTION ---
language = st.radio("Escolha o idioma / Choose language", ["Português", "English"])


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME[language])
    st.write(DESCRIPTION[language])
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experiência" if language == "Português" else "Experience")
st.write(EXPERIENCE[language])


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills" if language == "Português" else "Hard Skills")
st.write(HARD_SKILLS[language])


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Histórico" if language == "Português" else "Work History")
st.write("---")

for job_title, job_date, job_desc in WORK_HISTORY[language]:
    st.write(f"{job_title} ({job_date})")
    st.write(job_desc)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projetos" if language == "Português" else "Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Cursos" if language == "Português" else "Courses")
st.write("---")

col3, col4, col5 = st.columns(3, gap="small")
with col3:
    st.image(image="assets/introduction-to-cybersecurity.png")
with col4:
    st.image(image="assets/introduction-to-data-science.png")
with col5:
    st.image(image="assets/python-essentials-1.1.png")
