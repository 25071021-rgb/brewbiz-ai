import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="BrewBiz AI | Trợ Lý Tăng Trưởng Kinh Doanh",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# TalkPal / GenZ Inspired Modern Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .stApp {
        background: #F8FAFC;
    }
    
    /* Hero Banner TalkPal Style */
    .hero-container {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #EC4899 100%);
        padding: 40px 30px;
        border-radius: 24px;
        color: white;
        text-align: center;
        box-shadow: 0 20px 25px -5px rgba(124, 58, 237, 0.25);
        margin-bottom: 25px;
    }
    
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        font-size: 1.15rem;
        opacity: 0.95;
        max-width: 750px;
        margin: 0 auto 20px auto;
        line-height: 1.6;
    }
    
    .pill-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(8px);
        padding: 6px 16px;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 4px;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Feature Card TalkPal Style */
    .feature-card {
        background: white;
        border-radius: 20px;
        padding: 24px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.04);
        transition: all 0.3s ease;
        margin-bottom: 20px;
        height: 100%;
    }
    
    .card-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 800;
        margin-bottom: 12px;
    }
    
    .badge-purple { background: #F3E8FF; color: #7E22CE; }
    .badge-orange { background: #FFEDD5; color: #C2410C; }
    .badge-pink { background: #FCE7F3; color: #BE185D; }
    .badge-green { background: #DCFCE7; color: #15803D; }
    
    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 8px;
    }
    
    .card-desc {
        font-size: 0.9rem;
        color: #64748B;
        line-height: 1.5;
        margin-bottom: 16px;
    }
    
    /* Stats Bar */
    .stat-box {
        background: white;
        padding: 16px 20px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        text-align: center;
    }
    .stat-number {
        font-size: 1.6rem;
        font-weight: 800;
        color: #4F46E5;
    }
    .stat-label {
        font-size: 0.8rem;
        color: #64748B;
        font-weight: 600;
    }
    
    /* Output Box */
    .ai-output-box {
        background: #F1F5F9;
        border-left: 5px solid #8B5CF6;
        padding: 20px;
        border-radius: 12px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Session State for Page Navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

# Sidebar Navigation
st.sidebar.title("☕ BREWBIZ AI")
st.sidebar.caption("Trợ Lý Tăng Trưởng Kinh Doanh & Marketing")

nav_choice = st.sidebar.radio(
    "ĐIỀU HƯỚNG NHANH:",
    [
        "🏠 Trang Chủ Overview",
        "📈 1. Phân Tích Doanh Thu & Báo Cáo",
        "🎯 2. Trình Thiết Lập Chiến Dịch & Ngân Sách",
        "🎬 3. Xưởng Sáng Tạo Content & TikTok",
        "🛡️ 4. Trung Tâm Phê Duyệt SafeGuard"
    ]
)

# Page Router
if nav_choice == "🏠 Trang Chủ Overview":
    st.session_state.current_page = "home"
elif nav_choice == "📈 1. Phân Tích Doanh Thu & Báo Cáo":
    st.session_state.current_page = "reporting"
elif nav_choice == "🎯 2. Trình Thiết Lập Chiến Dịch & Ngân Sách":
    st.session_state.current_page = "campaign"
elif nav_choice == "🎬 3. Xưởng Sáng Tạo Content & TikTok":
    st.session_state.current_page = "content"
elif nav_choice == "🛡️ 4. Trung Tâm Phê Duyệt SafeGuard":
    st.session_state.current_page = "safeguard"

# ==========================================
# PAGE 0: TRANG CHỦ (LANDING OVERVIEW)
# ==========================================
if st.session_state.current_page == "home":
    st.markdown("""
    <div class="hero-container">
        <span class="pill-badge">✨ ALL-IN-ONE AI FOR RETAIL & F&B</span>
        <div class="hero-title">BREWBIZ AI ☕</div>
        <div class="hero-subtitle">
            Biến số liệu thô thành chiến lược tăng trưởng & bài viết triệu view chỉ trong 1-Click! 
            Tối ưu hóa toàn bộ quy trình vận hành cho chuỗi cửa hàng & thương hiệu của bạn.
        </div>
        <div>
            <span class="pill-badge">⚡ Báo Cáo Tự Động</span>
            <span class="pill-badge">🎯 Lập Campaign & Budget</span>
            <span class="pill-badge">🎬 Gen Z Content Studio</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics Highlights
    st.markdown("### 📊 THỐNG KÊ HOẠT ĐỘNG MÔ PHỎNG (CASE STUDY THE COFFEE HOUSE)")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="stat-box"><div class="stat-number">485 Tỷ</div><div class="stat-label">Doanh thu Quý ước tính</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-box"><div class="stat-number">800 Tr</div><div class="stat-label">Ngân sách Campaign Mùa Đông</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-box"><div class="stat-number">20s</div><div class="stat-label">Kịch bản TikTok/Reels</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">Duyệt An toàn SafeGuard</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🚀 CHỌN CHỨC NĂNG BẠN MUỐN SỬ DỤNG")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="feature-card">
            <span class="card-badge badge-purple">📈 PHÂN HỆ 1</span>
            <div class="card-title">Phân Tích Doanh Thu & Báo Cáo AI</div>
            <div class="card-desc">Tự động nhập số liệu doanh thu, đọc vị tỷ trọng sản phẩm (Đồ uống, Bánh, Đóng gói) và xuất ngay Executive Summary chuẩn C-Level.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 Bắt đầu Phân tích Doanh thu", key="btn_rep"):
            st.session_state.current_page = "reporting"
            st.rerun()

    with col_b:
        st.markdown("""
        <div class="feature-card">
            <span class="card-badge badge-orange">🎯 PHÂN HỆ 2 (MỚI: CỰC HỮU ÍCH)</span>
            <div class="card-title">Trình Thiết Lập Chiến Dịch & Ngân Sách</div>
            <div class="card-desc">Gõ tên chiến dịch + ngân sách ➔ AI tự tính bài toán chia tiền (Ads, KOLs, Content, Event), lập timeline 4 tuần và dự báo doanh số!</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 Thiết Lập Kế Hoạch & Ngân Sách", key="btn_camp"):
            st.session_state.current_page = "campaign"
            st.rerun()

    col_c, col_d = st.columns(2)
    with col_c:
        st.markdown("""
        <div class="feature-card">
            <span class="card-badge badge-pink">🎬 PHÂN HỆ 3</span>
            <div class="card-title">Xưởng Sáng Tạo Content & TikTok Studio</div>
            <div class="card-desc">Nhập ý kiến cá nhân (món mới, thời tiết, deal HOT) ➔ AI gen bài viết Social, kịch bản TikTok 20s theo đúng mong muốn của bạn.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 Vào Xưởng Sáng Tạo Content", key="btn_cont"):
            st.session_state.current_page = "content"
            st.rerun()

    with col_d:
        st.markdown("""
        <div class="feature-card">
            <span class="card-badge badge-green">🛡️ PHÂN HỆ 4</span>
            <div class="card-title">Trung Tâm Phê Duyệt & SafeGuard</div>
            <div class="card-desc">Quy trình Human-in-the-Loop 5 bước giúp kiểm soát rủi ro thông tin sai lệch, bảo vệ uy tín thương hiệu trước khi duyệt chi ngân sách.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 Xem Quy Trình Duyệt An Toàn", key="btn_safe"):
            st.session_state.current_page = "safeguard"
            st.rerun()

# ==========================================
# PAGE 1: BÁO CÁO & PHÂN TÍCH DOANH THU
# ==========================================
elif st.session_state.current_page == "reporting":
    if st.button("⬅️ Quay lại Trang Chủ Overview"):
        st.session_state.current_page = "home"
        st.rerun()
        
    st.header("📈 Phân Hệ 1: Phân Tích Doanh Thu & Báo Cáo AI")
    st.caption("Mô phỏng dữ liệu tài chính The Coffee House & Đề xuất chiến lược tự động")
    
    st.markdown("#### 1. Nhập Dữ Liệu Doanh Thu")
    c1, c2 = st.columns(2)
    with c1:
        rev = st.number_input("Tổng doanh thu quý (Tỷ VNĐ)", value=485.0, step=10.0)
        growth = st.number_input("Tăng trưởng QoQ (%)", value=12.0)
    with c2:
        bev = st.slider("Tỷ trọng Đồ uống (%)", 0, 100, 66)
        bakery = st.slider("Tỷ trọng Bánh & Đồ ăn (%)", 0, 100-bev, 20)
        packaged = 100 - bev - bakery
        st.info(f"Sản phẩm đóng gói (Cà phê hòa tan/hạt): **{packaged}%**")

    df = pd.DataFrame({
        "Danh mục sản phẩm": ["Đồ uống (Beverages)", "Bánh & Đồ ăn (Bakery & Food)", "Cà phê đóng gói (Packaged)"],
        "Tỷ trọng (%)": [bev, bakery, packaged],
        "Doanh thu ước tính (Tỷ VNĐ)": [rev*bev/100, rev*bakery/100, rev*packaged/100]
    })
    
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("Danh mục sản phẩm")["Doanh thu ước tính (Tỷ VNĐ)"])

    st.markdown("#### 2. AI Executive Summary & Đề Xuất Chiến Lược")
    st.success(f"💡 **Tóm tắt điều hành:** Tổng doanh thu đạt **{rev:,.0f} Tỷ VNĐ** (+{growth}% so với quý trước). Mảng Đồ uống đóng góp lớn nhất với **{bev}%** ({rev*bev/100:.1f} Tỷ VNĐ).")
    
    st.markdown("""
    **🚀 3 Khuyến nghị hành động từ AI Analyst:**
    1. **Tối ưu hóa Combo Upsell:** Kết hợp bán kèm Đồ uống + Bánh ngọt để nâng giá trị đơn hàng trung bình (AOV) từ 65k lên 85k.
    2. **Đẩy mạnh dòng sản phẩm theo mùa:** Ra mắt bộ sưu tập đồ uống nóng cho mùa lạnh để khai thác nhu cầu tăng cao.
    3. **Tự động hóa báo cáo tuần:** Sử dụng AI để tổng hợp dữ liệu giao dịch hàng ngày, giúp bộ phận vận hành phát hiện sớm cửa hàng tăng trưởng chậm.
    """)

# ==========================================
# PAGE 2: TRÌNH THIẾT LẬP CHIẾN DỊCH & NGÂN SÁCH (INTERACTIVE & USEFUL)
# ==========================================
elif st.session_state.current_page == "campaign":
    if st.button("⬅️ Quay lại Trang Chủ Overview"):
        st.session_state.current_page = "home"
        st.rerun()

    st.header("🎯 Phân Hệ 2: Trình Thiết Lập Chiến Dịch & Phân Bổ Ngân Sách Smart")
    st.caption("Công cụ tương tác giúp biến ý tưởng Marketing thành Bài toán Tài chính & Lộ trình triển khai cụ thể!")

    st.markdown("---")
    st.subheader("🛠️ Bước 1: Nhập Thông Tin Chiến Dịch Của Bạn")
    
    col1, col2 = st.columns(2)
    with col1:
        camp_name = st.text_input("Tên Chiến Dịch Marketing", value="Mùa Đông Ấm Áp")
        slogan = st.text_input("Slogan / Thông Điệp Cốt Lõi", value="Ấm áp từng khoảnh khắc")
        budget_input = st.number_input("Tổng Ngân Sách Dự Kiến (VNĐ)", value=800000000, step=50000000, format="%d")
    
    with col2:
        goal_option = st.selectbox(
            "Mục Tiêu Kinh Doanh Chính",
            [
                "🔥 Tăng 20% doanh số dòng đồ uống mùa đông",
                "✨ Ra mắt Món Mới (New Product Launch)",
                "🎯 Thu hút Khách hàng Gen Z & Sinh viên",
                "📈 Nâng cao giá trị đơn hàng trung bình (AOV)"
            ]
        )
        duration_weeks = st.slider("Thời Gian Triển Khai (Tháng/Tuần)", 2, 8, 4)

    st.markdown("---")
    st.subheader("💡 Bước 2: AI Tự Động Phân Bổ Ngân Sách & Dự Báo Chỉ Số")
    
    # Calculate Forecasts based on Budget
    est_reach = int(budget_input / 40)  # CPM ~ 40 VND
    est_vouchers = int(budget_input / 8000) # Cost per voucher red = 8k
    est_revenue_boost = budget_input * 3.2 # ROI 3.2x

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("👁️ Lượt Tiếp Cận Dự Kiến (Reach)", f"{est_reach:,.0f} lượt")
    with c2:
        st.metric("🎟️ Số Voucher Ưu Đãi Phát Ra", f"{est_vouchers:,.0f} lượt")
    with c3:
        st.metric("💰 Doanh Số Tăng Thêm Dự Báo (ROI 3.2x)", f"{est_revenue_boost:,.0f} VNĐ")

    st.markdown("#### Bảng Phân Bổ Ngân Sách Chi Tiết (Cho phép điều chỉnh):")
    
    p_ads = st.slider("1. Quảng cáo Mạng xã hội (Facebook/Instagram/TikTok Ads) %", 10, 60, 40)
    p_content = st.slider("2. Sản xuất Nội dung & Kịch bản %", 10, 40, 20)
    p_kol = st.slider("3. Hợp tác KOLs & Food Reviewers %", 5, 30, 15)
    p_instore = st.slider("4. Trang trí Cửa hàng & POSM %", 5, 20, 10)
    p_promo = 100 - p_ads - p_content - p_kol - p_instore

    if p_promo < 0:
        st.error("⚠️ Tổng phần trăm vượt quá 100%! Vui lòng giảm bớt các thanh trượt.")
    else:
        st.info(f"5. Hoạt động Khuyến mãi & Minigame (Tự động): **{p_promo}%**")

        b_df = pd.DataFrame({
            "Hạng Mục Chi Phí": [
                "Quảng cáo Mạng xã hội (Paid Ads)",
                "Sản xuất Nội dung & Media",
                "Hợp tác KOLs & Creators",
                "Trang trí Cửa hàng & POSM",
                "Khuyến mãi & Minigame"
            ],
            "Tỷ Lệ (%)": [p_ads, p_content, p_kol, p_instore, p_promo],
            "Ngân Sách Ước Tính (VNĐ)": [
                budget_input * p_ads / 100,
                budget_input * p_content / 100,
                budget_input * p_kol / 100,
                budget_input * p_instore / 100,
                budget_input * p_promo / 100
            ]
        })
        st.dataframe(b_df, use_container_width=True)

    st.markdown("---")
    st.subheader(f"📅 Bước 3: Lộ Trình Triển Khai {duration_weeks} Tuần Dành Cho Chiến Dịch '{camp_name}'")

    roadmap_data = {
        "Tuần": [f"Tuần {i+1}" for i in range(duration_weeks)],
        "Giai Đoạn": ["Khởi Động (Teasing)", "Bùng Nổ (Launch)", "Tăng Tốc (Engage)", "Chuyển Đổi (Convert)"][:duration_weeks],
        "Hoạt Động Trọng Tâm": [
            f"Công bố thông điệp '{slogan}', phát hành Key Visual trên Facebook/Instagram.",
            f"Tung video TikTok/Reels trải nghiệm món mới, mời 5-10 KOLs check-in cửa hàng.",
            f"Chạy Minigame tặng Voucher ưu đãi, kích hoạt chương trình tại điểm bán.",
            f"Đẩy mạnh quảng cáo Retargeting chốt đơn, tổng kết doanh số & vinh danh cửa hàng."
        ][:duration_weeks],
        "KPIs Đo Lường": [
            "100.000+ Reach, 5.000+ Engagement",
            "500.000+ Video Views, 20+ Bài Review",
            "2.000+ Voucher được quy đổi",
            "Đạt 100% Target Doanh Số Đề Ra"
        ][:duration_weeks]
    }
    
    st.table(pd.DataFrame(roadmap_data))
    
    # Export Plan Button
    st.download_button(
        label="📥 Tải Bản Kế Hoạch Chiến Dịch (CSV)",
        data=pd.DataFrame(roadmap_data).to_csv(index=False).encode('utf-8-sig'),
        file_name=f"Ke_Hoach_Marketing_{camp_name}.csv",
        mime="text/csv"
    )

# ==========================================
# PAGE 3: SÁNG TẠO CONTENT & TIKTOK STUDIO
# ==========================================
elif st.session_state.current_page == "content":
    if st.button("⬅️ Quay lại Trang Chủ Overview"):
        st.session_state.current_page = "home"
        st.rerun()

    st.header("🎬 Phân Hệ 3: Xưởng Sáng Tạo Content & TikTok Studio")
    st.caption("Nhập ý tưởng cá nhân ➔ AI gen bài viết Social, Kịch bản TikTok 20s và Prompt vẽ Poster ngay!")

    st.markdown("### 💡 BÀN PHÍM Ý TƯỞNG (INPUT Ý KIẾN CỦA BẠN)")
    user_idea = st.text_area(
        "Nhập ý tưởng hoặc góc nhìn bạn muốn đưa vào kịch bản/bài viết:",
        value="Trời mưa lạnh ngoài cửa kính, nhân viên văn phòng thèm ly Cà Phê Mùa Đông ấm nóng, áp dụng khuyến mãi Mua 1 Tặng 1 quà tặng bạn thân."
    )

    if st.button("✨ BẤM ĐỂ AI GEN KỊCH BẢN TƯƠNG TÁC", type="primary"):
        st.markdown(f"""
        <div class="ai-output-box">
            <b>🤖 AI PHẢN HỒI Ý KIẾN CỦA BẠN:</b><br>
            <i>"Tôi đã ghi nhận ý tưởng: '<b>{user_idea}</b>'. Dưới đây là bộ nội dung được thiết kế chuẩn xác theo góc nhìn bạn cung cấp!"</i>
        </div>
        """, unsafe_allow_html=True)

        t1, t2, t3 = st.tabs(["✍️ Bài Viết Social (FB/IG)", "🎬 Kịch Bản TikTok 20s", "🖼️ Prompt Tạo Poster AI"])

        with t1:
            st.subheader("Mẫu Bài Viết Social Theo Ý Kiến Bàn Giao")
            st.info(f"""
🌧️ **[Caption Facebook/Instagram]**

{user_idea.split(',')[0]}... Có những ngày thời tiết chiều lòng người đến lạ, chỉ muốn tìm một góc quen, cầm trên tay ly cà phê bốc khói ngút ngàn. 

☕ **MÙA ĐÔNG ẤM ÁP - ẤM ÁP TỪNG KHOẢNH KHẮC**
Đặc biệt, ghé quán ngay hôm nay để nhận ưu đãi **MUA 1 TẶNG 1** - Dành tặng riêng cho bạn và cạ cứng!

👉 Tag ngay đứa bạn thân vào đây để rủ đi trú mưa làm ly cà phê ấm nóng nào!
#TheCoffeeHouse #MuaDongAmAp #CaPheNuocNong #Mua1Tang1
            """)

        with t2:
            st.subheader("Kịch Bản TikTok / Reels (20 giây) Đúng Theo Ý Bạn")
            
            script_custom = pd.DataFrame({
                "Phân Cảnh": ["Scene 1 (0-4s)", "Scene 2 (4-8s)", "Scene 3 (8-13s)", "Scene 4 (13-17s)", "Scene 5 (17-20s)"],
                "Hình Ảnh (Visual)": [
                    "Cận cảnh giọt mưa rơi ngoài cửa kính văn phòng lạnh.",
                    "Nhân vật chính co ro nhìn đồng hồ, thèm một tách đồ uống nóng.",
                    "Barista rót dòng cà phê/trà nóng bốc khói nghi ngút vào ly sứ ấm áp.",
                    "Nhân vật mỉm cười trao ly cà phê thứ 2 cho bạn đồng nghiệp (Kèm Pop-up Mua 1 Tặng 1).",
                    "Hiển thị Logo The Coffee House & Slogan Mùa Đông Ấm Áp."
                ],
                "Thuyết Minh (Voiceover)": [
                    "“Trời mưa lạnh thế này, ước gì có ngay một ly cà phê ấm nóng nhỉ...”",
                    "“Ghé lại The Coffee House liền thôi!”",
                    "“Hương vị ấm áp vỗ về mọi giác quan trong ngày đông.”",
                    "“Lại còn được Mua 1 Tặng 1 để sưởi ấm cho cả đứa bạn thân nữa!”",
                    "“Mùa Đông Ấm Áp — Ấm áp từng khoảnh khắc.”"
                ],
                "Âm Thanh (SFX)": ["Tiếng mưa rơi nhẹ", "Tiếng chuông cửa quán", "Nhạc Lo-fi ấm cúng", "Nhạc tươi vui", "Jingle thương hiệu"]
            })
            st.table(script_custom)

        with t3:
            st.subheader("Prompt Sinh Ảnh Poster AI (Midjourney/DALL-E)")
            st.code(f"""
Create a photorealistic vertical poster for a coffee campaign.
Concept: {user_idea}.
A cozy interior setting of a modern coffee shop with rain drops on the window glass, warm amber lighting.
On the wooden table sits two steaming ceramic cups of hot latte with latte art.
Cozy, emotional, high detail, 8k resolution, cinematic lighting --ar 9:16
            """)

# ==========================================
# PAGE 4: SAFEGUARD & HUMAN CONTROL
# ==========================================
elif st.session_state.current_page == "safeguard":
    if st.button("⬅️ Quay lại Trang Chủ Overview"):
        st.session_state.current_page = "home"
        st.rerun()

    st.header("🛡️ Phân Hệ 4: Trung Tâm Phê Duyệt & SafeGuard")
    st.warning("⚠️ **Nguyên tắc an toàn:** AI đóng vai trò là Trợ lý khởi tạo (Drafting Assistant). Toàn bộ ngân sách và nội dung truyền thông phải được con người kiểm duyệt trước khi phát hành.")

    st.markdown("### 📋 Checklist Phê Duyệt 5 Bước (Human-in-the-Loop)")
    st.checkbox("1. Duyệt số liệu doanh thu & tính chính xác của công thức phân bổ ngân sách.", value=True)
    st.checkbox("2. Kiểm tra văn phong caption có tuân thủ đúng Brand Guideline không.", value=True)
    st.checkbox("3. Rà soát hình ảnh AI sinh ra (tránh lỗi ngón tay, sai logo thương hiệu).", value=True)
    st.checkbox("4. Đảm bảo quy định bảo mật thông tin nội bộ & bản quyền truyền thông.", value=True)
    st.checkbox("5. Phê duyệt hạn mức ngân sách thực tế trước khi giải ngân quảng cáo.", value=True)
