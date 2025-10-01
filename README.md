# GMO FactLens

A comprehensive web application that uses **Streamlit** for the frontend and **crewAI** for backend processing to find, scrape, summarize, and classify online articles and linkedin posts. The application determines if claims are based on fact or myth and classifies them into predefined categories.

## 🏗️ Project Structure

```
project1/
├── main.py                 # Main entry point
├── crewai_workflow.py      # CrewAI workflow orchestration
├── agents/
│   ├── __init__.py
│   ├── search_agent.py     # Web search using SerperAPI
│   ├── scrape_agent.py     # Content scraping using trafilatura
│   └── analysis_agent.py   # AI analysis using Google Gemini
├── ui/
│   ├── __init__.py
│   └── streamlit_ui.py     # Streamlit user interface
├── pyproject.toml          # Project dependencies
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── .gitignore              # Git ignore patterns
```

## ✨ Features

- 🔍 **Web Search**: Uses SerperAPI to find relevant articles/blog posts, and social media posts
- 📄 **Content Scraping**: Extracts clean content using trafilatura
- 🤖 **AI Analysis**: Uses Google Gemini for summarization and classification
- ✅ **Fact Checking**: Assesses claims as Fact, Myth, or Unclear
- 📊 **Beautiful UI**: Clean Streamlit interface with real-time updates
- 📈 **Data Visualization**: Charts and graphs using Plotly
- 📥 **Export Results**: Download analysis as JSON or CSV

## 📋 Categories

The application classifies findings into nine categories:
1. **Health** 🏥
2. **Environmental** 🌱
3. **Social Economics** 💰
4. **Conspiracy Theory** 🤔
5. **Corporate Control** 🏢
6. **Ethical/Religious Issues** ⛪
7. **Seed Ownership** 🌾
8. **Scientific Authority** 🔬
9. **Other** 📋

## 🛠️ Prerequisites

- Python 3.11 or higher
- SerperAPI key (for web search)
- Google API key (for Gemini AI)

## 📦 Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**:
   
   Create a `.env` file in the project root:
   ```env
   SERPER_API_KEY=your_serper_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```
   
   Or set environment variables:
   ```bash
   # Windows
   set SERPER_API_KEY=your_serper_api_key_here
   set GOOGLE_API_KEY=your_google_api_key_here
   
   # Linux/Mac
   export SERPER_API_KEY=your_serper_api_key_here
   export GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🔑 Getting API Keys

### SerperAPI Key
1. Visit [serper.dev](https://serper.dev)
2. Sign up for a free account
3. Get your API key from the dashboard

### Google API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Enable the Gemini API

## 🚀 Usage

1. **Run the application**:
   ```bash
   streamlit run main.py
   ```

2. **Open your browser** and navigate to the URL shown (usually `http://localhost:8501`)

3. **Enter a topic** in the sidebar (e.g., "gmo can cause cancer", "gmo is all about making money", "gmos are not organic")

4. **Click "Run Analysis"** to start the process

6. **View results** in organized tabs:
   - **Blogs**: Individual article analysis with expandable details
   - **Charts**: Visualizations of classification and fact/myth distribution
   - **Export**: Download results as JSON or CSV

## 🔄 Application Workflow

1. **User Input**: Topic entered in Streamlit interface
2. **Search Agent**: Uses SerperAPI to find top 10 relevant URLs
3. **Scrape Agent**: Extracts content using trafilatura with progress tracking
4. **Analysis Agent**: Uses Gemini to:
   - Generate summaries
   - Classify articles
   - Assess fact/myth status
   - Provide confidence levels
5. **Display**: Results shown in clean, organized format with visualizations

## 📊 Features

### Real-time Progress Tracking
- Progress bars for each processing step
- Status messages with detailed information
- Error handling with user-friendly messages

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Ensure both API keys are set correctly
   - Check the API key status in the sidebar
   - Verify API keys have sufficient credits

2. **No Results Found**:
   - Try a different search term
   - Check internet connection
   - Verify SerperAPI is working

3. **Analysis Failures**:
   - Check Google API key and Gemini access
   - Some articles may fail to scrape (this is normal)
   - Check the console for detailed error messages

4. **Import Errors**:
   - Ensure all dependencies are installed
   - Check Python version (3.11+ required)
   - Verify project structure is intact

### Performance Notes

- The application processes only the top 10 search results by default
- Content is limited to 5000 characters for analysis
- Processing time depends on blog count and content length
- Use specific search terms for better results

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

## 📄 License

This project is open source and available under the MIT License.

## 🔄 Version History

- **v2.0**: Modular architecture with enhanced features
- **v1.0**: Initial single-file implementation
