import streamlit as st

# إعدادات الفخامة (خط Cairo والألوان الذهبية)
st.set_page_config(page_title="المنصور استراتيجي", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    * { font-family: 'Cairo', sans-serif; direction: rtl; }
    .main { background-color: #0E1117; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-weight: 700; }
    p { color: #E0E0E0 !important; text-align: center; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1A1C24 !important; color: white !important;
        border: 1px solid #D4AF37 !important; border-radius: 10px !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37, #B8860B) !important;
        color: black !important; font-weight: bold !important;
        width: 100% !important; border-radius: 12px !important; height: 3.5em !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div style='text-align: center; font-size: 60px;'>🦅</div>", unsafe_allow_html=True)
st.markdown("<h1>مَنصة المَنصور استراتيجي</h1>", unsafe_allow_html=True)
st.markdown("<p>بوابة المستشار منصور الوصابي للتقارير والحلول الذكية</p>", unsafe_allow_html=True)
st.markdown("---")

if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.subheader("🔑 تفعيل النظام")
    code = st.text_input("أدخل كود VIP الخاص بك", type="password", placeholder="M-77-VIP")
    if st.button("دخول للنظام"):
        if code in ["M-77-VIP", "STR-2026-XP"]:
            st.session_state.auth = True
            st.rerun()
        else: st.error("الكود غير صحيح")
else:
    with st.form("pro_form"):
        col1, col2 = st.columns(2)
        with col1:
            p1 = st.text_input("اسم المشروع", placeholder="مثال: الاستجابة الطارئة للنازحين")
            p3 = st.text_input("عنوان النشاط", placeholder="مثال: ورشة تدريب سبل المعيشة")
        with col2:
            p2 = st.text_input("الجهة المنفذة", placeholder="مثال: مؤسسة بناء للتنمية")
            p4 = st.text_input("النطاق (زمان/مكان)", placeholder="مثال: صنعاء - أبريل 2026")
        
        st.markdown("---")
        p7 = st.text_area("أهم الإنجازات المحققة", placeholder="1. تم تدريب 50 شاباً..\n2. تم توزيع حقائب..")
        p10 = st.text_area("التوصيات الختامية", placeholder="توصية بزيادة الدعم الفني...")

        if st.form_submit_button("🚀 توليد الصياغة الاحترافية"):
            st.balloons()
            st.success("تم التوليد بنجاح! انسخ النص وضعه في Gemini")
            st.code(f"PRJ: {p1} | ACT: {p3} | RESULT: {p7}")
