import streamlit as st
import pandas as pd
import time
import random

# 1. إعدادات الهوية البصرية الفائقة
st.set_page_config(page_title="المنصور استراتيجي | PRO V18", layout="centered")

# بيانات المدير (المتحكم الوحيد)
ADMIN_EMAIL = "774575749m@gmail.com"
GITHUB_EDIT_LINK = "https://github.com/Mansour774/AlMansour-Strategic/edit/main/app.py"

# --- محرك التصميم المتقدم (تحسين التباين والوضوح) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    * { font-family: 'Cairo', sans-serif; direction: rtl; }
    .main { background-color: #0E1117; color: #FFFFFF; }
    
    /* تحسين وضوح الخطوط */
    h1, h2, h3 { color: #D4AF37 !important; font-weight: 800 !important; }
    label { color: #FFFFFF !important; font-weight: 700 !important; font-size: 1.15rem !important; background: rgba(212,175,55,0.05); padding: 5px 10px; border-radius: 5px; display: block; margin-bottom: 12px !important; }
    .stMarkdown p { color: #F0F0F0 !important; font-size: 1rem; }

    /* حقول الإدخال الاحترافية */
    .stTextInput input, .stTextArea textarea {
        background-color: #1A1E29 !important;
        color: #FFFFFF !important;
        border: 1px solid #3d4455 !important;
        border-radius: 12px !important;
        font-size: 1rem !important;
    }
    .stTextInput input:focus { border-color: #D4AF37 !important; }

    /* الأزرار الملكية */
    .stButton>button {
        width: 100% !important; border-radius: 12px !important;
        height: 3.8rem !important; font-weight: 800 !important; font-size: 1.2rem !important;
        transition: 0.3s all ease;
    }
    /* زر التأكيد (ذهبي) */
    div[data-testid="column"]:nth-of-type(2) .stButton>button {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%) !important; color: #000 !important; border: none !important;
    }
    
    /* شارة الباقة */
    .package-badge { padding: 8px 20px; border-radius: 50px; font-weight: bold; border: 1px solid #D4AF37; color: #D4AF37; }
    .admin-only-btn { background: #D4AF37 !important; color: black !important; font-weight: bold; text-decoration: none; padding: 10px 20px; border-radius: 10px; display: inline-block; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الحالة الأمنية ---
if 'is_logged_in' not in st.session_state: st.session_state.is_logged_in = False
if 'waiting_otp' not in st.session_state: st.session_state.waiting_otp = False
if 'user_role' not in st.session_state: st.session_state.user_role = "User"
if 'step' not in st.session_state: st.session_state.step = 1

# الأكواد المعتمدة (VIP)
VIP_CODES = {"MANSOUR-GOLD": "الباقة الذهبية (مفتوح)", "YEMEN-2026": "الباقة الفضية (10 تقارير)"}

# --- شاشة الدخول والتحقق ---
if not st.session_state.is_logged_in:
    st.markdown("<h1 style='text-align:center;'>بوابة المنصور الاستراتيجية</h1>", unsafe_allow_html=True)
    
    if not st.session_state.waiting_otp:
        st.subheader("🔑 تسجيل الدخول")
        email_input = st.text_input("أدخل بريدك الإلكتروني الرسمي", placeholder="example@domain.com")
        if st.button("إرسال رمز التفعيل 📧"):
            if "@" in email_input and "." in email_input:
                # محاكاة إرسال OTP
                st.session_state.temp_email = email_input
                st.session_state.waiting_otp = True
                st.session_state.generated_otp = str(random.randint(1000, 9999))
                # في النسخة الحقيقية سيرسل إيميل، هنا سنظهره للمدير فقط للتجربة
                if email_input == ADMIN_EMAIL: 
                    st.info(f"كود التحقق الخاص بك هو: {st.session_state.generated_otp}")
                st.rerun()
            else: st.error("يرجى إدخال إيميل صحيح")
    else:
        st.subheader("✅ تم إرسال الرمز")
        otp_val = st.text_input(f"أدخل الرمز المرسل إلى {st.session_state.temp_email}", placeholder="4 أرقام")
        if st.button("تأكيد الرمز والدخول"):
            if otp_val == st.session_state.generated_otp:
                st.session_state.is_logged_in = True
                if st.session_state.temp_email == ADMIN_EMAIL: st.session_state.user_role = "Admin"
                st.success("تم التحقق بنجاح!")
                time.sleep(1); st.rerun()
            else: st.error("الرمز غير صحيح")
        if st.button("تغيير الإيميل"): st.session_state.waiting_otp = False; st.rerun()

# --- واجهة العمل الاستراتيجية ---
else:
    # هيدر المستخدم
    st.markdown(f"<div style='text-align:left;'><span class='package-badge'>الدور: {st.session_state.user_role}</span></div>", unsafe_allow_html=True)
    st.progress(st.session_state.step / 4)

    # المرحلة 1
    if st.session_state.step == 1:
        st.subheader("1️⃣ معلومات النشاط والسياق")
        q1 = st.text_input("اسم المشروع / النشاط الاستراتيجي", placeholder="مثال: ورشة عمل التخطيط التشغيلي للمنظمات")
        q2 = st.text_input("الجهة المنفذة والشركاء", placeholder="مثال: مركز المنصور بالتعاون مع وزارة التخطيط")
        q3 = st.text_input("الموقع والزمان", placeholder="مثال: عدن، قاعة الفخامة - مايو 2026")
        
        if st.button("التالي ⬅️"):
            st.session_state.update({"q1":q1,"q2":q2,"q3":q3, "step":2}); st.rerun()

    # المرحلة 2
    elif st.session_state.step == 2:
        st.subheader("2️⃣ الإحصائيات والمنهجية")
        q5 = st.text_area("توصيف المستفيدين (أرقام دقيقة)", placeholder="مثال: 50 متدرب (20 مدراء أقسام، 30 موظفين ميدانيين)")
        
        c1, c2 = st.columns(2)
        m = c1.number_input("عدد الذكور", min_value=0)
        f = c2.number_input("عدد الإناث", min_value=0)
        if m+f > 0:
            st.bar_chart(pd.DataFrame({'الجنس':['ذكور','إناث'],'العدد':[m,f]}).set_index('الجنس'), color="#D4AF37")
            
        q7 = st.text_area("منهجية التنفيذ المعتمدة", placeholder="مثال: تم استخدام نموذج SWOT وتحليل الفجوات GAP Analysis")
        
        col_p, col_n = st.columns(2)
        if col_p.button("⬅️ السابق"): st.session_state.step = 1; st.rerun()
        if col_n.button("التالي ⬅️"):
            st.session_state.update({"q5":q5,"m":m,"f":f,"q7":q7,"step":3}); st.rerun()

    # المرحلة 3
    elif st.session_state.step == 3:
        st.subheader("3️⃣ التحليل الاستراتيجي والنتائج")
        q6 = st.text_area("الأهداف المحققة (Outcomes)", placeholder="مثال: الخروج بخطة تشغيلية معمدة لعام 2027")
        q8 = st.text_area("التحديات والحلول المنفذة", placeholder="مثال: ضيق الوقت، وتم حله بتمديد ساعات الورشة المسائية")
        
        col_p, col_n = st.columns(2)
        if col_p.button("⬅️ السابق"): st.session_state.step = 2; st.rerun()
        if col_n.button("التالي ⬅️"):
            st.session_state.update({"q6":q6,"q8":q8,"step":4}); st.rerun()

    # المرحلة 4
    elif st.session_state.step == 4:
        st.subheader("4️⃣ الأثر والتوصيات الختامية")
        q10 = st.text_area("التوصيات الاستراتيجية للمستقبل", placeholder="مثال: ضرورة الانتقال لمرحلة الأتمتة الكاملة للتقارير")
        q11 = st.text_area("قصة أثر أو نجاح ملموسة", placeholder="مثال: إشادة المانحين بسرعة وجودة المخرجات الميدانية")
        
        col_p, col_n = st.columns(2)
        if col_p.button("⬅️ السابق"): st.session_state.step = 3; st.rerun()
        if st.button("🚀 صياغة التقرير وتصديره"):
            st.balloons()
            final_report = f"تقرير {st.session_state.q1} | الجهة: {st.session_state.q2} | الإحصائيات: {st.session_state.m} ذكور و {st.session_state.f} إناث | النتائج: {st.session_state.q6} | الأثر: {q11}"
            st.success("✅ التقرير جاهز بمعايير دولية")
            st.code(final_report)
            st.download_button("📥 تحميل PDF/Text", final_report, file_name="Strategic_Report.txt")

    # --- الجزء الخاص بالمدير فقط (مخفي تماماً عن الآخرين) ---
    if st.session_state.user_role == "Admin":
        st.markdown("---")
        with st.expander("🔐 لوحة تحكم الإدارة العليا (ظاهرة لك فقط)"):
            st.write("أهلاً يا مستشار منصور، يمكنك تعديل النظام من هنا:")
            st.markdown(f'<a href="{GITHUB_EDIT_LINK}" target="_blank" class="admin-only-btn">⚙️ تعديل كود المنصة على GitHub</a>', unsafe_allow_html=True)
            if st.button("توليد كود VIP جديد"):
                st.code(f"VIP-{random.randint(1000,9999)}")
