
st.header("📬 Let's Connect")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        st.success("Thank you for reaching out!")

st.header("📞 Contact")
st.write("Email: gamit3175@gmail.com")
st.write("LinkedIn: linkedin.com/in/amit-gupta-aa0b41203")
st.write("Location: Lucknow, Uttar Pradesh, India")



import streamlit as st
from pathlib import Path

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Amit Gupta | Technical Lead",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
if Path("styles.css").exists():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# -----------------------------
# HERO SECTION
# -----------------------------
col1, col2 = st.columns([1, 3])

with col1:
    if Path("profile.jpg").exists():
        st.image("profile.jpg", width=220)

with col2:

    st.markdown("""
    <div class="hero-tag">
    Hello, I'm
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 class="hero-name">
    Amit Gupta
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 class="hero-role">
    Technical Lead | Java Backend Developer | DevOps Engineer
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="hero-desc">
    Building scalable enterprise applications,
    secure CI/CD pipelines and cloud-native solutions.
    </p>
    """, unsafe_allow_html=True)

# -----------------------------
# RESUME BUTTON
# -----------------------------
if Path("AMIT_JAVA_DEV_RESUME.pdf").exists():

    with open(
        "AMIT_JAVA_DEV_RESUME.pdf",
        "rb"
    ) as pdf:

        st.download_button(
            "📄 Download Resume",
            pdf,
            file_name="Amit_Gupta_Resume.pdf"
        )

st.divider()

# -----------------------------
# STATS
# -----------------------------
st.markdown("## 📊 Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Experience", "4.5+ Years")

with c2:
    st.metric("Team Led", "7+")

with c3:
    st.metric("Projects", "10+")

with c4:
    st.metric("Awards", "3+")

# -----------------------------
# ABOUT
# -----------------------------
st.markdown("## 👨‍💻 About Me")

st.markdown("""
I am Amit Gupta, a Technical Lead, Java Backend Developer,
and DevOps Engineer with over 4.5 years of experience in
designing, developing, modernizing, and supporting
enterprise-grade applications.

My expertise lies in building scalable backend systems
using Java, Spring Boot, Hibernate, REST APIs,
DevOps practices, and cloud-native technologies.

Throughout my journey at Tata Consultancy Services (TCS),
I have worked on mission-critical enterprise applications,
leading engineering teams, driving modernization initiatives,
implementing automation solutions, and improving software
delivery processes.

My technical strengths include Java, Spring Boot,
Linux, Jenkins, Docker, Kubernetes, Terraform,
AWS, Google Cloud Platform, CI/CD automation,
SonarQube, SAST, DAST, and SCA compliance.

I am passionate about solving complex engineering
problems, mentoring teams, optimizing delivery pipelines,
and creating measurable business value through technology.
""")

# -----------------------------
# EXPERIENCE
# -----------------------------
st.markdown("## 💼 Professional Experience")

st.markdown("""
### Tata Consultancy Services (TCS)

**Technical Lead / System Engineer**

**February 2022 – Present**

#### Key Responsibilities

- Lead a team of 7 engineers.
- DevOps & Security Lead for critical applications.
- Designed REST APIs using Java, Spring Boot and Hibernate.
- Implemented CI/CD pipelines using Jenkins.
- Automated reporting and operational processes.
- Managed production support and incident resolution.
- Collaborated with stakeholders and business teams.

#### Key Achievements

- Improved batch processing performance significantly.
- Reduced operational effort through automation.
- Led modernization initiatives successfully.
- Mentored junior developers and engineers.
""")

# -----------------------------
# SKILLS
# -----------------------------
st.markdown("## ⚡ Technical Skills")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.info("""
Backend Development

• Java

• Spring Boot

• Hibernate

• REST APIs
""")

with s2:
    st.info("""
DevOps

• Jenkins

• Docker

• Kubernetes

• Terraform
""")

with s3:
    st.info("""
Cloud

• AWS

• GCP

• Linux

• CI/CD
""")

with s4:
    st.info("""
Security

• SonarQube

• SAST

• DAST

• SCA
""")

# -----------------------------
# PROJECTS
# -----------------------------
st.markdown("## 🚀 Featured Projects")

p1, p2 = st.columns(2)

with p1:
    st.success("""
Enterprise Banking Platform

• 1000+ TPS

• AWS KMS Encryption

• Secure CI/CD

• Enterprise Architecture
""")

with p2:
    st.success("""
Application Modernization

• Spring to Spring Boot

• Legacy Migration

• Automation

• Performance Optimization
""")

# -----------------------------
# CERTIFICATIONS
# -----------------------------
st.markdown("## 🏆 Certifications")

st.success(
    "AWS Certified Cloud Practitioner"
)

st.success(
    "Google Cloud Associate Cloud Engineer"
)

# -----------------------------
# AWARDS
# -----------------------------
st.markdown("## 🌟 Awards & Recognition")

st.warning("🏅 Best Team Award")
st.warning("🏅 Going The Extra Mile Award")
st.warning("🏅 Star of the Month Award")

# -----------------------------
# CONTACT
# -----------------------------
st.header("📬 Let's Connect")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        st.success("Thank you for reaching out!")

st.header("📞 Contact")
st.write("Email: gamit3175@gmail.com")
st.write("LinkedIn: linkedin.com/in/amit-gupta-aa0b41203")
st.write("Location: Lucknow, Uttar Pradesh, India") 
st.divider()

st.caption(
    "© 2025 Amit Gupta | Technical Lead | Java Backend Developer | DevOps Engineer"
)

