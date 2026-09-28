import json

with open("records.json", encoding="utf-8") as f:
    records = json.load(f)
with open("categories.json", encoding="utf-8") as f:
    categories = json.load(f)

# assign stable ids and normalize
for i, r in enumerate(records):
    r["id"] = f"seed-{i}"
    r["merchant"] = r.get("merchant") or ""
    r["memo"] = r.get("memo") or ""

records_json = json.dumps(records, ensure_ascii=False).replace("</", "<\\/")
categories_json = json.dumps(categories, ensure_ascii=False).replace("</", "<\\/")

template = open("template.html", encoding="utf-8").read()
out = template.replace("__SEED_RECORDS__", records_json).replace("__SEED_CATEGORIES__", categories_json)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(out)

print("wrote index.html", len(out), "bytes;", len(records), "records,", len(categories), "categories")
