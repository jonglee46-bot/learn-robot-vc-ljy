"""facts.csv 로 실습 결과를 만든다.

현재 폴더의 facts.csv, sources.md 를 읽어 humanoid_count.csv, bom_chart.html,
index.html, expected.json 을 쓴다.
"""
import csv, json, re
from collections import Counter
from html import escape
from pathlib import Path

rows = list(csv.DictReader(Path("facts.csv").open(encoding="utf-8-sig")))
fact = {r["번호"]: r for r in rows}
state = Counter(r["상태"] for r in rows)
sources = len(re.findall(r"^\| S\d\d \|", Path("sources.md").read_text(encoding="utf-8"), re.M))

# Block 1: 휴머노이드 수량 표. 평균을 내지 않고 집계 대상과 함께 둔다
near = re.search(r"Nearly|\d[\d,]*", fact["F13"]["비고"]) and re.search(r"\d,\d{3}", fact["F13"]["비고"]).group()
count = [
    ("IFR", fact["F13"]["값(원문)"], "판매", fact["F13"]["출처"]),
    ("IFR", f"Nearly {near}", "판매, 키 140cm 초과", fact["F13"]["교차 출처"]),
    ("Counterpoint", fact["F14"]["값(원문)"], "설치", fact["F14"]["출처"]),
    ("BofA", fact["F15"]["값(원문)"], "출하 추정", fact["F15"]["출처"]),
]
with open("humanoid_count.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["기관", "수량", "집계 대상", "출처"])
    w.writerows(count)

# Block 2: BOM 차트
bom = [("F27", "Optimus Gen 2, 중국 공급망 제외 가정"), ("F26", "Optimus Gen 2, 중국 공급망 포함"),
       ("F19", "중국산 휴머노이드, 2025년"), ("F20", "중국산 휴머노이드, 2030년 전망")]
num = lambda v: float(re.sub(r"[^\d.]", "", v))
top = max(num(fact[k]["값(원문)"]) for k, _ in bom)
bars = []
for k, name in bom:
    v = fact[k]["값(원문)"]
    label = v.replace("below ", "") + ("달러 미만" if v.startswith("below") else "달러")
    bars.append(f'<div class="row"><p class="name">{escape(name)}</p><div class="track"><span class="bar" style="width:{num(v) / top * 50:.1f}%"></span>'
                f'<span class="val">{label} [{fact[k]["출처"]}]</span></div></div>')
CHART = "".join(bars)
NOTE = "로봇과 추정 기관이 달라 막대끼리 직접 비교하지 않는다."
STYLE = """:root{--bg:#fbfaf7;--ink:#1f2530;--sub:#5d6470;--line:#dfdcd3;--bar:#2e5bab;--head:#1b2c5e}
@media (prefers-color-scheme:dark){:root{--bg:#16191f;--ink:#eceef2;--sub:#a4abb8;--line:#333945;--bar:#6f9be8;--head:#2b3f7a}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,"Malgun Gothic","Noto Sans KR",sans-serif}
main{max-width:800px;margin:0 auto;padding:32px 16px}h1{margin:4px 0 8px;font-size:clamp(26px,6vw,36px);line-height:1.3}h2{margin:36px 0 10px;font-size:21px}
.eyebrow,.note,.source{color:var(--sub);font-size:14px}.lead{margin:0 0 8px}table{width:100%;border-collapse:collapse;font-size:15px}th{background:var(--head);color:#fff;text-align:left}
th,td{padding:9px 10px;border:1px solid var(--line)}.row{margin:0 0 12px}.name{margin:0 0 3px;font-size:14px}.track{display:flex;align-items:center;gap:8px;min-height:30px}
.bar{display:block;height:24px;background:var(--bar);border-radius:0 4px 4px 0;flex:none}.val{white-space:nowrap;font-size:14px;font-weight:600}
.links{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 0;padding:0;list-style:none}.links a{display:inline-block;padding:9px 14px;border:1px solid var(--line);border-radius:6px;color:inherit}"""
Path("bom_chart.html").write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>BOM 차트</title><style>{STYLE}</style></head><body><main><h1>휴머노이드 BOM</h1>{CHART}<p class="note">{NOTE}</p></main></body></html>', encoding="utf-8")

# 대시보드 한 장
trs = "".join(f"<tr><td>{a}</td><td>{escape(b)} [{d}]</td><td>{c}</td></tr>" for a, b, c, d in count)
html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>로봇 밸류체인</title>
<style>{STYLE}</style>
</head>
<body>
<main>
<p class="eyebrow">자동차 부품사 재직자 강의</p>
<h1>로봇 밸류체인</h1>
<p class="lead">자동차 부품사는 로봇 밸류체인의 어느 단계에서 자사의 기술과 공급 역량으로 새 사업 기회를 만들 수 있는가?</p>
<ul class="links">
<li><a href="docs/Robot_Value_Chain_Textbook.pdf">교재 PDF</a></li>
<li><a href="docs/Robot_Value_Chain_Deck.pdf">강의 덱 PDF</a></li>
</ul>
<h2>휴머노이드 수량은 기관마다 다르다</h2>
<table><thead><tr><th>기관</th><th>2025년 수량</th><th>집계 대상</th></tr></thead><tbody>{trs}</tbody></table>
<h2>휴머노이드 BOM은 공급망과 시점에 따라 달라진다</h2>
{CHART}
<p class="note">{NOTE}</p>
<p class="source">기업 사례는 학습용이며 투자 권유가 아니다. 번호는 교재의 출처 표를 따른다.</p>
</main>
</body>
</html>
"""
Path("index.html").write_text(html, encoding="utf-8")

v = lambda value, block, d=None: {"value": value, "block": block, **({"decimals": d} if d is not None else {})}
expected = {"values": {
    "facts_total": v(len(rows), 0, 0),
    "facts_cross": v(state["교차확인"], 0, 0),
    "facts_diff": v(state["출처 간 불일치"], 0, 0),
    "facts_hold": v(state["보류"], 0, 0),
    "sources_total": v(sources, 0, 0),
    "humanoid_ifr_sales": v(count[0][1], 1),
    "humanoid_ifr_full": v(count[1][1], 1),
    "humanoid_counterpoint": v(count[2][1], 1),
    "humanoid_bofa": v(count[3][1], 1),
    "bom_excl_china": v(fact["F27"]["값(원문)"], 2),
    "bom_incl_china": v(fact["F26"]["값(원문)"], 2),
    "bom_china_2025": v(fact["F19"]["값(원문)"], 2),
    "bom_china_2030": v(fact["F20"]["값(원문)"], 2),
}}
Path("expected.json").write_text(json.dumps(expected, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(rows), dict(state), sources)
for c in count:
    print(c)
