# # # import streamlit as st
# # # from PyPDF2 import PdfReader
# # # import pandas as pd
# # # import time
# # # import matplotlib.pyplot as plt
# # # from sklearn.feature_extraction.text import TfidfVectorizer
# # # from sklearn.metrics.pairwise import cosine_similarity

# # # # 🎨 **Custom CSS for a Beautiful UI**
# # # st.markdown("""
# # #     <style>
# # #     body {
# # #         background-color: #121212;
# # #         color: white;
# # #     }
# # #     .stApp {
# # #         background-color: #1E1E1E;
# # #     }
# # #     h1 {
# # #         text-align: center;
# # #         color: #4CAF50;
# # #         font-size: 36px;
# # #         font-weight: bold;
# # #     }
# # #     .stTextArea, .stFileUploader {
# # #         border-radius: 10px;
# # #         box-shadow: 0 0 10px #4CAF50;
# # #     }
# # #     .stButton>button {
# # #         background-color: #4CAF50;
# # #         color: white;
# # #         padding: 12px 18px;
# # #         font-size: 18px;
# # #         border-radius: 8px;
# # #         border: none;
# # #         transition: 0.3s;
# # #     }
# # #     .stButton>button:hover {
# # #         background-color: #45a049;
# # #     }
# # #     .stDataFrame {
# # #         border-radius: 10px;
# # #         box-shadow: 0px 0px 10px rgba(0, 255, 0, 0.5);
# # #     }
# # #     </style>
# # # """, unsafe_allow_html=True)

# # # # 📌 **Page Title**
# # # st.title("🚀 Resume Ranking System")

# # # col1, col2 = st.columns(2)

# # # with col1:
# # #     st.header("📤 Upload Resumes")
# # #     uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

# # # with col2:
# # #     st.header("📝 Job Description")
# # #     job_description = st.text_area("Enter the job description...")

# # # # 📌 **Extract Text from PDF Resumes**
# # # def extract_text_from_pdf(file):
# # #     pdf = PdfReader(file)
# # #     text = "".join([page.extract_text() or "" for page in pdf.pages])
# # #     return text.strip()

# # # # 📌 **Rank Resumes Using TF-IDF & Cosine Similarity**
# # # def rank_resumes(job_description, resumes):
# # #     documents = [job_description] + resumes
# # #     vectorizer = TfidfVectorizer().fit_transform(documents)
# # #     vectors = vectorizer.toarray()
# # #     job_desc_vector = vectors[0]
# # #     resume_vectors = vectors[1:]
# # #     return cosine_similarity([job_desc_vector], resume_vectors).flatten()

# # # # 📌 **AI Suggestions for Resume Improvement**
# # # def generate_resume_tips(score):
# # #     if score > 80:
# # #         return "🔥 Excellent match! Your resume is well-optimized."
# # #     elif score > 60:
# # #         return "✅ Good match! Consider adding more relevant keywords."
# # #     else:
# # #         return "⚡ Low match! Try improving your skills section and adding industry-specific terms."

# # # # 📌 **Start Ranking Process**
# # # if uploaded_files and job_description:
# # #     st.header("📊 Resume Rankings")

# # #     resumes = [extract_text_from_pdf(file) for file in uploaded_files]

# # #     progress_bar = st.progress(0)
# # #     for i in range(100):
# # #         time.sleep(0.02)
# # #         progress_bar.progress(i + 1)

# # #     scores = rank_resumes(job_description, resumes)

# # #     results_df = pd.DataFrame({
# # #         "Resume": [file.name for file in uploaded_files],
# # #         "Match Score (%)": (scores * 100).round(2),
# # #         "AI Suggestion": [generate_resume_tips(score * 100) for score in scores]
# # #     }).sort_values(by="Match Score (%)", ascending=False)

# # #     st.dataframe(results_df.style.format({"Match Score (%)": "{:.2f}"}))
# # #     st.success(f"✅ Ranking Complete! 🎯 Top Match: **{results_df.iloc[0]['Resume']}**")
    
# # import streamlit as st
# # import pandas as pd
# # import time
# # import matplotlib.pyplot as plt
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from sklearn.metrics.pairwise import cosine_similarity
# # from PyPDF2 import PdfReader
# # import plotly.express as px
# # import plotly.graph_objects as go
# # import base64
# # from io import BytesIO
# # import requests
# # import json

# # # Page configuration
# # st.set_page_config(
# #     page_title="Resume Ranking System",
# #     page_icon="📊",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # Custom CSS for elegant UI
# # st.markdown("""
# # <style>
# #     /* Main theme colors */
# #     :root {
# #         --primary-color: #3b82f6;
# #         --primary-light: #93c5fd;
# #         --primary-dark: #1d4ed8;
# #         --secondary-color: #f3f4f6;
# #         --text-color: #1f2937;
# #         --success-color: #10b981;
# #         --warning-color: #f59e0b;
# #         --danger-color: #ef4444;
# #     }
    
# #     /* Base styling */
# #     .main {
# #         background-color: #f8fafc;
# #         color: var(--text-color);
# #     }
    
# #     h1, h2, h3 {
# #         color: var(--primary-dark);
# #     }
    
# #     /* Card styling */
# #     .card {
# #         border-radius: 10px;
# #         border: 1px solid #e5e7eb;
# #         padding: 1.5rem;
# #         margin-bottom: 1rem;
# #         background-color: white;
# #         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
# #     }
    
# #     .card-header {
# #         border-bottom: 1px solid #e5e7eb;
# #         padding-bottom: 0.75rem;
# #         margin-bottom: 1rem;
# #         font-weight: 600;
# #         font-size: 1.25rem;
# #         color: var(--primary-dark);
# #     }
    
# #     /* Button styling */
# #     .stButton > button {
# #         background-color: var(--primary-color);
# #         color: white;
# #         border-radius: 6px;
# #         padding: 0.5rem 1rem;
# #         font-weight: 500;
# #         border: none;
# #         transition: all 0.3s ease;
# #     }
    
# #     .stButton > button:hover {
# #         background-color: var(--primary-dark);
# #         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
# #     }
    
# #     /* File uploader styling */
# #     .stFileUploader > div > div {
# #         border: 2px dashed var(--primary-light);
# #         border-radius: 10px;
# #         padding: 2rem;
# #         background-color: #f8fafc;
# #     }
    
# #     /* Text area styling */
# #     .stTextArea > div > div > textarea {
# #         border-radius: 6px;
# #         border-color: #e5e7eb;
# #     }
    
# #     /* Metrics styling */
# #     .metric-card {
# #         background-color: white;
# #         border-radius: 8px;
# #         padding: 1rem;
# #         box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
# #         border-left: 4px solid var(--primary-color);
# #     }
    
# #     .metric-value {
# #         font-size: 1.5rem;
# #         font-weight: 700;
# #         color: var(--primary-dark);
# #     }
    
# #     .metric-label {
# #         font-size: 0.875rem;
# #         color: #6b7280;
# #     }
    
# #     /* Progress bar animation */
# #     @keyframes pulse {
# #         0% {
# #             box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7);
# #         }
# #         70% {
# #             box-shadow: 0 0 0 10px rgba(59, 130, 246, 0);
# #         }
# #         100% {
# #             box-shadow: 0 0 0 0 rgba(59, 130, 246, 0);
# #         }
# #     }
    
# #     .stProgress > div > div > div {
# #         background-color: var(--primary-color);
# #         animation: pulse 2s infinite;
# #     }
    
# #     /* Dataframe styling */
# #     .dataframe-container {
# #         border-radius: 8px;
# #         overflow: hidden;
# #         border: 1px solid #e5e7eb;
# #     }
    
# #     /* Expander styling */
# #     .streamlit-expanderHeader {
# #         font-weight: 600;
# #         color: var(--primary-dark);
# #     }
    
# #     /* Success message styling */
# #     .success-message {
# #         background-color: #ecfdf5;
# #         border-left: 4px solid var(--success-color);
# #         padding: 1rem;
# #         border-radius: 6px;
# #         margin: 1rem 0;
# #     }
    
# #     /* Sidebar styling */
# #     .css-1d391kg {
# #         background-color: #f1f5f9;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # Sidebar
# # with st.sidebar:
# #     st.title("⚙️ Settings")
    
# #     st.markdown("### Analysis Options")
    
# #     min_match_threshold = st.slider(
# #         "Minimum Match Threshold (%)", 
# #         min_value=0, 
# #         max_value=100, 
# #         value=50,
# #         help="Resumes below this threshold will be marked as poor matches"
# #     )
    
# #     keyword_weight = st.slider(
# #         "Keyword Importance", 
# #         min_value=1, 
# #         max_value=10, 
# #         value=5,
# #         help="How much to weight exact keyword matches"
# #     )
    
# #     st.markdown("### Visualization Settings")
    
# #     chart_type = st.selectbox(
# #         "Chart Type",
# #         options=["Bar Chart", "Horizontal Bar", "Radar Chart"],
# #         index=0
# #     )
    
# #     color_theme = st.selectbox(
# #         "Color Theme",
# #         options=["Blues", "Greens", "Purples", "Oranges"],
# #         index=0
# #     )
    
# #     st.markdown("---")
# #     st.markdown("### About")
# #     st.markdown("""
# #     This app helps you rank resumes based on job descriptions using NLP techniques.
    
# #     **Features:**
# #     - PDF resume analysis
# #     - TF-IDF vectorization
# #     - Cosine similarity scoring
# #     - AI-powered improvement tips
# #     """)

# # # Main content
# # st.title("📊 Resume Ranking System")

# # # Sample job description
# # sample_job_description = """
# # Job Title: Full Stack Developer

# # Requirements:
# # - 3+ years of experience in web development
# # - Proficient in JavaScript, React, and Node.js
# # - Experience with database design and management (SQL, MongoDB)
# # - Knowledge of cloud services (AWS, Azure, or GCP)
# # - Strong problem-solving skills and attention to detail
# # - Bachelor's degree in Computer Science or related field

# # Responsibilities:
# # - Develop and maintain web applications
# # - Collaborate with cross-functional teams
# # - Implement responsive design and ensure cross-browser compatibility
# # - Optimize applications for maximum speed and scalability
# # - Stay up-to-date with emerging trends and technologies
# # """

# # # Function to extract text from PDF
# # def extract_text_from_pdf(file):
# #     try:
# #         pdf = PdfReader(file)
# #         text = "".join([page.extract_text() or "" for page in pdf.pages])
# #         return text.strip()
# #     except Exception as e:
# #         st.error(f"Error extracting text from {file.name}: {str(e)}")
# #         return ""

# # # Function to rank resumes
# # def rank_resumes(job_description, resumes):
# #     documents = [job_description] + resumes
# #     vectorizer = TfidfVectorizer(stop_words='english').fit_transform(documents)
# #     vectors = vectorizer.toarray()
# #     job_desc_vector = vectors[0]
# #     resume_vectors = vectors[1:]
# #     return cosine_similarity([job_desc_vector], resume_vectors).flatten()

# # # Function to generate resume tips
# # def generate_resume_tips(score, resume_text, job_description):
# #     score_percentage = score * 100
    
# #     # Extract keywords from job description
# #     vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
# #     vectorizer.fit_transform([job_description])
# #     keywords = vectorizer.get_feature_names_out()
    
# #     # Check which keywords are missing
# #     missing_keywords = [keyword for keyword in keywords if keyword.lower() not in resume_text.lower()]
    
# #     if score_percentage > 80:
# #         tips = [
# #             "Your resume is well-optimized for this position!",
# #             "Consider adding more specific achievements with metrics",
# #             "Tailor your professional summary even further"
# #         ]
# #     elif score_percentage > 60:
# #         tips = [
# #             "Add more relevant keywords to improve matching",
# #             "Quantify your achievements with specific metrics",
# #             "Highlight projects relevant to the job description"
# #         ]
# #     else:
# #         tips = [
# #             "Significantly revise your resume to match job requirements",
# #             "Add relevant skills and experiences mentioned in the job description",
# #             "Consider a skills-based format to highlight relevant capabilities"
# #         ]
    
# #     if missing_keywords:
# #         tips.append(f"Consider adding these keywords: {', '.join(missing_keywords[:5])}")
    
# #     return tips

# # # Function to create a downloadable CSV file (instead of Excel)
# # def to_csv(df):
# #     output = BytesIO()
# #     df.to_csv(output, index=False)
# #     processed_data = output.getvalue()
# #     return processed_data

# # # Function to create download link
# # def get_download_link(df, filename="resume_rankings.csv"):
# #     val = to_csv(df)
# #     b64 = base64.b64encode(val).decode()
# #     return f'<a href="data:text/csv;base64,{b64}" download="{filename}">Download CSV file</a>'

# # # Main layout
# # tab1, tab2 = st.tabs(["📤 Upload & Analyze", "📋 Instructions"])

# # with tab1:
# #     col1, col2 = st.columns([1, 1])
    
# #     with col1:
# #         st.markdown('<div class="card">', unsafe_allow_html=True)
# #         st.markdown('<div class="card-header">Upload Resumes</div>', unsafe_allow_html=True)
# #         uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)
# #         st.markdown('</div>', unsafe_allow_html=True)
    
# #     with col2:
# #         st.markdown('<div class="card">', unsafe_allow_html=True)
# #         st.markdown('<div class="card-header">Job Description</div>', unsafe_allow_html=True)
# #         job_description = st.text_area("Enter the job description...", height=200)
        
# #         col_a, col_b = st.columns([1, 1])
# #         with col_a:
# #             if st.button("Load Sample Job Description"):
# #                 # Use session state instead of experimental_rerun
# #                 st.session_state.job_description = sample_job_description
# #                 job_description = sample_job_description
# #         st.markdown('</div>', unsafe_allow_html=True)
    
# #     # Analysis process
# #     if uploaded_files and job_description:
# #         st.markdown("---")
# #         st.subheader("📈 Analysis Results")
        
# #         # Extract text from resumes
# #         with st.spinner("Processing resumes..."):
# #             progress_bar = st.progress(0)
# #             resumes = []
# #             resume_names = []
            
# #             for i, file in enumerate(uploaded_files):
# #                 resume_text = extract_text_from_pdf(file)
# #                 if resume_text:
# #                     resumes.append(resume_text)
# #                     resume_names.append(file.name)
# #                 progress_bar.progress((i + 1) / len(uploaded_files))
# #                 time.sleep(0.1)
            
# #             # Calculate scores
# #             if resumes:
# #                 scores = rank_resumes(job_description, resumes)
                
# #                 # Create results dataframe
# #                 results_df = pd.DataFrame({
# #                     "Resume": resume_names,
# #                     "Match Score (%)": (scores * 100).round(2)
# #                 })
                
# #                 # Add match category
# #                 def get_match_category(score):
# #                     if score >= 75:
# #                         return "Excellent Match"
# #                     elif score >= 60:
# #                         return "Good Match"
# #                     elif score >= 40:
# #                         return "Fair Match"
# #                     else:
# #                         return "Poor Match"
                
# #                 results_df["Match Category"] = results_df["Match Score (%)"].apply(get_match_category)
                
# #                 # Sort by score
# #                 results_df = results_df.sort_values(by="Match Score (%)", ascending=False)
                
# #                 # Display metrics
# #                 st.markdown('<div style="display: flex; justify-content: space-between; margin-bottom: 20px;">', unsafe_allow_html=True)
                
# #                 metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                
# #                 with metric_col1:
# #                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="metric-value">{len(resumes)}</div>', unsafe_allow_html=True)
# #                     st.markdown('<div class="metric-label">Resumes Analyzed</div>', unsafe_allow_html=True)
# #                     st.markdown('</div>', unsafe_allow_html=True)
                
# #                 with metric_col2:
# #                     top_score = results_df["Match Score (%)"].max()
# #                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="metric-value">{top_score:.1f}%</div>', unsafe_allow_html=True)
# #                     st.markdown('<div class="metric-label">Top Match Score</div>', unsafe_allow_html=True)
# #                     st.markdown('</div>', unsafe_allow_html=True)
                
# #                 with metric_col3:
# #                     avg_score = results_df["Match Score (%)"].mean()
# #                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="metric-value">{avg_score:.1f}%</div>', unsafe_allow_html=True)
# #                     st.markdown('<div class="metric-label">Average Score</div>', unsafe_allow_html=True)
# #                     st.markdown('</div>', unsafe_allow_html=True)
                
# #                 with metric_col4:
# #                     good_matches = results_df[results_df["Match Score (%)"] >= min_match_threshold].shape[0]
# #                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="metric-value">{good_matches}</div>', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="metric-label">Matches Above {min_match_threshold}%</div>', unsafe_allow_html=True)
# #                     st.markdown('</div>', unsafe_allow_html=True)
                
# #                 st.markdown('</div>', unsafe_allow_html=True)
                
# #                 # Display top match
# #                 if not results_df.empty:
# #                     top_match = results_df.iloc[0]
# #                     st.markdown(f"""
# #                     <div class="success-message">
# #                         <h3>🏆 Top Match: {top_match['Resume']}</h3>
# #                         <p>Match Score: <strong>{top_match['Match Score (%)']}%</strong> | Category: <strong>{top_match['Match Category']}</strong></p>
# #                     </div>
# #                     """, unsafe_allow_html=True)
                
# #                 # Display visualization
# #                 st.subheader("📊 Visual Comparison")
                
# #                 fig = None
                
# #                 if chart_type == "Bar Chart":
# #                     fig = px.bar(
# #                         results_df,
# #                         x="Resume",
# #                         y="Match Score (%)",
# #                         color="Match Category",
# #                         color_discrete_map={
# #                             "Excellent Match": "#10b981",
# #                             "Good Match": "#3b82f6",
# #                             "Fair Match": "#f59e0b",
# #                             "Poor Match": "#ef4444"
# #                         },
# #                         title="Resume Match Scores"
# #                     )
# #                     fig.add_hline(y=min_match_threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold ({min_match_threshold}%)")
                
# #                 elif chart_type == "Horizontal Bar":
# #                     fig = px.bar(
# #                         results_df,
# #                         y="Resume",
# #                         x="Match Score (%)",
# #                         color="Match Category",
# #                         color_discrete_map={
# #                             "Excellent Match": "#10b981",
# #                             "Good Match": "#3b82f6",
# #                             "Fair Match": "#f59e0b",
# #                             "Poor Match": "#ef4444"
# #                         },
# #                         title="Resume Match Scores",
# #                         orientation='h'
# #                     )
# #                     fig.add_vline(x=min_match_threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold ({min_match_threshold}%)")
                
# #                 elif chart_type == "Radar Chart":
# #                     # For radar chart, we need to prepare the data differently
# #                     fig = go.Figure()
                    
# #                     for i, row in results_df.iterrows():
# #                         fig.add_trace(go.Scatterpolar(
# #                             r=[row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"]],
# #                             theta=["Relevance", "Skills", "Experience", "Education", "Relevance"],
# #                             fill='toself',
# #                             name=row["Resume"]
# #                         ))
                    
# #                     fig.update_layout(
# #                         polar=dict(
# #                             radialaxis=dict(
# #                                 visible=True,
# #                                 range=[0, 100]
# #                             )
# #                         ),
# #                         title="Resume Match Radar"
# #                     )
                
# #                 if fig:
# #                     fig.update_layout(
# #                         height=500,
# #                         margin=dict(l=20, r=20, t=40, b=20),
# #                         paper_bgcolor="white",
# #                         plot_bgcolor="white",
# #                         font=dict(color="#1f2937")
# #                     )
# #                     # FIX: Add a unique key to the plotly_chart
# #                     st.plotly_chart(fig, use_container_width=True, key="main_chart")
                
# #                 # Display results table
# #                 st.subheader("📋 Detailed Results")
                
# #                 st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
# #                 st.dataframe(
# #                     results_df.style.format({"Match Score (%)": "{:.2f}"})
# #                     .background_gradient(cmap=color_theme, subset=["Match Score (%)"])
# #                     .set_properties(**{'text-align': 'left'})
# #                     .set_table_styles([
# #                         {'selector': 'th', 'props': [('background-color', '#f1f5f9'), ('color', '#1f2937'), ('font-weight', 'bold')]},
# #                         {'selector': 'tr:hover', 'props': [('background-color', '#f1f5f9')]},
# #                     ]),
# #                     use_container_width=True
# #                 )
# #                 st.markdown('</div>', unsafe_allow_html=True)
                
# #                 # Download button (using CSV instead of Excel)
# #                 st.markdown(get_download_link(results_df), unsafe_allow_html=True)
                
# #                 # Detailed analysis for each resume
# #                 st.subheader("🔍 Individual Resume Analysis")
                
# #                 for i, (_, row) in enumerate(results_df.iterrows()):
# #                     resume_name = row["Resume"]
# #                     score = row["Match Score (%)"] / 100
                    
# #                     with st.expander(f"{resume_name} - {row['Match Score (%)']}% ({row['Match Category']})"):
# #                         col1, col2 = st.columns([2, 1])
                        
# #                         with col1:
# #                             st.markdown("### Improvement Tips")
# #                             tips = generate_resume_tips(score, resumes[resume_names.index(resume_name)], job_description)
                            
# #                             for tip in tips:
# #                                 st.markdown(f"- {tip}")
                        
# #                         with col2:
# #                             # Create a gauge chart for the score
# #                             gauge_fig = go.Figure(go.Indicator(
# #                                 mode="gauge+number",
# #                                 value=row["Match Score (%)"],
# #                                 domain={'x': [0, 1], 'y': [0, 1]},
# #                                 title={'text': "Match Score"},
# #                                 gauge={
# #                                     'axis': {'range': [0, 100]},
# #                                     'bar': {'color': "#3b82f6"},
# #                                     'steps': [
# #                                         {'range': [0, 40], 'color': "#fee2e2"},
# #                                         {'range': [40, 60], 'color': "#fef3c7"},
# #                                         {'range': [60, 75], 'color': "#dbeafe"},
# #                                         {'range': [75, 100], 'color': "#d1fae5"}
# #                                     ],
# #                                     'threshold': {
# #                                         'line': {'color': "red", 'width': 4},
# #                                         'thickness': 0.75,
# #                                         'value': min_match_threshold
# #                                     }
# #                                 }
# #                             ))
                            
# #                             gauge_fig.update_layout(
# #                                 height=250,
# #                                 margin=dict(l=20, r=20, t=30, b=20),
# #                                 paper_bgcolor="white",
# #                                 font=dict(color="#1f2937")
# #                             )
                            
# #                             # FIX: Add a unique key to each gauge chart
# #                             st.plotly_chart(gauge_fig, use_container_width=True, key=f"gauge_chart_{i}")

# # with tab2:
# #     st.markdown("""
# #     ## 📋 How to Use This App
    
# #     This Resume Ranking System helps you find the best candidates for a job position by analyzing resumes against a job description.
    
# #     ### Step 1: Upload Resumes
# #     - Click on the "Upload Resumes" area to select PDF files
# #     - You can upload multiple resumes at once
    
# #     ### Step 2: Enter Job Description
# #     - Enter the complete job description in the text area
# #     - Include all requirements, responsibilities, and qualifications
# #     - Use the "Load Sample" button for a quick test
    
# #     ### Step 3: Analyze Results
# #     - The system will process the resumes and rank them based on relevance
# #     - Review the visual comparison and detailed results
# #     - Check individual resume analysis for improvement tips
    
# #     ### Step 4: Export Results
# #     - Download the results as a CSV file for further analysis
    
# #     ### How It Works
    
# #     This app uses Natural Language Processing (NLP) techniques:
    
# #     1. **Text Extraction**: Extracts text from PDF resumes
# #     2. **TF-IDF Vectorization**: Converts text into numerical vectors
# #     3. **Cosine Similarity**: Measures similarity between job description and resumes
# #     4. **AI Analysis**: Generates improvement tips based on matching scores
    
# #     ### Tips for Best Results
    
# #     - Use detailed job descriptions with specific requirements
# #     - Ensure PDFs are properly formatted and text-extractable
# #     - Upload resumes in similar formats for consistent analysis
# #     """)

# # # Footer
# # st.markdown("---")
# # st.markdown("""
# # <div style="text-align: center; color: #6b7280; font-size: 0.8rem;">
# #     © 2023 Resume Ranking System | Built with Streamlit
# # </div>
# # """, unsafe_allow_html=True)


# import streamlit as st
# import pandas as pd
# import time
# import matplotlib.pyplot as plt
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from PyPDF2 import PdfReader
# import plotly.express as px
# import plotly.graph_objects as go
# import base64
# from io import BytesIO
# import requests
# import json
# import random

# # Page configuration
# st.set_page_config(
#     page_title="Resume Ranking System",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for elegant UI with enhanced animations
# st.markdown("""
# <style>
#     /* Main theme colors */
#     :root {
#         --primary-color: #3b82f6;
#         --primary-light: #93c5fd;
#         --primary-dark: #1d4ed8;
#         --secondary-color: #f3f4f6;
#         --text-color: #1f2937;
#         --success-color: #10b981;
#         --warning-color: #f59e0b;
#         --danger-color: #ef4444;
#     }
    
#     /* Base styling */
#     .main {
#         background-color: #f8fafc;
#         color: var(--text-color);
#     }
    
#     h1, h2, h3 {
#         color: var(--primary-dark);
#     }
    
#     /* Title animation */
#     .title-animation {
#         display: inline-block;
#         background: linear-gradient(45deg, var(--primary-color), var(--primary-dark));
#         background-size: 200% 200%;
#         color: white;
#         padding: 0.5rem 1rem;
#         border-radius: 8px;
#         margin-bottom: 1rem;
#         animation: gradient-shift 3s ease infinite;
#         box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
#         transition: transform 0.3s ease;
#     }
    
#     .title-animation:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4);
#     }
    
#     @keyframes gradient-shift {
#         0% {
#             background-position: 0% 50%;
#         }
#         50% {
#             background-position: 100% 50%;
#         }
#         100% {
#             background-position: 0% 50%;
#         }
#     }
    
#     /* Card styling with animations */
#     .card {
#         border-radius: 10px;
#         border: 1px solid #e5e7eb;
#         padding: 1.5rem;
#         margin-bottom: 1rem;
#         background-color: white;
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
#         transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
#         position: relative;
#         overflow: hidden;
#     }
    
#     .card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
#     }
    
#     .card::after {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 4px;
#         background: linear-gradient(90deg, var(--primary-light), var(--primary-dark));
#         transform: scaleX(0);
#         transform-origin: left;
#         transition: transform 0.5s ease;
#     }
    
#     .card:hover::after {
#         transform: scaleX(1);
#     }
    
#     .card-header {
#         border-bottom: 1px solid #e5e7eb;
#         padding-bottom: 0.75rem;
#         margin-bottom: 1rem;
#         font-weight: 600;
#         font-size: 1.25rem;
#         color: var(--primary-dark);
#         position: relative;
#         display: inline-block;
#     }
    
#     .card-header::after {
#         content: '';
#         position: absolute;
#         bottom: 0;
#         left: 0;
#         width: 100%;
#         height: 2px;
#         background: linear-gradient(90deg, var(--primary-color), transparent);
#     }
    
#     /* Button styling with animations */
#     .stButton > button {
#         background-color: var(--primary-color);
#         color: white;
#         border-radius: 6px;
#         padding: 0.5rem 1rem;
#         font-weight: 500;
#         border: none;
#         transition: all 0.3s ease;
#         position: relative;
#         overflow: hidden;
#         z-index: 1;
#     }
    
#     .stButton > button::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: -100%;
#         width: 100%;
#         height: 100%;
#         background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
#         transition: left 0.7s ease;
#         z-index: -1;
#     }
    
#     .stButton > button:hover {
#         background-color: var(--primary-dark);
#         box-shadow: 0 4px 10px rgba(29, 78, 216, 0.3);
#         transform: translateY(-2px);
#     }
    
#     .stButton > button:hover::before {
#         left: 100%;
#     }
    
#     /* File uploader styling with animations */
#     .stFileUploader > div > div {
#         border: 2px dashed var(--primary-light);
#         border-radius: 10px;
#         padding: 2rem;
#         background-color: #f8fafc;
#         transition: all 0.3s ease;
#     }
    
#     .stFileUploader > div > div:hover {
#         border-color: var(--primary-color);
#         background-color: rgba(147, 197, 253, 0.1);
#         transform: scale(1.01);
#     }
    
#     /* Text area styling with animations */
#     .stTextArea > div > div > textarea {
#         border-radius: 6px;
#         border-color: #e5e7eb;
#         transition: all 0.3s ease;
#     }
    
#     .stTextArea > div > div > textarea:focus {
#         border-color: var(--primary-color);
#         box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
#     }
    
#     /* Metrics styling with animations */
#     .metric-card {
#         background-color: white;
#         border-radius: 8px;
#         padding: 1rem;
#         box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
#         border-left: 4px solid var(--primary-color);
#         transition: all 0.3s ease;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .metric-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
#     }
    
#     .metric-card::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background: linear-gradient(45deg, transparent, rgba(147, 197, 253, 0.1), transparent);
#         transform: translateX(-100%);
#         transition: transform 0.6s ease;
#     }
    
#     .metric-card:hover::before {
#         transform: translateX(100%);
#     }
    
#     .metric-value {
#         font-size: 1.5rem;
#         font-weight: 700;
#         color: var(--primary-dark);
#         display: inline-block;
#         animation: count-up 2s ease-out;
#     }
    
#     @keyframes count-up {
#         from {
#             opacity: 0;
#             transform: translateY(20px);
#         }
#         to {
#             opacity: 1;
#             transform: translateY(0);
#         }
#     }
    
#     .metric-label {
#         font-size: 0.875rem;
#         color: #6b7280;
#         position: relative;
#         display: inline-block;
#     }
    
#     .metric-label::after {
#         content: '';
#         position: absolute;
#         bottom: -2px;
#         left: 0;
#         width: 0;
#         height: 1px;
#         background-color: var(--primary-color);
#         transition: width 0.3s ease;
#     }
    
#     .metric-card:hover .metric-label::after {
#         width: 100%;
#     }
    
#     /* Progress bar animation */
#     @keyframes pulse {
#         0% {
#             box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7);
#         }
#         70% {
#             box-shadow: 0 0 0 10px rgba(59, 130, 246, 0);
#         }
#         100% {
#             box-shadow: 0 0 0 0 rgba(59, 130, 246, 0);
#         }
#     }
    
#     .stProgress > div > div > div {
#         background-color: var(--primary-color);
#         animation: pulse 2s infinite, progress-fill 1.5s ease-out;
#     }
    
#     @keyframes progress-fill {
#         from {
#             width: 0%;
#         }
#     }
    
#     /* Dataframe styling with animations */
#     .dataframe-container {
#         border-radius: 8px;
#         overflow: hidden;
#         border: 1px solid #e5e7eb;
#         transition: all 0.3s ease;
#         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
#     }
    
#     .dataframe-container:hover {
#         box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
#     }
    
#     /* Expander styling with animations */
#     .streamlit-expanderHeader {
#         font-weight: 600;
#         color: var(--primary-dark);
#         transition: all 0.3s ease;
#         border-radius: 4px;
#     }
    
#     .streamlit-expanderHeader:hover {
#         background-color: rgba(147, 197, 253, 0.1);
#         padding-left: 5px;
#     }
    
#     /* Success message styling with animations */
#     .success-message {
#         background-color: #ecfdf5;
#         border-left: 4px solid var(--success-color);
#         padding: 1rem;
#         border-radius: 6px;
#         margin: 1rem 0;
#         transition: all 0.3s ease;
#         animation: slide-in 0.5s ease-out;
#     }
    
#     @keyframes slide-in {
#         from {
#             opacity: 0;
#             transform: translateX(-20px);
#         }
#         to {
#             opacity: 1;
#             transform: translateX(0);
#         }
#     }
    
#     .success-message:hover {
#         box-shadow: 0 5px 15px rgba(16, 185, 129, 0.2);
#         transform: translateY(-2px);
#     }
    
#     /* Sidebar styling with animations */
#     .css-1d391kg {
#         background-color: #f1f5f9;
#     }
    
#     /* Animated icons */
#     .animated-icon {
#         display: inline-block;
#         animation: float 3s ease-in-out infinite;
#     }
    
#     @keyframes float {
#         0% {
#             transform: translateY(0px);
#         }
#         50% {
#             transform: translateY(-10px);
#         }
#         100% {
#             transform: translateY(0px);
#         }
#     }
    
#     /* Animated list items */
#     .animated-list li {
#         opacity: 0;
#         animation: fade-in 0.5s ease forwards;
#     }
    
#     @keyframes fade-in {
#         from {
#             opacity: 0;
#             transform: translateY(10px);
#         }
#         to {
#             opacity: 1;
#             transform: translateY(0);
#         }
#     }
    
#     /* Staggered animation for list items */
#     .animated-list li:nth-child(1) { animation-delay: 0.1s; }
#     .animated-list li:nth-child(2) { animation-delay: 0.2s; }
#     .animated-list li:nth-child(3) { animation-delay: 0.3s; }
#     .animated-list li:nth-child(4) { animation-delay: 0.4s; }
#     .animated-list li:nth-child(5) { animation-delay: 0.5s; }
#     .animated-list li:nth-child(6) { animation-delay: 0.6s; }
#     .animated-list li:nth-child(7) { animation-delay: 0.7s; }
#     .animated-list li:nth-child(8) { animation-delay: 0.8s; }
    
#     /* Animated section headers */
#     .animated-header {
#         position: relative;
#         display: inline-block;
#         padding-bottom: 5px;
#     }
    
#     .animated-header::after {
#         content: '';
#         position: absolute;
#         width: 100%;
#         transform: scaleX(0);
#         height: 2px;
#         bottom: 0;
#         left: 0;
#         background-color: var(--primary-color);
#         transform-origin: bottom right;
#         transition: transform 0.3s ease-out;
#     }
    
#     .animated-header:hover::after {
#         transform: scaleX(1);
#         transform-origin: bottom left;
#     }
    
#     /* Animated download button */
#     .download-btn {
#         display: inline-block;
#         padding: 8px 16px;
#         background-color: var(--primary-color);
#         color: white;
#         border-radius: 4px;
#         text-decoration: none;
#         transition: all 0.3s ease;
#         margin-top: 10px;
#         font-weight: 500;
#     }
    
#     .download-btn:hover {
#         background-color: var(--primary-dark);
#         box-shadow: 0 4px 10px rgba(29, 78, 216, 0.3);
#         transform: translateY(-2px);
#     }
    
#     /* Animated tabs */
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 10px;
#     }
    
#     .stTabs [data-baseweb="tab"] {
#         transition: all 0.3s ease;
#         border-radius: 4px 4px 0 0;
#     }
    
#     .stTabs [data-baseweb="tab"]:hover {
#         background-color: rgba(147, 197, 253, 0.1);
#     }
    
#     .stTabs [aria-selected="true"] {
#         background-color: var(--primary-light) !important;
#         color: var(--primary-dark) !important;
#     }
    
#     /* Animated dividers */
#     .animated-divider {
#         height: 3px;
#         background: linear-gradient(90deg, transparent, var(--primary-color), transparent);
#         margin: 20px 0;
#         animation: pulse-width 4s infinite;
#     }
    
#     @keyframes pulse-width {
#         0% {
#             opacity: 0.6;
#         }
#         50% {
#             opacity: 1;
#         }
#         100% {
#             opacity: 0.6;
#         }
#     }
    
#     /* Typing animation for headers */
#     .typing-animation {
#         border-right: 2px solid var(--primary-color);
#         white-space: nowrap;
#         overflow: hidden;
#         animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
#     }
    
#     @keyframes typing {
#         from { width: 0 }
#         to { width: 100% }
#     }
    
#     @keyframes blink-caret {
#         from, to { border-color: transparent }
#         50% { border-color: var(--primary-color) }
#     }
    
#     /* Animated background for sections */
#     .animated-bg {
#         position: relative;
#         overflow: hidden;
#     }
    
#     .animated-bg::before {
#         content: '';
#         position: absolute;
#         top: -50%;
#         left: -50%;
#         width: 200%;
#         height: 200%;
#         background: radial-gradient(circle, rgba(147, 197, 253, 0.1) 0%, transparent 70%);
#         animation: rotate 20s linear infinite;
#         z-index: -1;
#     }
    
#     @keyframes rotate {
#         0% {
#             transform: rotate(0deg);
#         }
#         100% {
#             transform: rotate(360deg);
#         }
#     }
    
#     /* Animated tooltip */
#     .tooltip {
#         position: relative;
#         display: inline-block;
#     }
    
#     .tooltip .tooltiptext {
#         visibility: hidden;
#         width: 120px;
#         background-color: var(--primary-dark);
#         color: white;
#         text-align: center;
#         border-radius: 6px;
#         padding: 5px;
#         position: absolute;
#         z-index: 1;
#         bottom: 125%;
#         left: 50%;
#         margin-left: -60px;
#         opacity: 0;
#         transition: opacity 0.3s;
#     }
    
#     .tooltip .tooltiptext::after {
#         content: "";
#         position: absolute;
#         top: 100%;
#         left: 50%;
#         margin-left: -5px;
#         border-width: 5px;
#         border-style: solid;
#         border-color: var(--primary-dark) transparent transparent transparent;
#     }
    
#     .tooltip:hover .tooltiptext {
#         visibility: visible;
#         opacity: 1;
#     }
# </style>

# <script>
#     // Function to add ripple effect to buttons
#     document.addEventListener('DOMContentLoaded', function() {
#         const buttons = document.querySelectorAll('button');
        
#         buttons.forEach(button => {
#             button.addEventListener('click', function(e) {
#                 const x = e.clientX - e.target.getBoundingClientRect().left;
#                 const y = e.clientY - e.target.getBoundingClientRect().top;
                
#                 const ripple = document.createElement('span');
#                 ripple.style.position = 'absolute';
#                 ripple.style.width = '1px';
#                 ripple.style.height = '1px';
#                 ripple.style.borderRadius = '50%';
#                 ripple.style.backgroundColor = 'rgba(255, 255, 255, 0.7)';
#                 ripple.style.transform = 'scale(0)';
#                 ripple.style.animation = 'ripple 0.6s linear';
#                 ripple.style.left = x + 'px';
#                 ripple.style.top = y + 'px';
                
#                 this.appendChild(ripple);
                
#                 setTimeout(() => {
#                     ripple.remove();
#                 }, 600);
#             });
#         });
#     });
    
#     // Animation for elements when they come into view
#     document.addEventListener('DOMContentLoaded', function() {
#         const observer = new IntersectionObserver((entries) => {
#             entries.forEach(entry => {
#                 if (entry.isIntersecting) {
#                     entry.target.classList.add('animate-in');
#                 }
#             });
#         }, { threshold: 0.1 });
        
#         document.querySelectorAll('.animate-on-scroll').forEach(element => {
#             observer.observe(element);
#         });
#     });
# </script>

# <style>
#     @keyframes ripple {
#         to {
#             transform: scale(100);
#             opacity: 0;
#         }
#     }
    
#     .animate-on-scroll {
#         opacity: 0;
#         transform: translateY(20px);
#         transition: opacity 0.6s ease, transform 0.6s ease;
#     }
    
#     .animate-in {
#         opacity: 1;
#         transform: translateY(0);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Function to create animated text
# def animated_text(text, animation_type="title"):
#     if animation_type == "title":
#         return f'<h1 class="title-animation">{text}</h1>'
#     elif animation_type == "typing":
#         return f'<h2 class="typing-animation" style="display:inline-block; max-width:100%;">{text}</h2>'
#     elif animation_type == "header":
#         return f'<h3 class="animated-header">{text}</h3>'
#     return text

# # Function to create animated divider
# def animated_divider():
#     return '<div class="animated-divider"></div>'

# # Function to create animated icon
# def animated_icon(emoji):
#     return f'<span class="animated-icon">{emoji}</span>'

# # Sidebar
# with st.sidebar:
#     st.markdown(animated_text("⚙️ Settings", "title"), unsafe_allow_html=True)
    
#     st.markdown("### Analysis Options")
    
#     min_match_threshold = st.slider(
#         "Minimum Match Threshold (%)", 
#         min_value=0, 
#         max_value=100, 
#         value=50,
#         help="Resumes below this threshold will be marked as poor matches"
#     )
    
#     keyword_weight = st.slider(
#         "Keyword Importance", 
#         min_value=1, 
#         max_value=10, 
#         value=5,
#         help="How much to weight exact keyword matches"
#     )
    
#     st.markdown(animated_divider(), unsafe_allow_html=True)
#     st.markdown("### Visualization Settings")
    
#     chart_type = st.selectbox(
#         "Chart Type",
#         options=["Bar Chart", "Horizontal Bar", "Radar Chart"],
#         index=0
#     )
    
#     color_theme = st.selectbox(
#         "Color Theme",
#         options=["Blues", "Greens", "Purples", "Oranges"],
#         index=0
#     )
    
#     st.markdown(animated_divider(), unsafe_allow_html=True)
#     st.markdown("### About")
#     st.markdown(f"""
#     This app helps you rank resumes based on job descriptions using NLP techniques.
    
#     <div class="animated-list">
#     <ul>
#         <li>{animated_icon("📄")} PDF resume analysis</li>
#         <li>{animated_icon("🔍")} TF-IDF vectorization</li>
#         <li>{animated_icon("📊")} Cosine similarity scoring</li>
#         <li>{animated_icon("🤖")} AI-powered improvement tips</li>
#     </ul>
#     </div>
#     """, unsafe_allow_html=True)

# # Main content
# st.markdown(animated_text("📊 Resume Ranking System", "title"), unsafe_allow_html=True)

# # Sample job description
# sample_job_description = """
# Job Title: Full Stack Developer

# Requirements:
# - 3+ years of experience in web development
# - Proficient in JavaScript, React, and Node.js
# - Experience with database design and management (SQL, MongoDB)
# - Knowledge of cloud services (AWS, Azure, or GCP)
# - Strong problem-solving skills and attention to detail
# - Bachelor's degree in Computer Science or related field

# Responsibilities:
# - Develop and maintain web applications
# - Collaborate with cross-functional teams
# - Implement responsive design and ensure cross-browser compatibility
# - Optimize applications for maximum speed and scalability
# - Stay up-to-date with emerging trends and technologies
# """

# # Function to extract text from PDF
# def extract_text_from_pdf(file):
#     try:
#         pdf = PdfReader(file)
#         text = "".join([page.extract_text() or "" for page in pdf.pages])
#         return text.strip()
#     except Exception as e:
#         st.error(f"Error extracting text from {file.name}: {str(e)}")
#         return ""

# # Function to rank resumes
# def rank_resumes(job_description, resumes):
#     documents = [job_description] + resumes
#     vectorizer = TfidfVectorizer(stop_words='english').fit_transform(documents)
#     vectors = vectorizer.toarray()
#     job_desc_vector = vectors[0]
#     resume_vectors = vectors[1:]
#     return cosine_similarity([job_desc_vector], resume_vectors).flatten()

# # Function to generate resume tips
# def generate_resume_tips(score, resume_text, job_description):
#     score_percentage = score * 100
    
#     # Extract keywords from job description
#     vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
#     vectorizer.fit_transform([job_description])
#     keywords = vectorizer.get_feature_names_out()
    
#     # Check which keywords are missing
#     missing_keywords = [keyword for keyword in keywords if keyword.lower() not in resume_text.lower()]
    
#     if score_percentage > 80:
#         tips = [
#             "Your resume is well-optimized for this position!",
#             "Consider adding more specific achievements with metrics",
#             "Tailor your professional summary even further"
#         ]
#     elif score_percentage > 60:
#         tips = [
#             "Add more relevant keywords to improve matching",
#             "Quantify your achievements with specific metrics",
#             "Highlight projects relevant to the job description"
#         ]
#     else:
#         tips = [
#             "Significantly revise your resume to match job requirements",
#             "Add relevant skills and experiences mentioned in the job description",
#             "Consider a skills-based format to highlight relevant capabilities"
#         ]
    
#     if missing_keywords:
#         tips.append(f"Consider adding these keywords: {', '.join(missing_keywords[:5])}")
    
#     return tips

# # Function to create a downloadable CSV file
# def to_csv(df):
#     output = BytesIO()
#     df.to_csv(output, index=False)
#     processed_data = output.getvalue()
#     return processed_data

# # Function to create download link
# def get_download_link(df, filename="resume_rankings.csv"):
#     val = to_csv(df)
#     b64 = base64.b64encode(val).decode()
#     return f'<a href="data:text/csv;base64,{b64}" download="{filename}" class="download-btn">Download CSV file</a>'

# # Function to create animated list
# def create_animated_list(items):
#     html = '<ul class="animated-list">'
#     for item in items:
#         html += f'<li>{item}</li>'
#     html += '</ul>'
#     return html

# # Main layout with animated tabs
# tab1, tab2 = st.tabs(["📤 Upload & Analyze", "📋 Instructions"])

# with tab1:
#     st.markdown('<div class="animated-bg">', unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 1])
    
#     with col1:
#         st.markdown('<div class="card animate-on-scroll">', unsafe_allow_html=True)
#         st.markdown('<div class="card-header">Upload Resumes</div>', unsafe_allow_html=True)
#         uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col2:
#         st.markdown('<div class="card animate-on-scroll">', unsafe_allow_html=True)
#         st.markdown('<div class="card-header">Job Description</div>', unsafe_allow_html=True)
#         job_description = st.text_area("Enter the job description...", height=200)
        
#         col_a, col_b = st.columns([1, 1])
#         with col_a:
#             if st.button("Load Sample Job Description"):
#                 # Use session state instead of experimental_rerun
#                 st.session_state.job_description = sample_job_description
#                 job_description = sample_job_description
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Analysis process
#     if uploaded_files and job_description:
#         st.markdown(animated_divider(), unsafe_allow_html=True)
#         st.markdown(animated_text("📈 Analysis Results", "typing"), unsafe_allow_html=True)
        
#         # Extract text from resumes
#         with st.spinner("Processing resumes..."):
#             progress_bar = st.progress(0)
#             resumes = []
#             resume_names = []
            
#             for i, file in enumerate(uploaded_files):
#                 resume_text = extract_text_from_pdf(file)
#                 if resume_text:
#                     resumes.append(resume_text)
#                     resume_names.append(file.name)
#                 progress_bar.progress((i + 1) / len(uploaded_files))
#                 time.sleep(0.1)
            
#             # Calculate scores
#             if resumes:
#                 scores = rank_resumes(job_description, resumes)
                
#                 # Create results dataframe
#                 results_df = pd.DataFrame({
#                     "Resume": resume_names,
#                     "Match Score (%)": (scores * 100).round(2)
#                 })
                
#                 # Add match category
#                 def get_match_category(score):
#                     if score >= 75:
#                         return "Excellent Match"
#                     elif score >= 60:
#                         return "Good Match"
#                     elif score >= 40:
#                         return "Fair Match"
#                     else:
#                         return "Poor Match"
                
#                 results_df["Match Category"] = results_df["Match Score (%)"].apply(get_match_category)
                
#                 # Sort by score
#                 results_df = results_df.sort_values(by="Match Score (%)", ascending=False)
                
#                 # Display metrics with animation
#                 st.markdown('<div style="display: flex; justify-content: space-between; margin-bottom: 20px;" class="animate-on-scroll">', unsafe_allow_html=True)
                
#                 metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                
#                 with metric_col1:
#                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{len(resumes)}</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">Resumes Analyzed</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with metric_col2:
#                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{results_df["Match Score (%)"].max():.1f}%</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">Top Match Score</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with metric_col3:
#                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{results_df["Match Score (%)"].mean():.1f}%</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">Average Score</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with metric_col4:
#                     good_matches = results_df[results_df["Match Score (%)"] >= min_match_threshold].shape[0]
#                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{good_matches}</div>', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-label">Matches Above {min_match_threshold}%</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Display top match with animation
#                 if not results_df.empty:
#                     top_match = results_df.iloc[0]
#                     st.markdown(f"""
#                     <div class="success-message animate-on-scroll">
#                         <h3>{animated_icon("🏆")} Top Match: {top_match['Resume']}</h3>
#                         <p>Match Score: <strong>{top_match['Match Score (%)']}%</strong> | Category: <strong>{top_match['Match Category']}</strong></p>
#                     </div>
#                     """, unsafe_allow_html=True)
                
#                 # Display visualization with animation
#                 st.markdown(animated_text("📊 Visual Comparison", "header"), unsafe_allow_html=True)
                
#                 fig = None
                
#                 if chart_type == "Bar Chart":
#                     fig = px.bar(
#                         results_df,
#                         x="Resume",
#                         y="Match Score (%)",
#                         color="Match Category",
#                         color_discrete_map={
#                             "Excellent Match": "#10b981",
#                             "Good Match": "#3b82f6",
#                             "Fair Match": "#f59e0b",
#                             "Poor Match": "#ef4444"
#                         },
#                         title="Resume Match Scores"
#                     )
#                     fig.add_hline(y=min_match_threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold ({min_match_threshold}%)")
#                     # Add animation to the chart
#                     fig.update_layout(
#                         updatemenus=[
#                             dict(
#                                 type="buttons",
#                                 showactive=False,
#                                 buttons=[
#                                     dict(
#                                         label="Play",
#                                         method="animate",
#                                         args=[None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]
#                                     )
#                                 ],
#                                 x=0.1,
#                                 y=1.1
#                             )
#                         ]
#                     )
                
#                 elif chart_type == "Horizontal Bar":
#                     fig = px.bar(
#                         results_df,
#                         y="Resume",
#                         x="Match Score (%)",
#                         color="Match Category",
#                         color_discrete_map={
#                             "Excellent Match": "#10b981",
#                             "Good Match": "#3b82f6",
#                             "Fair Match": "#f59e0b",
#                             "Poor Match": "#ef4444"
#                         },
#                         title="Resume Match Scores",
#                         orientation='h'
#                     )
#                     fig.add_vline(x=min_match_threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold ({min_match_threshold}%)")
#                     # Add animation to the chart
#                     fig.update_layout(
#                         updatemenus=[
#                             dict(
#                                 type="buttons",
#                                 showactive=False,
#                                 buttons=[
#                                     dict(
#                                         label="Play",
#                                         method="animate",
#                                         args=[None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]
#                                     )
#                                 ],
#                                 x=0.1,
#                                 y=1.1
#                             )
#                         ]
#                     )
                
#                 elif chart_type == "Radar Chart":
#                     # For radar chart, we need to prepare the data differently
#                     fig = go.Figure()
                    
#                     for i, row in results_df.iterrows():
#                         fig.add_trace(go.Scatterpolar(
#                             r=[row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"]],
#                             theta=["Relevance", "Skills", "Experience", "Education", "Relevance"],
#                             fill='toself',
#                             name=row["Resume"]
#                         ))
                    
#                     fig.update_layout(
#                         polar=dict(
#                             radialaxis=dict(
#                                 visible=True,
#                                 range=[0, 100]
#                             )
#                         ),
#                         title="Resume Match Radar"
#                     )
                
#                 if fig:
#                     fig.update_layout(
#                         height=500,
#                         margin=dict(l=20, r=20, t=40, b=20),
#                         paper_bgcolor="white",
#                         plot_bgcolor="white",
#                         font=dict(color="#1f2937"),
#                         # Add hover effects
#                         hovermode="closest",
#                         hoverlabel=dict(
#                             bgcolor="white",
#                             font_size=12,
#                             font_family="Arial"
#                         )
#                     )
#                     # Add a unique key to the plotly_chart
#                     st.plotly_chart(fig, use_container_width=True, key="main_chart")
                
#                 # Display results table with animation
#                 st.markdown(animated_text("📋 Detailed Results", "header"), unsafe_allow_html=True)
                
#                 st.markdown('<div class="dataframe-container animate-on-scroll">', unsafe_allow_html=True)
#                 st.dataframe(
#                     results_df.style.format({"Match Score (%)": "{:.2f}"})
#                     .background_gradient(cmap=color_theme, subset=["Match Score (%)"])
#                     .set_properties(**{'text-align': 'left'})
#                     .set_table_styles([
#                         {'selector': 'th', 'props': [('background-color', '#f1f5f9'), ('color', '#1f2937'), ('font-weight', 'bold')]},
#                         {'selector': 'tr:hover', 'props': [('background-color', '#f1f5f9')]},
#                     ]),
#                     use_container_width=True
#                 )
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Download button with animation
#                 st.markdown(get_download_link(results_df), unsafe_allow_html=True)
                
#                 # Detailed analysis for each resume with animations
#                 st.markdown(animated_text("🔍 Individual Resume Analysis", "header"), unsafe_allow_html=True)
                
#                 for i, (_, row) in enumerate(results_df.iterrows()):
#                     resume_name = row["Resume"]
#                     score = row["Match Score (%)"] / 100
                    
#                     with st.expander(f"{resume_name} - {row['Match Score (%)']}% ({row['Match Category']})"):
#                         col1, col2 = st.columns([2, 1])
                        
#                         with col1:
#                             st.markdown(animated_text("Improvement Tips", "header"), unsafe_allow_html=True)
#                             tips = generate_resume_tips(score, resumes[resume_names.index(resume_name)], job_description)
                            
#                             # Create animated list of tips
#                             st.markdown(create_animated_list(tips), unsafe_allow_html=True)
                        
#                         with col2:
#                             # Create an animated gauge chart for the score
#                             gauge_fig = go.Figure(go.Indicator(
#                                 mode="gauge+number",
#                                 value=row["Match Score (%)"],
#                                 domain={'x': [0, 1], 'y': [0, 1]},
#                                 title={'text': "Match Score"},
#                                 gauge={
#                                     'axis': {'range': [0, 100]},
#                                     'bar': {'color': "#3b82f6"},
#                                     'steps': [
#                                         {'range': [0, 40], 'color': "#fee2e2"},
#                                         {'range': [40, 60], 'color': "#fef3c7"},
#                                         {'range': [60, 75], 'color': "#dbeafe"},
#                                         {'range': [75, 100], 'color': "#d1fae5"}
#                                     ],
#                                     'threshold': {
#                                         'line': {'color': "red", 'width': 4},
#                                         'thickness': 0.75,
#                                         'value': min_match_threshold
#                                     }
#                                 }
#                             ))
                            
#                             # Add animation to the gauge
#                             gauge_fig.update_layout(
#                                 height=250,
#                                 margin=dict(l=20, r=20, t=30, b=20),
#                                 paper_bgcolor="white",
#                                 font=dict(color="#1f2937"),
#                                 # Add transition animation
#                                 updatemenus=[
#                                     dict(
#                                         type="buttons",
#                                         showactive=False,
#                                         buttons=[
#                                             dict(
#                                                 label="Animate",
#                                                 method="animate",
#                                                 args=[None, {"frame": {"duration": 1000, "redraw": True}, "fromcurrent": True}]
#                                             )
#                                         ],
#                                         x=0.1,
#                                         y=1.1,
#                                         visible=False
#                                     )
#                                 ]
#                             )
                            
#                             # Add a unique key to each gauge chart
#                             st.plotly_chart(gauge_fig, use_container_width=True, key=f"gauge_chart_{i}")
    
#     st.markdown('</div>', unsafe_allow_html=True)  # Close animated-bg div

# with tab2:
#     st.markdown('<div class="animated-bg">', unsafe_allow_html=True)
#     st.markdown(animated_text("📋 How to Use This App", "typing"), unsafe_allow_html=True)
    
#     st.markdown("""
#     This Resume Ranking System helps you find the best candidates for a job position by analyzing resumes against a job description.
#     """)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown(f"""
#         <div class="card animate-on-scroll">
#             <h3>{animated_icon("1️⃣")} Step 1: Upload Resumes</h3>
#             <ul class="animated-list">
#                 <li>Click on the "Upload Resumes" area to select PDF files</li>
#                 <li>You can upload multiple resumes at once</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown(f"""
#         <div class="card animate-on-scroll">
#             <h3>{animated_icon("3️⃣")} Step 3: Analyze Results</h3>
#             <ul class="animated-list">
#                 <li>The system will process the resumes and rank them based on relevance</li>
#                 <li>Review the visual comparison and detailed results</li>
#                 <li>Check individual resume analysis for improvement tips</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown(f"""
#         <div class="card animate-on-scroll">
#             <h3>{animated_icon("2️⃣")} Step 2: Enter Job Description</h3>
#             <ul class="animated-list">
#                 <li>Enter the complete job description in the text area</li>
#                 <li>Include all requirements, responsibilities, and qualifications</li>
#                 <li>Use the "Load Sample" button for a quick test</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown(f"""
#         <div class="card animate-on-scroll">
#             <h3>{animated_icon("4️⃣")} Step 4: Export Results</h3>
#             <ul class="animated-list">
#                 <li>Download the results as a CSV file for further analysis</li>
#                 <li>Share the insights with your hiring team</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown(animated_divider(), unsafe_allow_html=True)
#     st.markdown(animated_text("How It Works", "header"), unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="animate-on-scroll">
#     This app uses Natural Language Processing (NLP) techniques:
    
#     <div class="card" style="margin-top: 1rem;">
#         <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
#             <div style="background-color: #3b82f6; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">1</div>
#             <strong>Text Extraction</strong>
#         </div>
#         <p>Extracts text from PDF resumes using PyPDF2 library</p>
#     </div>
    
#     <div class="card">
#         <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
#             <div style="background-color: #3b82f6; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">2</div>
#             <strong>TF-IDF Vectorization</strong>
#         </div>
#         <p>Converts text into numerical vectors that represent the importance of words</p>
#     </div>
    
#     <div class="card">
#         <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
#             <div style="background-color: #3b82f6; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">3</div>
#             <strong>Cosine Similarity</strong>
#         </div>
#         <p>Measures similarity between job description and resumes vectors</p>
#     </div>
    
#     <div class="card">
#         <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
#             <div style="background-color: #3b82f6; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">4</div>
#             <strong>AI Analysis</strong>
#         </div>
#         <p>Generates improvement tips based on matching scores and missing keywords</p>
#     </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown(animated_divider(), unsafe_allow_html=True)
#     st.markdown(animated_text("Tips for Best Results", "header"), unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="card animate-on-scroll">
#         <ul class="animated-list">
#             <li>Use detailed job descriptions with specific requirements</li>
#             <li>Ensure PDFs are properly formatted and text-extractable</li>
#             <li>Upload resumes in similar formats for consistent analysis</li>
#             <li>Adjust the minimum match threshold based on your hiring needs</li>
#             <li>Consider the keyword importance setting for technical positions</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown('</div>', unsafe_allow_html=True)  # Close animated-bg div

# # Footer with animation
# st.markdown(animated_divider(), unsafe_allow_html=True)
# st.markdown(f"""
# <div style="text-align: center; color: #6b7280; font-size: 0.8rem;" class="animate-on-scroll">
#     <p>© 2023 Resume Ranking System | Built with Streamlit</p>
#     <p style="margin-top: 0.5rem;">Made with {animated_icon("❤️")} by AI-Powered Resume Analysis Team</p>
# </div>
# """, unsafe_allow_html=True)

# # Add confetti effect when analysis is complete
# if 'resumes' in locals() and len(resumes) > 0:
#     st.balloons()

    import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader
import plotly.express as px
import plotly.graph_objects as go
import base64
from io import BytesIO
import requests
import json
import random

# Page configuration
st.set_page_config(
    page_title="Resume Ranking System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for elegant UI with enhanced animations and responsiveness
st.markdown("""
<style>
    /* Main theme colors - Updated with a more cohesive palette */
    :root {
        --primary-color: #4f46e5;
        --primary-light: #818cf8;
        --primary-dark: #3730a3;
        --secondary-color: #f3f4f6;
        --text-color: #1f2937;
        --success-color: #10b981;
        --warning-color: #f59e0b;
        --danger-color: #ef4444;
        --background-color: #f8fafc;
        --card-background: #ffffff;
    }
    
    /* Base styling with improved responsiveness */
    .main {
        background-color: var(--background-color);
        color: var(--text-color);
        max-width: 100% !important;
    }
    
    h1, h2, h3 {
        color: var(--primary-dark);
    }
    
    /* Responsive containers */
    .container {
        width: 100%;
        padding-right: 15px;
        padding-left: 15px;
        margin-right: auto;
        margin-left: auto;
    }
    
    @media (min-width: 576px) {
        .container {
            max-width: 540px;
        }
    }
    
    @media (min-width: 768px) {
        .container {
            max-width: 720px;
        }
    }
    
    @media (min-width: 992px) {
        .container {
            max-width: 960px;
        }
    }
    
    @media (min-width: 1200px) {
        .container {
            max-width: 1140px;
        }
    }
    
    /* Title animation with improved performance */
    .title-animation {
        display: inline-block;
        background: linear-gradient(45deg, var(--primary-color), var(--primary-dark));
        background-size: 200% 200%;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        animation: gradient-shift 3s ease infinite;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        will-change: transform, box-shadow;
    }
    
    .title-animation:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.4);
    }
    
    @keyframes gradient-shift {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    
    /* Card styling with improved animations and responsiveness */
    .card {
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        padding: 1.5rem;
        margin-bottom: 1rem;
        background-color: var(--card-background);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        position: relative;
        overflow: hidden;
        width: 100%;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
    }
    
    .card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-light), var(--primary-dark));
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.5s ease;
    }
    
    .card:hover::after {
        transform: scaleX(1);
    }
    
    .card-header {
        border-bottom: 1px solid #e5e7eb;
        padding-bottom: 0.75rem;
        margin-bottom: 1rem;
        font-weight: 600;
        font-size: 1.25rem;
        color: var(--primary-dark);
        position: relative;
        display: inline-block;
    }
    
    .card-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, var(--primary-color), transparent);
    }
    
    /* Button styling with improved animations */
    .stButton > button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        z-index: 1;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.7s ease;
        z-index: -1;
    }
    
    .stButton > button:hover {
        background-color: var(--primary-dark);
        box-shadow: 0 4px 10px rgba(55, 48, 163, 0.3);
        transform: translateY(-2px);
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    /* File uploader styling with improved animations */
    .stFileUploader > div > div {
        border: 2px dashed var(--primary-light);
        border-radius: 10px;
        padding: 2rem;
        background-color: #f8fafc;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div > div:hover {
        border-color: var(--primary-color);
        background-color: rgba(129, 140, 248, 0.1);
        transform: scale(1.01);
    }
    
    /* Text area styling with improved focus states */
    .stTextArea > div > div > textarea {
        border-radius: 6px;
        border-color: #e5e7eb;
        transition: all 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.2);
    }
    
    /* Metrics styling with improved animations */
    .metric-card {
        background-color: white;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        border-left: 4px solid var(--primary-color);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        height: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent, rgba(129, 140, 248, 0.1), transparent);
        transform: translateX(-100%);
        transition: transform 0.6s ease;
    }
    
    .metric-card:hover::before {
        transform: translateX(100%);
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--primary-dark);
        display: inline-block;
        animation: count-up 2s ease-out;
    }
    
    @keyframes count-up {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #6b7280;
        position: relative;
        display: inline-block;
    }
    
    .metric-label::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 0;
        height: 1px;
        background-color: var(--primary-color);
        transition: width 0.3s ease;
    }
    
    .metric-card:hover .metric-label::after {
        width: 100%;
    }
    
    /* Progress bar animation with improved performance */
    @keyframes pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(79, 70, 229, 0.7);
        }
        70% {
            box-shadow: 0 0 0 10px rgba(79, 70, 229, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(79, 70, 229, 0);
        }
    }
    
    .stProgress > div > div > div {
        background-color: var(--primary-color);
        animation: pulse 2s infinite, progress-fill 1.5s ease-out;
        will-change: width, opacity;
    }
    
    @keyframes progress-fill {
        from {
            width: 0%;
        }
    }
    
    /* Dataframe styling with improved responsiveness */
    .dataframe-container {
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        width: 100%;
        overflow-x: auto;
    }
    
    .dataframe-container:hover {
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Expander styling with improved animations */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: var(--primary-dark);
        transition: all 0.3s ease;
        border-radius: 4px;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: rgba(129, 140, 248, 0.1);
        padding-left: 5px;
    }
    
    /* Success message styling with improved animations */
    .success-message {
        background-color: #ecfdf5;
        border-left: 4px solid var(--success-color);
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
        transition: all 0.3s ease;
        animation: slide-in 0.5s ease-out;
    }
    
    @keyframes slide-in {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .success-message:hover {
        box-shadow: 0 5px 15px rgba(16, 185, 129, 0.2);
        transform: translateY(-2px);
    }
    
    /* Sidebar styling with improved colors */
    .css-1d391kg, [data-testid="stSidebar"] {
        background-color: #f1f5f9;
    }
    
    /* Animated icons with improved performance */
    .animated-icon {
        display: inline-block;
        animation: float 3s ease-in-out infinite;
        will-change: transform;
    }
    
    @keyframes float {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0px);
        }
    }
    
    /* Animated list items with improved staggered animation */
    .animated-list li {
        opacity: 0;
        animation: fade-in 0.5s ease forwards;
        will-change: opacity, transform;
    }
    
    @keyframes fade-in {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Staggered animation for list items */
    .animated-list li:nth-child(1) { animation-delay: 0.1s; }
    .animated-list li:nth-child(2) { animation-delay: 0.2s; }
    .animated-list li:nth-child(3) { animation-delay: 0.3s; }
    .animated-list li:nth-child(4) { animation-delay: 0.4s; }
    .animated-list li:nth-child(5) { animation-delay: 0.5s; }
    .animated-list li:nth-child(6) { animation-delay: 0.6s; }
    .animated-list li:nth-child(7) { animation-delay: 0.7s; }
    .animated-list li:nth-child(8) { animation-delay: 0.8s; }
    
    /* Animated section headers with improved hover effect */
    .animated-header {
        position: relative;
        display: inline-block;
        padding-bottom: 5px;
    }
    
    .animated-header::after {
        content: '';
        position: absolute;
        width: 100%;
        transform: scaleX(0);
        height: 2px;
        bottom: 0;
        left: 0;
        background-color: var(--primary-color);
        transform-origin: bottom right;
        transition: transform 0.3s ease-out;
    }
    
    .animated-header:hover::after {
        transform: scaleX(1);
        transform-origin: bottom left;
    }
    
    /* Animated download button with improved hover effect */
    .download-btn {
        display: inline-block;
        padding: 8px 16px;
        background-color: var(--primary-color);
        color: white;
        border-radius: 4px;
        text-decoration: none;
        transition: all 0.3s ease;
        margin-top: 10px;
        font-weight: 500;
    }
    
    .download-btn:hover {
        background-color: var(--primary-dark);
        box-shadow: 0 4px 10px rgba(55, 48, 163, 0.3);
        transform: translateY(-2px);
    }
    
    /* Animated tabs with improved active state */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        transition: all 0.3s ease;
        border-radius: 4px 4px 0 0;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(129, 140, 248, 0.1);
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-light) !important;
        color: var(--primary-dark) !important;
    }
    
    /* Animated dividers with improved visual effect */
    .animated-divider {
        height: 3px;
        background: linear-gradient(90deg, transparent, var(--primary-color), transparent);
        margin: 20px 0;
        animation: pulse-width 4s infinite;
        will-change: opacity;
    }
    
    @keyframes pulse-width {
        0% {
            opacity: 0.6;
        }
        50% {
            opacity: 1;
        }
        100% {
            opacity: 0.6;
        }
    }
    
    /* Typing animation for headers with improved performance */
    .typing-animation {
        border-right: 2px solid var(--primary-color);
        white-space: nowrap;
        overflow: hidden;
        animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
        will-change: width, border-color;
    }
    
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: var(--primary-color) }
    }
    
    /* Animated background for sections with improved performance */
    .animated-bg {
        position: relative;
        overflow: hidden;
    }
    
    .animated-bg::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(129, 140, 248, 0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
        z-index: -1;
        will-change: transform;
    }
    
    @keyframes rotate {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
    
    /* Animated tooltip with improved visibility */
    .tooltip {
        position: relative;
        display: inline-block;
    }
    
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 120px;
        background-color: var(--primary-dark);
        color: white;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -60px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .tooltip .tooltiptext::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: var(--primary-dark) transparent transparent transparent;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    
    /* Responsive grid system */
    .row {
        display: flex;
        flex-wrap: wrap;
        margin-right: -15px;
        margin-left: -15px;
    }
    
    .col {
        position: relative;
        width: 100%;
        padding-right: 15px;
        padding-left: 15px;
    }
    
    /* Responsive columns */
    @media (min-width: 576px) {
        .col-sm-6 {
            flex: 0 0 50%;
            max-width: 50%;
        }
        .col-sm-12 {
            flex: 0 0 100%;
            max-width: 100%;
        }
    }
    
    @media (min-width: 768px) {
        .col-md-3 {
            flex: 0 0 25%;
            max-width: 25%;
        }
        .col-md-4 {
            flex: 0 0 33.333333%;
            max-width: 33.333333%;
        }
        .col-md-6 {
            flex: 0 0 50%;
            max-width: 50%;
        }
        .col-md-8 {
            flex: 0 0 66.666667%;
            max-width: 66.666667%;
        }
        .col-md-12 {
            flex: 0 0 100%;
            max-width: 100%;
        }
    }
    
    @media (min-width: 992px) {
        .col-lg-3 {
            flex: 0 0 25%;
            max-width: 25%;
        }
        .col-lg-4 {
            flex: 0 0 33.333333%;
            max-width: 33.333333%;
        }
        .col-lg-6 {
            flex: 0 0 50%;
            max-width: 50%;
        }
        .col-lg-8 {
            flex: 0 0 66.666667%;
            max-width: 66.666667%;
        }
    }
    
    /* Mobile optimizations */
    @media (max-width: 768px) {
        .title-animation {
            font-size: 1.5rem;
            padding: 0.4rem 0.8rem;
        }
        
        .card {
            padding: 1rem;
        }
        
        .metric-value {
            font-size: 1.2rem;
        }
        
        .metric-label {
            font-size: 0.75rem;
        }
        
        .stButton > button {
            width: 100%;
        }
    }
    
    /* Improved animation for elements when they come into view */
    .animate-on-scroll {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
        will-change: opacity, transform;
    }
    
    .animate-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    /* Ripple effect for buttons */
    @keyframes ripple {
        to {
            transform: scale(100);
            opacity: 0;
        }
    }
</style>

<script>
    // Function to add ripple effect to buttons
    document.addEventListener('DOMContentLoaded', function() {
        const buttons = document.querySelectorAll('button');
        
        buttons.forEach(button => {
            button.addEventListener('click', function(e) {
                const x = e.clientX - e.target.getBoundingClientRect().left;
                const y = e.clientY - e.target.getBoundingClientRect().top;
                
                const ripple = document.createElement('span');
                ripple.style.position = 'absolute';
                ripple.style.width = '1px';
                ripple.style.height = '1px';
                ripple.style.borderRadius = '50%';
                ripple.style.backgroundColor = 'rgba(255, 255, 255, 0.7)';
                ripple.style.transform = 'scale(0)';
                ripple.style.animation = 'ripple 0.6s linear';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                
                this.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            });
        });
    });
    
    // Animation for elements when they come into view
    document.addEventListener('DOMContentLoaded', function() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.animate-on-scroll').forEach(element => {
            observer.observe(element);
        });
    });
</script>
""", unsafe_allow_html=True)

# Function to create animated text
def animated_text(text, animation_type="title"):
    if animation_type == "title":
        return f'<h1 class="title-animation">{text}</h1>'
    elif animation_type == "typing":
        return f'<h2 class="typing-animation" style="display:inline-block; max-width:100%;">{text}</h2>'
    elif animation_type == "header":
        return f'<h3 class="animated-header">{text}</h3>'
    return text

# Function to create animated divider
def animated_divider():
    return '<div class="animated-divider"></div>'

# Function to create animated icon
def animated_icon(emoji):
    return f'<span class="animated-icon">{emoji}</span>'

# Function to create responsive row
def responsive_row():
    return '<div class="row">'

# Function to close responsive row
def close_responsive_row():
    return '</div>'

# Function to create responsive column
def responsive_column(lg=None, md=None, sm=None):
    classes = []
    if lg:
        classes.append(f"col-lg-{lg}")
    if md:
        classes.append(f"col-md-{md}")
    if sm:
        classes.append(f"col-sm-{sm}")
    if not classes:
        classes.append("col")
    
    return f'<div class="{" ".join(classes)}">'

# Function to close responsive column
def close_responsive_column():
    return '</div>'

# Sample job description
sample_job_description = """
Job Title: Full Stack Developer

Requirements:
- 3+ years of experience in web development
- Proficient in JavaScript, React, and Node.js
- Experience with database design and management (SQL, MongoDB)
- Knowledge of cloud services (AWS, Azure, or GCP)
- Strong problem-solving skills and attention to detail
- Bachelor's degree in Computer Science or related field

Responsibilities:
- Develop and maintain web applications
- Collaborate with cross-functional teams
- Implement responsive design and ensure cross-browser compatibility
- Optimize applications for maximum speed and scalability
- Stay up-to-date with emerging trends and technologies
"""

# Function to extract text from PDF
def extract_text_from_pdf(file):
    try:
        pdf = PdfReader(file)
        text = "".join([page.extract_text() or "" for page in pdf.pages])
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text from {file.name}: {str(e)}")
        return ""

# Function to rank resumes
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer(stop_words='english').fit_transform(documents)
    vectors = vectorizer.toarray()
    job_desc_vector = vectors[0]
    resume_vectors = vectors[1:]
    return cosine_similarity([job_desc_vector], resume_vectors).flatten()

# Function to generate resume tips
def generate_resume_tips(score, resume_text, job_description):
    score_percentage = score * 100
    
    # Extract keywords from job description
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    vectorizer.fit_transform([job_description])
    keywords = vectorizer.get_feature_names_out()
    
    # Check which keywords are missing
    missing_keywords = [keyword for keyword in keywords if keyword.lower() not in resume_text.lower()]
    
    if score_percentage > 80:
        tips = [
            "Your resume is well-optimized for this position!",
            "Consider adding more specific achievements with metrics",
            "Tailor your professional summary even further"
        ]
    elif score_percentage > 60:
        tips = [
            "Add more relevant keywords to improve matching",
            "Quantify your achievements with specific metrics",
            "Highlight projects relevant to the job description"
        ]
    else:
        tips = [
            "Significantly revise your resume to match job requirements",
            "Add relevant skills and experiences mentioned in the job description",
            "Consider a skills-based format to highlight relevant capabilities"
        ]
    
    if missing_keywords:
        tips.append(f"Consider adding these keywords: {', '.join(missing_keywords[:5])}")
    
    return tips

# Function to create a downloadable CSV file
def to_csv(df):
    output = BytesIO()
    df.to_csv(output, index=False)
    processed_data = output.getvalue()
    return processed_data

# Function to create download link
def get_download_link(df, filename="resume_rankings.csv"):
    val = to_csv(df)
    b64 = base64.b64encode(val).decode()
    return f'<a href="data:text/csv;base64,{b64}" download="{filename}" class="download-btn">Download CSV file</a>'

# Function to create animated list
def create_animated_list(items):
    html = '<ul class="animated-list">'
    for item in items:
        html += f'<li>{item}</li>'
    html += '</ul>'
    return html

# Function to create card - FIXED THE SYNTAX ERROR HERE
def create_card(title=None, content=None, classes=""):
    html = f'<div class="card {classes} animate-on-scroll">'
    if title:
        html += f'<div class="card-header">{title}</div>'
    if content:
        html += content 
        html += f'<div class="card-header">{title}</div>'
    if content:
        html += content
    html += '</div>'
    return html

# Sidebar
with st.sidebar:
    st.markdown(animated_text("⚙️ Settings", "title"), unsafe_allow_html=True)
    
    st.markdown("### Analysis Options")
    
    min_match_threshold = st.slider(
        "Minimum Match Threshold (%)", 
        min_value=0, 
        max_value=100, 
        value=50,
        help="Resumes below this threshold will be marked as poor matches"
    )
    
    keyword_weight = st.slider(
        "Keyword Importance", 
        min_value=1, 
        max_value=10, 
        value=5,
        help="How much to weight exact keyword matches"
    )
    
    st.markdown(animated_divider(), unsafe_allow_html=True)
    st.markdown("### Visualization Settings")
    
    chart_type = st.selectbox(
        "Chart Type",
        options=["Bar Chart", "Horizontal Bar", "Radar Chart"],
        index=0
    )
    
    color_theme = st.selectbox(
        "Color Theme",
        options=["Blues", "Purples", "Greens", "Oranges"],
        index=0
    )
    
    st.markdown(animated_divider(), unsafe_allow_html=True)
    st.markdown("### About")
    st.markdown(f"""
    This app helps you rank resumes based on job descriptions using NLP techniques.
    
    <div class="animated-list">
    <ul>
        <li>{animated_icon("📄")} PDF resume analysis</li>
        <li>{animated_icon("🔍")} TF-IDF vectorization</li>
        <li>{animated_icon("📊")} Cosine similarity scoring</li>
        <li>{animated_icon("🤖")} AI-powered improvement tips</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown(animated_text("📊 Resume Ranking System", "title"), unsafe_allow_html=True)

# Main layout with animated tabs
tab1, tab2 = st.tabs(["📤 Upload & Analyze", "📋 Instructions"])

with tab1:
    st.markdown('<div class="animated-bg">', unsafe_allow_html=True)
    
    # Use responsive row and columns
    st.markdown(responsive_row(), unsafe_allow_html=True)
    st.markdown(responsive_column(lg=6, md=6, sm=12), unsafe_allow_html=True)
    
    st.markdown(create_card(title="Upload Resumes"), unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)
    
    st.markdown(close_responsive_column(), unsafe_allow_html=True)
    st.markdown(responsive_column(lg=6, md=6, sm=12), unsafe_allow_html=True)
    
    st.markdown(create_card(title="Job Description"), unsafe_allow_html=True)
    job_description = st.text_area("Enter the job description...", height=200)
    
    if st.button("Load Sample Job Description"):
        # Use session state instead of experimental_rerun
        st.session_state.job_description = sample_job_description
        job_description = sample_job_description
    
    st.markdown(close_responsive_column(), unsafe_allow_html=True)
    st.markdown(close_responsive_row(), unsafe_allow_html=True)
    
    # Analysis process
    if uploaded_files and job_description:
        st.markdown(animated_divider(), unsafe_allow_html=True)
        st.markdown(animated_text("📈 Analysis Results", "typing"), unsafe_allow_html=True)
        
        # Extract text from resumes
        with st.spinner("Processing resumes..."):
            progress_bar = st.progress(0)
            resumes = []
            resume_names = []
            
            for i, file in enumerate(uploaded_files):
                resume_text = extract_text_from_pdf(file)
                if resume_text:
                    resumes.append(resume_text)
                    resume_names.append(file.name)
                progress_bar.progress((i + 1) / len(uploaded_files))
                time.sleep(0.1)
            
            # Calculate scores
            if resumes:
                scores = rank_resumes(job_description, resumes)
                
                # Create results dataframe
                results_df = pd.DataFrame({
                    "Resume": resume_names,
                    "Match Score (%)": (scores * 100).round(2)
                })
                
                # Add match category
                def get_match_category(score):
                    if score >= 75:
                        return "Excellent Match"
                    elif score >= 60:
                        return "Good Match"
                    elif score >= 40:
                        return "Fair Match"
                    else:
                        return "Poor Match"
                
                results_df["Match Category"] = results_df["Match Score (%)"].apply(get_match_category)
                
                # Sort by score
                results_df = results_df.sort_values(by="Match Score (%)", ascending=False)
                
                # Display metrics with animation and responsive layout
                st.markdown(responsive_row(), unsafe_allow_html=True)
                
                # First metric
                st.markdown(responsive_column(lg=3, md=6, sm=6), unsafe_allow_html=True)
                st.markdown('<div class="metric-card animate-on-scroll">', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-value">{len(resumes)}</div>', unsafe_allow_html=True)
                st.markdown('<div class="metric-label">Resumes Analyzed</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown(close_responsive_column(), unsafe_allow_html=True)
                
                # Second metric
                st.markdown(responsive_column(lg=3, md=6, sm=6), unsafe_allow_html=True)
                st.markdown('<div class="metric-card animate-on-scroll">', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-value">{results_df["Match Score (%)"].max():.1f}%</div>', unsafe_allow_html=True)
                st.markdown('<div class="metric-label">Top Match Score</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown(close_responsive_column(), unsafe_allow_html=True)
                
                # Third metric
                st.markdown(responsive_column(lg=3, md=6, sm=6), unsafe_allow_html=True)
                st.markdown('<div class="metric-card animate-on-scroll">', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-value">{results_df["Match Score (%)"].mean():.1f}%</div>', unsafe_allow_html=True)
                st.markdown('<div class="metric-label">Average Score</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown(close_responsive_column(), unsafe_allow_html=True)
                
                # Fourth metric
                st.markdown(responsive_column(lg=3, md=6, sm=6), unsafe_allow_html=True)
                good_matches = results_df[results_df["Match Score (%)"] >= min_match_threshold].shape[0]
                st.markdown('<div class="metric-card animate-on-scroll">', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-value">{good_matches}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-label">Matches Above {min_match_threshold}%</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown(close_responsive_column(), unsafe_allow_html=True)
                
                st.markdown(close_responsive_row(), unsafe_allow_html=True)
                
                # Display top match with animation
                if not results_df.empty:
                    top_match = results_df.iloc[0]
                    st.markdown(f"""
                    <div class="success-message animate-on-scroll">
                        <h3>{animated_icon("🏆")} Top Match: {top_match['Resume']}</h3>
                        <p>Match Score: <strong>{top_match['Match Score (%)']}%</strong> | Category: <strong>{top_match['Match Category']}</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Display visualization with animation
                st.markdown(animated_text("📊 Visual Comparison", "header"), unsafe_allow_html=True)
                
                fig = None
                
                if chart_type == "Bar Chart":
                    fig = px.bar(
                        results_df,
                        x="Resume",
                        y="Match Score (%)",
                        color="Match Category",
                        color_discrete_map={
                            "Excellent Match": "#10b981",
                            "Good Match": "#4f46e5",
                            "Fair Match": "#f59e0b",
                            "Poor Match": "#ef4444"
                        },
                        title="Resume Match Scores"
                    )
                    fig.add_hline(y=min_match_threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold ({min_match_threshold}%)")
                    # Add animation to the chart
                    fig.update_layout(
                        updatemenus=[
                            dict(
                                type="buttons",
                                showactive=False,
                                buttons=[
                                    dict(
                                        label="Play",
                                        method="animate",
                                        args=[None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]
                                    )
                                ],
                                x=0.1,
                                y=1.1
                            )
                        ]
                    )
                
                elif chart_type == "Horizontal Bar":
                    fig = px.bar(
                        results_df,
                        y="Resume",
                        x="Match Score (%)",
                        color="Match Category",
                        color_discrete_map={
                            "Excellent Match": "#10b981",
                            "Good Match": "#4f46e5",
                            "Fair Match": "#f59e0b",
                            "Poor Match": "#ef4444"
                        },
                        title="Resume Match Scores",
                        orientation='h'
                    )
                    fig.add_vline(x=min_match_threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold ({min_match_threshold}%)")
                    # Add animation to the chart
                    fig.update_layout(
                        updatemenus=[
                            dict(
                                type="buttons",
                                showactive=False,
                                buttons=[
                                    dict(
                                        label="Play",
                                        method="animate",
                                        args=[None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]
                                    )
                                ],
                                x=0.1,
                                y=1.1
                            )
                        ]
                    )
                
                elif chart_type == "Radar Chart":
                    # For radar chart, we need to prepare the data differently
                    fig = go.Figure()
                    
                    for i, row in results_df.iterrows():
                        fig.add_trace(go.Scatterpolar(
                            r=[row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"], row["Match Score (%)"]],
                            theta=["Relevance", "Skills", "Experience", "Education", "Relevance"],
                            fill='toself',
                            name=row["Resume"]
                        ))
                    
                    fig.update_layout(
                        polar=dict(
                            radialaxis=dict(
                                visible=True,
                                range=[0, 100]
                            )
                        ),
                        title="Resume Match Radar"
                    )
                
                if fig:
                    fig.update_layout(
                        height=500,
                        margin=dict(l=20, r=20, t=40, b=20),
                        paper_bgcolor="white",
                        plot_bgcolor="white",
                        font=dict(color="#1f2937"),
                        # Add hover effects
                        hovermode="closest",
                        hoverlabel=dict(
                            bgcolor="white",
                            font_size=12,
                            font_family="Arial"
                        )
                    )
                    # Add a unique key to the plotly_chart
                    st.plotly_chart(fig, use_container_width=True, key="main_chart")
                
                # Display results table with animation
                st.markdown(animated_text("📋 Detailed Results", "header"), unsafe_allow_html=True)
                
                st.markdown('<div class="dataframe-container animate-on-scroll">', unsafe_allow_html=True)
                st.dataframe(
                    results_df.style.format({"Match Score (%)": "{:.2f}"})
                    .background_gradient(cmap=color_theme, subset=["Match Score (%)"])
                    .set_properties(**{'text-align': 'left'})
                    .set_table_styles([
                        {'selector': 'th', 'props': [('background-color', '#f1f5f9'), ('color', '#1f2937'), ('font-weight', 'bold')]},
                        {'selector': 'tr:hover', 'props': [('background-color', '#f1f5f9')]},
                    ]),
                    use_container_width=True
                )
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Download button with animation
                st.markdown(get_download_link(results_df), unsafe_allow_html=True)
                
                # Detailed analysis for each resume with animations
                st.markdown(animated_text("🔍 Individual Resume Analysis", "header"), unsafe_allow_html=True)
                
                for i, (_, row) in enumerate(results_df.iterrows()):
                    resume_name = row["Resume"]
                    score = row["Match Score (%)"] / 100
                    
                    with st.expander(f"{resume_name} - {row['Match Score (%)']}% ({row['Match Category']})"):
                        st.markdown(responsive_row(), unsafe_allow_html=True)
                        
                        st.markdown(responsive_column(lg=8, md=8, sm=12), unsafe_allow_html=True)
                        st.markdown(animated_text("Improvement Tips", "header"), unsafe_allow_html=True)
                        tips = generate_resume_tips(score, resumes[resume_names.index(resume_name)], job_description)
                        
                        # Create animated list of tips
                        st.markdown(create_animated_list(tips), unsafe_allow_html=True)
                        st.markdown(close_responsive_column(), unsafe_allow_html=True)
                        
                        st.markdown(responsive_column(lg=4, md=4, sm=12), unsafe_allow_html=True)
                        # Create an animated gauge chart for the score
                        gauge_fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=row["Match Score (%)"],
                            domain={'x': [0, 1], 'y': [0, 1]},
                            title={'text': "Match Score"},
                            gauge={
                                'axis': {'range': [0, 100]},
                                'bar': {'color': "#4f46e5"},
                                'steps': [
                                    {'range': [0, 40], 'color': "#fee2e2"},
                                    {'range': [40, 60], 'color': "#fef3c7"},
                                    {'range': [60, 75], 'color': "#dbeafe"},
                                    {'range': [75, 100], 'color': "#d1fae5"}
                                ],
                                'threshold': {
                                    'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75,
                                    'value': min_match_threshold
                                }
                            }
                        ))
                        
                        # Add animation to the gauge
                        gauge_fig.update_layout(
                            height=250,
                            margin=dict(l=20, r=20, t=30, b=20),
                            paper_bgcolor="white",
                            font=dict(color="#1f2937"),
                            # Add transition animation
                            updatemenus=[
                                dict(
                                    type="buttons",
                                    showactive=False,
                                    buttons=[
                                        dict(
                                            label="Animate",
                                            method="animate",
                                            args=[None, {"frame": {"duration": 1000, "redraw": True}, "fromcurrent": True}]
                                        )
                                    ],
                                    x=0.1,
                                    y=1.1,
                                    visible=False
                                )
                            ]
                        )
                        
                        # Add a unique key to each gauge chart
                        st.plotly_chart(gauge_fig, use_container_width=True, key=f"gauge_chart_{i}")
                        st.markdown(close_responsive_column(), unsafe_allow_html=True)
                        
                        st.markdown(close_responsive_row(), unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close animated-bg div

with tab2:
    st.markdown('<div class="animated-bg">', unsafe_allow_html=True)
    st.markdown(animated_text("📋 How to Use This App", "typing"), unsafe_allow_html=True)
    
    st.markdown("""
    This Resume Ranking System helps you find the best candidates for a job position by analyzing resumes against a job description.
    """)
    
    st.markdown(responsive_row(), unsafe_allow_html=True)
    
    st.markdown(responsive_column(lg=6, md=6, sm=12), unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card animate-on-scroll">
        <h3>{animated_icon("1️⃣")} Step 1: Upload Resumes</h3>
        <ul class="animated-list">
            <li>Click on the "Upload Resumes" area to select PDF files</li>
            <li>You can upload multiple resumes at once</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card animate-on-scroll">
        <h3>{animated_icon("3️⃣")} Step 3: Analyze Results</h3>
        <ul class="animated-list">
            <li>The system will process the resumes and rank them based on relevance</li>
            <li>Review the visual comparison and detailed results</li>
            <li>Check individual resume analysis for improvement tips</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(close_responsive_column(), unsafe_allow_html=True)
    
    st.markdown(responsive_column(lg=6, md=6, sm=12), unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card animate-on-scroll">
        <h3>{animated_icon("2️⃣")} Step 2: Enter Job Description</h3>
        <ul class="animated-list">
            <li>Enter the complete job description in the text area</li>
            <li>Include all requirements, responsibilities, and qualifications</li>
            <li>Use the "Load Sample" button for a quick test</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card animate-on-scroll">
        <h3>{animated_icon("4️⃣")} Step 4: Export Results</h3>
        <ul class="animated-list">
            <li>Download the results as a CSV file for further analysis</li>
            <li>Share the insights with your hiring team</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(close_responsive_column(), unsafe_allow_html=True)
    
    st.markdown(close_responsive_row(), unsafe_allow_html=True)
    
    st.markdown(animated_divider(), unsafe_allow_html=True)
    st.markdown(animated_text("How It Works", "header"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="animate-on-scroll">
    This app uses Natural Language Processing (NLP) techniques:
    
    <div class="card" style="margin-top: 1rem;">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <div style="background-color: #4f46e5; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">1</div>
            <strong>Text Extraction</strong>
        </div>
        <p>Extracts text from PDF resumes using PyPDF2 library</p>
    </div>
    
    <div class="card">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <div style="background-color: #4f46e5; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">2</div>
            <strong>TF-IDF Vectorization</strong>
        </div>
        <p>Converts text into numerical vectors that represent the importance of words</p>
    </div>
    
    <div class="card">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <div style="background-color: #4f46e5; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">3</div>
            <strong>Cosine Similarity</strong>
        </div>
        <p>Measures similarity between job description and resumes vectors</p>
    </div>
    
    <div class="card">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <div style="background-color: #4f46e5; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">4</div>
            <strong>AI Analysis</strong>
        </div>
        <p>Generates improvement tips based on matching scores and missing keywords</p>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(animated_divider(), unsafe_allow_html=True)
    st.markdown(animated_text("Tips for Best Results", "header"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card animate-on-scroll">
        <ul class="animated-list">
            <li>Use detailed job descriptions with specific requirements</li>
            <li>Ensure PDFs are properly formatted and text-extractable</li>
            <li>Upload resumes in similar formats for consistent analysis</li>
            <li>Adjust the minimum match threshold based on your hiring needs</li>
            <li>Consider the keyword importance setting for technical positions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close animated-bg div

# Footer with animation
st.markdown(animated_divider(), unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; color: #6b7280; font-size: 0.8rem;" class="animate-on-scroll">
    <p>© 2023 Resume Ranking System | Built with Streamlit</p>
    <p style="margin-top: 0.5rem;">Made with {animated_icon("❤️")} by AI-Powered Resume Analysis Team</p>
</div>
""", unsafe_allow_html=True)

# Add confetti effect when analysis is complete
if 'resumes' in locals() and len(resumes) > 0:
    st.balloons()