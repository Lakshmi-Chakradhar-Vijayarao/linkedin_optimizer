from cse_helper import google_cse_search
from openai_helper import get_related_roles_via_openai

def clean_entity(entity):
    if not entity:
        return ""
    return entity.split("|")[0].split(",")[0].strip()

def fetch_real_connections(role, location, university=None, company=None, max_results=5):
    """
    Fetch real LinkedIn connections based on role, location, university, and company.
    """
    location = location.strip() or "worldwide"
    search_terms = [f'"{role}"', f'"{location}"', '("engineer" OR "developer" OR "scientist")']

    if university:
        search_terms.append(f'"{clean_entity(university)}"')
    if company:
        search_terms.append(f'"{clean_entity(company)}"')

    query = 'site:linkedin.com/in ' + " ".join(search_terms)
    results = google_cse_search(query, num_results=max_results, debug=True)

    # Retry with stripped query if fallback is returned
    if results and "Fallback" in results[0][0]:
        stripped_query = f'site:linkedin.com/in "{role}" "{location}"'
        return google_cse_search(stripped_query, num_results=max_results, debug=True)

    return results

def fetch_recruiters(role, location, max_results=5):
    """
    Fetch recruiters or hiring managers using dynamic related roles.
    """
    location = location.strip() or "worldwide"
    related_roles = get_related_roles_via_openai(role) or [role]

    role_query_block = " OR ".join([f'"{r}"' for r in related_roles])

    recruiter_titles = (
        '"technical recruiter" OR "lead recruiter" OR '
        '"talent acquisition specialist" OR "hiring manager" OR "recruitment lead"'
    )

    query = (
        f'site:linkedin.com/in ({recruiter_titles}) ({role_query_block}) "{location}"'
    )

    results = google_cse_search(query, num_results=max_results, debug=True)

    if results and "Fallback" in results[0][0]:
        fallback_query = (
            f'site:linkedin.com/in ("recruiter" OR "talent acquisition") "{role}" "{location}"'
        )
        return google_cse_search(fallback_query, num_results=max_results, debug=True)

    return results
