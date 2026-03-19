names = ["Ahmed", "Fatima", "Omar", "Leila", "Karim"]
scores = [85, 92, 78, 88, 95]
 
# Generator function - yields values one at a time (lazy evaluation)
def score_filter(name_score_pairs):
    for name, score in name_score_pairs:
        if score >= 85:
            yield (name, score)
 
# zip() pairs names with scores
paired = zip(names, scores)
 
# Dictionary comprehension from generator
high_scorers = {name: score for name, score in score_filter(paired)}
 
# sorted() with key parameter - sorts by score descending
sorted_results = sorted(high_scorers.items(), key=lambda x: x[1], reverse=True)
 
for name, score in sorted_results:
    print(f"{name}: {score}")
 