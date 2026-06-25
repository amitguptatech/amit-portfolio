
import streamlit as st

st.set_page_config(page_title="Amit Gupta | Technical Lead", page_icon="🚀", layout="wide")

st.markdown("""
<style>
.main {background:#0f172a;}
.hero{padding:40px;text-align:center;}
.card{background:#1e293b;padding:20px;border-radius:12px;margin:10px 0;color:white;}
h1,h2,h3,h4,p,li{color:white;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>Amit Gupta</h1>
<h3>Technical Lead | Java Backend Developer | DevOps Engineer</h3>
<p>Building Scalable Enterprise Applications, Secure CI/CD Pipelines and Cloud-Native Solutions</p>
</div>
""", unsafe_allow_html=True)

st.header("👨‍💻 About Me")
st.markdown("""
I am Amit Gupta, a Technical Lead, Java Backend Developer, and DevOps Engineer with over 4.5 years of experience in designing, developing, modernizing, and supporting enterprise-grade applications.

My expertise lies in building scalable backend systems using Java, Spring Boot, Hibernate, REST APIs, DevOps practices, and cloud-native technologies. I lead engineering teams, drive modernization initiatives, implement automation solutions, and improve software delivery processes.
""")

st.header("💼 Professional Experience")
st.markdown("""
### Tata Consultancy Services (TCS)
**Technical Lead / System Engineer | Feb 2022 – Present**

- Lead a team of 7 engineers.
- DevOps & Security Lead for critical enterprise applications.
- Designed REST APIs using Java, Spring Boot, and Hibernate.
- Implemented CI/CD pipelines using Jenkins.
- Automated reporting and operational processes.
- Improved batch processing performance significantly.
- Managed production support and incident resolution.
""")

st.header("🚀 Featured Projects")
c1,c2 = st.columns(2)
with c1:
    st.info("Enterprise Banking Platform\n\n1000+ TPS • Secure Architecture • Cloud Enabled")
with c2:
    st.info("Application Modernization\n\nSpring to Spring Boot Migration • Performance Optimization")

st.header("⚡ Technical Skills")
st.write("Java, Spring Boot, Hibernate, REST APIs, Jenkins, Docker, Kubernetes, Terraform, AWS, GCP, Linux, CI/CD, SonarQube, Oracle")

st.header("🏆 Certifications")
st.success("AWS Certified Cloud Practitioner")
st.success("Google Cloud Associate Cloud Engineer")

st.header("🌟 Awards & Recognition")
st.write("Best Team Award • Going The Extra Mile Award • Star of the Month")

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
