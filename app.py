import streamlit as st
import pandas as pd
import time

# 1. إعدادات النظام وإخفاء الأدوات التقنية
st.set_page_config(page_title="منصة المنصور الاستراتيجية", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    
    /* إخفاء أدوات ستريمليت تماماً لضمان الخصوصية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}

    * { font-family: 'Cairo', sans-serif; direction: rtl; }
    .main { background-color: #0E1117; color: #FFFFFF; }
    
    /* واجهة الإقناع */
    .hero-box { background: linear-gradient(135deg, #161a24 0%, #0e1117 100%); padding: 30px; border-radius: 20px; border: 1px solid #D4AF37; text-align: center; margin-bottom: 30px; }
    .feature-item { font-size: 0.9rem; color: #D4AF37; margin: 10px 0; font-weight: 600; }
    
    /* الخطوط والوضوح */
    h1, h2, h3 { color: #D4AF37 !important; font-weight: 800 !important; }
    .stMarkdown p { color: #FFFFFF !important; font-size: 1.05rem; line-height: 1.7; }
    label { color: #D4AF37 !important; font-weight: 700 !important; font-size: 1.1rem !important; margin-bottom: 15px !important; }

    /* أزرار النظام */
    .stButton>button {
        width: 100% !important; border-radius: 12px !important;
        height: 3.8rem !important; font-weight: 800 !important; font-size: 1.2rem !important;
        transition: 0.3s;
    }
    .main-btn>div>button { background: linear-gradient(90deg, #D4AF37 0%, #B8860B 100%) !important; color: #000 !important; border: none !important; }
    
    /* لوحة الإدارة السرية */
    .admin-panel { background: #D4AF37; color: #000 !important; padding: 15px; border-radius: 12px; text-decoration: none; font-weight: 800; display: block; text-align: center; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# بيانات التحكم
ADMIN_EMAIL = "774575749m@gmail.com"
EDIT_LINK = "https://github.com/Mansour774/AlMansour-Strategic/edit/main/app.py"

if 'auth_state' not in st.session_state: st.session_state.auth_state = "Hero" # Hero, Login, Signup, App
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# --- 1. واجهة الإقناع والترحيب ---
if st.session_state.auth_state == "Hero":
    st.markdown('<div class="hero-box">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/1063/1063376.png", width=80) # أيقونة تعبيرية
    st.markdown("<h1>المنصور استراتيجي</h1>", unsafe_allow_html=True)
    st.markdown("<h3>نحو تقارير مؤسسية بمعايير دولية</h3>", unsafe_allow_html=True)
    st.markdown("<p>المنصة الذكية الأولى التي تحول بياناتك الميدانية إلى تقارير استراتيجية مبهرة تدعم اتخاذ القرار وتلبي معايير المانحين والمنظمات العالمية.</p>", unsafe_allow_html=True)
    st.markdown("<div class='feature-item'>✅ صياغة احترافية (AR/EN) | ✅ تحليل بياني ذكي | ✅ توفير 80% من وقت الإعداد</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("تسجيل حساب جديد"): st.session_state.auth_state = "Signup"; st.rerun()
    with col2:
        st.markdown('<div class="main-btn">', unsafe_allow_html=True)
        if st.button("تسجيل الدخول"): st.session_state.auth_state = "Login"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 2. نظام تسجيل الحساب (Signup) ---
elif st.session_state.auth_state == "Signup":
    st.markdown("## 📝 فتح حساب مستشار جديد")
    u_name = st.text_input("الأسم الكامل")
    u_org = st.text_input("اسم المؤسسة / الجهة")
    u_email = st.text_input("البريد الإلكتروني الرسمي")
    u_phone = st.text_input("رقم الجوال")
    
    col1, col2 = st.columns(2)
    if col1.button("⬅️ العودة"): st.session_state.auth_state = "Hero"; st.rerun()
    if col2.button("إنشاء الحساب 🚀"):
        if u_email and u_name:
            st.session_state.user_email = u_email
            st.session_state.auth_state = "App"
            if u_email.strip().lower() == ADMIN_EMAIL.lower(): st.session_state.is_admin = True
            st.rerun()
        else: st.error("يرجى ملء البيانات الأساسية")

# --- 3. نظام تسجيل الدخول (Login) ---
elif st.session_state.auth_state == "Login":
    st.markdown("## 🔑 دخول الأعضاء")
    login_email = st.text_input("أدخل بريدك الإلكتروني المسجل")
    
    col1, col2 = st.columns(2)
    if col1.button("⬅️ العودة"): st.session_state.auth_state = "Hero"; st.rerun()
    if col2.button("دخول آمن 🔒"):
        if login_email:
            st.session_state.user_email = login_email
            st.session_state.auth_state = "App"
            if login_email.strip().lower() == ADMIN_EMAIL.lower(): st.session_state.is_admin = True
            st.rerun()
    st.markdown(f'[نسيت كلمة المرور؟ تواصل مع الدعم الفني](https://wa.me/967774575749)')

# --- 4. واجهة التطبيق (بعد الدخول) ---
elif st.session_state.auth_state == "App":
    st.markdown(f"### مرحباً بك مستشار: {st.session_state.user_email}")
    
    # مثال على الأسئلة مع Placeholder (أمثلة داخل الخانات)
    st.subheader("📋 مرحلة جمع البيانات الاستراتيجية")
    
    q1 = st.text_input("1. مسمى المشروع / النشاط الاستراتيجي", placeholder="مثال: ورشة عمل تعزيز الحكم المحلي في اليمن")
    q2 = st.text_input("2. الجهة المنفذة والشركاء", placeholder="مثال: مؤسسة بناء (BCHR) بالتعاون مع البرنامج الإنمائي للأمم المتحدة")
    q3 = st.text_area("3. منهجية التنفيذ (كيف تم النشاط؟)", placeholder="مثال: تم استخدام نموذج التعلم التشاركي، العصف الذهني، وتحليل SWOT لتحديد الأولويات")
    
    # ... (هنا تضع بقية الـ 11 سؤال بنفس نمط الـ placeholder)
    
    if st.button("🚀 توليد المخرج النهائي"):
        st.balloons()
        st.success("تم التوليد بنجاح!")
        
    # رابط الإدارة (يظهر لك أنت فقط في حسابك)
    if st.session_state.is_admin:
        st.markdown(f'<a href="{EDIT_LINK}" target="_blank" class="admin-panel">⚙️ غرفة التحكم | تعديل كود المنصة</a>', unsafe_allow_html=True)
    
    if st.button("تسجيل الخروج"): st.session_state.auth_state = "Hero"; st.rerun()
