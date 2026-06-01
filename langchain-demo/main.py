from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

text = ''' 
Breakfast gives you energy for the day.
Fruits and vegetables provide important vitamins.
Whole grains are a good source of fiber.
Protein helps build and repair muscles.
Drinking water keeps your body hydrated.
Eating a variety of foods improves nutrition.
Vegetables add color and nutrients to meals.
Cooking at home gives you control over ingredients.
Baking uses dry heat to cook food in an oven.
Boiling cooks food in hot water.
Simmering gently cooks food just below boiling.
Steaming helps vegetables keep more nutrients.
Olive oil is often used for healthy cooking.
Too much added sugar can harm your health.
Salt enhances flavor but should be limited.
Dairy products provide calcium for strong bones.
Fruits like strawberries contain natural atioxidants.
Leafy greens are rich in vitamins and minerals.
Nuts and seeds contain healthy fats and protein.
Reading food labels helps you make better choices.
Meal prepping saves time during busy weeks.
Grilling adds a smoky flavor to meat and vegetables.
Soups are a simple way to combine many ingredients.
Snacks are healthier when they include fruits or nuts.
Breakfast cereals can be high in added sugar.
Fermented foods can support gut health.
Balanced meals include carbs, protein, and healthy fats.
Desserts taste best when eaten in moderation.
Fresh produce is often found around the edges of grocery stores.
Trying new recipes makes cooking more enjoyable.
'''

chunks = text.split('.')

chunks = [chunk.strip() for chunk in chunks if chunk.strip()]


#chunks = ['Breakfast gives you energy for the day', 'Fruits and vegetables provide important vitamins', 'Whole grains are a good source of fiber', 'Protein helps build and repair muscles', 'Drinking water keeps your body hydrated', 'Eating a variety of foods improves nutrition', 'Vegetables add color and nutrients to meals', 'Cooking at home gives you control over ingredients', 'Baking uses dry heat to cook food in an oven', 'Boiling cooks food in hot water', 'Simmering gently cooks food just below boiling', 'Steaming helps vegetables keep more nutrients', 'Olive oil is often used for healthy cooking', 'Too much added sugar can harm your health', 'Salt enhances flavor but should be limited', 'Dairy products provide calcium for strong bones', 'Fruits like strawberries contain natural atioxidants', 'Leafy greens are rich in vitamins and minerals', 'Nuts and seeds contain healthy fats and protein', 'Reading food labels helps you make better choices', 'Meal prepping saves time during busy weeks', 'Grilling adds a smoky flavor to meat and vegetables', 'Soups are a simple way to combine many ingredients', 'Snacks are healthier when they include fruits or nuts', 'Breakfast cereals can be high in added sugar', 'Fermented foods can support gut health', 'Balanced meals include carbs, protein, and healthy fats', 'Desserts taste best when eaten in moderation', 'Fresh produce is often found around the edges of grocery stores', 'Trying new recipes makes cooking more enjoyable']

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(chunks)
print(embeddings.shape)

query = input("Enter your query: ")


query_embedding = model.encode(query)

similarities = cosine_similarity(
    [query_embedding],
    embeddings
)

best_match_index = similarities.argmax()
print(chunks[best_match_index])


