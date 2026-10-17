"""questions.json -> practice/index.html (single offline file) and practice/bank.md. Run from project root after questions_src.py."""
import json
Q = json.load(open("practice/questions.json"))
t = open("scripts/template.html").read()
open("practice/index.html", "w").write(t.replace("/*DATA*/", json.dumps(Q, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")))
W = {1: "Week 1 · Software process & models", 2: "Week 2 · FBS & Think and Link", 3: "Week 3 · UML, VeriSIM, quality", 4: "Week 4 · Mapping & abstraction"}
out = ["# SCD practice bank", "", "NPTEL = assignment question (2026); EXTRA = self-written.", ""]
for w in W:
    out += [f"## {W[w]}", ""]
    for q in Q:
        if q["week"] == w:
            out += [f"**{q['id']}** ({q['type']}) {q['question']}", ""] + [f"- {o['k']}. {o['text']}" for o in q["options"]]
            out += ["", f"**Answer:** {', '.join(q['answer'])}. {q['explanation']}", ""]
open("practice/bank.md", "w").write("\n".join(out))
