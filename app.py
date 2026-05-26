"""
╔══════════════════════════════════════════════════════════════════════╗
║         PHARMA INTELLIGENCE PORTAL  ·  Executive Analytics Suite    ║
║         Premium Drug Statistics Dashboard · Streamlit + Plotly      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io

# ──────────────────────────────────────────────────────────────────────
# PAGE CONFIG  (must be first Streamlit call)
# ──────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PharmaIQ · Executive Analytics",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────────
# GLOBAL CSS INJECTION
# ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ─────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,300&family=DM+Mono:wght@400;500&family=Syne:wght@700;800&display=swap');

/* ── CSS Variables ────────────────────────────────────────────────── */
:root {
    --bg-deep:      #0d1117;
    --bg-surface:   #161b22;
    --bg-card:      #1c2230;
    --bg-hover:     #21293a;
    --border:       #2a3448;
    --border-glow:  #00e5a0;
    --accent-teal:  #00e5a0;
    --accent-blue:  #3b9eff;
    --accent-amber: #f5a623;
    --accent-rose:  #ff6b8a;
    --text-primary: #e8edf5;
    --text-secondary: #8b95a8;
    --text-muted:   #4e5a6e;
    --font-body:    'DM Sans', sans-serif;
    --font-mono:    'DM Mono', monospace;
    --font-display: 'Syne', sans-serif;
    --radius-sm:    6px;
    --radius-md:    12px;
    --radius-lg:    18px;
    --shadow-card:  0 4px 24px rgba(0,0,0,0.45), 0 1px 4px rgba(0,229,160,0.06);
}

/* ── Global Resets ────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: var(--font-body) !important;
    background-color: var(--bg-deep) !important;
    color: var(--text-primary) !important;
}

/* ── Streamlit App Background ─────────────────────────────────────── */
.stApp {
    background: linear-gradient(160deg, #0d1117 0%, #111827 60%, #0d1a1f 100%) !important;
}

/* ── Main block padding ───────────────────────────────────────────── */
.block-container {
    padding: 1.5rem 2.5rem 3rem 2.5rem !important;
    max-width: 1600px !important;
}

/* ── Sidebar ──────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: var(--bg-surface) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] .block-container {
    padding: 1.5rem 1.2rem !important;
}

/* ── Tabs ─────────────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    padding: 4px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-secondary) !important;
    font-family: var(--font-body) !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.03em !important;
    padding: 8px 18px !important;
    transition: all 0.2s ease !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(0,229,160,0.15), rgba(59,158,255,0.1)) !important;
    color: var(--accent-teal) !important;
    border: 1px solid rgba(0,229,160,0.3) !important;
}
.stTabs [data-baseweb="tab-panel"] {
    background: transparent !important;
    padding: 1.5rem 0 0 0 !important;
}

/* ── Expander ─────────────────────────────────────────────────────── */
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}
.streamlit-expanderContent {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 var(--radius-md) var(--radius-md) !important;
}

/* ── Select / Multiselect ─────────────────────────────────────────── */
.stMultiSelect [data-baseweb="select"] > div,
.stSelectbox [data-baseweb="select"] > div {
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-primary) !important;
}
.stMultiSelect span[data-baseweb="tag"] {
    background: rgba(0,229,160,0.15) !important;
    border: 1px solid rgba(0,229,160,0.35) !important;
    color: var(--accent-teal) !important;
    border-radius: 4px !important;
}

/* ── Sliders ──────────────────────────────────────────────────────── */
.stSlider [data-baseweb="slider"] [role="slider"] {
    background: var(--accent-teal) !important;
    border: 2px solid var(--bg-deep) !important;
    box-shadow: 0 0 10px rgba(0,229,160,0.5) !important;
}
.stSlider [data-baseweb="slider"] [data-testid="stSliderTrackFill"] {
    background: linear-gradient(90deg, var(--accent-teal), var(--accent-blue)) !important;
}

/* ── Download Button ──────────────────────────────────────────────── */
.stDownloadButton > button {
    background: linear-gradient(135deg, rgba(0,229,160,0.2), rgba(59,158,255,0.15)) !important;
    border: 1px solid rgba(0,229,160,0.5) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--accent-teal) !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    padding: 0.5rem 1.2rem !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}
.stDownloadButton > button:hover {
    background: linear-gradient(135deg, rgba(0,229,160,0.35), rgba(59,158,255,0.25)) !important;
    box-shadow: 0 0 18px rgba(0,229,160,0.3) !important;
}

/* ── Scrollbar ────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent-teal); }

/* ── Plotly container ─────────────────────────────────────────────── */
.js-plotly-plot .plotly {
    border-radius: var(--radius-md) !important;
}

/* ── HR divider utility ───────────────────────────────────────────── */
.section-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.4rem 0;
}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# DATA GENERATION  (fully standalone, no network dependency)
# ──────────────────────────────────────────────────────────────────────
@st.cache_data
def load_local_data() -> pd.DataFrame:
    np.random.seed(42)

    conditions = {
        "Depression":        140,
        "Diabetes, Type 2":  120,
        "Hypertension":      115,
        "Anxiety":           100,
        "Bipolar Disorder":   80,
        "ADHD":               75,
        "Insomnia":           65,
        "Migraine":           60,
        "Rheumatoid Arthritis": 55,
        "GERD":               50,
        "Asthma":             45,
        "Epilepsy":           40,
        "Hypothyroidism":     38,
        "Chronic Pain":       35,
        "Fibromyalgia":       30,
    }

    drug_pool = {
        "Depression":          ["Sertraline","Escitalopram","Fluoxetine","Bupropion","Venlafaxine","Duloxetine","Mirtazapine","Paroxetine"],
        "Diabetes, Type 2":    ["Metformin","Glipizide","Sitagliptin","Empagliflozin","Liraglutide","Dapagliflozin","Canagliflozin","Pioglitazone"],
        "Hypertension":        ["Lisinopril","Amlodipine","Losartan","Hydrochlorothiazide","Metoprolol","Atenolol","Valsartan","Olmesartan"],
        "Anxiety":             ["Buspirone","Lorazepam","Alprazolam","Clonazepam","Hydroxyzine","Propranolol","Pregabalin","Diazepam"],
        "Bipolar Disorder":    ["Lithium","Valproate","Quetiapine","Lamotrigine","Aripiprazole","Olanzapine","Risperidone","Ziprasidone"],
        "ADHD":                ["Adderall","Ritalin","Vyvanse","Strattera","Concerta","Focalin","Intuniv","Kapvay"],
        "Insomnia":            ["Zolpidem","Eszopiclone","Ramelteon","Doxepin","Trazodone","Suvorexant","Melatonin","Temazepam"],
        "Migraine":            ["Sumatriptan","Rizatriptan","Topiramate","Propranolol","Amitriptyline","Valproic Acid","Frovatriptan","Zolmitriptan"],
        "Rheumatoid Arthritis":["Methotrexate","Adalimumab","Etanercept","Infliximab","Leflunomide","Tocilizumab","Abatacept","Tofacitinib"],
        "GERD":                ["Omeprazole","Pantoprazole","Ranitidine","Famotidine","Lansoprazole","Esomeprazole","Cimetidine","Rabeprazole"],
        "Asthma":              ["Albuterol","Fluticasone","Montelukast","Budesonide","Formoterol","Tiotropium","Salmeterol","Ipratropium"],
        "Epilepsy":            ["Levetiracetam","Phenytoin","Carbamazepine","Oxcarbazepine","Gabapentin","Zonisamide","Lacosamide","Felbamate"],
        "Hypothyroidism":      ["Levothyroxine","Liothyronine","Armour Thyroid","Synthroid","Cytomel","NP Thyroid","Tirosint","Euthyrox"],
        "Chronic Pain":        ["Tramadol","Gabapentin","Pregabalin","Duloxetine","Acetaminophen","Celecoxib","Tapentadol","Oxycodone"],
        "Fibromyalgia":        ["Pregabalin","Duloxetine","Milnacipran","Cyclobenzaprine","Amitriptyline","Tramadol","Gabapentin","Hydroxychloroquine"],
    }

    records = []
    for cond, n in conditions.items():
        drugs = drug_pool[cond]
        for _ in range(n):
            drug = np.random.choice(drugs)
            # Skewed towards extremes (U-shaped distribution)
            raw = np.random.beta(0.55, 0.55) * 9 + 1
            rating = float(np.clip(round(raw), 1, 10))
            review_count = int(np.random.lognormal(mean=5.2, sigma=1.1))
            useful_count = int(review_count * np.random.beta(2, 3))
            records.append({
                "drugName":    drug,
                "condition":   cond,
                "rating":      rating,
                "reviewCount": review_count,
                "usefulCount": useful_count,
            })

    df = pd.DataFrame(records)
    return df

# ──────────────────────────────────────────────────────────────────────
# PLOTLY THEME DEFAULTS
# ──────────────────────────────────────────────────────────────────────
PLOTLY_BASE = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans, sans-serif", color="#8b95a8", size=11),
    margin=dict(l=20, r=20, t=40, b=20),
    hoverlabel=dict(
        bgcolor="#1c2230",
        bordercolor="#2a3448",
        font=dict(family="DM Sans, sans-serif", color="#e8edf5", size=12),
    ),
)

TEAL_PALETTE  = ["#00e5a0", "#00bfff", "#3b9eff", "#7c6fff", "#b94fff", "#ff6b8a"]
BLUE_GRADIENT = px.colors.sequential.Blues[::-1]

def hex_to_rgba(hex_color: str, alpha: float = 0.2) -> str:
    """Convert a #rrggbb hex string to an rgba() CSS string."""
    hex_color = hex_color.lstrip("#")
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

def apply_base(fig: go.Figure, title: str = "", height: int = 380) -> go.Figure:
    fig.update_layout(
        **PLOTLY_BASE,
        height=height,
        title=dict(text=title, font=dict(family="Syne, sans-serif", size=14, color="#e8edf5"), x=0, pad=dict(l=4)),
        xaxis=dict(gridcolor="#1e2a38", linecolor="#2a3448", zerolinecolor="#2a3448"),
        yaxis=dict(gridcolor="#1e2a38", linecolor="#2a3448", zerolinecolor="#2a3448"),
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="#2a3448", borderwidth=1),
    )
    return fig

# ──────────────────────────────────────────────────────────────────────
# HTML COMPONENT HELPERS
# ──────────────────────────────────────────────────────────────────────
def kpi_card(icon: str, label: str, value: str, delta: str = "", accent: str = "#00e5a0") -> str:
    delta_html = f'<div style="font-size:0.72rem;color:{accent};margin-top:4px;letter-spacing:.04em">{delta}</div>' if delta else ""
    return f"""
    <div style="
        background: linear-gradient(145deg, #1c2230, #1a2035);
        border: 1px solid #2a3448;
        border-left: 3px solid {accent};
        border-radius: 12px;
        padding: 18px 20px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.4), 0 0 0 0 {accent};
        transition: transform .2s;
        height: 100%;
    ">
        <div style="font-size:1.55rem;margin-bottom:6px">{icon}</div>
        <div style="font-size:0.7rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#4e5a6e;margin-bottom:4px">{label}</div>
        <div style="font-size:1.9rem;font-weight:700;color:#e8edf5;font-family:'Syne',sans-serif;line-height:1">{value}</div>
        {delta_html}
    </div>"""

def section_header(title: str, subtitle: str = "") -> str:
    sub_html = f'<p style="margin:0;font-size:.82rem;color:#4e5a6e;margin-top:2px">{subtitle}</p>' if subtitle else ""
    return f"""
    <div style="margin-bottom:1.2rem">
        <h3 style="margin:0;font-family:'Syne',sans-serif;font-size:1.05rem;font-weight:700;
                   color:#e8edf5;letter-spacing:.02em">{title}</h3>
        {sub_html}
    </div>"""

def insight_chip(label: str, value: str, color: str) -> str:
    return f"""
    <div style="display:inline-flex;flex-direction:column;background:rgba(0,0,0,.25);
                border:1px solid {color}33;border-radius:10px;padding:14px 18px;min-width:170px">
        <span style="font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:{color};font-weight:600">{label}</span>
        <span style="font-size:1.05rem;font-weight:600;color:#e8edf5;margin-top:4px">{value}</span>
    </div>"""

# ──────────────────────────────────────────────────────────────────────
# LOAD DATA
# ──────────────────────────────────────────────────────────────────────
df_raw = load_local_data()

# ──────────────────────────────────────────────────────────────────────
# SIDEBAR — Control Panel
# ──────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:10px 0 18px">
        <div style="font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:#00e5a0;letter-spacing:.05em">⚕️ PharmaIQ</div>
        <div style="font-size:.68rem;color:#4e5a6e;letter-spacing:.12em;text-transform:uppercase;margin-top:2px">Executive Analytics Suite</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr style="border-color:#2a3448;margin:0 0 16px">', unsafe_allow_html=True)

    # ── Condition Filter ──
    st.markdown("""
    <div style="font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                color:#00e5a0;margin-bottom:6px">🏥 Medical Condition</div>
    <div style="font-size:.75rem;color:#4e5a6e;margin-bottom:8px">Filter the entire dashboard by one or more therapeutic areas.</div>
    """, unsafe_allow_html=True)

    all_conditions = sorted(df_raw["condition"].unique())
    selected_conditions = st.multiselect(
        label="Conditions",
        options=all_conditions,
        default=all_conditions,
        label_visibility="collapsed",
    )

    st.markdown('<hr style="border-color:#2a3448;margin:14px 0">', unsafe_allow_html=True)

    # ── Drug Search ──
    st.markdown("""
    <div style="font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                color:#3b9eff;margin-bottom:6px">💊 Drug Name Search</div>
    <div style="font-size:.75rem;color:#4e5a6e;margin-bottom:8px">Narrow results to specific medications within the selected conditions.</div>
    """, unsafe_allow_html=True)

    available_drugs = sorted(df_raw[df_raw["condition"].isin(selected_conditions)]["drugName"].unique()) if selected_conditions else []
    selected_drugs = st.multiselect(
        label="Drugs",
        options=available_drugs,
        default=[],
        placeholder="All drugs (no filter)",
        label_visibility="collapsed",
    )

    st.markdown('<hr style="border-color:#2a3448;margin:14px 0">', unsafe_allow_html=True)

    # ── Rating Range ──
    st.markdown("""
    <div style="font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                color:#f5a623;margin-bottom:6px">⭐ Rating Range</div>
    <div style="font-size:.75rem;color:#4e5a6e;margin-bottom:8px">Show only records where the patient rating falls within this band.</div>
    """, unsafe_allow_html=True)

    rating_range = st.slider(
        label="Rating",
        min_value=1.0, max_value=10.0,
        value=(1.0, 10.0), step=0.5,
        label_visibility="collapsed",
    )

    st.markdown('<hr style="border-color:#2a3448;margin:14px 0">', unsafe_allow_html=True)

    # ── Min Reviews ──
    st.markdown("""
    <div style="font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                color:#ff6b8a;margin-bottom:6px">📊 Min Review Count</div>
    <div style="font-size:.75rem;color:#4e5a6e;margin-bottom:8px">Exclude records with fewer reviews than this threshold.</div>
    """, unsafe_allow_html=True)

    min_reviews = st.slider(
        label="Min Reviews",
        min_value=0, max_value=2000,
        value=0, step=50,
        label_visibility="collapsed",
    )

    st.markdown('<hr style="border-color:#2a3448;margin:14px 0">', unsafe_allow_html=True)

    # ── Download ──
    st.markdown("""
    <div style="font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                color:#7c6fff;margin-bottom:8px">⬇ Export</div>
    """, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# APPLY FILTERS
# ──────────────────────────────────────────────────────────────────────
df = df_raw.copy()

if selected_conditions:
    df = df[df["condition"].isin(selected_conditions)]

if selected_drugs:
    df = df[df["drugName"].isin(selected_drugs)]

df = df[
    (df["rating"] >= rating_range[0]) &
    (df["rating"] <= rating_range[1]) &
    (df["reviewCount"] >= min_reviews)
]

# Download button (inside sidebar, after filter applied)
with st.sidebar:
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="⬇  Download Filtered CSV",
        data=csv_buffer.getvalue(),
        file_name="pharmaiq_filtered_data.csv",
        mime="text/csv",
    )

    st.markdown(f"""
    <div style="text-align:center;margin-top:10px">
        <span style="font-size:.7rem;color:#4e5a6e">{len(df):,} records in current view</span>
    </div>
    """, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="display:flex;align-items:flex-end;justify-content:space-between;
            padding-bottom:1rem;border-bottom:1px solid #2a3448;margin-bottom:1.6rem">
    <div>
        <div style="font-size:.7rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;
                    color:#00e5a0;margin-bottom:4px">⚕ Pharmaceutical Intelligence Platform</div>
        <h1 style="margin:0;font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;
                   color:#e8edf5;line-height:1.1">Drug Analytics Portal</h1>
        <p style="margin:6px 0 0;font-size:.85rem;color:#4e5a6e">
            Real-world evidence · Patient sentiment · Engagement metrics
        </p>
    </div>
    <div style="text-align:right">
        <div style="font-size:.68rem;color:#4e5a6e;letter-spacing:.06em">DATASET SNAPSHOT</div>
        <div style="font-family:'DM Mono',monospace;font-size:.8rem;color:#3b9eff;margin-top:2px">
            v2025.1 · Synthetic RWE
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# GUARD — empty filter
# ──────────────────────────────────────────────────────────────────────
if df.empty:
    st.markdown("""
    <div style="text-align:center;padding:4rem;background:#1c2230;border:1px solid #2a3448;
                border-radius:16px;margin-top:2rem">
        <div style="font-size:2.5rem;margin-bottom:12px">🔍</div>
        <div style="font-size:1.1rem;font-weight:600;color:#e8edf5">No data matches your current filters</div>
        <div style="font-size:.85rem;color:#4e5a6e;margin-top:6px">Adjust the sidebar controls to broaden your selection.</div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ──────────────────────────────────────────────────────────────────────
# KPI METRICS
# ──────────────────────────────────────────────────────────────────────
n_unique_drugs   = df["drugName"].nunique()
n_conditions     = df["condition"].nunique()
avg_rating       = df["rating"].mean()
total_reviews    = df["reviewCount"].sum()
avg_useful_pct   = (df["usefulCount"] / df["reviewCount"].replace(0, np.nan)).mean() * 100

k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(kpi_card("💊", "Unique Drugs", f"{n_unique_drugs}", accent="#00e5a0"), unsafe_allow_html=True)
with k2:
    st.markdown(kpi_card("🏥", "Conditions", f"{n_conditions}", accent="#3b9eff"), unsafe_allow_html=True)
with k3:
    st.markdown(kpi_card("⭐", "Avg. Rating", f"{avg_rating:.2f} / 10",
                         delta=f"↑ Above midpoint" if avg_rating >= 5 else "↓ Below midpoint",
                         accent="#f5a623"), unsafe_allow_html=True)
with k4:
    st.markdown(kpi_card("📝", "Total Reviews", f"{total_reviews:,}",
                         delta=f"~{avg_useful_pct:.0f}% marked useful",
                         accent="#ff6b8a"), unsafe_allow_html=True)

st.markdown("<div style='margin-top:1.6rem'></div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# EXECUTIVE SUMMARY EXPANDER
# ──────────────────────────────────────────────────────────────────────
top_cond     = df.groupby("condition")["reviewCount"].sum().idxmax()
top_drug     = df.groupby("drugName")["reviewCount"].sum().idxmax()
best_rated   = df.groupby("drugName")["rating"].mean().idxmax()
worst_rated  = df.groupby("drugName")["rating"].mean().idxmin()
high_engage  = df.groupby("drugName").apply(
    lambda x: (x["usefulCount"] / x["reviewCount"].replace(0, np.nan)).mean()
).idxmax()

with st.expander("📋  Executive Summary  —  click to expand key insights", expanded=True):
    st.markdown(f"""
    <div style="padding:.4rem 0;line-height:1.9;font-size:.88rem;color:#8b95a8">
        The current filtered view covers
        <span style="color:#e8edf5;font-weight:600">{len(df):,} patient records</span>
        across <span style="color:#3b9eff;font-weight:600">{n_conditions} therapeutic condition(s)</span>
        and <span style="color:#00e5a0;font-weight:600">{n_unique_drugs} unique medications</span>.
        The portfolio carries an average patient satisfaction score of
        <span style="color:#f5a623;font-weight:600">{avg_rating:.2f}/10</span>,
        with <span style="color:#ff6b8a;font-weight:600">{avg_useful_pct:.1f}%</span>
        of reviews marked as clinically useful by peers.<br><br>
        The dominant therapeutic area by review volume is
        <span style="color:#e8edf5;font-weight:600">{top_cond}</span>, while
        <span style="color:#00e5a0;font-weight:600">{top_drug}</span> leads in total engagement.
        <span style="color:#00e5a0;font-weight:600">{best_rated}</span> holds the highest mean patient rating in this cohort,
        whereas <span style="color:#ff6b8a;font-weight:600">{worst_rated}</span> records the lowest satisfaction index.
        <span style="color:#3b9eff;font-weight:600">{high_engage}</span> demonstrates the strongest peer-usefulness ratio,
        suggesting high clinical consensus around its therapeutic value.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-top:0.6rem'></div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# CHART TABS
# ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "  📊  Market Overview & Condition Dominance  ",
    "  🧠  Patient Sentiment & Rating Polarity  ",
    "  💡  Engagement & Usefulness Metrics  ",
])

# ╔══════════════ TAB 1 ════════════════════════════════════════════════╗
with tab1:
    col_a, col_b = st.columns([1, 1], gap="large")

    # ── Donut: reviews by condition ──
    with col_a:
        st.markdown(section_header("Condition Share by Review Volume",
                                   "Patient engagement distributed across therapeutic areas"), unsafe_allow_html=True)
        cond_reviews = df.groupby("condition")["reviewCount"].sum().reset_index()
        cond_reviews.columns = ["Condition", "Reviews"]
        cond_reviews = cond_reviews.sort_values("Reviews", ascending=False)

        fig_donut = go.Figure(go.Pie(
            labels=cond_reviews["Condition"],
            values=cond_reviews["Reviews"],
            hole=0.58,
            marker=dict(
                colors=px.colors.qualitative.Safe,
                line=dict(color="#0d1117", width=2),
            ),
            textinfo="percent",
            hovertemplate="<b>%{label}</b><br>Reviews: %{value:,}<br>Share: %{percent}<extra></extra>",
        ))
        fig_donut.add_annotation(
            text=f"<b>{cond_reviews['Reviews'].sum():,}</b><br><span style='font-size:10px'>Total Reviews</span>",
            x=0.5, y=0.5, showarrow=False,
            font=dict(color="#e8edf5", size=15, family="Syne, sans-serif"),
            align="center",
        )
        apply_base(fig_donut, height=380)
        fig_donut.update_layout(legend=dict(orientation="v", x=1, y=0.5,
                                            font=dict(size=10, color="#8b95a8")))
        st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar": False})

    # ── Horizontal bar: top 12 drugs by reviews ──
    with col_b:
        st.markdown(section_header("Top Drugs by Review Engagement",
                                   "Medications ranked by cumulative patient review volume"), unsafe_allow_html=True)
        top_drugs_df = (
            df.groupby("drugName")["reviewCount"]
            .sum()
            .reset_index()
            .sort_values("reviewCount", ascending=True)
            .tail(12)
        )

        fig_hbar = go.Figure(go.Bar(
            x=top_drugs_df["reviewCount"],
            y=top_drugs_df["drugName"],
            orientation="h",
            marker=dict(
                color=top_drugs_df["reviewCount"],
                colorscale=[[0, "#1a3a4a"], [0.5, "#00b0ff"], [1, "#00e5a0"]],
                showscale=False,
                line=dict(width=0),
            ),
            hovertemplate="<b>%{y}</b><br>Reviews: %{x:,}<extra></extra>",
            text=top_drugs_df["reviewCount"].apply(lambda v: f"{v:,}"),
            textposition="outside",
            textfont=dict(size=10, color="#4e5a6e"),
        ))
        apply_base(fig_hbar, height=380)
        fig_hbar.update_layout(
            yaxis=dict(gridcolor="rgba(0,0,0,0)"),
            xaxis_title="Total Reviews",
            bargap=0.35,
        )
        st.plotly_chart(fig_hbar, use_container_width=True, config={"displayModeBar": False})

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Average rating by condition (sorted bar) ──
    st.markdown(section_header("Mean Patient Satisfaction by Condition",
                               "Average rating score per therapeutic area · Scale 1–10"), unsafe_allow_html=True)
    cond_rating = (
        df.groupby("condition")["rating"]
        .mean()
        .reset_index()
        .sort_values("rating", ascending=False)
    )
    cond_rating.columns = ["Condition", "Avg Rating"]

    fig_cond_bar = go.Figure(go.Bar(
        x=cond_rating["Condition"],
        y=cond_rating["Avg Rating"],
        marker=dict(
            color=cond_rating["Avg Rating"],
            colorscale=[[0, "#b94fff"], [0.5, "#3b9eff"], [1, "#00e5a0"]],
            showscale=True,
            colorbar=dict(
                tickfont=dict(color="#4e5a6e", size=10),
                outlinewidth=0,
                thickness=10,
                len=0.7,
            ),
            line=dict(width=0),
        ),
        hovertemplate="<b>%{x}</b><br>Avg Rating: %{y:.2f}<extra></extra>",
        text=cond_rating["Avg Rating"].round(2),
        textposition="outside",
        textfont=dict(size=9, color="#4e5a6e"),
    ))
    apply_base(fig_cond_bar, height=340)
    fig_cond_bar.add_hline(y=5, line_dash="dot", line_color="#4e5a6e",
                           annotation_text=" Midpoint (5.0)", annotation_font_color="#4e5a6e",
                           annotation_font_size=10)
    fig_cond_bar.update_layout(xaxis_tickangle=-35, yaxis_range=[0, 11], bargap=0.3)
    st.plotly_chart(fig_cond_bar, use_container_width=True, config={"displayModeBar": False})


# ╔══════════════ TAB 2 ════════════════════════════════════════════════╗
with tab2:
    col_left, col_right = st.columns([1.1, 0.9], gap="large")

    # ── U-shaped rating histogram ──
    with col_left:
        st.markdown(section_header("Patient Rating Distribution",
                                   "U-shaped bimodal sentiment profile across all records"), unsafe_allow_html=True)

        fig_hist = go.Figure()
        fig_hist.add_trace(go.Histogram(
            x=df["rating"],
            nbinsx=10,
            marker=dict(
                color=df["rating"].values if len(df) > 0 else [5],
                colorscale=[[0, "#ff6b8a"], [0.45, "#4e5a6e"], [0.55, "#4e5a6e"], [1, "#00e5a0"]],
                line=dict(color="#0d1117", width=1.5),
            ),
            hovertemplate="Rating: %{x}<br>Count: %{y}<extra></extra>",
            name="",
        ))
        apply_base(fig_hist, height=360)
        fig_hist.update_layout(
            xaxis=dict(title="Rating (1–10)", tickvals=list(range(1, 11))),
            yaxis_title="Number of Reviews",
            showlegend=False,
            bargap=0.08,
        )
        # Shade extremes
        for xs, xe, col in [(0.5, 3.5, "rgba(255,107,138,.06)"), (7.5, 10.5, "rgba(0,229,160,.06)")]:
            fig_hist.add_vrect(x0=xs, x1=xe, fillcolor=col, line_width=0)
        fig_hist.add_annotation(x=2, y=0, yref="paper", text="⚠ Low sentiment",
                                showarrow=False, font=dict(color="#ff6b8a", size=9), yanchor="bottom", ay=-30)
        fig_hist.add_annotation(x=9, y=0, yref="paper", text="✓ High satisfaction",
                                showarrow=False, font=dict(color="#00e5a0", size=9), yanchor="bottom")
        st.plotly_chart(fig_hist, use_container_width=True, config={"displayModeBar": False})

    # ── Box plot: rating by condition ──
    with col_right:
        st.markdown(section_header("Rating Spread by Condition",
                                   "Interquartile distribution & outlier visibility"), unsafe_allow_html=True)

        box_conditions = df["condition"].value_counts().head(8).index.tolist()
        df_box = df[df["condition"].isin(box_conditions)]

        fig_box = go.Figure()
        palette = TEAL_PALETTE + ["#a0b4c8", "#c8a0b4"]
        for i, cond in enumerate(box_conditions):
            sub = df_box[df_box["condition"] == cond]["rating"]
            fig_box.add_trace(go.Box(
                y=sub,
                name=cond[:18] + ("…" if len(cond) > 18 else ""),
                marker=dict(color=palette[i % len(palette)], size=3, opacity=0.6),
                line=dict(color=palette[i % len(palette)], width=1.5),
                fillcolor=hex_to_rgba(palette[i % len(palette)], alpha=0.12),
                boxmean=True,
                hovertemplate="<b>%{x}</b><br>Rating: %{y}<extra></extra>",
            ))
        apply_base(fig_box, height=360)
        fig_box.update_layout(
            yaxis=dict(title="Rating", range=[0, 11]),
            xaxis=dict(tickangle=-30),
            showlegend=False,
            boxgap=0.25,
            boxgroupgap=0.1,
        )
        st.plotly_chart(fig_box, use_container_width=True, config={"displayModeBar": False})

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Violin: overall + by top conditions ──
    st.markdown(section_header("Rating Density Violin — Top Conditions",
                               "Full distribution shape including tails and modes"), unsafe_allow_html=True)

    top6_conds = df["condition"].value_counts().head(6).index.tolist()
    df_violin = df[df["condition"].isin(top6_conds)]

    fig_violin = go.Figure()
    for i, cond in enumerate(top6_conds):
        sub = df_violin[df_violin["condition"] == cond]["rating"]
        fig_violin.add_trace(go.Violin(
            x=[cond[:16]] * len(sub),
            y=sub,
            name=cond[:16],
            box_visible=True,
            meanline_visible=True,
            fillcolor=hex_to_rgba(TEAL_PALETTE[i % len(TEAL_PALETTE)], alpha=0.2),
            line_color=TEAL_PALETTE[i % len(TEAL_PALETTE)],
            opacity=0.9,
            bandwidth=0.5,
            hovertemplate="<b>%{x}</b><br>Rating: %{y:.1f}<extra></extra>",
        ))
    apply_base(fig_violin, height=320)
    fig_violin.update_layout(
        yaxis=dict(title="Rating", range=[0, 11]),
        showlegend=False,
        violingroupgap=0.15,
    )
    st.plotly_chart(fig_violin, use_container_width=True, config={"displayModeBar": False})


# ╔══════════════ TAB 3 ════════════════════════════════════════════════╗
with tab3:
    col_p, col_q = st.columns([1.15, 0.85], gap="large")

    # ── Scatter: helpful votes vs rating ──
    with col_p:
        st.markdown(section_header("Helpfulness vs. Rating Scatter",
                                   "Correlation between peer-useful votes and mean patient satisfaction"), unsafe_allow_html=True)

        scatter_df = (
            df.groupby(["drugName", "condition"])
            .agg(avg_rating=("rating", "mean"),
                 total_useful=("usefulCount", "sum"),
                 total_reviews=("reviewCount", "sum"))
            .reset_index()
        )

        fig_scatter = px.scatter(
            scatter_df,
            x="avg_rating",
            y="total_useful",
            color="condition",
            size="total_reviews",
            hover_name="drugName",
            color_discrete_sequence=px.colors.qualitative.Safe,
            size_max=40,
            custom_data=["drugName", "condition", "total_reviews"],
        )
        fig_scatter.update_traces(
            hovertemplate="<b>%{customdata[0]}</b><br>Condition: %{customdata[1]}<br>"
                          "Avg Rating: %{x:.2f}<br>Useful Votes: %{y:,}<br>"
                          "Reviews: %{customdata[2]:,}<extra></extra>",
            marker=dict(line=dict(width=0.5, color="#0d1117"), opacity=0.85),
        )
        apply_base(fig_scatter, height=400)
        fig_scatter.update_layout(
            xaxis=dict(title="Average Patient Rating", range=[0, 11]),
            yaxis=dict(title="Total Useful Votes"),
            legend=dict(orientation="h", x=0, y=-0.18, font=dict(size=9)),
        )
        st.plotly_chart(fig_scatter, use_container_width=True, config={"displayModeBar": False})

    # ── Usefulness rate by condition ──
    with col_q:
        st.markdown(section_header("Peer-Usefulness Rate by Condition",
                                   "Average % of reviews marked useful by other patients"), unsafe_allow_html=True)

        use_rate = df.copy()
        use_rate["useful_rate"] = use_rate["usefulCount"] / use_rate["reviewCount"].replace(0, np.nan)
        use_cond = (
            use_rate.groupby("condition")["useful_rate"]
            .mean()
            .reset_index()
            .sort_values("useful_rate", ascending=True)
        )
        use_cond.columns = ["Condition", "Useful Rate"]
        use_cond["Pct"] = (use_cond["Useful Rate"] * 100).round(1)

        fig_use = go.Figure(go.Bar(
            x=use_cond["Pct"],
            y=use_cond["Condition"],
            orientation="h",
            marker=dict(
                color=use_cond["Pct"],
                colorscale=[[0, "#1a273a"], [0.5, "#7c6fff"], [1, "#3b9eff"]],
                showscale=False,
                line=dict(width=0),
            ),
            text=use_cond["Pct"].apply(lambda v: f"{v:.1f}%"),
            textposition="outside",
            textfont=dict(size=10, color="#4e5a6e"),
            hovertemplate="<b>%{y}</b><br>Usefulness: %{x:.1f}%<extra></extra>",
        ))
        apply_base(fig_use, height=400)
        fig_use.update_layout(
            xaxis=dict(title="Usefulness Rate (%)", range=[0, 75]),
            yaxis=dict(gridcolor="rgba(0,0,0,0)"),
            bargap=0.3,
        )
        st.plotly_chart(fig_use, use_container_width=True, config={"displayModeBar": False})

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Heatmap: avg rating drug × condition ──
    st.markdown(section_header("Drug × Condition Rating Heatmap",
                               "Mean patient satisfaction across top drugs and conditions"), unsafe_allow_html=True)

    top_d = df["drugName"].value_counts().head(16).index.tolist()
    top_c = df["condition"].value_counts().head(10).index.tolist()
    heat_df = (
        df[df["drugName"].isin(top_d) & df["condition"].isin(top_c)]
        .groupby(["drugName", "condition"])["rating"]
        .mean()
        .unstack(fill_value=np.nan)
    )
    heat_df = heat_df.reindex(index=top_d, columns=top_c)

    fig_heat = go.Figure(go.Heatmap(
        z=heat_df.values,
        x=heat_df.columns.tolist(),
        y=heat_df.index.tolist(),
        colorscale=[
            [0.0, "#1a1030"], [0.3, "#7c3fbf"], [0.6, "#3b9eff"],
            [0.8, "#00c896"], [1.0, "#00e5a0"],
        ],
        zmin=1, zmax=10,
        text=np.where(np.isnan(heat_df.values), "", np.round(heat_df.values, 1).astype(str)),
        texttemplate="%{text}",
        textfont=dict(size=8, color="#e8edf5"),
        hovertemplate="Drug: <b>%{y}</b><br>Condition: <b>%{x}</b><br>Avg Rating: <b>%{z:.2f}</b><extra></extra>",
        colorbar=dict(
            title=dict(text="Avg Rating", font=dict(color="#8b95a8", size=10)),
            tickfont=dict(color="#4e5a6e", size=9),
            outlinewidth=0,
            thickness=10,
            len=0.8,
        ),
        xgap=2, ygap=2,
    ))
    apply_base(fig_heat, height=440)
    fig_heat.update_layout(
        xaxis=dict(side="bottom", tickangle=-35, tickfont=dict(size=9)),
        yaxis=dict(tickfont=dict(size=9)),
    )
    st.plotly_chart(fig_heat, use_container_width=True, config={"displayModeBar": False})


# ──────────────────────────────────────────────────────────────────────
# INSIGHTS PANEL
# ──────────────────────────────────────────────────────────────────────
st.markdown("<div style='margin-top:1.2rem'></div>", unsafe_allow_html=True)
st.markdown("""
<div style="display:flex;align-items:center;gap:10px;margin-bottom:1rem">
    <div style="width:3px;height:22px;background:linear-gradient(180deg,#00e5a0,#3b9eff);border-radius:2px"></div>
    <div>
        <span style="font-family:'Syne',sans-serif;font-size:1.05rem;font-weight:700;color:#e8edf5">
            Intelligent Insights Panel
        </span>
        <span style="font-size:.75rem;color:#4e5a6e;margin-left:10px">
            Programmatic analysis based on active filters
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

with st.container():
    drug_avg_rating  = df.groupby("drugName")["rating"].mean()
    drug_total_rev   = df.groupby("drugName")["reviewCount"].sum()
    drug_useful_rate = (
        df.groupby("drugName")
        .apply(lambda x: (x["usefulCount"] / x["reviewCount"].replace(0, np.nan)).mean())
    )

    best_drug     = drug_avg_rating.idxmax()
    best_score    = drug_avg_rating.max()
    worst_drug    = drug_avg_rating.idxmin()
    worst_score   = drug_avg_rating.min()
    most_rev_drug = drug_total_rev.idxmax()
    most_rev_val  = drug_total_rev.max()
    useful_drug   = drug_useful_rate.idxmax()
    useful_val    = drug_useful_rate.max() * 100

    most_common_cond = df["condition"].value_counts().idxmax()
    most_common_n    = df["condition"].value_counts().max()

    # Pre-compute plain display strings (no nested HTML tags)
    health_score   = f"{(avg_rating / 10 * 100):.0f}/100"
    drugs_str      = str(n_unique_drugs)
    conds_str      = str(n_conditions)
    useful_pct_str = f"{avg_useful_pct:.1f}%"
    health_desc    = (
        f"{health_score} composite score based on mean rating across "
        f"{drugs_str} drugs in {conds_str} condition(s). "
        f"Peer usefulness consensus at {useful_pct_str}."
    )

    # ── Row 1: five stat chips ────────────────────────────────────────
    chips_row = (
        f'<div style="display:flex;flex-wrap:wrap;gap:12px;'
        f'background:#1c2230;border:1px solid #2a3448;'
        f'border-radius:14px;padding:20px 20px 14px 20px">'
        + insight_chip("🏆 Highest Rated Drug",  f"{best_drug} ({best_score:.2f}/10)",      "#00e5a0")
        + insight_chip("⚠️ Lowest Rated Drug",   f"{worst_drug} ({worst_score:.2f}/10)",     "#ff6b8a")
        + insight_chip("📊 Most Reviewed Drug",   f"{most_rev_drug} ({most_rev_val:,} reviews)", "#3b9eff")
        + insight_chip("💡 Highest Usefulness",   f"{useful_drug} ({useful_val:.1f}%)",       "#7c6fff")
        + insight_chip("🏥 Dominant Condition",   f"{most_common_cond} ({most_common_n:,} records)", "#f5a623")
        + "</div>"
    )
    st.markdown(chips_row, unsafe_allow_html=True)

    # ── Row 2: Portfolio Health Score card (plain text, no nested tags) ──
    health_card = (
        f'<div style="margin-top:10px;background:#1c2230;border:1px solid #2a3448;'
        f'border-top:2px solid #00e5a0;border-radius:14px;padding:18px 22px;">'
        f'<div style="font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;'
        f'color:#00e5a0;font-weight:600;margin-bottom:8px;">📈 Portfolio Health Score</div>'
        f'<div style="display:flex;align-items:baseline;gap:10px;flex-wrap:wrap">'
        f'<span style="font-family:\'Syne\',sans-serif;font-size:2.2rem;font-weight:800;'
        f'color:#e8edf5;line-height:1">{health_score}</span>'
        f'<span style="font-size:.82rem;color:#4e5a6e;max-width:560px;line-height:1.6">'
        f'composite score &nbsp;·&nbsp; {drugs_str} drugs across {conds_str} condition(s) '
        f'&nbsp;·&nbsp; {useful_pct_str} peer-usefulness consensus'
        f'</span>'
        f'</div>'
        f'</div>'
    )
    st.markdown(health_card, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-top:3rem;padding-top:1rem;border-top:1px solid #2a3448;
            display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px">
    <div style="font-size:.72rem;color:#2a3448">
        ⚕️ <span style="color:#4e5a6e">PharmaIQ · Executive Analytics Suite</span>
        <span style="color:#2a3448"> · </span>
        <span style="color:#4e5a6e">Synthetic RWE dataset — for demonstration purposes only</span>
    </div>
    <div style="font-family:'DM Mono',monospace;font-size:.68rem;color:#2a3448">
        v2025.1 · Streamlit + Plotly
    </div>
</div>
""", unsafe_allow_html=True)