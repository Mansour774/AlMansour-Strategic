import streamlit as st

# 1. إعدادات الهوية البصرية (Premium Executive)
st.set_page_config(page_title="المنصور استراتيجي", layout="centered")

# رابط التعديل المباشر (الخفيف) لراحتك
DIRECT_EDIT_URL = "https://github.com/Mansour774/AlMansour-Strategic/edit/main/app.py"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    * {{ font-family: 'Cairo', sans-serif; direction: rtl; }}
    .main {{ background-color: #0E1117; }}
    
    /* الشعار النصي الفخم */
    .logo-box {{ text-align: center; padding: 15px 0; }}
    .logo-main {{ color: #D4AF37; font-size: 2.5rem; font-weight: 800; line-height: 1; }}
    .logo-sub {{ color: #ffffff; font-size: 0.9rem; letter-spacing: 2px; border-top: 1px solid #D4AF37; padding-top: 5px; display: inline-block; opacity: 0.8; }}

    /* أزرار النظام */
    .stButton>button {{
        background: linear-gradient(90deg, #D4AF37 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 700 !important; border-radius: 8px !important;
        height: 3.2rem !important; border: none !important; transition: 0.3s;
    }}
    .trial-btn>button {{ background: #1a1c24 !important; color: #D4AF37 !important; border: 1px solid #D4AF37 !important; }}

    /* زر الواتساب */
    .wa-btn {{
        background-color: #25D366; color: white !important; padding: 10px;
        border-radius: 8px; text-decoration: none; display: flex;
        justify-content: center; font-weight: bold; margin-top: 10px; font-size: 0.9rem;
    }}

    /* رابط الإدارة الخفيف في الأسفل */
    .admin-link {{ position: fixed; left: 15px; bottom: 15px; font-size: 0.75rem; color: #444 !important; text-decoration: none; font-weight: bold; }}
    .admin-link:hover {{ color: #D4AF37 !important; }}
    </style>
    <a href="{DIRECT_EDIT_URL}" target="_blank" class="admin-link">⚙️ تعديل الكود المباشر</a>
    """, unsafe_allow_html=True)

# إدارة الحالة (الدخول والمراحل)
if 'auth' not in st.session_state: st.session_state.auth = False
if 'step' not in st.session_state: st.session_state.step = 1

# عرض الشعار في القمة
st.markdown('<div class="logo-box"><div class="logo-main">AL MANSOUR</div><div class="logo-sub">STRATEGIC SOLUTIONS</div></div>', unsafe_allow_html=True)

if not st.session_state.auth:
    st.markdown("<h3 style='text-align:center; color:#D4AF37;'>مرحباً بك في منصة الخبراء</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#E0E0E0;'>اختر وسيلة الدخول للبدء في إعداد تقريرك الاحترافي</p>", unsafe_allow_html=True)
    
    col_auth1, col_auth2 = st.columns(2)
    with col_auth1:
        if st.button("🚀 ابدأ تجربة مجانية"):
            st.session_state.auth = True
            st.session_state.mode = "Trial"
            st.rerun()
            
    with col_auth2:
        code = st.text_input("", placeholder="أدخل كود VIP للدخول الكامل", type="password")
        if st.button("تفعيل كود VIP"):
            if code == "M-77-VIP":
                st.session_state.auth = True
                st.session_state.mode = "VIP"
                st.rerun()
            else: st.error("الكود غير صحيح")

    st.markdown("<hr style='opacity:0.1;'>", unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/967774575749" class="wa-btn">💬 طلب كود تفعيل VIP (واتساب)</a>', unsafe_allow_html=True)

else:
    # واجهة العمل
    st.progress(st.session_state.step / 4)
    if st.session_state.get("mode") == "Trial":
        st.warning("⚠️ أنت الآن في وضع 'التجربة المجانية'")

    if st.session_state.step == 1:
        st.subheader("🏷️ المرحلة 1: بيانات الهوية")
        q1 = st.text_input("1. اسم المشروع", placeholder="مثال: التمكين الرقمي")
        q2 = st.text_input("2. الجهة المنفذة")
        q3 = st.text_input("3. عنوان النشاط")
        q4 = st.text_input("4. النطاق (زمان/مكان)")
        if st.button("التالي ⬅️"):
            st.session_state.update({"q1":q1,"q2":q2,"q3":q3,"q4":q4, "step":2}); st.rerun()

    elif st.session_state.step == 2:
        st.subheader("🎯 المرحلة 2: المضمون")
        q5 = st.text_input("5. إحصائيات الحضور")
        q6 = st.text_area("6. أهداف النشاط")
        col1, col2 = st.columns(2)
        if col1.button("➡️ السابق"): st.session_state.step = 1; st.rerun()
        if col2.button("التالي ⬅️"):
            st.session_state.update({"q5":q5,"q6":q6, "step":3}); st.rerun()

    elif st.session_state.step == 3:
        st.subheader("📈 المرحلة 3: التحليل")
        q7 = st.text_area("7. أهم الإنجازات")
        q8 = st.text_area("8. التحديات")
        q9 = st.text_area("9. الحلول")
        col1, col2 = st.columns(2)
        if col1.button("➡️ السابق"): st.session_state.step = 2; st.rerun()
        if col2.button("التالي ⬅️"):
            st.session_state.update({"q7":q7,"q8":q8,"q9":q9, "step":4}); st.rerun()

    elif st.session_state.step == 4:
        st.subheader("🏁 المرحلة 4: الختام")
        q10 = st.text_area("10. التوصيات")
        q11 = st.text_input("11. وصف الصور")
        col1, col2 = st.columns(2)
        if col1.button("➡️ السابق"): st.session_state.step = 3; st.rerun()
        if st.button("🚀 توليد التقرير النهائي"):
            st.balloons()
            res = f"STRATEGIC REPORT DATA\nPRJ: {st.session_state.q1}\nORG: {st.session_state.q2}\nGOALS: {st.session_state.q6}\nACHIEVEMENTS: {st.session_state.q7}"
            st.code(res)
            if st.button("إعادة البدء 🔄"):
                st.session_state.step = 1; st.rerun()

st.markdown("<p style='text-align:center; font-size:0.7rem; color:#444; margin-top:50px;'>منصور الوصابي © 2026</p>", unsafe_allow_html=True)
