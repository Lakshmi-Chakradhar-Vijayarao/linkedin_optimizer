🧠 LinkedIn Optimizer (AI + Google CSE Powered)

Boost your LinkedIn profile visibility, credibility, and hiring potential using AI-driven optimization based on your resume and target job role.

> Built with OpenAI, Google Custom Search, Streamlit, and resume parsing logic.

---

🚀 Features

* 📄 **Resume Parsing**: Extracts key education and experience data from PDF, DOCX, or TXT resumes.
* 🧠 **AI-Powered Optimization**: Uses OpenAI to generate:

  * Headline, About section, Skills, Experience, and more — tailored to your role.
* 🔍 **Suggested Connections**: Fetches real LinkedIn profiles similar to your target role.
* 🧲 **Recruiter Discovery**: Identifies hiring managers and recruiters via Google CSE.
* 🧬 **Related Role Intelligence**: Dynamically expands job roles using OpenAI (e.g., "AI Engineer" → "ML Engineer", "Data Scientist").

---

📦 Tech Stack

* `Streamlit` – frontend UI
* `OpenAI API` – GPT-3.5 for generation
* `Google Custom Search API` – for profile lookups
* `PyMuPDF` / `python-docx` – resume text extraction
* `.env` – secure key storage

---

⚙️ Getting Started

1. Clone the repo

```bash
git clone https://github.com/Lakshmi-Chakradhar-Vijayarao/linkedin_optimizer.git
cd linkedin_optimizer
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create `.env` file

```env
OPENAI_API_KEY=your_openai_key_here
GOOGLE_CSE_API_KEY=your_google_cse_key_here
GOOGLE_CSE_CX=your_cse_cx_here
```

4. Run the app

```bash
streamlit run app.py
```

---

🔐 Environment Variables

Make sure your `.env` file contains:

| Key                  | Description                  |
| -------------------- | ---------------------------- |
| `OPENAI_API_KEY`     | Your OpenAI secret key       |
| `GOOGLE_CSE_API_KEY` | Google Custom Search API key |
| `GOOGLE_CSE_CX`      | Your Custom Search Engine ID |

---

☁️ Deploy on Streamlit Cloud (Optional)

1. Push this repo to GitHub ✅
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub → Select this repo
4. Add environment secrets in **App Settings > Secrets**:

```toml
OPENAI_API_KEY="your-key"
GOOGLE_CSE_API_KEY="your-key"
GOOGLE_CSE_CX="your-cx"
```

5. Click **Deploy** 🚀

---

📄 License

This project is under the MIT License. Feel free to use, modify, and share.


