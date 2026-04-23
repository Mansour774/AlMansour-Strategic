import streamlit as st

# 1. إعدادات الهوية البصرية (Premium Executive)
st.set_page_config(page_title="المنصور استراتيجي", layout="centered")

# رابط الإدارة الخاص بك لكي لا تنساه أبداً
ADMIN_LINK = "https://github.com/Mansour774/AlMansour-Strategic/edit/main/app.py"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    * {{ font-family: 'Cairo', sans-serif; direction: rtl; }}
    .main {{ background-color: #0E1117; }}
    
    /* الشعار النصي الفخم */
    .logo-box {{ text-align: center; padding: 10px 0; }}
    .logo-main {{ color: #D4AF37; font-size: 2.5rem; font-weight: 800; line-height: 1; }}
    .logo-sub {{ color: #ffffff; font-size: 1rem; letter-spacing: 2px; border-top: 1px solid #D4AF37; padding-top: 5px; display: inline-block; opacity: 0.8; }}

    /* توازن الخطوط والأزرار */
    .stButton>button {{
        background: linear-gradient(90deg, #D4AF37 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 700 !important; border-radius: 10px !important;
        height: 3.2rem !important; border: none !important;
    }}
    
    /* زر الواتساب */
    .wa-btn {{
        background-color: #25D366; color: white !important; padding: 12px;
        border-radius: 10px; text-decoration: none; display: flex;
        justify-content: center; font-weight: bold; margin-top: 10px;
    }}

    /* رابط الإدارة في الأسفل */
    .admin-link {{ position: fixed; left: 10px; bottom: 10px; font-size: 0.7rem; color: #333 !important; text-decoration: none; }}
    .admin-link:hover {{ color: #D4AF37 !important; }}
    </style>
    <a href="{ADMIN_LINK}" target="_blank" class="admin-link">⚙️ Management Portal</a>
    """, unsafe_allow_html=True)

# إدارة المراحل
if 'auth' not in st.session_state: st.session_state.auth = False
if 'step' not in st.session_state: st.session_state.step = 1

# عرض الشعار في القمة
st.markdown('<div class="logo-box"><div class="logo-main">AL MANSOUR</div><div class="logo-sub">STRATEGIC SOLUTIONS</div></div>', unsafe_allow_html=True)

if not st.session_state.auth:
    st.markdown("<h3 style='text-align:center; color:#D4AF37;'>🔑 نظام الدخول</h3>", unsafe_allow_html=True)
    code = st.text_input("أدخل كود VIP", type="password")
    if st.button("تفعيل النظام"):
        if code == "M-77-VIP": st.session_state.auth = True; st.rerun()
        else: st.error("الكود غير صحيح")
    st.markdown(f'<a href="https://wa.me/967774575749" class="wa-btn">💬 طلب كود (واتساب)</a>', unsafe_allow_html=True)

else:
    st.progress(st.session_state.step / 4)
    
    if st.session_state.step == 1:
        st.subheader("🏷️ المرحلة 1: الهوية")
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
        if col2.button("🚀 توليد التقرير"):
            st.balloons()
            st.code(f"PRJ: {st.session_state.q1}\nACHIEVEMENTS: {st.session_state.q7}")

st.markdown("<p style='text-align:center; font-size:0.7rem; color:#444; margin-top:50px;'>منصور الوصابي © 2026</p>", unsafe_allow_html=True)
