import json
from pathlib import Path

Output = Path(__file__).resolve().parent
Documents = {s: json.loads((Output / (s + ".structure.json")).read_text()) for s in ["original", "avk", "r02", "memo", "report", "hazard"]}
Tables = {s: {x["bodyIndex"]: x["rows"] for x in d["tables"]} for s, d in Documents.items()}
OUT = {"hazardTables": [], "slopeTables": {}, "hazardImages": [], "slopeImages": []}

for i, j in zip([668, 671, 690, 693, 958, 961, 964, 967, 971], [48, 53, 58, 63, 68, 73, 78, 83, 88]):
    A = Tables["r02"][i][2:]
    B = Tables["hazard"][j][1:]
    OUT["hazardTables"].append({"dianaBodyIndex": i, "sourceBodyIndex": j, "rows": len(A), "cells": sum(map(len, A)), "equal": A == B, "differences": [(k + 1, x, y) for k, (x, y) in enumerate(zip(A, B)) if x != y]})

OUT["slopeTables"]["periods"] = {"equal": Tables["avk"][755] == Tables["memo"][53], "cells": sum(map(len, Tables["avk"][755]))}
OUT["slopeTables"]["coefficients"] = []
for i, j in enumerate([131, 138, 145, 152, 159]):
    for k, n in [(4, 1), (7, 2)]:
        A = Tables["avk"][766][2 * i + n][2:]
        B = Tables["memo"][j][k][2:]
        OUT["slopeTables"]["coefficients"].append({"dianaRow": 2 * i + n + 1, "sourceBodyIndex": j, "sourceRow": k + 1, "cells": len(A), "equal": A == B, "diana": A, "source": B})

Parts = Documents["r02"]["parts"]
for x in Documents["hazard"]["images"]:
    if x["bodyIndex"] < 91:
        continue
    s = Documents["hazard"]["nodes"][x["bodyIndex"] - 1]["text"].split("Figure ")[1]
    t = "word/media/diana-hazard-" + s.lower() + ".png"
    DATA = [y for y in Documents["r02"]["images"] if y["part"] == t]
    OUT["hazardImages"].append({"label": s, "part": t, "matchesSource": Parts[t] == x["sha256"], "uses": len(DATA), "bodyIndices": [y["bodyIndex"] for y in DATA]})

for s in ["image41.png", "image42.png", "image43.png"]:
    t = "word/media/" + s
    OUT["slopeImages"].append({"part": t, "matchesMemo": [x["bodyIndex"] for x in Documents["memo"]["images"] if x["sha256"] == Parts[t]], "preservedFromAVK": Parts[t] == Documents["avk"]["parts"][t]})

A = Documents["avk"]["nodes"]
B = Documents["r02"]["nodes"]
i = next(x["bodyIndex"] for x in A if x["text"] == "Slope Design Parameters")
j = next(x["bodyIndex"] for x in A if x["text"] == "Conclusions")
OUT["chapter10"] = {"start": i, "endBefore": j, "count": j - i, "equal": A[i - 1:j - 1] == B[i - 1:j - 1]}
OUT["tableChangedCells"] = {s: sum(x != y for t in Tables[s] for a, b in zip(Tables[s][t], Tables["original"][t]) for x, y in zip(a, b)) for s in ["avk"]}
OUT["hazardTotals"] = {"tables": len(OUT["hazardTables"]), "cells": sum(x["cells"] for x in OUT["hazardTables"]), "allTablesMatch": all(x["equal"] for x in OUT["hazardTables"]), "images": len(OUT["hazardImages"]), "allImagesMatch": all(x["matchesSource"] and x["uses"] == 1 for x in OUT["hazardImages"])}
(Output / "coverage.json").write_text(json.dumps(OUT, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in OUT.items() if k not in ["hazardImages", "slopeTables"]}, ensure_ascii=False, indent=2))
print("slope periods:", OUT["slopeTables"]["periods"])
print("slope coefficients:", all(x["equal"] for x in OUT["slopeTables"]["coefficients"]), "cells:", sum(x["cells"] for x in OUT["slopeTables"]["coefficients"]))
