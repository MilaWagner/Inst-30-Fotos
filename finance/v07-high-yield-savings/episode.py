# Ролик «Where Should $10,000 Live?» (Head to Head, тема blush)
THEME = "blush"
LOOK = "finn_casual"
SECTIONS = [
 {
  "label": "The question",
  "text": "If your savings sit in a regular bank account, they may be earning almost nothing. In the next few minutes, you'll find out where ten thousand dollars should actually live, and how to earn up to ten times more interest without taking more risk. Here's the setup. Five places for your cash, judged on three things: the rate, the safety, and how fast you can get your money. This is about the US, for education only, and it's not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "hook",
    "kicker": "Head to Head",
    "text": "Your savings may be earning almost nothing."
   },
   {
    "at": "In the next few minutes",
    "type": "hook",
    "kicker": "In this video",
    "text": "Where $10,000 should live, for up to 10× the interest."
   },
   {
    "at": "Here's the setup",
    "type": "ident",
    "series": "Head to Head",
    "title": "Where Should $10,000 Live?"
   },
   {
    "at": "Five places for your cash",
    "type": "checklist",
    "head": "5 contenders, 3 tests",
    "items": [
     "Rate",
     "Safety",
     "Access"
    ],
    "marks": [
     "the rate",
     "the safety",
     "how fast"
    ]
   },
   {
    "at": "This is about the US",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "Contender 1",
  "text": "Contender one: the regular bank savings account. As of late 2026, the average US savings account pays well under one percent a year, according to the FDIC. On ten thousand dollars, that's roughly forty dollars a year. Safety is excellent: deposits at insured banks are protected up to two hundred and fifty thousand dollars per depositor, per bank, for each ownership category. Access is instant. Great safety, great access, terrible rate.",
  "beats": [
   {
    "at": "^",
    "type": "score",
    "tag": "CONTENDER 1",
    "name": "Regular savings",
    "color": [
     112,
     120,
     138
    ],
    "rows": [
     [
      "Rate",
      1,
      "well under 1%"
     ],
     [
      "Safety",
      5,
      "FDIC insured"
     ],
     [
      "Access",
      5,
      "instant"
     ]
    ],
    "step": 1.2
   },
   {
    "at": "On ten thousand dollars",
    "type": "bignum",
    "head": "$10,000 for a year",
    "num": "~$40",
    "sub": "at a typical bank savings rate (FDIC national average)"
   },
   {
    "at": "Safety is excellent",
    "type": "bignum",
    "head": "FDIC deposit insurance",
    "num": "$250,000",
    "sub": "per depositor, per bank, per ownership category"
   }
  ]
 },
 {
  "label": "Contender 2",
  "text": "Contender two: the high-yield savings account. Same idea, usually at an online bank or a credit union, but some of them pay around four percent, according to comparison sites. On ten thousand dollars, that's about four hundred dollars a year instead of forty. Is it safe? At an FDIC insured bank, or an NCUA insured credit union, it gets the same protection. Access is good, but moving money to your main account can take one to three business days.",
  "beats": [
   {
    "at": "^",
    "type": "score",
    "tag": "CONTENDER 2",
    "name": "High-yield savings",
    "color": [
     36,
     156,
     92
    ],
    "rows": [
     [
      "Rate",
      4,
      "around 4% at some banks"
     ],
     [
      "Safety",
      5,
      "FDIC / NCUA insured"
     ],
     [
      "Access",
      4,
      "1–3 days to transfer"
     ]
    ],
    "step": 1.2
   },
   {
    "at": "On ten thousand dollars",
    "type": "bars",
    "head": "$10,000 for one year",
    "step": 1.5,
    "rows": [
     [
      "Regular savings",
      40,
      "~$40",
      [
       112,
       120,
       138
      ]
     ],
     [
      "High-yield savings",
      400,
      "~$400",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "note": "Rates change often. Sources: FDIC, NerdWallet, Bankrate (late 2026)"
   }
  ]
 },
 {
  "label": "Contender 3",
  "text": "Contender three: the certificate of deposit, or CD. You lock in a fixed rate for a set term, like six months or a year. That's its superpower: if rates fall, yours doesn't. But your money is tied up, and you may pay a penalty if you withdraw early. Great for money with a known date, bad for an emergency fund.",
  "beats": [
   {
    "at": "^",
    "type": "score",
    "tag": "CONTENDER 3",
    "name": "Certificate of deposit",
    "color": [
     52,
     104,
     214
    ],
    "rows": [
     [
      "Rate",
      4,
      "fixed for the term"
     ],
     [
      "Safety",
      5,
      "FDIC insured"
     ],
     [
      "Access",
      1,
      "locked, early penalty"
     ]
    ],
    "step": 1.2
   },
   {
    "at": "Great for money with a known date",
    "type": "say",
    "text": "Known date? CD. Emergency fund? No.",
    "char": [
     "think",
     420,
     640,
     "maya"
    ]
   }
  ]
 },
 {
  "label": "Contender 4",
  "text": "Contender four: the money market fund. It's an investment fund, usually very low risk, often paying a rate similar to the best savings accounts. But here's the catch many people miss: it's not FDIC insured. Don't confuse it with a money market account at a bank, which is insured.",
  "beats": [
   {
    "at": "^",
    "type": "score",
    "tag": "CONTENDER 4",
    "name": "Money market fund",
    "color": [
     222,
     160,
     36
    ],
    "rows": [
     [
      "Rate",
      4,
      "similar to top savings"
     ],
     [
      "Safety",
      3,
      "low risk, NOT FDIC"
     ],
     [
      "Access",
      4,
      "usually quick"
     ]
    ],
    "step": 1.2
   },
   {
    "at": "Don't confuse it",
    "type": "twocol",
    "head": "Similar names, different safety",
    "step": 2.0,
    "cols": [
     [
      "Money market ACCOUNT",
      [
       "At a bank",
       "FDIC insured"
      ],
      [
       36,
       156,
       92
      ]
     ],
     [
      "Money market FUND",
      [
       "An investment fund",
       "NOT FDIC insured"
      ],
      [
       206,
       64,
       60
      ]
     ]
    ]
   }
  ]
 },
 {
  "label": "Contender 5",
  "text": "Contender five: Treasury bills, short-term loans to the US government. Their interest is exempt from state and local income tax, which can matter if you live in a high-tax state. But buying them takes a bit more effort, and your money is committed until they mature.",
  "beats": [
   {
    "at": "^",
    "type": "score",
    "tag": "CONTENDER 5",
    "name": "Treasury bills",
    "color": [
     112,
     78,
     186
    ],
    "rows": [
     [
      "Rate",
      4,
      "short-term US govt"
     ],
     [
      "Safety",
      5,
      "backed by US govt"
     ],
     [
      "Access",
      2,
      "held to maturity"
     ]
    ],
    "step": 1.2
   },
   {
    "at": "Their interest is exempt",
    "type": "say",
    "text": "No state or local income tax on the interest.",
    "sub": "Helpful in high-tax states",
    "char": [
     "point_right",
     420,
     640,
     "sam"
    ]
   }
  ]
 },
 {
  "label": "The fine print",
  "text": "Before we pick a winner, the fine print that trips people up. High-yield rates are variable. They usually move with the Federal Reserve, so four percent today can be three percent next year. Watch for promotional rates that drop after a few months, minimum balances, monthly fees, and conditions like direct deposit. And interest from savings is taxable, usually as ordinary income.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "The fine print",
    "items": [
     "Rates are variable (they follow the Fed)",
     "Promo rates that drop",
     "Minimums, fees, conditions",
     "Interest is taxable"
    ],
    "marks": [
     "High-yield rates are variable",
     "Watch for promotional",
     "minimum balances",
     "And interest"
    ]
   }
  ]
 },
 {
  "label": "The verdict",
  "text": "So, the verdict. For an emergency fund and money you might need soon, the high-yield savings account wins: strong rate, insured, easy access. A CD wins for money with a fixed date. T-bills can win in high-tax states. The regular savings account loses, because the same safety is available for far more interest. And inflation is the hidden opponent: at under one percent, your cash loses buying power every year.",
  "beats": [
   {
    "at": "^",
    "type": "countries",
    "head": "The verdict",
    "rows": [
     [
      "Emergency fund",
      "High-yield savings ✓"
     ],
     [
      "Money with a fixed date",
      "CD"
     ],
     [
      "High-tax state",
      "Consider T-bills"
     ],
     [
      "Regular savings",
      "Same safety, far less"
     ]
    ],
    "marks": [
     "For an emergency fund",
     "A CD wins",
     "T-bills can win",
     "The regular savings"
    ]
   },
   {
    "at": "And inflation is the hidden opponent",
    "type": "say",
    "text": "Inflation is the hidden opponent.",
    "sub": "Under 1% loses buying power every year",
    "char": [
     "worried",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Your move",
  "text": "Your move takes about ten minutes. Compare a few insured banks, check the APY, fees and minimums, open the account, link it to your checking, and set up an automatic transfer every payday. Name it Emergency Fund, so you're less tempted to spend it. Next on the channel: is whole life insurance worth it? See you there.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Your 10-minute move",
    "items": [
     "Compare insured banks",
     "Check APY, fees, minimums",
     "Open + link to checking",
     "Auto-transfer every payday",
     "Name it Emergency Fund"
    ],
    "marks": [
     "Compare a few",
     "check the APY",
     "open the account",
     "set up an automatic",
     "Name it"
    ]
   },
   {
    "at": "Next on the channel",
    "type": "subscribe",
    "next": "Is whole life insurance worth it?",
    "next_sub": "what it costs and who it's for",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
