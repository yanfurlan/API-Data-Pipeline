# Salvar em CSV

import os

# Directory to save the file
output_dir = "output_data"
os.makedirs(output_dir, exist_ok=True)

# Save to CSV
csv_file = os.path.join(output_dir, "weather_data.csv")
df.to_csv(csv_file, index=False)

print(f"Arquivo CSV salvo em: {csv_file}")
