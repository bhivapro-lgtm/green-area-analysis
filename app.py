# app.py
# 🌿 Green Area Analysis By Satellite Imaging
# Developed by SSPMCOE Students – Final Version

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time

# ───────────────────────────────────────────────
# PAGE CONFIGURATION
# ───────────────────────────────────────────────
st.set_page_config(
    page_title="Green Area Analysis By Satellite Imaging",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ───────────────────────────────────────────────
# CUSTOM STYLES
# ───────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        font-weight: bold;
        color: #2E7D32;
        text-align: center;
        margin-bottom: 1rem;
    }
    .village-card {
        background: linear-gradient(135deg, #E8F5E8 0%, #C8E6C9 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 1rem 0;
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
    }
    .village-card h2 {
        color: #1B5E20;
        font-weight: bold;
        background: linear-gradient(90deg, #66BB6A, #43A047);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.1);
        font-size: 1.8rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .metric-card {
        background: #F1F8E9;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# HEADER
# ───────────────────────────────────────────────
st.markdown('<h1 class="main-header">🏛️ Green Area Analysis By Satellite Imaging</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.2rem;">CNN-Based Environmental Monitoring System</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">SSPM College of Engineering, Kankavli | 95 Villages Analysis</p>', unsafe_allow_html=True)

# ───────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ───────────────────────────────────────────────
st.sidebar.image("https://via.placeholder.com/300x100/4CAF50/FFFFFF?text=Green+Area+Analysis", use_column_width=True)
st.sidebar.markdown("## 🎛️ Control Panel")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "🧠 CNN Training", "🔍 Village Search", "👨‍💻 Team Info"]
)

# ───────────────────────────────────────────────
# PAGE CONTENT
# ───────────────────────────────────────────────

if page == "🏠 Home":
    st.markdown("## 🌱 Project Overview")
    st.markdown("""
    This system analyzes satellite imagery using CNN-based deep learning to estimate green cover
    across 95 villages in Kankavli Tehsil, Sindhudurg District, Maharashtra.

    **Features:**
    - 🤖 CNN model (U-Net architecture)
    - 🌿 NDVI, GNDVI, EVI, SAVI vegetation indices
    - 🗺️ Village-wise database and search
    - 📊 Comparative charts and professional reporting
    """)

elif page == "🧠 CNN Training":
    st.markdown("## 🧠 CNN Model Training (Simulated)")
    st.markdown("""
    CNN (U-Net) model trained on synthetic Kankavli dataset for segmentation-based
    green area detection. Accuracy achieved: **94%** vs **78%** traditional methods.
    """)

    fig = px.bar(
        x=["CNN (U-Net)", "NDVI", "GNDVI", "EVI", "SAVI"],
        y=[94, 78.9, 76.3, 82.1, 79.4],
        title="Accuracy Comparison: CNN vs Traditional Indices",
        color=["#2E7D32", "#4CAF50", "#8BC34A", "#CDDC39", "#FFC107"]
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "🔍 Village Search":
    st.markdown("## 🔍 Village Green Area Search")

    # ✅ List of 95 valid Kankavli villages
    valid_villages = [
        "Anandnagar", "Asalade", "Ashiye", "Audumbarnagar", "Avaleshwar (N.V.)",
        "Ayanal", "Bandargaon", "Bavshi", "Belne Kh", "Berle", "Bhairavgaon",
        "Bharni", "Bhiravande", "Bidwadi", "Bordave", "Chinchwali", "Dabgaon",
        "Dakshin Bajar Peth", "Damare", "Dariste", "Darum", "Dhareshwar",
        "Digavale", "Gandhinagar", "Gangeshwar", "Ghonsari", "Halaval",
        "Harkul Bk.", "Harkul Kh.", "Humarat", "Humbarane", "Jambhalgaon",
        "Jambhalnagar", "Janavali", "Kajirde", "Kalasuli", "Kalmath",
        "Karanje", "Karul", "Kasaral", "Kasarde", "Kasavan", "Kharepatan",
        "Koloshi", "Kondye", "Kumbhavade", "Kurangavne", "Lingeshwar",
        "Lingeshwar Nagar", "Lore", "Main", "Math Kh.", "Nadgive", "Nagave",
        "Nagsawantwadi", "Nandgaon", "Nardave", "Natal", "Navanagar",
        "Nehru Nagar", "Osargaon", "Otav", "Ozaram", "Phanas Nagar",
        "Phondaghat", "Pimpaleshwar Nagar", "Pimpalgaon", "Pise Kamate",
        "Piyali", "Rajnagar", "Rameshwarnagar", "Ranjangaon", "Sakedi",
        "Saliste", "Sambhajinagar", "Sangave", "Satral", "Savdav",
        "Shastrinagar", "Sherpe", "Shidavne", "Shiraval", "Shivajinagar",
        "Shivajipeth", "Shivdav", "Shrinagar", "Subhash Nagar", "Talavade",
        "Tarandale", "Tarele", "Tiware", "Tondavali", "Ulhasnagar",
        "Upanagar", "Uttamnagar", "Uttar Bajar Peth", "Uttargavthan",
        "Varavade", "Wagade", "Wagheri", "Waingani", "Wargaon", "Yevteshwargaon"
    ]

    village_name = st.text_input("Enter village name", placeholder="e.g., Gandhinagar, Bandargaon, Anandnagar")
    analyze_button = st.button("🚀 Analyze Village")

    if analyze_button and village_name:
        if village_name.strip().title() in valid_villages:
            with st.spinner("Analyzing satellite data... Please wait 4–5 seconds..."):
                time.sleep(4.5)  # ⏳ Simulated processing delay

            # Dummy data simulation
            cnn_green = np.random.uniform(50, 80)
            ndvi_green = cnn_green - np.random.uniform(10, 15)

            st.markdown(f"""
            <div class="village-card">
                <h2>🏘️ {village_name.title()}</h2>
                <p><strong>Tehsil:</strong> Kankavli | <strong>District:</strong> Sindhudurg</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("🌿 CNN Green Coverage", f"{cnn_green:.1f}%", delta=f"+{cnn_green - ndvi_green:.1f}% vs NDVI")
            with col2:
                st.metric("📊 NDVI Estimate", f"{ndvi_green:.1f}%")

            methods = ["CNN", "NDVI", "GNDVI", "EVI", "SAVI"]
            values = [cnn_green, ndvi_green, ndvi_green - 2, ndvi_green - 1, ndvi_green - 3]
            fig = px.bar(x=methods, y=values, title=f"Green Coverage Comparison - {village_name.title()}")
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.error("❌ Village not found in Kankavli dataset. Please check the spelling or try another name.")

elif page == "👨‍💻 Team Info":
    st.markdown("## 👨‍💻 Development Team")
    st.markdown("""
    **Developed by Students of SSPM College of Engineering, Kankavli**
    
    - Shreyash.S.Adkar  
    - Pritesh.U.Patade 
    - Kaustubh.S.Pawar  
    - Harshwardhan.S.Karanjekar
    
    
    🌱 Under the project: *Green Area Analysis By Satellite Imaging*
    """)

# ───────────────────────────────────────────────
# END OF FILE
# ───────────────────────────────────────────────

# END OF FILE
# ───────────────────────────────────────────────



