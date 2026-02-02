from pathlib import Path
import streamlit as st
from PIL import Image
import requests
import os

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file_by_language = {
    "Português": current_dir / "assets" / "CV.pdf",
    "English": current_dir / "assets" / "CV_EN.pdf",
}
profile_pic = current_dir / "assets" / "profile-pic.png"

st.set_page_config(
    page_title="CV Digital | Bruno Teixeira", page_icon=":wave:", layout="centered"
)

NAME = {"Português": "Bruno Teixeira", "English": "Bruno Teixeira"}
DESCRIPTION = {
    "Português": "Engenheiro de Dados com experiência em pipelines de ETL, automação e arquitetura analítica em nuvem, atuando principalmente com Google BigQuery (GCP) e provisionamento de servidores Linux em AWS EC2.",
    "English": "Data Engineer with experience in cloud-based ETL pipelines, analytics engineering, and data platform automation, primarily using Google BigQuery (GCP) and Linux server provisioning on AWS EC2.",
}

EMAIL = "itbttex@icloud.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/bruno-teixeira-6b543a201/",
    "GitHub": "https://github.com/bttex",
}
PROJECTS = {
    "🏆 GitHub Tracker - Monitora o status de builds no GitHub Actions e novas releases de um repositório": "https://github.com/bttex/github_tracker",
    "🏆 TNT Tracker - Automatiza o rastreamento de encomendas no portal da TNT Brasil": "https://github.com/bttex/tnt_tracker",
    "🏆 Telegram Bot - Um bot que faz web scraping e captura informações de servidores": "https://github.com/bttex/telegrambot",
}

EXPERIENCE = {
    "Português": """
- ✔️ Graduando em Ciência de Dados na Universidade Descomplica — Ago/2024 – Presente
- ✔️ 5 anos de experiência profissional na área de dados
- ✔️ Forte atuação em Engenharia de Dados com Python e SQL
- ✔️ Experiência prática com Google BigQuery (GCP) como data warehouse analítico
- ✔️ Provisionamento e administração de servidores Linux em AWS EC2
- ✔️ Background sólido em BI e consumo analítico (Power BI e Excel)
    """,
    "English": """
- ✔️ Bachelor’s degree in Data Science in progress at Descomplica University — Aug/2024 – Present
- ✔️ 5 years of professional experience in the data field
- ✔️ Strong background in Data Engineering using Python and SQL
- ✔️ Hands-on experience with Google BigQuery (GCP) as an analytical data warehouse
- ✔️ Linux server provisioning and administration on AWS EC2
- ✔️ Solid background in BI and analytics consumption (Power BI and Excel)
    """,
}


HARD_SKILLS = {
    "Português": """
- 👩‍💻 Programação & Dados: Python (Pandas, Scikit-learn, Streamlit), SQL
- 🔄 Engenharia de Dados: ETL / ELT pipelines, automação de workflows
- ☁️ Cloud & Data Platforms: Google Cloud Platform (BigQuery), AWS EC2
- 🐧 Infraestrutura: Provisionamento e administração de servidores Linux
- 📊 Analytics & BI (background): Power BI, Excel
- 🗄️ Bancos de Dados: BigQuery, PostgreSQL, MySQL, SQL Server
    """,
    "English": """
- 👩‍💻 Programming & Data: Python (Pandas, Scikit-learn, Streamlit), SQL
- 🔄 Data Engineering: ETL / ELT pipelines, workflow automation
- ☁️ Cloud & Data Platforms: Google Cloud Platform (BigQuery), AWS EC2
- 🐧 Infrastructure: Linux server provisioning and administration
- 📊 Analytics & BI (background): Power BI, Excel
- 🗄️ Databases: BigQuery, PostgreSQL, MySQL, SQL Server
    """,
}


WORK_HISTORY = {
    "Português": [
        (
            "🚧 Engenheiro de Dados | Vertex Digital",
            "01/2023 - Presente",
            """
- ► Desenvolvimento e manutenção de pipelines de ETL utilizando Python e SQL, com dados armazenados no Google BigQuery.
- ► Otimização de consultas e processos no BigQuery, gerando aproximadamente R$5.000 em economia anual.
- ► Automação de ingestão e transformação de dados para suporte a dashboards quase em tempo real.
- ► Provisionamento e gerenciamento de servidores Linux em AWS EC2 para execução de processos e aplicações de dados.
- ► Desenvolvimento de aplicações analíticas em Streamlit e suporte a camadas analíticas consumidas por Power BI.
        """,
        ),
        (
            "🚧 Analista de BI | MP Advogados",
            "11/2021 - 12/2022",
            """
- ► Apuração e análise de resultados corporativos.
- ► Participação em reuniões com foco na melhoria de processos analíticos e operacionais.
- ► Desenvolvimento de relatórios e dashboards em Power BI e Excel.
        """,
        ),
        (
            "🚧 Assistente Técnico em BI | Eletromecânica do Maranhão",
            "01/2021 - 10/2021",
            """
- ► Apoio à tomada de decisão gerencial por meio da geração de relatórios operacionais e financeiros.
- ► Desenvolvimento e melhoria de processos internos para aumento de eficiência em áreas técnicas.
- ► Consolidação de pacotes de relatórios para análise de desempenho do negócio.
        """,
        ),
    ],
    "English": [
        (
            "🚧 Data Engineer | Vertex Digital",
            "01/2023 - Present",
            """
- ► Designed and maintained ETL pipelines using Python and SQL, with data stored and processed in Google BigQuery.
- ► Optimized BigQuery queries and data workflows, generating approximately R$5,000 in annual cost savings.
- ► Automated data ingestion and transformation to support near real-time analytics and dashboards.
- ► Provisioned and managed Linux servers on AWS EC2 to run data pipelines and analytical applications.
- ► Built analytical applications with Streamlit and supported analytics layers consumed by Power BI.
        """,
        ),
        (
            "🚧 BI Analyst | MP Advogados",
            "11/2021 - 12/2022",
            """
- ► Tracked and analyzed company performance metrics.
- ► Participated in team discussions focused on improving analytical and operational processes.
- ► Developed reports and dashboards using Power BI and Excel.
        """,
        ),
        (
            "🚧 BI Technical Assistant | Eletromecânica do Maranhão",
            "01/2021 - 10/2021",
            """
- ► Assisted managers in decision-making processes by producing operational and financial reports.
- ► Developed and implemented internal processes to improve efficiency in technical areas.
- ► Generated reporting packages for business performance analysis.
        """,
        ),
    ],
}


# --- LANGUAGE SELECTION ---
language = st.radio("Escolha o idioma / Choose language", ["Português", "English"])

selected_resume = resume_file_by_language[language]
# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(selected_resume, "rb") as pdf_file:
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
        file_name=selected_resume.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experiência" if language == "Português" else "Experience")
st.write(EXPERIENCE[language])


# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills" if language == "Português" else "Hard Skills")
st.write(HARD_SKILLS[language])


# --- WORK HISTORY ---
st.write("\n")
st.subheader("Histórico" if language == "Português" else "Work History")
st.write("---")

for job_title, job_date, job_desc in WORK_HISTORY[language]:
    st.write(f"{job_title} ({job_date})")
    st.write(job_desc)

token = os.getenv("GITHUB_TOKEN")


def get_github_projects(username):
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}
    all_repos = []
    page = 1

    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("Erro na API:", response.status_code, response.text)
            return []

        repos = response.json()
        if not repos:
            break

        all_repos.extend(repos)
        page += 1

    return all_repos


# Mapeamento dos nomes dos repositórios para os nomes desejados
repo_name_mapping = {
    "telegrambot": {
        "Português": "Telegram Bot - Um bot que faz web scraping e captura informações de servidores",
        "English": "Telegram Bot - A bot that does web scraping and captures server information",
    },
    "tnt_tracker": {
        "Português": "TNT Tracker - Automatiza o rastreamento de encomendas no portal da TNT Brasil",
        "English": "TNT Tracker - Automates package tracking on TNT Brasil portal",
    },
    "github_tracker": {
        "Português": "GitHub Tracker - Monitora o status de builds no GitHub Actions e novas releases de um repositório",
        "English": "GitHub Tracker - Monitors build status on GitHub Actions and new releases of a repository",
    },
}


def get_normalized_name(repo_name, language):
    return repo_name_mapping.get(repo_name, {}).get(language, repo_name.capitalize())


# Seu nome de usuário no GitHub
github_username = "bttex"

# Obter os projetos
projects = get_github_projects(github_username)

# Filtrar os repositórios que você deseja exibir
desired_repositories = ["telegrambot", "tnt_tracker", "github_tracker"]
filtered_projects = [
    project for project in projects if project["name"] in desired_repositories
]
# --- Projects & Accomplishments ---
st.write("\n")
st.subheader("Projetos" if language == "Português" else "Projects")
st.write("---")
# Exibir os 3 primeiros projetos
# Exibir os projetos com os nomes normalizados
for project in filtered_projects[:3]:  # Limite para os 3 primeiros
    repo_name = project["name"]
    normalized_name = get_normalized_name(repo_name, language)
    repo_description = project.get("description", "Sem descrição")

    st.write(f"{normalized_name}")
    st.write(f"Link: {project['html_url']}")
    st.write("---")


st.write("\n")
st.subheader("Cursos" if language == "Português" else "Courses")
st.write("---")

col3, col4, col5 = st.columns(3, gap="small")
with col3:
    st.image(image="assets/introduction-to-cybersecurity.png")
with col4:
    st.image(image="assets/introduction-to-data-science.png")
with col5:
    st.image(image="assets/python-essentials-1.1.png")
