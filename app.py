import streamlit as st
import sqlite3
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import openai

# ================== إعدادات ==================
st.set_page_config(page_title="المنصور استراتيجي", layout="centered")

openai.api_key = "YOUR_API_KEY"

ADMIN_EMAIL = "almansoourd@gmail.com"
WHATSAPP_LINK = "https://wa.me/967774575749"

# ================== قاعدة البيانات ==================
conn = sqlite3.connect("almansour.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    title TEXT,
    content TEXT,
    created_at TEXT
)
""")

# ================== إدارة الاستخدام ==================
if "usage" not in st.session_state:
    st.session_state.usage = 0

FREE_LIMIT = 3

# ================== AI تحسين ==================
def enhance_text(text, mode):
    prompt = f"""
    أنت خبير تقارير دولية.
    قم بإعادة صياغة النص التالي بأسلوب {mode} احترافي دون تغيير المعنى:

    {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ================== PDF ==================
def create_pdf(title, content):
    file_name = "report.pdf"
    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()

    story = []
    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(content.replace("\n", "<br/>"), styles["Normal"]))

    doc.build(story)
    return file_name

# ================== Login ==================
if "user" not in st.session_state:
    st.title("🚀 منصة المنصور الاستراتيجية")

    email = st.text_input("📧 البريد الإلكتروني")
    if st.button("دخول"):
        if email:
            st.session_state.user = email
            st.session_state.is_admin = email == ADMIN_EMAIL
            st.rerun()

    st.stop()

# ================== الحد المجاني ==================
if st.session_state.usage >= FREE_LIMIT and not st.session_state.is_admin:
    st.warning("🚫 انتهت التجربة المجانية")
    st.markdown(f"[📞 تواصل للاشتراك]({WHATSAPP_LINK})")
    st.stop()

# ================== الواجهة ==================
st.title("📊 منصة التقارير الذكية")
st.write(f"👤 المستخدم: {st.session_state.user}")

# ================== أنواع التقارير ==================
report_types = [
    "📊 تقرير إنجاز",
    "💰 تقرير مالي",
    "🏥 تقرير طبي",
    "💻 تقرير تقني",
    "🏗 تقرير ميداني",
    "👥 محضر اجتماع",
    "📢 تقرير تسويقي"
]

r_type = st.selectbox("اختر نوع التقرير", report_types)

project = st.text_input("اسم المشروع")
goal = st.text_area("الأهداف")
challenge = st.text_area("التحديات")
results = st.text_area("النتائج")

# ================== مساعد الصياغة ==================
def ai_buttons(label, text_key):
    col1, col2, col3, col4 = st.columns(4)

    if col1.button(f"✨ {label} احترافي"):
        if st.session_state.get(text_key):
            st.session_state[f"{text_key}_ai"] = enhance_text(st.session_state[text_key], "احترافي")

    if col2.button(f"📈 {label} تحليل"):
        if st.session_state.get(text_key):
            st.session_state[f"{text_key}_ai"] = enhance_text(st.session_state[text_key], "تحليلي")

    if col3.button(f"🧾 {label} رسمي"):
        if st.session_state.get(text_key):
            st.session_state[f"{text_key}_ai"] = enhance_text(st.session_state[text_key], "رسمي")

    if col4.button(f"⚡ {label} مختصر"):
        if st.session_state.get(text_key):
            st.session_state[f"{text_key}_ai"] = enhance_text(st.session_state[text_key], "مختصر")

    if f"{text_key}_ai" in st.session_state:
        st.info(st.session_state[f"{text_key}_ai"])

        if st.button(f"✔ اعتماد {label}"):
            st.session_state[text_key] = st.session_state[f"{text_key}_ai"]

# ربط الحقول بالـ session
st.session_state["goal"] = goal
st.session_state["challenge
