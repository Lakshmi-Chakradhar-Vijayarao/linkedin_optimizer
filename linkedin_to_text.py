import zipfile
import json
import pandas as pd

def extract_linkedin_data(uploaded_zip_file):
    extracted = {}

    with zipfile.ZipFile(uploaded_zip_file) as archive:
        for file in archive.namelist():
            if file.endswith("Profile.json"):
                profile_data = json.load(archive.open(file))
                extracted['profile'] = {
                    "full_name": profile_data.get("fullName", ""),
                    "headline": profile_data.get("headline", ""),
                    "summary": profile_data.get("summary", ""),
                    "education": profile_data.get("education", []),
                }

            elif file.endswith("Experience.json"):
                exp_data = json.load(archive.open(file))
                experiences = []
                for item in exp_data:
                    role = item.get("title", "")
                    company = item.get("companyName", "")
                    desc = item.get("description", "")
                    date = item.get("timePeriod", {}).get("startDate", {}).get("year", "")
                    experiences.append(f"{role} at {company} ({date}): {desc}")
                extracted['experience'] = experiences

            elif file.endswith("Skills.json"):
                skills_data = json.load(archive.open(file))
                skills = [s.get("name") for s in skills_data]
                extracted['skills'] = skills

            elif file.endswith("Connections.csv"):
                df = pd.read_csv(archive.open(file))
                extracted['connections'] = df.to_dict(orient="records")

            elif file.endswith("Messages.csv"):
                df = pd.read_csv(archive.open(file))
                extracted['messages'] = df.to_dict(orient="records")

            elif file.endswith("Articles.csv") or file.endswith("Posts.csv"):
                df = pd.read_csv(archive.open(file))
                extracted['posts'] = df["Title"].head(5).tolist() if "Title" in df else []

    return extracted
