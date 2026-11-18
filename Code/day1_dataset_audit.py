from pathlib import Path
from PIL import Image 
import pandas as pd
project_path = Path(__file__).resolve().parent.parent
dataset_path = project_path / "Dataset"

data_path = next(dataset_path.iterdir())

print("Dataset Path:", data_path)
print("dataset path:",data_path)

splits=["train","val","test"]

extensions={".jpg",".jpeg",".png",".bmp",".webp"}
records=[]

for split in splits:
    split_path=data_path/split

    print("\n","="*45)
    print("SPLIT:",split.upper())
    print("="*45)
    if not split_path.exists():
        print("Folder missing:",split)
        continue

    for class_folder in sorted (split_path.iterdir()): 
        
        if not class_folder.is_dir():
            continue

        # Find all images inside the class folder
        image_files = [
            f for f in class_folder.rglob("*")
            if f.is_file() and f.suffix.lower() in extensions
        ]

        # Initialize counters
        valid_count = 0
        invalid_count = 0

        widths = []
        heights = []

        # Check every image
        for image_path in image_files:

            try:
                with Image.open(image_path) as img:
                    width, height = img.size
                    img.verify()

                valid_count += 1

                widths.append(width)
                heights.append(height)

            except Exception:
        
               invalid_count += 1   

# result store 
        records.append({
            "Split": split,
            "Class": class_folder.name,
            "Total Images": len(image_files),
            "Valid Images": valid_count,
            "Invalid Images": invalid_count,
            "Avg Width": round(sum(widths) / len(widths), 2) if widths else 0,
            "Avg Height": round(sum(heights) / len(heights), 2) if heights else 0
        })       

#final data set report
df=pd.DataFrame(records)
print("\nFinal DatatSet Report")
print(df.to_string(index=False))

#split_wise image totals
print("\n Split Totals")
if not df.empty:
    print(df.groupby("Split")["Valid Images"].sum())
else:
    print("no image data found")    


#CSV report save
report_path=project_path/"reports" 
report_path.mkdir(exist_ok=True)
df.to_csv(
     report_path/"day1_dataset_audit.csv",
     index=False
)
print("\nReport saved successfully")