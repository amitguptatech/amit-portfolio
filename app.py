import streamlit as st
from pathlib import Path
import base64

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Amit Gupta | Technical Lead",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LOAD ASSETS
# ============================================================

resume_data = None
if Path("AMIT_JAVA_DEV_RESUME.pdf").exists():
    with open("AMIT_JAVA_DEV_RESUME.pdf", "rb") as pdf_file:
        resume_data = pdf_file.read()

def get_base64_image(path):
    if Path(path).exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

profile_b64 = get_base64_image("profile.jpg")

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
    padding-left:6%;
    padding-right:6%;
    max-width:1200px;
}

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
    scroll-behavior:smooth;
}

.stApp{
    background:linear-gradient(160deg,#0b1120 0%,#111827 50%,#0b1120 100%);
    color:#e5e7eb;
}

h1,h2,h3{font-family:'Poppins',sans-serif;}

/* HERO */
.hero-card{
    padding:36px;
    border-radius:22px;
    background:rgba(255,255,255,0.04);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0px 15px 40px rgba(0,0,0,.35);
    height:100%;
}

.profile-circle-wrap{
    display:flex;
    justify-content:center;
    margin-bottom:18px;
}

.profile-circle{
    width:220px;
    height:220px;
    border-radius:50%;
    object-fit:cover;
    border:5px solid #38bdf8;
    box-shadow:0 0 35px rgba(56,189,248,.55);
    transition:.35s;
}

.profile-circle:hover{transform:scale(1.04);}

.profile-fallback{
    width:220px;
    height:220px;
    border-radius:50%;
    border:5px solid #38bdf8;
    box-shadow:0 0 35px rgba(56,189,248,.55);
    display:flex;
    align-items:center;
    justify-content:center;
    font-family:'Poppins',sans-serif;
    font-size:64px;
    font-weight:800;
    color:#38bdf8;
    background:#1e293b;
}

.name{font-size:46px;font-weight:800;color:white;margin-bottom:6px;font-family:'Poppins',sans-serif;}
.role{font-size:20px;color:#38bdf8;font-weight:600;margin-bottom:16px;}
.tagline{font-size:16.5px;color:#cbd5e1;line-height:1.8;}

/* METRICS */
.metric-card{
    background:#1e293b;
    padding:22px 10px;
    border-radius:16px;
    text-align:center;
    transition:.3s;
    border:1px solid #334155;
}
.metric-card:hover{transform:translateY(-6px);box-shadow:0 10px 30px rgba(0,0,0,.35);}
.metric-number{font-size:32px;font-weight:800;color:#38bdf8;font-family:'Poppins',sans-serif;}
.metric-title{font-size:14px;color:#cbd5e1;margin-top:4px;}

/* BUTTONS */
.social-btn{
    display:inline-block;padding:11px 20px;border-radius:10px;
    text-decoration:none;font-weight:700;margin-right:10px;margin-top:6px;
    transition:.3s;font-size:14.5px;
}
.linkedin{background:#0A66C2;color:white !important;}
.github{background:#24292e;color:white !important;}
.emailbtn{background:#2563EB;color:white !important;}
.social-btn:hover{transform:translateY(-3px);}

.section-title{
    font-size:30px;font-weight:700;color:#38bdf8;
    margin-top:46px;margin-bottom:18px;font-family:'Poppins',sans-serif;
    border-bottom:2px solid #1e293b;padding-bottom:10px;
}

.about-card{
    background:#1e293b;padding:26px;border-radius:16px;
    border:1px solid #334155;font-size:16.5px;line-height:1.9;color:#d1d5db;
}

/* TIMELINE */
.timeline{position:relative;margin-left:15px;padding-left:25px;border-left:3px solid #38bdf8;}
.timeline-item{background:#1e293b;padding:22px;border-radius:14px;margin-bottom:22px;border:1px solid #334155;}
.timeline-title{font-size:20px;font-weight:700;color:#38bdf8;}
.timeline-company{font-size:16.5px;font-weight:600;color:white;}
.timeline-date{font-size:14px;color:#94a3b8;margin-bottom:10px;}
.timeline-item ul{margin-top:8px;color:#d1d5db;line-height:1.8;}

/* SKILLS */
.skill-card{background:#1e293b;padding:20px;border-radius:14px;border:1px solid #334155;margin-bottom:18px;height:100%;}
.skill-card h4{color:#38bdf8;margin-bottom:10px;font-family:'Poppins',sans-serif;}
.badge{display:inline-block;padding:7px 13px;background:#2563EB;margin:5px 4px 0 0;border-radius:20px;font-size:13px;font-weight:600;color:white;}
.badge-theory{background:#475569;}

/* EDU / CERT */
.edu-card, .cert-card{background:#1e293b;padding:20px;border-radius:14px;border:1px solid #334155;margin-top:14px;}
.edu-card h4, .cert-card h4{color:#38bdf8;margin-bottom:4px;font-family:'Poppins',sans-serif;}

/* PROJECT */
.project-card{background:#1e293b;padding:24px;border-radius:16px;border:1px solid #334155;margin-bottom:20px;transition:.35s;height:100%;}
.project-card:hover{transform:translateY(-6px);box-shadow:0px 15px 35px rgba(0,0,0,.3);border:1px solid #38bdf8;}
.project-title{font-size:21px;font-weight:700;color:#38bdf8;margin-bottom:12px;font-family:'Poppins',sans-serif;}
.project-desc{font-size:15px;line-height:1.75;color:#d1d5db;margin-bottom:14px;}
.tech{display:inline-block;background:#2563EB;padding:5px 11px;border-radius:20px;margin:3px;font-size:12.5px;font-weight:600;color:white;}

/* CONNECT */
.connect-wrap{
    background:linear-gradient(135deg,rgba(56,189,248,0.08),rgba(37,99,235,0.05));
    border:1px solid rgba(56,189,248,0.25);
    border-radius:22px;padding:40px;text-align:center;
}
.connect-title{font-size:30px;font-weight:800;color:white;margin-bottom:8px;font-family:'Poppins',sans-serif;}
.connect-sub{color:#94a3b8;font-size:15.5px;margin-bottom:26px;}
.connect-btn{
    display:inline-flex;align-items:center;gap:8px;
    padding:14px 26px;border-radius:12px;font-weight:700;font-size:15px;
    text-decoration:none;margin:8px;transition:.3s;
}
.connect-btn:hover{transform:translateY(-4px);}
.connect-email{background:#2563EB;color:white !important;}
.connect-linkedin{background:#0A66C2;color:white !important;}
.connect-github{background:#24292e;color:white !important;border:1px solid #475569;}

/* FOOTER */
.footer-box{text-align:center;color:#64748b;padding:30px 10px;font-size:14px;}
.footer-box b{color:#38bdf8;}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================

left, right = st.columns([1, 2])

with left:
    if profile_b64:
        st.markdown(
            f"<div class='profile-circle-wrap'><img class='profile-circle' src='data:image/jpeg;base64,{profile_b64}'></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div class='profile-circle-wrap'><div class='profile-fallback'>AG</div></div>",
            unsafe_allow_html=True
        )

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
    st.markdown("<div class='hero-card'>", unsafe_allow_html=True)
    st.markdown("<div class='name'>Amit Gupta</div>", unsafe_allow_html=True)
    st.markdown("<div class='role'>Technical Lead | Java Backend Developer | DevOps Engineer</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='tagline'>
    Technical Lead and Java Backend Developer with 4.5+ years of experience building enterprise-grade
    applications with <b>Java</b>, <b>Spring Boot</b>, and <b>REST APIs</b>. I lead engineering teams,
    drive DevOps &amp; security initiatives, and modernize legacy systems &mdash; with growing hands-on
    exposure to <b>Docker</b>, <b>Kubernetes</b>, and <b>Terraform</b>.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <a class="social-btn linkedin" href="https://www.linkedin.com/in/amit-gupta-aa0b41203" target="_blank">🔗 LinkedIn</a>
    <a class="social-btn github" href="https://github.com/amitguptatech" target="_blank">💻 GitHub</a>
    <a class="social-btn emailbtn" href="mailto:gamit3175@gmail.com">📧 Email</a>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# HIGHLIGHTS (grounded in resume facts only)
# ============================================================

st.markdown("<div class='section-title'>Professional Highlights</div>", unsafe_allow_html=True)

h1, h2, h3, h4 = st.columns(4)
highlight_data = [
    ("4.5+", "Years Experience"),
    ("7", "Engineers Led"),
    ("3", "Critical Apps as DevOps Lead"),
    ("80%", "Batch Efficiency Gain"),
]
for col, (num, label) in zip([h1, h2, h3, h4], highlight_data):
    with col:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-number'>{num}</div>
            <div class='metric-title'>{label}</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# ABOUT ME
# ============================================================

st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
st.markdown("""
<div class='about-card'>
I'm a Technical Lead currently at Tata Consultancy Services, where I lead a team of 7 engineers across
development, automation, and production deployment for enterprise applications built with Java, Spring Boot,
and Hibernate. As DevOps &amp; Security Lead for 3 critical applications, I own secure CI/CD pipelines,
coordinate SAST/DAST/SCA remediation, and drive legacy modernization &mdash; including migrating batch
applications from Spring Framework to Spring Boot.
<br><br>
Beyond backend development, I automate Linux operations through shell scripting, manage Control-M batch
scheduling, and am actively building hands-on depth in containerization and Infrastructure-as-Code
(Docker, Kubernetes, Terraform). I care about writing reliable, maintainable code and mentoring the
engineers around me.
</div>
""", unsafe_allow_html=True)

# ============================================================
# PROFESSIONAL EXPERIENCE
# ============================================================

st.markdown("<div class='section-title'>Professional Experience</div>", unsafe_allow_html=True)

st.markdown("<div class='timeline'>", unsafe_allow_html=True)
st.markdown("""
<div class='timeline-item'>
    <div class='timeline-title'>Technical Lead / System Engineer</div>
    <div class='timeline-company'>Tata Consultancy Services (TCS)</div>
    <div class='timeline-date'>February 2022 – Present · Lucknow, India</div>
    <ul>
        <li>Lead a team of 7 engineers across development, automation, release management, and production deployment.</li>
        <li>Serve as DevOps &amp; Security Lead for 3 critical applications, ensuring secure CI/CD pipelines with Jenkins &amp; SonarQube.</li>
        <li>Design and deploy RESTful APIs using Java, Spring Boot, and Hibernate for enterprise-scale applications.</li>
        <li>Led migration of legacy batch applications from Spring Framework to Spring Boot.</li>
        <li>Automated data extraction and reporting, saving 80+ hours of manual effort per month.</li>
        <li>Implemented Control-M scheduling for Java and database batch jobs, and automated JBoss server restarts to reduce downtime.</li>
    </ul>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# TECHNICAL SKILLS (single consolidated section)
# ============================================================

st.markdown("<div class='section-title'>Technical Skills</div>", unsafe_allow_html=True)

sk1, sk2 = st.columns(2)
with sk1:
    st.markdown("""
    <div class='skill-card'>
        <h4>Languages &amp; Frameworks</h4>
        <span class='badge'>Java</span>
        <span class='badge'>Spring Boot</span>
        <span class='badge'>Spring MVC</span>
        <span class='badge'>Hibernate</span>
        <span class='badge'>REST APIs</span>
        <span class='badge'>Shell Scripting</span>
        <span class='badge'>SQL</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='skill-card'>
        <h4>Security &amp; Testing</h4>
        <span class='badge'>SonarQube</span>
        <span class='badge'>JUnit</span>
        <span class='badge'>SAST</span>
        <span class='badge'>DAST</span>
        <span class='badge'>SCA</span>
    </div>
    """, unsafe_allow_html=True)
with sk2:
    st.markdown("""
    <div class='skill-card'>
        <h4>DevOps &amp; Automation</h4>
        <span class='badge'>Jenkins</span>
        <span class='badge'>CI/CD</span>
        <span class='badge'>Linux</span>
        <span class='badge'>Control-M</span>
        <span class='badge'>Cronjob</span>
        <span class='badge'>Maven</span>
        <span class='badge'>GitHub / GitLab</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='skill-card'>
        <h4>Containerization &amp; IaC <span style='font-size:12px;color:#94a3b8;'>(working knowledge)</span></h4>
        <span class='badge badge-theory'>Docker</span>
        <span class='badge badge-theory'>Kubernetes</span>
        <span class='badge badge-theory'>Terraform</span>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FEATURED PROJECTS
# ============================================================

st.markdown("<div class='section-title'>Featured Projects</div>", unsafe_allow_html=True)

p1, p2 = st.columns(2)
with p1:
    st.markdown("""
    <div class="project-card">
        <div class="project-title">Enterprise Batch Modernization</div>
        <div class="project-desc">
        Migrated legacy Java batch applications from Spring Framework to Spring Boot and refactored
        complex batch jobs, improving execution efficiency by approximately 80%.
        </div>
        <span class="tech">Java</span><span class="tech">Spring Boot</span>
        <span class="tech">Control-M</span><span class="tech">Shell Scripting</span>
    </div>
    """, unsafe_allow_html=True)
with p2:
    st.markdown("""
    <div class="project-card">
        <div class="project-title">Secure CI/CD Pipeline Rollout</div>
        <div class="project-desc">
        Built and maintained secure CI/CD pipelines across 3 critical applications, integrating
        SonarQube, SAST, DAST, and SCA scans into the release process.
        </div>
        <span class="tech">Jenkins</span><span class="tech">SonarQube</span>
        <span class="tech">DevSecOps</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    "<p style='color:#64748b;font-size:13.5px;margin-top:4px;'>"
    "Want to showcase specific GitHub repos here instead? Swap these cards for your real project links."
    "</p>", unsafe_allow_html=True
)

# ============================================================
# EDUCATION
# ============================================================

st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)
st.markdown("""
<div class='edu-card'>
    <h4>Bachelor of Technology (B.Tech) — Electronics &amp; Communication Engineering</h4>
    Dr. Ambedkar Institute of Technology for Handicapped, Kanpur, U.P. &nbsp;|&nbsp; 08/2017 – 08/2021
</div>
<div class='edu-card'>
    <h4>Intermediate</h4>
    S.V.I.C, Sultanpur, U.P. &nbsp;|&nbsp; 07/2016 – 06/2017
</div>
""", unsafe_allow_html=True)

# ============================================================
# CERTIFICATIONS
# ============================================================

st.markdown("<div class='section-title'>Certifications</div>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class='cert-card'>
        <h4>🏆 Google Cloud Certified</h4>
        Associate Cloud Engineer
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class='cert-card'>
        <h4>🏆 AWS Certified</h4>
        Cloud Practitioner
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# AWARDS
# ============================================================

st.markdown("<div class='section-title'>Awards &amp; Recognition</div>", unsafe_allow_html=True)
st.markdown("""
<div class='about-card'>
🏆 <b>Best Team Award</b>, TCS<br>
✔ "Going the Extra Mile" Award — recognized for persistence and exemplary commitment<br>
✔ Star of the Month Award — recognized for extending assistance across multiple teams
</div>
""", unsafe_allow_html=True)

# ============================================================
# CONNECT WITH ME (single, dedicated section)
# ============================================================

st.markdown("<div class='section-title'>Connect With Me</div>", unsafe_allow_html=True)
st.markdown("""
<div class='connect-wrap'>
    <div class='connect-title'>Let's Build Something Great</div>
    <div class='connect-sub'>
        Open to Technical Lead roles, Java backend opportunities, and DevOps collaborations.
    </div>
    <a class='connect-btn connect-email' href='mailto:gamit3175@gmail.com'>📧 Email Me</a>
    <a class='connect-btn connect-linkedin' href='https://www.linkedin.com/in/amit-gupta-aa0b41203' target='_blank'>🔗 LinkedIn</a>
    <a class='connect-btn connect-github' href='https://github.com/amitguptatech' target='_blank'>💻 GitHub</a>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown("""
<div class='footer-box'>
    <b>Amit Gupta</b> — Technical Lead | Java Backend Developer | DevOps Engineer<br>
    © 2026 · Built with Streamlit &amp; Python
</div>
""", unsafe_allow_html=True)

# ============================================================
# END OF APP
# ============================================================
