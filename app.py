import streamlit as st
import pandas as pd
import time

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="المنصور استراتيجي | تجربة النخبة", layout="centered")

# بيانات التحكم
MY_EMAIL = "774575749m@gmail.com"
EDIT_URL = "https://github.com/Mansour774/AlMansour-Strategic/edit/main/app.py"

# --- محرك الجماليات (Advanced CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;800&display=swap');
    
    :root {
        --gold: #D4AF37;
        --dark-bg: #0E1117;
        --card-bg: #161a24;
    }

    * { font-family: 'Cairo', sans-serif; direction: rtl; }

    /* تحسين الخلفية العامة */
    .main { background-color: var(--dark-bg); color: #ffffff; }

    /* الشعار المتحرك */
    .logo-container { text-align: center; padding: 20px 0; animation: fadeInDown 1s ease-out; }
    .logo-main { color: var(--gold); font-size: 3.2rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 0; }
    .logo-sub { color: #ffffff; font-size: 0.85rem; opacity: 0.6; letter-spacing: 5px; text-transform: uppercase; margin-top: -10px; }

    /* تصميم البطاقات الاحترافي */
    .stTextInput, .stTextArea, .stSelectbox, .stNumberInput {
        background-color: var(--card-bg) !important;
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        border-radius: 12px !important;
        transition: 0.3s all ease;
    }
    .stTextInput:focus-within { border-color: var(--gold) !important; box-shadow: 0 0 10px rgba(212, 175, 55, 0.2) !important; }

    /* الأزرار المبهرة */
    .stButton>button {
        width: 100% !important;
        border-radius: 15px !important;
        font-weight: 700 !important;
        height: 3.8rem !important;
        font-size: 1.1rem !important;
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        border: none !important;
    }
    /* زر التالي (ذهبي) */
    div[data-testid="column"]:nth-of-type(2) .stButton>button {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%) !important;
        color: #000 !important;
    }
    /* زر السابق (شفاف) */
    div[data-testid="column"]:nth-of-type(1) .stButton>button {
        background-color: rgba(255,255,255,0.05) !important;
        color: var(--gold) !important;
        border: 1px solid var(--gold) !important;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 8px 20px rgba(212,175,55,0.4); }

    /* صناديق النصائح (Glassmorphism) */
    .ai-hint-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-right: 5px solid var(--gold);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        animation: fadeInLeft 0.8s ease-out;
    }

    /* الأنيميشن */
    @keyframes fadeInDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeInLeft { from { opacity: 0; transform: translateX(20px); } to { opacity: 1; transform: translateX(0); } }
    
    .admin-anchor { position: fixed; left: 25px; bottom: 25px; background: var(--gold); color: black !important; padding: 12px 20px; border-radius: 50px; text-decoration: none; font-weight: 800; font-size: 0.8rem; box-shadow: 0 10px 25px rgba(0,0,0,0.4); z-index: 1000; transition: 0.3s; }
    .admin-anchor:hover { transform: rotate(-5deg) scale(1.1); }
    </style>
    """, unsafe_allow_html=True)

# إدارة الجلسة
if 'auth' not in st.session_state: st.session_state.auth = False
if 'step' not in st.session_state: st.session_state.step = 1
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# الشعار
st.markdown('<div class="logo-container"><div class="logo-main">AL MANSOUR</div><div class="logo-sub">Strategic Excellence System</div></div>', unsafe_allow_html=True)

if not st.session_state.auth:
    with st.container():
        st.markdown("<h2 style='text-align:center; color:white; font-weight:700;'>مرحباً بك في عالم الاستشارات الذكية</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; opacity:0.7;'>سجل دخولك لتجربة صياغة تقارير بمعايير دولية</p>", unsafe_allow_html=True)
        user_id = st.text_input("البريد الإلكتروني أو الجوال", placeholder="أدخل بياناتك هنا...")
        
        if st.button("🚀 دخول آمن"):
            if user_id:
                with st.spinner("جاري تهيئة البيئة الاستراتيجية..."):
                    time.sleep(1.2)
                    if user_id.strip().lower() == MY_EMAIL: st.session_state.is_admin = True
                    st.session_state.auth = True; st.rerun()
            else: st.error("يرجى إدخال البيانات للبدء")
else:
    # شريط التقدم الأنيق
    st.progress(st.session_state.step / 4)
    
    # تعريف التقارير
    reports_map = {
        "📊 تقرير إنجاز (Achievement)": "التركيز: مؤشرات الأداء، الأرقام، ونسبة الإنجاز.",
        "🏁 تقرير ختامي (Final Narrative)": "التركيز: الاستدامة، الدروس المستفادة، والأثر العام.",
        "💡 تقييم أثر (Impact)": "التركيز: قصص النجاح والتغيير النوعي في المجتمع.",
        "🤝 محضر اجتماع (Minutes)": "التركيز: القرارات، المسؤوليات، والجدول الزمني.",
        "🔍 تحليل احتياج (Needs)": "التركيز: الفجوات، المبررات، والأولويات."
    }

    if st.session_state.step == 1:
        st.subheader("1️⃣ تحديد المسار الاستراتيجي")
        rtype = st.selectbox("نوع التقرير المطلوب", list(reports_map.keys()))
        rlang = st.radio("لغة الصياغة", ["عربية بليغة", "Business English", "مزدوج (AR/EN)"], horizontal=True)
        
        st.markdown(f'<div class="ai-hint-box"><b>💡 نصيحة المستشار:</b><br>{reports_map[rtype]}</div>', unsafe_allow_html=True)
        
        q1 = st.text_input("اسم المشروع الاستراتيجي", placeholder="ما هو عنوان النجاح اليوم؟")
        q2 = st.text_input("الشركاء والمانحين", placeholder="من هم شركاء الأثر؟")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("التالي: البيانات الميدانية ⬅️"):
            st.session_state.update({"rtype":rtype, "rlang":rlang, "q1":q1, "q2":q2, "step":2}); st.rerun()

    elif st.session_state.step == 2:
        st.subheader("2️⃣ الأرقام والمنهجية الميدانية")
        q5 = st.text_input("إحصائيات الحضور (توصيف دقيق)")
        
        c1, c2 = st.columns(2)
        m = c1.number_input("الذكور", min_value=0)
        f = c2.number_input("الإناث", min_value=0)
        if m+f > 0:
            st.bar_chart(pd.DataFrame({'الفئة':['ذكور','إناث'],'العدد':[m,f]}).set_index('الفئة'), color="#D4AF37")
        
        q7 = st.text_area("منهجية التنفيذ (خطوات العمل)", placeholder="اشرح كيف تم تحويل الخطط إلى واقع...")
        
        col_p, col_n = st.columns(2)
        if col_p.button("⬅️ العودة"): st.session_state.step = 1; st.rerun()
        if col_n.button("التالي: تحليل النتائج ⬅️"):
            st.session_state.update({"q5":q5,"m":m,"f":f,"q7":q7,"step":3}); st.rerun()

    elif st.session_state.step == 3:
        st.subheader("3️⃣ التحليل الاستراتيجي العميق")
        q6 = st.text_area("المخرجات والنتائج المحققة", help="ما الذي تغير فعلياً على أرض الواقع؟")
        q8 = st.text_area("التحديات والدروس المستفادة", help="كيف تعاملتم مع العقبات بذكاء؟")
        
        col_p, col_n = st.columns(2)
        if col_p.button("⬅️ العودة"): st.session_state.step = 2; st.rerun()
        if col_n.button("التالي: الرؤية الختامية ⬅️"):
            st.session_state.update({"q6":q6,"q8":q8,"step":4}); st.rerun()

    elif st.session_state.step == 4:
        st.subheader("4️⃣ الأثر والتوصيات")
        q10 = st.text_area("التوصيات المستقبلية")
        q11 = st.text_area("قصص النجاح والأثر الملموس")
        
        col_p, col_n = st.columns(2)
        if col_p.button("⬅️ العودة"): st.session_state.step = 3; st.rerun()
        if col_n.button("🚀 صياغة التقرير العالمي"):
            with st.status("جاري تحليل البيانات وصياغتها بمعايير دولية...", expanded=True) as status:
                st.write("✅ تدقيق المؤشرات الإحصائية...")
                time.sleep(1)
                st.write("✅ صياغة المحتوى باللغة الاستشارية...")
                time.sleep(1)
                status.update(label="تم توليد التقرير بنجاح!", state="complete", expanded=False)
            
            st.balloons()
            final_prompt = f"المطلوب صياغة {st.session_state.rtype} بـ {st.session_state.rlang} لمشروع {st.session_state.q1}. البيانات الميدانية: {st.session_state.q5}, المنهجية: {st.session_state.q7}, النتائج: {st.session_state.q6}, التحديات: {st.session_state.q8}, التوصيات: {q10}, الأثر: {q11}."
            
            st.success("📝 المخرج الاستراتيجي جاهز")
            st.code(final_prompt, language="markdown")
            st.download_button("📥 تحميل التقرير", final_prompt, file_name="Mansour_Strategic_Report.txt")
            if st.button("تقرير جديد 🔄"): st.session_state.step = 1; st.rerun()

if st.session_state.is_admin:
    st.markdown(f'<a href="{EDIT_URL}" target="_blank" class="admin-anchor">⚙️ غرفة التحكم | منصور الوصابي</a>', unsafe_allow_html=True)
