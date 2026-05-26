# 💊 Advanced Drug Analysis & Statistics Dashboard

An interactive, executive-level data analytics portal built with Python, Streamlit, and Plotly to analyze patient drug reviews, sentiment polarization, and medical condition distributions.

## 🚀 Features

* **Executive KPI Cards:** Instant high-level metrics tracking unique treatments, average ratings, total reviews, and user engagement.
* **Polarity Distribution Analysis:** Interactive histograms highlighting the traditional "U-shaped" nature of patient drug reviews (extreme positive vs. extreme side-effects).
* **Market Share Breakdown:** Macro-level distribution charts displaying dominant medical conditions and the top 10 most reviewed medications.
* **Dynamic Filtering:** Sidebar controls allowing instant, responsive data drilling by specific medical conditions.
* **Offline-Ready Architecture:** Includes a robust local data engine mimicking real-world clinical datasets for seamless, standalone deployment.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Streamlit (UI/UX & Deployment)
* **Visualization:** Plotly Express (Interactive Data Graphics)
* **Data Handling:** Pandas & NumPy

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
Install required dependencies:

Bash
pip install streamlit pandas plotly numpy
Run the local development server:

Bash
python -m streamlit run app.py
📊 Core Visualizations Inside
Patient Ratings Histogram: Displays the distribution of clinical ratings (1–10).

Top Reviewed Medications: Horizontal bar charts visualizing prescription volume trends.

Condition Market Breakdown: Donut/Pie chart analyzing condition prevalence.

Sentiment vs. Utility Mapping: Scatter plotting user helpfulness upvotes against patient satisfaction.
