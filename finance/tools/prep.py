"""prep.py <name>: sNAME.txt (## Label / text) -> sNAME.json с display-текстом и tts-текстом."""
import json, sys
import os
SP = os.environ.get("FIN_WORK", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "work")) + os.sep
n = sys.argv[1]
R = [("S and P T S X", "S&P/TSX"), ("S and P Dow Jones Indices", "S&P Dow Jones Indices"), ("S and P five hundred", "S&P 500"),
     ("A S X two hundred", "ASX 200"), ("A S X", "ASX"), ("F T S E one hundred", "FTSE 100"), ("I P O", "IPO"), ("E T Fs", "ETFs"), ("E T F", "ETF"),
     ("four oh one k", "401(k)"), ("an I R A", "an IRA"), ("I R A", "IRA"), ("I S A", "ISA"), ("T F S A", "TFSA"), ("R R S P", "RRSP"),
     ("seventeen ninety-two", "1792"), ("nineteen fifty-seven", "1957"), ("two thousand seven", "2007"), ("two thousand nine", "2009"),
     ("twenty fourteen", "2014"), ("nineteen seventy-six", "1976"), ("nineteen ninety-four", "1994"), ("nineteen sixty", "1960"), ("twenty twenty-two", "2022"), ("twenty twenty-five", "2025"), ("twenty twenty-six", "2026"), ("twenty twenty-eight", "2028"), ("twenty twenty", "2020"), ("A P Y", "APY"), ("annual credit report dot com", "AnnualCreditReport.com"), ("C P I", "CPI"), ("F D I C", "FDIC"), ("N C U A", "NCUA"), ("twenty twenty-six", "2026"), (" C D,", " CD,"), (" C D.", " CD."), (" C D ", " CD ")]
out = []
for blk in open(SP + f"s{n}.txt").read().strip().split("## ")[1:]:
    title, txt = blk.split("\n", 1); txt = " ".join(txt.split()); disp = txt
    for a, b in R: disp = disp.replace(a, b)
    out.append(dict(label=title, text=disp, tts=txt))
json.dump(out, open(SP + f"s{n}.json", "w"), ensure_ascii=False)
print(sum(len(o["tts"].split()) for o in out), "words")
