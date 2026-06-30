import streamlit as st
from pathlib import Path

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Amit Gupta | Technical Lead",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# LOAD RESUME
# ---------------------------------------------------

resume_data = None
if Path("resume.pdf").exists():
    with open("resume.pdf", "rb") as pdf_file:
        resume_data = pdf_file.read()

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:1rem;
padding-bottom:2rem;
padding-left:5%;
padding-right:5%;
}

html, body, [class*="css"]{
font-family:'Segoe UI',sans-serif;
background:#0f172a;
color:white;
scroll-behavior:smooth;
}

.stApp{
background:linear-gradient(135deg,#0f172a,#111827,#0f172a);
}

.hero-card{
padding:30px;
border-radius:20px;
background:rgba(255,255,255,0.05);
backdrop-filter:blur(15px);
border:1px solid rgba(255,255,255,0.08);
box-shadow:0px 15px 40px rgba(0,0,0,.35);
}

.profile-img img{
border-radius:50%;
border:6px solid #38bdf8;
box-shadow:0 0 35px rgba(56,189,248,.6);
transition:.4s;
}

.profile-img img:hover{
transform:scale(1.05);
}

.name{

font-size:52px;

font-weight:800;

margin-bottom:10px;

color:white;

}

.role{

font-size:24px;

color:#38bdf8;

font-weight:600;

margin-bottom:20px;

}

.tagline{

font-size:18px;

color:#cbd5e1;

line-height:1.8;

}

.metric-card{

background:#1e293b;

padding:20px;

border-radius:18px;

text-align:center;

transition:.3s;

border:1px solid #334155;

}

.metric-card:hover{

transform:translateY(-6px);

box-shadow:0 10px 30px rgba(0,0,0,.35);

}

.metric-number{

font-size:34px;

font-weight:800;

color:#38bdf8;

}

.metric-title{

font-size:16px;

color:white;

}

.social-btn{

display:inline-block;

padding:12px 22px;

border-radius:10px;

text-decoration:none;

font-weight:700;

margin-right:10px;

margin-top:10px;

transition:.3s;

}

.linkedin{

background:#0A66C2;

color:white !important;

}

.github{

background:#24292e;

color:white !important;

}

.resume{

background:#2563EB;

color:white !important;

}

.social-btn:hover{

transform:translateY(-4px);

}

.section-title{

font-size:34px;

font-weight:700;

color:#38bdf8;

margin-top:50px;

margin-bottom:20px;

}

.about-card{

background:#1e293b;

padding:25px;

border-radius:18px;

border:1px solid #334155;

font-size:18px;

line-height:1.9;

color:#d1d5db;

}

</style>

""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

left,right = st.columns([1,2])

with left:

    st.markdown("<div class='profile-img'>",unsafe_allow_html=True)

    st.image("photo.jpg",width=260)

    st.markdown("</div>",unsafe_allow_html=True)

    if resume_data:

        st.download_button(

            "📄 Download Resume",

            resume_data,

            file_name="Amit_Gupta_Resume.pdf",

            mime="application/pdf",

            use_container_width=True,

            type="primary"

        )

with right:

    st.markdown("<div class='hero-card'>",unsafe_allow_html=True)

    st.markdown("<div class='name'>Amit Gupta</div>",unsafe_allow_html=True)

    st.markdown("<div class='role'>Technical Lead | Java Backend Developer | DevOps Engineer</div>",unsafe_allow_html=True)

    st.markdown("""

<div class='tagline'>

Experienced Software Engineer with expertise in <b>Java</b>, <b>Spring Boot</b>, <b>AWS Cloud</b>, <b>DevOps</b>, <b>Linux</b>, and <b>Microservices</b>. Passionate about building scalable enterprise applications, designing secure cloud architectures, and leading high-performing engineering teams.

</div>

""",unsafe_allow_html=True)

    st.markdown("""

<a class="social-btn linkedin" href="https://www.linkedin.com/in/amit-gupta-aa0b41203" target="_blank">LinkedIn</a>

<a class="social-btn github" href="https://github.com/amitguptatech" target="_blank">GitHub</a>

<a class="social-btn resume" href="mailto:gamit3175@gmail.com">Email</a>

""",unsafe_allow_html=True)

    st.markdown("</div>",unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------
# HIGHLIGHTS
# ---------------------------------------------------

st.markdown("<div class='section-title'>Professional Highlights</div>",unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown("""

<div class='metric-card'>

<div class='metric-number'>4.5+</div>

<div class='metric-title'>Years Experience</div>

</div>

""",unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class='metric-card'>

<div class='metric-number'>10+</div>

<div class='metric-title'>Enterprise Projects</div>

</div>

""",unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class='metric-card'>

<div class='metric-number'>1000+</div>

<div class='metric-title'>TPS Applications</div>

</div>

""",unsafe_allow_html=True)

with c4:

    st.markdown("""

<div class='metric-card'>

<div class='metric-number'>7+</div>

<div class='metric-title'>Team Leadership</div>

</div>

""",unsafe_allow_html=True)

# ---------------------------------------------------
# ABOUT
# ---------------------------------------------------

st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)

st.markdown("""
<div class='about-card'>

I am a Technical Lead with hands-on experience in Java, Spring Boot, AWS, DevOps, Linux, Docker, Kubernetes, CI/CD, and Microservices. Currently working at Tata Consultancy Services (TCS), I design and develop secure, scalable enterprise applications capable of processing thousands of transactions per second.

I enjoy solving complex backend challenges, mentoring engineers, optimizing cloud infrastructure, and delivering high-quality software solutions. My focus is on building reliable systems with performance, security, and maintainability at the core.

</div>
""", unsafe_allow_html=True)

# ============================================================
# EXPERIENCE
# ============================================================

st.markdown("<div class='section-title'>Professional Experience</div>", unsafe_allow_html=True)

experience_css = """
<style>

.timeline{
position:relative;
margin-left:15px;
padding-left:25px;
border-left:3px solid #38bdf8;
}

.timeline-item{
background:#1e293b;
padding:20px;
border-radius:15px;
margin-bottom:25px;
border:1px solid #334155;
box-shadow:0px 8px 20px rgba(0,0,0,.25);
}

.timeline-title{
font-size:22px;
font-weight:700;
color:#38bdf8;
}

.timeline-company{
font-size:18px;
font-weight:600;
color:white;
}

.timeline-date{
font-size:15px;
color:#94a3b8;
margin-bottom:10px;
}

.skill-card{
background:#1e293b;
padding:20px;
border-radius:15px;
border:1px solid #334155;
margin-bottom:20px;
height:100%;
}

.badge{
display:inline-block;
padding:8px 14px;
background:#2563EB;
margin:6px;
border-radius:20px;
font-size:14px;
font-weight:600;
color:white;
}

.edu-card{
background:#1e293b;
padding:20px;
border-radius:15px;
border:1px solid #334155;
margin-top:15px;
}

.cert-card{
background:#1e293b;
padding:20px;
border-radius:15px;
border:1px solid #334155;
margin-top:15px;
}

</style>
"""

st.markdown(experience_css, unsafe_allow_html=True)

st.markdown("<div class='timeline'>", unsafe_allow_html=True)

st.markdown("""

<div class='timeline-item'>

<div class='timeline-title'>
Technical Lead
</div>

<div class='timeline-company'>
Tata Consultancy Services (TCS)
</div>

<div class='timeline-date'>
2022 – Present
</div>

<ul>

<li>Leading backend application development using Java & Spring Boot.</li>

<li>Designed highly scalable applications processing 1000+ TPS.</li>

<li>Implemented AWS KMS based end-to-end encryption.</li>

<li>Managed CI/CD pipelines using Jenkins & GitHub.</li>

<li>Led development team and mentored junior engineers.</li>

<li>Worked on AWS EC2, IAM, S3, CloudWatch and Linux servers.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# TECHNICAL SKILLS
# ============================================================

st.markdown("<div class='section-title'>Technical Skills</div>", unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:

    st.markdown("""

<div class='skill-card'>

<h3>Programming</h3>

<span class='badge'>Java</span>

<span class='badge'>Spring Boot</span>

<span class='badge'>REST API</span>

<span class='badge'>Microservices</span>

<span class='badge'>Python</span>

<span class='badge'>SQL</span>

<span class='badge'>Linux</span>

</div>

""",unsafe_allow_html=True)

    st.markdown("""

<div class='skill-card'>

<h3>Cloud</h3>

<span class='badge'>AWS EC2</span>

<span class='badge'>IAM</span>

<span class='badge'>S3</span>

<span class='badge'>CloudWatch</span>

<span class='badge'>AWS KMS</span>

<span class='badge'>Load Balancer</span>

<span class='badge'>VPC</span>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class='skill-card'>

<h3>DevOps</h3>

<span class='badge'>Docker</span>

<span class='badge'>Kubernetes</span>

<span class='badge'>Git</span>

<span class='badge'>GitHub</span>

<span class='badge'>Jenkins</span>

<span class='badge'>CI/CD</span>

<span class='badge'>Maven</span>

</div>

""",unsafe_allow_html=True)

    st.markdown("""

<div class='skill-card'>

<h3>Tools</h3>

<span class='badge'>IntelliJ</span>

<span class='badge'>VS Code</span>

<span class='badge'>Postman</span>

<span class='badge'>Swagger</span>

<span class='badge'>Eclipse</span>

<span class='badge'>Streamlit</span>

<span class='badge'>GitHub Actions</span>

</div>

""",unsafe_allow_html=True)

# ============================================================
# EDUCATION
# ============================================================

st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)

st.markdown("""

<div class='edu-card'>

<h3>Master of Science (Agriculture)</h3>

<b>Specialization:</b> Agriculture

</div>

""", unsafe_allow_html=True)

st.markdown("""

<div class='edu-card'>

<h3>Bachelor of Science (Agriculture)</h3>

<b>Specialization:</b> Agriculture

</div>

""", unsafe_allow_html=True)

# ============================================================
# CERTIFICATIONS
# ============================================================

st.markdown("<div class='section-title'>Certifications</div>", unsafe_allow_html=True)

c1,c2=st.columns(2)

with c1:

    st.markdown("""

<div class='cert-card'>

🏆 AWS Cloud Practitioner

<br><br>

✔ Cloud Fundamentals

<br>

✔ Security

<br>

✔ Networking

</div>

""", unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class='cert-card'>

🏆 DevOps & Linux

<br><br>

✔ Docker

<br>

✔ Kubernetes

<br>

✔ Jenkins CI/CD

</div>

""", unsafe_allow_html=True)

# ============================================================
# CAREER SUMMARY
# ============================================================

st.markdown("<div class='section-title'>Career Summary</div>", unsafe_allow_html=True)

st.info("""

✔ 4.5+ Years of Professional Experience

✔ Technical Lead at Tata Consultancy Services

✔ Expertise in Java, Spring Boot & AWS

✔ Strong DevOps & Cloud Knowledge

✔ Experience building enterprise applications handling 1000+ TPS

✔ Passionate about scalable architecture, cloud engineering and team leadership.

""")
# ============================================================
# FEATURED PROJECTS
# ============================================================

st.markdown("<div class='section-title'>Featured Projects</div>", unsafe_allow_html=True)

project_css = """
<style>

.project-card{
background:#1e293b;
padding:25px;
border-radius:18px;
border:1px solid #334155;
margin-bottom:25px;
transition:0.4s;
height:100%;
}

.project-card:hover{
transform:translateY(-8px);
box-shadow:0px 15px 35px rgba(0,0,0,.35);
border:1px solid #38bdf8;
}

.project-title{
font-size:24px;
font-weight:700;
color:#38bdf8;
margin-bottom:15px;
}

.project-desc{
font-size:16px;
line-height:1.8;
color:#d1d5db;
margin-bottom:18px;
}

.tech{
display:inline-block;
background:#2563EB;
padding:6px 12px;
border-radius:20px;
margin:4px;
font-size:13px;
font-weight:600;
color:white;
}

.github-btn{
display:inline-block;
margin-top:20px;
padding:10px 20px;
background:#0A66C2;
color:white !important;
text-decoration:none;
border-radius:8px;
font-weight:bold;
}

.github-btn:hover{
background:#2563EB;
}

</style>
"""

st.markdown(project_css, unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:

    st.markdown("""

<div class="project-card">

<div class="project-title">

Enterprise Banking Platform

</div>

<div class="project-desc">

Designed and developed secure enterprise banking applications capable of processing more than <b>1000 transactions per second</b>. Implemented AWS KMS encryption, REST APIs, Spring Boot Microservices and scalable cloud deployment.

</div>

<span class="tech">Java</span>

<span class="tech">Spring Boot</span>

<span class="tech">AWS</span>

<span class="tech">REST API</span>

<span class="tech">Microservices</span>

<span class="tech">Docker</span>

<br>

<a class="github-btn"

href="https://github.com/amitguptatech"

target="_blank">

View GitHub

</a>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="project-card">

<div class="project-title">

Image Upload Web Application

</div>

<div class="project-desc">

Developed a cloud-based image upload application deployed on AWS EC2 with secure storage and scalable backend architecture. Implemented user-friendly interface and cloud integration.

</div>

<span class="tech">Python</span>

<span class="tech">AWS EC2</span>

<span class="tech">Linux</span>

<span class="tech">GitHub</span>

<span class="tech">HTML</span>

<span class="tech">CSS</span>

<br>

<a class="github-btn"

href="https://github.com/amitguptatech"

target="_blank">

View GitHub

</a>

</div>

""",unsafe_allow_html=True)

# ============================================================
# PROJECT HIGHLIGHTS
# ============================================================

st.markdown("<div class='section-title'>Project Highlights</div>", unsafe_allow_html=True)

m1,m2,m3,m4=st.columns(4)

m1.metric("Enterprise Projects","10+")

m2.metric("Transactions/sec","1000+")

m3.metric("Cloud Deployments","15+")

m4.metric("Applications","20+")

# ============================================================
# KEY ACHIEVEMENTS
# ============================================================

st.markdown("<div class='section-title'>Key Achievements</div>", unsafe_allow_html=True)

st.success("""

🏆 Successfully delivered enterprise-scale banking applications.

🏆 Led development team for multiple enterprise projects.

🏆 Implemented secure AWS KMS based encryption.

🏆 Improved CI/CD deployment efficiency.

🏆 Developed scalable Java Microservices.

🏆 Built cloud-native applications on AWS.

🏆 Experience in DevOps automation.

🏆 Strong expertise in Linux Administration.

""")

# ============================================================
# TECHNOLOGY EXPERTISE
# ============================================================

st.markdown("<div class='section-title'>Technology Expertise</div>", unsafe_allow_html=True)

tech1,tech2,tech3=st.columns(3)

with tech1:

    st.info("""

### Backend

✔ Java

✔ Spring Boot

✔ REST APIs

✔ Microservices

✔ SQL

✔ Maven

""")

with tech2:

    st.info("""

### Cloud

✔ AWS EC2

✔ IAM

✔ S3

✔ KMS

✔ CloudWatch

✔ Load Balancer

""")

with tech3:

    st.info("""

### DevOps

✔ Docker

✔ Kubernetes

✔ Jenkins

✔ GitHub

✔ Linux

✔ CI/CD

""")

# ============================================================
# WHY WORK WITH ME
# ============================================================

st.markdown("<div class='section-title'>Why Work With Me?</div>", unsafe_allow_html=True)

st.markdown("""

I enjoy designing **high-performance backend systems**, solving complex engineering problems and leading teams to deliver enterprise-grade software.

My expertise spans **Java**, **Spring Boot**, **AWS Cloud**, **DevOps**, **Linux**, **Docker**, **Microservices**, and **CI/CD**.

I believe in writing clean, scalable, maintainable code while continuously learning modern cloud technologies and software architecture.

""")
# ============================================================
# GITHUB & OPEN SOURCE
# ============================================================

st.markdown("<div class='section-title'>GitHub & Open Source</div>", unsafe_allow_html=True)

github_col1, github_col2 = st.columns([2,1])

with github_col1:

    st.markdown("""
<div class='project-card'>

<div class='project-title'>
💻 Open Source Portfolio
</div>

<div class='project-desc'>

I actively use GitHub to manage personal projects, cloud deployments,
Java backend applications and Python automation scripts.

My repositories demonstrate experience in:

• Java & Spring Boot

• Python Development

• AWS Cloud

• DevOps Automation

• Linux Administration

• Streamlit Applications

• REST APIs

</div>

<a class="github-btn"
href="https://github.com/amitguptatech"
target="_blank">

Visit GitHub Profile

</a>

</div>
""", unsafe_allow_html=True)

with github_col2:

    st.metric("Repositories","20+")

    st.metric("Languages","Java • Python")

    st.metric("Cloud","AWS")

    st.metric("DevOps","Docker/K8s")


# ============================================================
# SERVICES
# ============================================================

st.markdown("<div class='section-title'>What I Do</div>", unsafe_allow_html=True)

s1,s2,s3 = st.columns(3)

with s1:

    st.markdown("""
<div class='project-card'>

## ☕ Backend Development

✔ Java

✔ Spring Boot

✔ REST APIs

✔ Microservices

✔ Database Design

✔ High Performance APIs

</div>
""", unsafe_allow_html=True)

with s2:

    st.markdown("""
<div class='project-card'>

## ☁ Cloud Engineering

✔ AWS

✔ EC2

✔ IAM

✔ S3

✔ CloudWatch

✔ AWS KMS

</div>
""", unsafe_allow_html=True)

with s3:

    st.markdown("""
<div class='project-card'>

## ⚙ DevOps

✔ Docker

✔ Kubernetes

✔ Jenkins

✔ GitHub Actions

✔ Linux

✔ CI/CD Pipelines

</div>
""", unsafe_allow_html=True)

# ============================================================
# PROFESSIONAL STRENGTHS
# ============================================================

st.markdown("<div class='section-title'>Professional Strengths</div>", unsafe_allow_html=True)

strength1,strength2 = st.columns(2)

with strength1:

    st.success("""

✅ Problem Solving

✅ System Design

✅ Technical Leadership

✅ Cloud Architecture

✅ Secure Coding

✅ Performance Optimization

""")

with strength2:

    st.success("""

✅ Team Mentoring

✅ Agile Development

✅ Production Support

✅ DevOps Automation

✅ Linux Administration

✅ Client Communication

""")

# ============================================================
# CAREER GOALS
# ============================================================

st.markdown("<div class='section-title'>Career Vision</div>", unsafe_allow_html=True)

st.info("""

My goal is to become a Cloud Solution

# ============================================================
# CONTACT
# ============================================================

st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)

contact1, contact2 = st.columns([2, 1])

with contact1:

    st.markdown("""
<div class='project-card'>

## Let's Build Something Amazing

"I'm always interested in discussing:"

✔ Technical Lead Opportunities

✔ Java Backend Development

✔ Spring Boot Projects

✔ AWS Cloud Solutions

✔ DevOps Automation

✔ Microservices Architecture

✔ Freelance Consulting

✔ Enterprise Software Development

Feel free to connect with me through any of the channels.

</div>

""", unsafe_allow_html=True)

with contact2:

    st.info("""
### 📧 Email

gamit3175@gmail.com
""")

    st.info("""
### 💼 LinkedIn

linkedin.com/in/amit-gupta-aa0b41203
""")

    st.info("""
### 💻 GitHub

github.com/amitguptatech
""")

    st.info("""
### 📍 Location

India
""")

# ============================================================
# QUICK LINKS
# ============================================================

st.markdown("<div class='section-title'>Quick Links</div>", unsafe_allow_html=True)

q1, q2, q3 = st.columns(3)

with q1:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/amitguptatech/amit-portfolio",
        use_container_width=True
    )

with q2:
    st.link_button(
        "🔗 LinkedIn",
        "https://linkedin.com/in/amit-gupta-aa0b41203",
        use_container_width=True
    )

with q3:
    st.link_button(
        "📧 Email",
        "mailto:gamit3175@gmail.com",
        use_container_width=True
    )

# ============================================================
# DOWNLOAD RESUME
# ============================================================

st.markdown("<div class='section-title'>Resume</div>", unsafe_allow_html=True)

if resume_data:

    st.download_button(
        label="📄 Download My Resume",
        data=resume_data,
        file_name="Amit_Gupta_Resume.pdf",
        mime="application/pdf",
        use_container_width=True,
        type="primary"
    )

# ============================================================
# CURRENT FOCUS
# ============================================================

st.markdown("<div class='section-title'>Current Focus</div>", unsafe_allow_html=True)

focus1, focus2, focus3 = st.columns(3)

with focus1:

    st.success("""
☁ AWS

Cloud Architecture

Security

Automation
""")

with focus2:

    st.success("""
☕

Java

Spring Boot

Microservices
""")

with focus3:

    st.success("""
⚙ DevOps

Docker

Kubernetes

CI/CD
""")

# ============================================================
# VISITOR MESSAGE
# ============================================================

st.markdown("<div class='section-title'>Thank You</div>", unsafe_allow_html=True)

st.markdown("""

Thank you for visiting my portfolio.

I'm passionate about building scalable enterprise software,
leading engineering teams, and delivering high-quality cloud solutions.

If you have an exciting opportunity or project,
I'd be delighted to connect.

""")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;color:#94A3B8;padding:25px">

<h3 style="color:#38BDF8;">
Amit Gupta
</h3>

Technical Lead | Java Backend Developer | AWS Cloud | DevOps

<br><br>

<a href="https://linkedin.com/in/amit-gupta-aa0b41203"
target="_blank"
style="text-decoration:none;color:#38BDF8;font-weight:bold;">
LinkedIn
</a>

&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;

<a href="https://github.com/amitguptatech/amit-portfolio"
target="_blank"
style="text-decoration:none;color:#38BDF8;font-weight:bold;">
GitHub
</a>

<br><br>

© 2026 Amit Gupta

<br>

Built using ❤️ with Streamlit & Python

</div>

""",
unsafe_allow_html=True)

# ============================================================
# END OF APP
# ============================================================
