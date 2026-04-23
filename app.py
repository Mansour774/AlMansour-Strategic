import streamlit as st
import pandas as pd
import time
import random

# 1. إعدادات الهوية البصرية وإخفاء أدوات Streamlit
st.set_page_config(page_title="المنصور استراتيجي | PRO", layout="centered")

# --- كود سري لإخفاء الأيقونات العلوية (GitHub, Edit, Menu) ---
st.markdown("""
    <style>
    /* إخفاء شريط الأدوات العلوي تماماً */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stHeader"] {display:none !important;}
    
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    * { font-family: 'Cairo', sans-serif; direction: rtl; }
    .main { background-color: #0E1117; color: #FFFFFF; }
    
    /* تنسيق العناوين والوضوح */
    h1, h2, h3 { color: #D4AF37 !important; font-weight: 800 !important; text-align: center; }
    label { color: #FFFFFF !important; font-weight: 700 !important; font-size: 1.1rem !important; }

    /* الأزرار الملكية */
    .stButton>button {
        width: 100% !important; border-radius: 12px !important;
        height: 3.8rem !important; font-weight: 800 !important; font-size: 1.2rem !important;
        transition: 0.3s all ease;
    }
    div[data-testid="column"]:nth-of-type(2) .stButton>button {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%) !important; color: #000 !important; border: none !important;
    }
    
    .admin-secret-panel { background: #D4AF37; color: black !important; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; display: block; text-align: center; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# بيانات المدير
ADMIN_EMAIL = "774575749m@gmail.com"
EDIT_LINK = "https://github.com/Mansour774/AlMansour-Strategic/edit/main/app.py"

# إدارة الحالة
if 'is_logged_in' not in st.session_state: st.session_state.is_logged_in = False
if 'waiting_otp' not in st.session_state: st.session_state.waiting_otp = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# --- شاشة الدخول ---
if not st.session_state.is_logged_in:
    st.markdown("<h1>بوابة المنصور الاستراتيجية</h1>")
    
    if not st.session_state.waiting_otp:
        st.subheader("🔑 تسجيل الدخول")
        email_in = st.text_input("أدخل البريد الإلكتروني الرسمي", placeholder="example@mail.com")
        if st.button("إرسال رمز التحقق 📧"):
            if "@" in email_in:
                st.session_state.temp_email = email_in
                st.session_state.waiting_otp = True
                # الرمز الآن سيظهر في رسالة "تنبيه" لغرض التجربة حتى نربط سيرفر الإيميلات
                st.session_state.otp_code = str(random.randint(1000, 9999))
                st.rerun()
            else: st.error("يرجى إدخال إيميل صحيح")
    else:
        st.info(f"كود التحقق الخاص بك هو: {st.session_state.otp_code} (سيتم إرساله للإيميل تلقائياً في التحديث القادم)")
        otp_in = st.text_input(f"أدخل الرمز المرسل إلى {st.session_state.temp_email}")
        if st.button("تأكيد ودخول"):
            if otp_in == st.session_state.otp_code:
                st.session_state.is_logged_in = True
                if st.session_state.temp_email.strip().lower() == ADMIN_EMAIL.lower():
                    st.session_state.is_admin = True
                st.rerun()
            else: st.error("الرمز غير صحيح")

# --- واجهة العمل ---
else:
    st.markdown(f"### مرحباً بك في المنصة")
    st.progress(0.5)

    # الأسئلة الاستراتيجية هنا (نفس الأسئلة الـ 11 السابقة)
    st.subheader("1️⃣ معلومات النشاط")
    q1 = st.text_input("اسم المشروع الاستراتيجي")
    
    # ... (بقية الكود الخاص بالـ 11 سؤال والمخرجات)
    
    # لوحة الإدارة (لا تظهر إلا لك)
    if st.session_state.is_admin:
        st.markdown("---")
        st.markdown(f'<a href="{EDIT_LINK}" target="_blank" class="admin-secret-panel">⚙️ الدخول لغرفة التحكم (مستشار منصور)</a>', unsafe_allow_html=True)
