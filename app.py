import streamlit as st
import os
import time
import requests

# 1. Initialize Page Configuration
st.set_page_config(
    page_title="MemoryOS — Build Memories",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Frontend Pipeline State Variables
if "pipeline_running" not in st.session_state:
    st.session_state.pipeline_running = False
if "pipeline_step" not in st.session_state:
    st.session_state.pipeline_step = 0

# Initialize Chat History Container for the Backend Connection
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Session initialized. Memory context active. Ask me anything!"}
    ]

# TARGET URL FOR YOUR TEAMMATES' FASTAPI SERVER
FASTAPI_API_URL = "http://127.0.0.1:8000/v1/chat/completions"

# 2. Inject FontAwesome and Custom Fonts
st.html("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
""")

# 3. Load style.css
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.html(f"<style>{f.read()}</style>")
    else:
        st.error("style.css not found. Please verify the file path.")

load_css()

# 4. Premium Sidebar Custom Content
with st.sidebar:
    st.html("""
    <div class="sidebar-branding">
        <div class="logo-wrapper">
            <div class="hologram-ring"></div>
            <span class="logo-icon"><i class="fa-solid fa-brain"></i></span>
        </div>
        <div class="brand-details">
            <h1 class="brand-title">MemoryOS</h1>
            <p class="brand-tagline">Don't just take notes. Build memories.</p>
        </div>
    </div>
    <div class="sidebar-separator"></div>
    """)
    
    # Navigation Configuration
    try:
        from streamlit_option_menu import option_menu
        selected_nav = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Upload Lecture",
                "Memory Panel",
                "Memory Chat",
                "Search Chats",
                "Images",
                "Recents",
                "Settings"
            ],
            icons=[
                "grid-1x2-fill",        # Dashboard
                "cloud-upload-fill",   # Upload Lecture
                "cpu-fill",            # Memory Panel
                "chat-square-text-fill",# Memory Chat
                "search",              # Search Chats
                "image-fill",          # Images
                "clock-history",       # Recents
                "gear-fill"            # Settings
            ],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0px !important", "background-color": "transparent"},
                "icon": {"color": "#38BDF8", "font-size": "1.05rem"}, 
                "nav-link": {
                    "font-size": "0.95rem", 
                    "text-align": "left", 
                    "margin": "4px 0px", 
                    "color": "#CBD5E1", 
                    "background-color": "transparent",
                    "font-family": "'Inter', sans-serif"
                },
                "nav-link-selected": {
                    "background": "linear-gradient(90deg, rgba(56, 189, 248, 0.15) 0%, rgba(139, 92, 246, 0.05) 100%)", 
                    "color": "#38BDF8", 
                    "border-left": "3.5px solid #38BDF8",
                    "font-weight": "600"
                },
            }
        )
    except Exception:
        selected_nav = st.radio(
            "Navigation",
            ["Dashboard", "Upload Lecture", "Memory Panel", "Memory Chat", "Search Chats", "Images", "Recents", "Settings"],
            label_visibility="collapsed"
        )
    
    st.html("""<div class="sidebar-spacer"></div>""")
    
    st.html("""
    <div class="sidebar-status-card">
        <div class="status-indicator">
            <span class="pulse-dot"></span>
            <span class="status-text">Cognitive Engine Active</span>
        </div>
        <div class="system-details">
            <span class="detail-label">Sync status:</span>
            <span class="detail-value">Optimal</span>
        </div>
        <div class="system-details">
            <span class="detail-label">Storage load:</span>
            <span class="detail-value">12.4 GB</span>
        </div>
        <div class="sidebar-footer-version">
            MemoryOS v0.1.0-alpha
        </div>
    </div>
    """)

# 5. Main Area Router Based on Selected Navigation
if selected_nav == "Dashboard":
    st.html("""
    <div class="header-container">
        <div>
            <div class="section-tag"><i class="fa-solid fa-chart-simple"></i> COGNITIVE OVERVIEW</div>
            <h1 class="main-title">Learning Overview</h1>
            <p class="subtitle">Real-time state visualization of your persistent knowledge graphs.</p>
        </div>
        <div class="quick-status">
            <div class="status-pill success"><i class="fa-solid fa-circle-nodes"></i> 248 Nodes</div>
            <div class="status-pill primary"><i class="fa-solid fa-link"></i> 582 Edges</div>
        </div>
    </div>
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.html('<div class="metric-card"><div class="metric-icon"><i class="fa-solid fa-file-invoice"></i></div><div class="metric-label">Processed Docs</div><div class="metric-value">42</div><div class="metric-delta positive"><i class="fa-solid fa-arrow-trend-up"></i> +8 this week</div></div>')
    with col2:
        st.html('<div class="metric-card"><div class="metric-icon"><i class="fa-solid fa-brain"></i></div><div class="metric-label">Memory Clusters</div><div class="metric-value">18</div><div class="metric-delta positive"><i class="fa-solid fa-arrow-trend-up"></i> +3 this week</div></div>')
    with col3:
        st.html('<div class="metric-card font-accent"><div class="metric-icon"><i class="fa-solid fa-bolt"></i></div><div class="metric-label">API Synapses</div><div class="metric-value">99.8%</div><div class="metric-delta positive"><i class="fa-solid fa-circle-check"></i> Latency 14ms</div></div>')
    with col4:
        st.html('<div class="metric-card"><div class="metric-icon"><i class="fa-solid fa-clock-rotate-left"></i></div><div class="metric-label">Last Synchronization</div><div class="metric-value">Just Now</div><div class="metric-delta neutral"><i class="fa-solid fa-rotate"></i> Automatic</div></div>')

    st.markdown("""<div class="layout-spacer"></div>""", unsafe_allow_html=True)
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        st.html("""
        <div class="glass-card full-height">
            <div class="card-header">
                <h3><i class="fa-solid fa-circle-nodes"></i> Knowledge Graph Projection</h3>
                <span class="card-subtitle">Active nodes in cognitive state</span>
            </div>
            <div class="graph-viewport">
                <svg width="100%" height="320" viewBox="0 0 600 320" style="background: transparent;">
                    <line x1="300" y1="160" x2="180" y2="100" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.5" stroke-dasharray="4 2" />
                    <line x1="300" y1="160" x2="420" y2="100" stroke="rgba(139, 92, 246, 0.3)" stroke-width="1.5" />
                    <line x1="300" y1="160" x2="300" y2="260" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.5" />
                    <line x1="180" y1="100" x2="100" y2="160" stroke="rgba(203, 213, 225, 0.2)" stroke-width="1" />
                    <line x1="180" y1="100" x2="220" y2="220" stroke="rgba(203, 213, 225, 0.2)" stroke-width="1" />
                    <line x1="420" y1="100" x2="500" y2="160" stroke="rgba(203, 213, 225, 0.2)" stroke-width="1" />
                    <line x1="420" y1="100" x2="380" y2="220" stroke="rgba(203, 213, 225, 0.2)" stroke-width="1" />
                    
                    <circle cx="300" cy="160" r="16" fill="url(#primaryGlow)" class="graph-node-center" />
                    <circle cx="180" cy="100" r="10" fill="url(#accentGlow)" class="graph-node" />
                    <circle cx="420" cy="100" r="10" fill="url(#accentGlow)" class="graph-node" />
                    <circle cx="300" cy="260" r="8" fill="url(#primaryGlow)" class="graph-node" />
                    
                    <circle cx="100" cy="160" r="6" fill="#1F2937" stroke="#CBD5E1" stroke-width="1.5" class="graph-node-leaf" />
                    <circle cx="220" cy="220" r="6" fill="#1F2937" stroke="#CBD5E1" stroke-width="1.5" class="graph-node-leaf" />
                    <circle cx="500" cy="160" r="6" fill="#1F2937" stroke="#CBD5E1" stroke-width="1.5" class="graph-node-leaf" />
                    <circle cx="380" cy="220" r="6" fill="#1F2937" stroke="#CBD5E1" stroke-width="1.5" class="graph-node-leaf" />
                    
                    <text x="300" y="135" text-anchor="middle" fill="#F8FAFC" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="600">MemoryOS</text>
                    <text x="180" y="80" text-anchor="middle" fill="#38BDF8" font-family="'Space Grotesk', sans-serif" font-size="10">Hackathon</text>
                    <text x="420" y="80" text-anchor="middle" fill="#8B5CF6" font-family="'Space Grotesk', sans-serif" font-size="10">Design System</text>
                    <text x="300" y="285" text-anchor="middle" fill="#CBD5E1" font-family="'Space Grotesk', sans-serif" font-size="10">Cognee DB</text>
                    
                    <defs>
                        <radialGradient id="primaryGlow" cx="50%" cy="50%" r="50%">
                            <stop offset="0%" stop-color="#38BDF8" />
                            <stop offset="100%" stop-color="#0284C7" />
                        </radialGradient>
                        <radialGradient id="accentGlow" cx="50%" cy="50%" r="50%">
                            <stop offset="0%" stop-color="#8B5CF6" />
                            <stop offset="100%" stop-color="#6D28D9" />
                        </radialGradient>
                    </defs>
                </svg>
            </div>
            <div class="card-footer">
                <span class="status-pill info"><i class="fa-solid fa-circle-info"></i> Double click nodes to expand synapse details.</span>
            </div>
        </div>
        """)
        
    with right_col:
        st.html('<div class="glass-card full-height"><div class="card-header"><h3><i class="fa-solid fa-bolt"></i> System Controls</h3><span class="card-subtitle">Test design system components</span></div><div class="card-body">')
        
        st.text_input("Synapse Identifier", placeholder="Enter memory reference...", key="test_ref_input")
        st.slider("Semantic Threshold", min_value=0.0, max_value=1.0, value=0.75, step=0.05, key="test_slider")
        st.selectbox("Storage Tier", ["Hot Cache", "Graph Persistence", "Decentralized Memory"], key="test_select")
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.button("Commit Memory", type="primary", use_container_width=True)
        with btn_col2:
            st.button("Reset State", type="secondary", use_container_width=True)
            
        st.html('</div></div>')

    st.html("""
    <div class="layout-spacer"></div>
    <h2 class="section-title"><i class="fa-solid fa-bookmark"></i> Recent Memorized Synapses</h2>
    """)
    
    card_col1, card_col2, card_col3 = st.columns(3)
    with card_col1:
        st.html('<div class="memory-card"><div class="card-meta"><span class="badge badge-primary">Design System</span><span class="card-time">2 hrs ago</span></div><h4 class="card-title">Futuristic Color Theme Config</h4><p class="card-desc">Implemented specific hex shades: #0B1220 deep background, #38BDF8 cyan electric highlights, and #8B5CF6 royal purple accents. Clean layout configured with neon custom borders.</p><div class="card-action"><a href="#" class="card-link">Inspect Synapse <i class="fa-solid fa-chevron-right"></i></a></div></div>')
    with card_col2:
        st.html('<div class="memory-card"><div class="card-meta"><span class="badge badge-accent">Hackathon Goal</span><span class="card-time">5 hrs ago</span></div><h4 class="card-title">MemoryOS Concept Pitch</h4><p class="card-desc">"Don\'t just take notes. Build memories." Concept maps raw text documents to a vector and knowledge graph structure, visualizing connections as a virtual second brain system.</p><div class="card-action"><a href="#" class="card-link">Inspect Synapse <i class="fa-solid fa-chevron-right"></i></a></div></div>')
    with card_col3:
        st.html('<div class="memory-card"><div class="card-meta"><span class="badge badge-success">Architecture</span><span class="card-time">Yesterday</span></div><h4 class="card-title">Cognee Integrator API</h4><p class="card-desc">Connected Python\'s Cognee backend module directly to streamlit components. Leverages SQLite database locally to preserve vectors and graph coordinates across user restarts.</p><div class="card-action"><a href="#" class="card-link">Inspect Synapse <i class="fa-solid fa-chevron-right"></i></a></div></div>')

elif selected_nav == "Upload Lecture":
    st.html("""
    <div class="header-container">
        <div>
            <div class="section-tag"><i class="fa-solid fa-plus-circle"></i> OMNI-CHANNEL INTAKE</div>
            <h1 class="main-title">Build New Memory</h1>
            <p class="subtitle">Upload documentation or media files to route directly through n8n to Cognee DB.</p>
        </div>
    </div>
    <div class="layout-spacer"></div>
    """)
    
    st.html('<div class="glass-card">')
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.text_input("Memory Title", placeholder="e.g. Data Structures Lecture 4...", key="mem_title")
        
        input_type = st.tabs(["📄 Document File Upload", "📝 Raw Markdown/Text"])
        
        with input_type[0]:
            st.file_uploader("Drop document formats to trigger n8n transcription webhooks", type=["pdf", "txt", "docx", "mp3", "wav"], key="uploaded_lecture_files")
        with input_type[1]:
            st.text_area("Memory Content Block", placeholder="Paste structural notes here...", height=150, key="mem_content")
        
        st.html('<div class="layout-spacer"></div>')
        
        if st.button("Encode & Synthesize VIA n8n", type="primary", use_container_width=True):
            st.session_state.pipeline_running = True
            st.session_state.pipeline_step = 1
            
        if st.session_state.pipeline_running:
            st.html('<div style="margin-top: 15px; padding: 12px; background: rgba(56, 189, 248, 0.05); border-left: 3px solid #38BDF8; font-size:0.9rem;">')
            with st.spinner("Executing live extraction pipelines..."):
                if st.session_state.pipeline_step == 1:
                    st.write("🔗 **[Step 1/3]** n8n Trigger Hook Active - Parsing chunks out of document framework...")
                    time.sleep(1)
                    st.session_state.pipeline_step = 2
                    st.rerun()
                elif st.session_state.pipeline_step == 2:
                    st.write("🧠 **[Step 2/3]** Cognee Vector Transformation Engine compiling entity links...")
                    time.sleep(1)
                    st.session_state.pipeline_step = 3
                    st.rerun()
                elif st.session_state.pipeline_step == 3:
                    st.success("✅ **[Step 3/3]** Context matrix synchronized into SQLite backend memory successfully!")
                    st.session_state.pipeline_running = False
            st.html('</div>')
            
    with col_r:
        st.html('<div class="nested-panel"><h4><i class="fa-solid fa-circle-nodes"></i> Enrichment Settings</h4><p class="panel-desc">Configure parameters before routing downstream.</p></div>')
        st.text_input("Category / Tag", placeholder="e.g. Lecture, Research", key="mem_tag")
        st.multiselect("Parent Graph Targets", ["MemoryOS Launch", "Cognee Setup", "Color System"], key="mem_parents")
        st.toggle("Auto-extract Entities", value=True, key="mem_extract")
        st.toggle("Sync to Cloud Cluster", value=False, key="mem_sync")
    st.html('</div>')

elif selected_nav == "Memory Panel":
    st.html("""
    <div class="header-container">
        <div>
            <div class="section-tag"><i class="fa-solid fa-brain"></i> DATA MATRIX</div>
            <h1 class="main-title">Memory Panel</h1>
            <p class="subtitle">Index matrix metrics and relational graph cluster statuses.</p>
        </div>
    </div>
    <div class="layout-spacer"></div>
    """)
    st.html("""
    <div class="glass-card">
        <div class="card-body">
            <div class="system-details" style="padding: 14px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between;">
                <span class="detail-label" style="font-size: 1rem;">Knowledge Vectors:</span>
                <span class="detail-value" style="font-size: 1.1rem; color: #8B5CF6; font-weight: 600;">1,024</span>
            </div>
            <div class="system-details" style="padding: 14px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between;">
                <span class="detail-label" style="font-size: 1rem;">Graph Clusters:</span>
                <span class="detail-value" style="font-size: 1.1rem; color: #8B5CF6; font-weight: 600;">14 Base</span>
            </div>
            <div class="system-details" style="padding: 14px 0; display: flex; justify-content: space-between;">
                <span class="detail-label" style="font-size: 1rem;">Pipeline Linkage:</span>
                <span class="detail-value" style="font-size: 1.1rem; color: #38BDF8; font-weight: 600;">Cognee / n8n Production Engine</span>
            </div>
        </div>
    </div>
    """)

# LIVE COGNEE BACKEND CONNECTION INTEGRATED HERE
elif selected_nav == "Memory Chat":
    header_col, action_col = st.columns([3, 1])
    with header_col:
        st.html("""
        <div class="header-container">
            <div>
                <div class="section-tag"><i class="fa-solid fa-comments"></i> CHAT SYNAPSE</div>
                <h1 class="main-title">Query Memory Engine</h1>
                <p class="subtitle">Chat naturally with your second brain. Answers are contextualized by your indexed memories.</p>
            </div>
        </div>
        """)
    with action_col:
        st.html('<div style="height: 25px;"></div>')
        if st.button("➕ New Chat Thread", type="primary", use_container_width=True):
            # Dynamic Session Reset Trigger
            st.session_state.chat_history = [
                {"role": "assistant", "content": "Workspace memory cleared. New query session initialized."}
            ]
            st.toast("Chat workspace memory reset.")

    st.html('<div class="layout-spacer"></div>')
    
    # 1. Render all historical bubbles stored inside the Session State logs
    st.html('<div class="chat-container">')
    for msg in st.session_state.chat_history:
        avatar = "fa-user" if msg["role"] == "user" else "fa-brain"
        css_class = "user" if msg["role"] == "user" else "assistant"
        st.html(f"""
        <div class="chat-message {css_class}">
            <div class="chat-avatar"><i class="fa-solid {avatar}"></i></div>
            <div class="chat-bubble-wrapper">
                <div class="chat-bubble">{msg['content']}</div>
            </div>
        </div>
        """)
    st.html('</div>')

    # 2. Capture a live input entry from the text tray box
    if user_prompt := st.chat_input("Ask MemoryOS to recall anything..."):
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        st.rerun()

    # 3. Handle data transmission loop if the user has a pending prompt sequence
    if len(st.session_state.chat_history) > 0 and st.session_state.chat_history[-1]["role"] == "user":
        latest_user_message = st.session_state.chat_history[-1]["content"]
        
        # Package JSON payload strictly aligned with your friend's FastAPI models
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": latest_user_message}]
        }
        
        try:
            with st.spinner("Connecting to memory cluster database..."):
                response = requests.post(FASTAPI_API_URL, json=payload, timeout=45)
                
                if response.status_code == 200:
                    # Target data dictionary path directly out of your friend's response schema
                    backend_answer = response.json()["choices"][0]["message"]["content"]
                else:
                    backend_answer = f"⚠️ Server Error: Return code execution failed with error state [{response.status_code}]."
        except Exception as e:
            backend_answer = f"🔌 Connection Dropped: Couldn't connect to the local FastAPI cluster. Verify that `uvicorn backend.app:app` is actively running on host port 8000. Logs: {str(e)}"
            
        st.session_state.chat_history.append({"role": "assistant", "content": backend_answer})
        st.rerun()

elif selected_nav == "Search Chats":
    st.html("""
    <div class="header-container">
        <div>
            <div class="section-tag"><i class="fa-solid fa-magnifying-glass"></i> SEMANTIC QUERY</div>
            <h1 class="main-title">Search History Clusters</h1>
            <p class="subtitle">Scan vector logs to locate past chat sequences based on keywords or concepts.</p>
        </div>
    </div>
    <div class="layout-spacer"></div>
    """)
    st.text_input("🔍 Search database index...", placeholder="Type keywords like 'design system' or 'Cognee setup'...", key="chat_search_query")

elif selected_nav == "Images":
    st.html("""
    <div class="header-container">
        <div>
            <div class="section-tag"><i class="fa-solid fa-image"></i> GRAPHICS ENGINE</div>
            <h1 class="main-title">Image Assets & Diagrams</h1>
            <p class="subtitle">Review parsed charts, diagram layers, and architectural mockups extracted from processing inputs.</p>
        </div>
    </div>
    <div class="layout-spacer"></div>
    """)
    st.html('<div class="glass-card"><p style="color: #64748B;">No graphical components rendered in current workspace node cluster.</p></div>')

elif selected_nav == "Recents":
    st.html("""
    <div class="header-container">
        <div>
            <div class="section-tag"><i class="fa-solid fa-clock"></i> REPOSITORIES</div>
            <h1 class="main-title">Recents</h1>
            <p class="subtitle">Chronological sequence of sessions and logs processed by the system.</p>
        </div>
    </div>
    <div class="layout-spacer"></div>
    """)
    st.html("""
    <div class="glass-card">
        <div class="card-body">
            <div style="font-size: 1rem; color: #CBD5E1; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between;">
                <span><i class="fa-solid fa-message" style="color: #38BDF8; margin-right: 12px;"></i> Color Theme Design Matrix Selection</span>
                <span style="color: #64748B; font-size: 0.9rem;">11:10 AM</span>
            </div>
            <div style="font-size: 1rem; color: #CBD5E1; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between;">
                <span><i class="fa-solid fa-message" style="color: #38BDF8; margin-right: 12px;"></i> Cognee DB Integrator Endpoint Setup</span>
                <span style="color: #64748B; font-size: 0.9rem;">11:12 AM</span>
            </div>
        </div>
    </div>
    """)

elif selected_nav == "Settings":
    st.html("""
    <div class="header-container">
        <div>
            <div class="section-tag"><i class="fa-solid fa-sliders"></i> ENGINE SETTINGS</div>
            <h1 class="main-title">Configuration</h1>
            <p class="subtitle">Tune backend connections, cognitive thresholds, and UI theme behaviors.</p>
        </div>
    </div>
    <div class="layout-spacer"></div>
    """)
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.html('<div class="glass-card"><div class="card-header"><h3><i class="fa-solid fa-gears"></i> Engine Hyperparameters</h3></div><div class="card-body">')
        st.slider("Chunk Size (Tokens)", min_value=128, max_value=2048, value=512, step=128, key="setting_chunk_size")
        st.slider("LLM Temperature", min_value=0.0, max_value=1.0, value=0.3, step=0.05, key="setting_temperature")
        st.html('</div></div>')
    with col_s2:
        st.html('<div class="glass-card"><div class="card-header"><h3><i class="fa-solid fa-network-wired"></i> Database Connections</h3></div><div class="card-body">')
        st.text_input("SQLite Storage Path", value="./cognee_persisted.db", key="setting_db_path")
        st.button("Run Diagnostic Integrity Test", type="secondary", use_container_width=True)
        st.html('</div></div>')