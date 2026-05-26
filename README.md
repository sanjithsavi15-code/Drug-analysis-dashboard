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

<h2>📦 Installation & Setup</h2>

<ul>
  <li><b>Clone the repository:</b> git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git</li>
  <li><b>Navigate into the folder:</b> cd YOUR_REPO_NAME</li>
  <li><b>Install required dependencies:</b> pip install streamlit pandas plotly numpy</li>
  <li><b>Run the local development server:</b> python -m streamlit run app.py</li>
</ul>

<h2>📊 Core Visualizations Inside</h2>

<ul>
  <li><b>Patient Ratings Histogram:</b> Displays the distribution of clinical ratings (1–10).</li>
  <li><b>Top Reviewed Medications:</b> Horizontal bar charts visualizing prescription volume trends.</li>
  <li><b>Condition Market Breakdown:</b> Donut/Pie chart analyzing condition prevalence.</li>
  <li><b>Sentiment vs. Utility Mapping:</b> Scatter plotting user helpfulness upvotes against patient satisfaction.</li>
</ul>
