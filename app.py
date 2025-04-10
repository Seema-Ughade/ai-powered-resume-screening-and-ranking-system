# # import streamlit as st
# # from PyPDF2 import PdfReader
# # import pandas as pd
# # import time
# # import matplotlib.pyplot as plt
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from sklearn.metrics.pairwise import cosine_similarity

# # # 🎨 **Custom CSS for a Beautiful UI**
# # st.markdown("""
# #     <style>
# #     body {
# #         background-color: #121212;
# #         color: white;
# #     }
# #     .stApp {
# #         background-color: #1E1E1E;
# #     }
# #     h1 {
# #         text-align: center;
# #         color: #4CAF50;
# #         font-size: 36px;
# #         font-weight: bold;
# #     }
# #     .stTextArea, .stFileUploader {
# #         border-radius: 10px;
# #         box-shadow: 0 0 10px #4CAF50;
# #     }
# #     .stButton>button {
# #         background-color: #4CAF50;
# #         color: white;
# #         padding: 12px 18px;
# #         font-size: 18px;
# #         border-radius: 8px;
# #         border: none;
# #         transition: 0.3s;
# #     }
# #     .stButton>button:hover {
# #         background-color: #45a049;
# #     }
# #     .stDataFrame {
# #         border-radius: 10px;
# #         box-shadow: 0px 0px 10px rgba(0, 255, 0, 0.5);
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # # 📌 **Page Title**
# # st.title("🚀 Resume Ranking System")

# # col1, col2 = st.columns(2)

# # with col1:
# #     st.header("📤 Upload Resumes")
# #     uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

# # with col2:
# #     st.header("📝 Job Description")
# #     job_description = st.text_area("Enter the job description...")

# # # 📌 **Extract Text from PDF Resumes**
# # def extract_text_from_pdf(file):
# #     pdf = PdfReader(file)
# #     text = "".join([page.extract_text() or "" for page in pdf.pages])
# #     return text.strip()

# # # 📌 **Rank Resumes Using TF-IDF & Cosine Similarity**
# # def rank_resumes(job_description, resumes):
# #     documents = [job_description] + resumes
# #     vectorizer = TfidfVectorizer().fit_transform(documents)
# #     vectors = vectorizer.toarray()
# #     job_desc_vector = vectors[0]
# #     resume_vectors = vectors[1:]
# #     return cosine_similarity([job_desc_vector], resume_vectors).flatten()

# # # 📌 **AI Suggestions for Resume Improvement**
# # def generate_resume_tips(score):
# #     if score > 80:
# #         return "🔥 Excellent match! Your resume is well-optimized."
# #     elif score > 60:
# #         return "✅ Good match! Consider adding more relevant keywords."
# #     else:
# #         return "⚡ Low match! Try improving your skills section and adding industry-specific terms."

# # # 📌 **Start Ranking Process**
# # if uploaded_files and job_description:
# #     st.header("📊 Resume Rankings")

# #     resumes = [extract_text_from_pdf(file) for file in uploaded_files]

# #     progress_bar = st.progress(0)
# #     for i in range(100):
# #         time.sleep(0.02)
# #         progress_bar.progress(i + 1)

# #     scores = rank_resumes(job_description, resumes)

# #     results_df = pd.DataFrame({
# #         "Resume": [file.name for file in uploaded_files],
# #         "Match Score (%)": (scores * 100).round(2),
# #         "AI Suggestion": [generate_resume_tips(score * 100) for score in scores]
# #     }).sort_values(by="Match Score (%)", ascending=False)

# #     st.dataframe(results_df.style.format({"Match Score (%)": "{:.2f}"}))
# #     st.success(f"✅ Ranking Complete! 🎯 Top Match: **{results_df.iloc[0]['Resume']}**")
    
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

# # Page configuration
# st.set_page_config(
#     page_title="Resume Ranking System",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for elegant UI
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
    
#     /* Card styling */
#     .card {
#         border-radius: 10px;
#         border: 1px solid #e5e7eb;
#         padding: 1.5rem;
#         margin-bottom: 1rem;
#         background-color: white;
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
#     }
    
#     .card-header {
#         border-bottom: 1px solid #e5e7eb;
#         padding-bottom: 0.75rem;
#         margin-bottom: 1rem;
#         font-weight: 600;
#         font-size: 1.25rem;
#         color: var(--primary-dark);
#     }
    
#     /* Button styling */
#     .stButton > button {
#         background-color: var(--primary-color);
#         color: white;
#         border-radius: 6px;
#         padding: 0.5rem 1rem;
#         font-weight: 500;
#         border: none;
#         transition: all 0.3s ease;
#     }
    
#     .stButton > button:hover {
#         background-color: var(--primary-dark);
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
#     }
    
#     /* File uploader styling */
#     .stFileUploader > div > div {
#         border: 2px dashed var(--primary-light);
#         border-radius: 10px;
#         padding: 2rem;
#         background-color: #f8fafc;
#     }
    
#     /* Text area styling */
#     .stTextArea > div > div > textarea {
#         border-radius: 6px;
#         border-color: #e5e7eb;
#     }
    
#     /* Metrics styling */
#     .metric-card {
#         background-color: white;
#         border-radius: 8px;
#         padding: 1rem;
#         box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
#         border-left: 4px solid var(--primary-color);
#     }
    
#     .metric-value {
#         font-size: 1.5rem;
#         font-weight: 700;
#         color: var(--primary-dark);
#     }
    
#     .metric-label {
#         font-size: 0.875rem;
#         color: #6b7280;
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
#         animation: pulse 2s infinite;
#     }
    
#     /* Dataframe styling */
#     .dataframe-container {
#         border-radius: 8px;
#         overflow: hidden;
#         border: 1px solid #e5e7eb;
#     }
    
#     /* Expander styling */
#     .streamlit-expanderHeader {
#         font-weight: 600;
#         color: var(--primary-dark);
#     }
    
#     /* Success message styling */
#     .success-message {
#         background-color: #ecfdf5;
#         border-left: 4px solid var(--success-color);
#         padding: 1rem;
#         border-radius: 6px;
#         margin: 1rem 0;
#     }
    
#     /* Sidebar styling */
#     .css-1d391kg {
#         background-color: #f1f5f9;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Sidebar
# with st.sidebar:
#     st.title("⚙️ Settings")
    
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
    
#     st.markdown("---")
#     st.markdown("### About")
#     st.markdown("""
#     This app helps you rank resumes based on job descriptions using NLP techniques.
    
#     **Features:**
#     - PDF resume analysis
#     - TF-IDF vectorization
#     - Cosine similarity scoring
#     - AI-powered improvement tips
#     """)

# # Main content
# st.title("📊 Resume Ranking System")

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

# # Function to create a downloadable Excel file
# def to_excel(df):
#     output = BytesIO()
#     with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
#         df.to_excel(writer, sheet_name='Resume Rankings', index=False)
#     processed_data = output.getvalue()
#     return processed_data

# # Function to create download link
# def get_download_link(df, filename="resume_rankings.xlsx"):
#     val = to_excel(df)
#     b64 = base64.b64encode(val).decode()
#     return f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">Download Excel file</a>'

# # Main layout
# tab1, tab2 = st.tabs(["📤 Upload & Analyze", "📋 Instructions"])

# with tab1:
#     col1, col2 = st.columns([1, 1])
    
#     with col1:
#         st.markdown('<div class="card">', unsafe_allow_html=True)
#         st.markdown('<div class="card-header">Upload Resumes</div>', unsafe_allow_html=True)
#         uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col2:
#         st.markdown('<div class="card">', unsafe_allow_html=True)
#         st.markdown('<div class="card-header">Job Description</div>', unsafe_allow_html=True)
#         job_description = st.text_area("Enter the job description...", height=200)
        
#         col_a, col_b = st.columns([1, 1])
#         with col_a:
#             if st.button("Load Sample Job Description"):
#                 job_description = sample_job_description
#                 st.rerun()

#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Analysis process
#     if uploaded_files and job_description:
#         st.markdown("---")
#         st.subheader("📈 Analysis Results")
        
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
                
#                 # Display metrics
#                 st.markdown('<div style="display: flex; justify-content: space-between; margin-bottom: 20px;">', unsafe_allow_html=True)
                
#                 metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                
#                 with metric_col1:
#                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{len(resumes)}</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">Resumes Analyzed</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with metric_col2:
#                     top_score = results_df["Match Score (%)"].max()
#                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{top_score:.1f}%</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">Top Match Score</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with metric_col3:
#                     avg_score = results_df["Match Score (%)"].mean()
#                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{avg_score:.1f}%</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">Average Score</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with metric_col4:
#                     good_matches = results_df[results_df["Match Score (%)"] >= min_match_threshold].shape[0]
#                     st.markdown('<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{good_matches}</div>', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-label">Matches Above {min_match_threshold}%</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Display top match
#                 if not results_df.empty:
#                     top_match = results_df.iloc[0]
#                     st.markdown(f"""
#                     <div class="success-message">
#                         <h3>🏆 Top Match: {top_match['Resume']}</h3>
#                         <p>Match Score: <strong>{top_match['Match Score (%)']}%</strong> | Category: <strong>{top_match['Match Category']}</strong></p>
#                     </div>
#                     """, unsafe_allow_html=True)
                
#                 # Display visualization
#                 st.subheader("📊 Visual Comparison")
                
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
#                         font=dict(color="#1f2937")
#                     )
#                     st.plotly_chart(fig, use_container_width=True)
                
#                 # Display results table
#                 st.subheader("📋 Detailed Results")
                
#                 st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
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
                
#                 # Download button
#                 st.markdown(get_download_link(results_df), unsafe_allow_html=True)
                
#                 # Detailed analysis for each resume
#                 st.subheader("🔍 Individual Resume Analysis")
                
#                 for i, (_, row) in enumerate(results_df.iterrows()):
#                     resume_name = row["Resume"]
#                     score = row["Match Score (%)"] / 100
                    
#                     with st.expander(f"{resume_name} - {row['Match Score (%)']}% ({row['Match Category']})"):
#                         col1, col2 = st.columns([2, 1])
                        
#                         with col1:
#                             st.markdown("### Improvement Tips")
#                             tips = generate_resume_tips(score, resumes[resume_names.index(resume_name)], job_description)
                            
#                             for tip in tips:
#                                 st.markdown(f"- {tip}")
                        
#                         with col2:
#                             # Create a gauge chart for the score
#                             fig = go.Figure(go.Indicator(
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
                            
#                             fig.update_layout(
#                                 height=250,
#                                 margin=dict(l=20, r=20, t=30, b=20),
#                                 paper_bgcolor="white",
#                                 font=dict(color="#1f2937")
#                             )
                            
#                             st.plotly_chart(fig, use_container_width=True)

# with tab2:
#     st.markdown("""
#     ## 📋 How to Use This App
    
#     This Resume Ranking System helps you find the best candidates for a job position by analyzing resumes against a job description.
    
#     ### Step 1: Upload Resumes
#     - Click on the "Upload Resumes" area to select PDF files
#     - You can upload multiple resumes at once
    
#     ### Step 2: Enter Job Description
#     - Enter the complete job description in the text area
#     - Include all requirements, responsibilities, and qualifications
#     - Use the "Load Sample" button for a quick test
    
#     ### Step 3: Analyze Results
#     - The system will process the resumes and rank them based on relevance
#     - Review the visual comparison and detailed results
#     - Check individual resume analysis for improvement tips
    
#     ### Step 4: Export Results
#     - Download the results as an Excel file for further analysis
    
#     ### How It Works
    
#     This app uses Natural Language Processing (NLP) techniques:
    
#     1. **Text Extraction**: Extracts text from PDF resumes
#     2. **TF-IDF Vectorization**: Converts text into numerical vectors
#     3. **Cosine Similarity**: Measures similarity between job description and resumes
#     4. **AI Analysis**: Generates improvement tips based on matching scores
    
#     ### Tips for Best Results
    
#     - Use detailed job descriptions with specific requirements
#     - Ensure PDFs are properly formatted and text-extractable
#     - Upload resumes in similar formats for consistent analysis
#     """)

# # Footer
# st.markdown("---")
# st.markdown("""
# <div style="text-align: center; color: #6b7280; font-size: 0.8rem;">
#     © 2023 Resume Ranking System | Built with Streamlit
# </div>
# """, unsafe_allow_html=True)




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

# Page configuration
st.set_page_config(
    page_title="Resume Ranking System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for elegant UI
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #3b82f6;
        --primary-light: #93c5fd;
        --primary-dark: #1d4ed8;
        --secondary-color: #f3f4f6;
        --text-color: #1f2937;
        --success-color: #10b981;
        --warning-color: #f59e0b;
        --danger-color: #ef4444;
    }
    
    /* Base styling */
    .main {
        background-color: #f8fafc;
        color: var(--text-color);
    }
    
    h1, h2, h3 {
        color: var(--primary-dark);
    }
    
    /* Card styling */
    .card {
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        padding: 1.5rem;
        margin-bottom: 1rem;
        background-color: white;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .card-header {
        border-bottom: 1px solid #e5e7eb;
        padding-bottom: 0.75rem;
        margin-bottom: 1rem;
        font-weight: 600;
        font-size: 1.25rem;
        color: var(--primary-dark);
    }
    
    /* Button styling */
    .stButton > button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: var(--primary-dark);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* File uploader styling */
    .stFileUploader > div > div {
        border: 2px dashed var(--primary-light);
        border-radius: 10px;
        padding: 2rem;
        background-color: #f8fafc;
    }
    
    /* Text area styling */
    .stTextArea > div > div > textarea {
        border-radius: 6px;
        border-color: #e5e7eb;
    }
    
    /* Metrics styling */
    .metric-card {
        background-color: white;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        border-left: 4px solid var(--primary-color);
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--primary-dark);
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #6b7280;
    }
    
    /* Progress bar animation */
    @keyframes pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7);
        }
        70% {
            box-shadow: 0 0 0 10px rgba(59, 130, 246, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(59, 130, 246, 0);
        }
    }
    
    .stProgress > div > div > div {
        background-color: var(--primary-color);
        animation: pulse 2s infinite;
    }
    
    /* Dataframe styling */
    .dataframe-container {
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: var(--primary-dark);
    }
    
    /* Success message styling */
    .success-message {
        background-color: #ecfdf5;
        border-left: 4px solid var(--success-color);
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f1f5f9;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    
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
    
    st.markdown("### Visualization Settings")
    
    chart_type = st.selectbox(
        "Chart Type",
        options=["Bar Chart", "Horizontal Bar", "Radar Chart"],
        index=0
    )
    
    color_theme = st.selectbox(
        "Color Theme",
        options=["Blues", "Greens", "Purples", "Oranges"],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This app helps you rank resumes based on job descriptions using NLP techniques.
    
    **Features:**
    - PDF resume analysis
    - TF-IDF vectorization
    - Cosine similarity scoring
    - AI-powered improvement tips
    """)

# Main content
st.title("📊 Resume Ranking System")

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

# Function to create a downloadable CSV file (instead of Excel)
def to_csv(df):
    output = BytesIO()
    df.to_csv(output, index=False)
    processed_data = output.getvalue()
    return processed_data

# Function to create download link
def get_download_link(df, filename="resume_rankings.csv"):
    val = to_csv(df)
    b64 = base64.b64encode(val).decode()
    return f'<a href="data:text/csv;base64,{b64}" download="{filename}">Download CSV file</a>'

# Main layout
tab1, tab2 = st.tabs(["📤 Upload & Analyze", "📋 Instructions"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">Upload Resumes</div>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">Job Description</div>', unsafe_allow_html=True)
        job_description = st.text_area("Enter the job description...", height=200)
        
        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("Load Sample Job Description"):
                # Use session state instead of experimental_rerun
                st.session_state.job_description = sample_job_description
                job_description = sample_job_description
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Analysis process
    if uploaded_files and job_description:
        st.markdown("---")
        st.subheader("📈 Analysis Results")
        
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
                
                # Display metrics
                st.markdown('<div style="display: flex; justify-content: space-between; margin-bottom: 20px;">', unsafe_allow_html=True)
                
                metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                
                with metric_col1:
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{len(resumes)}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">Resumes Analyzed</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with metric_col2:
                    top_score = results_df["Match Score (%)"].max()
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{top_score:.1f}%</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">Top Match Score</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with metric_col3:
                    avg_score = results_df["Match Score (%)"].mean()
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{avg_score:.1f}%</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">Average Score</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with metric_col4:
                    good_matches = results_df[results_df["Match Score (%)"] >= min_match_threshold].shape[0]
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{good_matches}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-label">Matches Above {min_match_threshold}%</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Display top match
                if not results_df.empty:
                    top_match = results_df.iloc[0]
                    st.markdown(f"""
                    <div class="success-message">
                        <h3>🏆 Top Match: {top_match['Resume']}</h3>
                        <p>Match Score: <strong>{top_match['Match Score (%)']}%</strong> | Category: <strong>{top_match['Match Category']}</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Display visualization
                st.subheader("📊 Visual Comparison")
                
                fig = None
                
                if chart_type == "Bar Chart":
                    fig = px.bar(
                        results_df,
                        x="Resume",
                        y="Match Score (%)",
                        color="Match Category",
                        color_discrete_map={
                            "Excellent Match": "#10b981",
                            "Good Match": "#3b82f6",
                            "Fair Match": "#f59e0b",
                            "Poor Match": "#ef4444"
                        },
                        title="Resume Match Scores"
                    )
                    fig.add_hline(y=min_match_threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold ({min_match_threshold}%)")
                
                elif chart_type == "Horizontal Bar":
                    fig = px.bar(
                        results_df,
                        y="Resume",
                        x="Match Score (%)",
                        color="Match Category",
                        color_discrete_map={
                            "Excellent Match": "#10b981",
                            "Good Match": "#3b82f6",
                            "Fair Match": "#f59e0b",
                            "Poor Match": "#ef4444"
                        },
                        title="Resume Match Scores",
                        orientation='h'
                    )
                    fig.add_vline(x=min_match_threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold ({min_match_threshold}%)")
                
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
                        font=dict(color="#1f2937")
                    )
                    # FIX: Add a unique key to the plotly_chart
                    st.plotly_chart(fig, use_container_width=True, key="main_chart")
                
                # Display results table
                st.subheader("📋 Detailed Results")
                
                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
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
                
                # Download button (using CSV instead of Excel)
                st.markdown(get_download_link(results_df), unsafe_allow_html=True)
                
                # Detailed analysis for each resume
                st.subheader("🔍 Individual Resume Analysis")
                
                for i, (_, row) in enumerate(results_df.iterrows()):
                    resume_name = row["Resume"]
                    score = row["Match Score (%)"] / 100
                    
                    with st.expander(f"{resume_name} - {row['Match Score (%)']}% ({row['Match Category']})"):
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            st.markdown("### Improvement Tips")
                            tips = generate_resume_tips(score, resumes[resume_names.index(resume_name)], job_description)
                            
                            for tip in tips:
                                st.markdown(f"- {tip}")
                        
                        with col2:
                            # Create a gauge chart for the score
                            gauge_fig = go.Figure(go.Indicator(
                                mode="gauge+number",
                                value=row["Match Score (%)"],
                                domain={'x': [0, 1], 'y': [0, 1]},
                                title={'text': "Match Score"},
                                gauge={
                                    'axis': {'range': [0, 100]},
                                    'bar': {'color': "#3b82f6"},
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
                            
                            gauge_fig.update_layout(
                                height=250,
                                margin=dict(l=20, r=20, t=30, b=20),
                                paper_bgcolor="white",
                                font=dict(color="#1f2937")
                            )
                            
                            # FIX: Add a unique key to each gauge chart
                            st.plotly_chart(gauge_fig, use_container_width=True, key=f"gauge_chart_{i}")

with tab2:
    st.markdown("""
    ## 📋 How to Use This App
    
    This Resume Ranking System helps you find the best candidates for a job position by analyzing resumes against a job description.
    
    ### Step 1: Upload Resumes
    - Click on the "Upload Resumes" area to select PDF files
    - You can upload multiple resumes at once
    
    ### Step 2: Enter Job Description
    - Enter the complete job description in the text area
    - Include all requirements, responsibilities, and qualifications
    - Use the "Load Sample" button for a quick test
    
    ### Step 3: Analyze Results
    - The system will process the resumes and rank them based on relevance
    - Review the visual comparison and detailed results
    - Check individual resume analysis for improvement tips
    
    ### Step 4: Export Results
    - Download the results as a CSV file for further analysis
    
    ### How It Works
    
    This app uses Natural Language Processing (NLP) techniques:
    
    1. **Text Extraction**: Extracts text from PDF resumes
    2. **TF-IDF Vectorization**: Converts text into numerical vectors
    3. **Cosine Similarity**: Measures similarity between job description and resumes
    4. **AI Analysis**: Generates improvement tips based on matching scores
    
    ### Tips for Best Results
    
    - Use detailed job descriptions with specific requirements
    - Ensure PDFs are properly formatted and text-extractable
    - Upload resumes in similar formats for consistent analysis
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; font-size: 0.8rem;">
    © 2025 Resume Ranking System | Built with Streamlit
</div>
""", unsafe_allow_html=True)

print("Resume Ranking System is running successfully!")