import streamlit as st

# 1. إعدادات الهوية البصرية (الفخامة والاحترافية)
st.set_page_config(page_title="المنصور استراتيجي", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #121212; color: #D4AF37; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1E1E1E; color: #FFFFFF; border: 1px solid #D4AF37; text-align: right;
    }
    h1, h2, h3, p { color: #D4AF37 !important; text-align: right; }
    .stButton>button { 
        background-color: #D4AF37; color: black; font-weight: bold; width: 100%;
        border-radius: 8px; border: none; height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🦅 منصة المنصور استراتيجي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>تحت إشراف المستشار منصور الوصابي</p>", unsafe_allow_html=True)

# نظام التحقق
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.subheader("🔑 تفعيل النظام")
    code = st.text_input("أدخل كود التفعيل الخاص بك", type="password")
    if st.button("دخول للنظام"):
        if code in ["M-77-VIP", "STR-2026-XP", "FREE-MAN-2026"]:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("الكود خاطئ. تواصل مع المستشار منصور 774575749")
else:
    st.markdown("### 📝 نموذج البيانات الاستراتيجية")
    with st.form("main_form"):
        p1 = st.text_input("1. اسم المشروع")
        p2 = st.text_input("2. الجهة المنفذة")
        p3 = st.text_input("3. عنوان النشاط")
        p4 = st.text_input("4. النطاق الزماني والمكاني")
        p5 = st.text_input("5. إحصائيات الحضور")
        p6 = st.text_area("6. أهداف النشاط")
        p7 = st.text_area("7. أهم الإنجازات")
        p8 = st.text_area("8. التحديات والمخاطر")
        p9 = st.text_area("9. الحلول والمعالجات")
        p10 = st.text_area("10. التوصيات الختامية")
        p11 = st.text_input("11. وصف الصور المرفقة")
        
        if st.form_submit_button("🚀 توليد التقرير النهائي"):
            st.success("تم بنجاح! انسخ الكود أدناه وضعه في محرك الذكاء الاصطناعي:")
            out = f"""
            [AL-MANSOUR-STRATEGIC-V3.5]
            {{
              "METADATA": {{"PRJ": "{p1}", "ORG": "{p2}", "ACT": "{p3}", "LOC": "{p4}"}},
              "STATS": {{"GND": "{p5}", "GOAL": "{p6}", "RESULT": "{p7}"}},
              "LOGS": {{"CHLNG": "{p8}", "SOL": "{p9}"}},
              "FINAL": {{"REC": "{p10}", "IMG": "{p11}"}}
            }}
            [DECODING]: Generate a high-level professional NGO report (AR/EN).
            """
            st.code(out)

