from sentence_transformers import SentenceTransformer
from sihapp.models import Candidate, Internship
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_embeddings():
    candidates = Candidate.objects.all()
    internships = Internship.objects.all()
    
    candidate_embeddings = {c.id: model.encode(c.skills) for c in candidates}
    internship_embeddings = {i.id: model.encode(i.skills_required) for i in internships}
    
    return candidate_embeddings, internship_embeddings
def match_candidates():
    candidate_embeddings, internship_embeddings = generate_embeddings()
    results = []
    
    for c_id, c_emb in candidate_embeddings.items():
        candidate = Candidate.objects.get(id=c_id)
        for i_id, i_emb in internship_embeddings.items():
            internship = Internship.objects.get(id=i_id)
            
            # Semantic similarity
            sim_score = cosine_similarity([c_emb], [i_emb])[0][0]
            
            # Location match
            location_score = 1 if candidate.internship_location.lower() == internship.location.lower() else 0
            
            # Participation factor
            participation_score = 0.1 * candidate.past_participation
            
            # Total score
            total_score = 0.7 * sim_score + 0.2 * location_score + participation_score
            
            results.append({
                'candidate': candidate.name,
                'internship': f"{internship.title} at {internship.company_name}",
                'score': round(total_score, 2)
            })
    
    # Sort descending
    results = sorted(results, key=lambda x: x['score'], reverse=True)
    return results
