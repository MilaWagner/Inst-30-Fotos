# Ролик «When Can You Retire? Alex's plan» (разбор на герое, тема sun)
THEME = "sun"
LOOK = "finn"
SECTIONS = [
 {
  "label": "Meet Alex",
  "text": "Most people have no idea how much money they need to retire, so they either panic or ignore it. In the next few minutes, you'll work out your own retirement number, in five simple steps. Meet Alex. Alex is thirty-five, has a steady job, and keeps asking the same question: when can I actually retire? Most people answer with an age. But retirement isn't really an age. It's a number. Let's build Alex's plan together, using real rules from the US, the UK, Canada and Australia, and you can follow along with your own numbers. This is for education only, and it's not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "hook",
    "kicker": "Plan It",
    "text": "Most people have no idea how much they need to retire."
   },
   {
    "at": "In the next few minutes",
    "type": "hook",
    "kicker": "In this video",
    "text": "Work out your own retirement number in 5 steps."
   },
   {
    "at": "Meet Alex",
    "type": "ident",
    "series": "Plan It",
    "title": "When Can You Actually Retire?"
   },
   {
    "at": "Alex is thirty-five",
    "type": "say",
    "text": "Alex, 35: \"When can I actually retire?\"",
    "char": [
     "think",
     420,
     640,
     "sam"
    ]
   },
   {
    "at": "But retirement isn't",
    "type": "bignum",
    "head": "Retirement isn't an age",
    "num": "It's a number",
    "sub": "savings + pensions that cover your spending"
   },
   {
    "at": "Let's build Alex's plan",
    "type": "checklist",
    "head": "Alex's plan in 5 steps",
    "items": [
     "Yearly spending",
     "What pensions cover",
     "The target",
     "The timeline",
     "Stress test"
    ],
    "marks": [
     "Let's build",
     "Let's build",
     "using real rules",
     "using real rules",
     "you can follow"
    ]
   },
   {
    "at": "This is for education",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "Step 1: Spending",
  "text": "Step one: how much will Alex spend each year in retirement? Not earn. Spend. Alex looks at today's costs, takes out the things that will end, like commuting and saving for retirement itself, and adds a bit for travel and health. Alex lands on forty thousand dollars a year. Your number will be different, and that's the point: the plan starts with your life, not a magic figure.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "STEP 1",
    "text": "Spending",
    "pct": "per year"
   },
   {
    "at": "Alex looks at today's costs",
    "type": "twocol",
    "head": "Retirement spending",
    "step": 2.5,
    "cols": [
     [
      "Goes away",
      [
       "Commuting",
       "Saving for retirement"
      ],
      [
       112,
       120,
       138
      ]
     ],
     [
      "Goes up",
      [
       "Travel",
       "Health"
      ],
      [
       190,
       120,
       10
      ]
     ]
    ]
   },
   {
    "at": "Alex lands on",
    "type": "bignum",
    "head": "Alex's yearly spending",
    "num": "$40,000",
    "sub": "your number will be different"
   }
  ]
 },
 {
  "label": "Step 2: Pensions",
  "text": "Step two: what will pensions cover? State pensions reduce how much Alex needs to save. In the United States, Social Security's full retirement age is sixty-seven for anyone born in 1960 or later. In the United Kingdom, the State Pension age is rising from sixty-six to sixty-seven between 2026 and 2028. In Canada, the standard age for the Canada Pension Plan is sixty-five, but you can start anywhere from sixty to seventy. And in Australia, the Age Pension age is sixty-seven, while superannuation can usually be accessed from sixty. Rules change, so check your official government estimate. Alex's estimate says pensions will cover about fifteen thousand a year. So savings need to cover twenty-five thousand.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "STEP 2",
    "text": "Pensions",
    "pct": ""
   },
   {
    "at": "In the United States",
    "type": "countries",
    "head": "State pension ages",
    "rows": [
     [
      "United States",
      "Social Security: 67 (born 1960+)"
     ],
     [
      "United Kingdom",
      "State Pension: 66 → 67 (2026–2028)"
     ],
     [
      "Canada",
      "CPP: 65 (start 60–70)"
     ],
     [
      "Australia",
      "Age Pension 67 · super from 60"
     ]
    ],
    "marks": [
     "In the United States",
     "In the United Kingdom",
     "In Canada",
     "And in Australia"
    ]
   },
   {
    "at": "Alex's estimate says",
    "type": "bars",
    "head": "Alex's $40,000 a year",
    "step": 1.5,
    "rows": [
     [
      "Pensions cover",
      15000,
      "$15,000",
      [
       52,
       104,
       214
      ]
     ],
     [
      "Savings must cover",
      25000,
      "$25,000",
      [
       190,
       120,
       10
      ]
     ]
    ],
    "note": "Example numbers"
   }
  ]
 },
 {
  "label": "Step 3: The target",
  "text": "Step three: turn that into a target. Here's the simplest rule: multiply the yearly amount your savings must cover by twenty-five. Twenty-five thousand times twenty-five is six hundred and twenty-five thousand dollars. That's Alex's number. Where does twenty-five come from? In 1994, financial planner William Bengen studied historical US stock and bond returns. Withdrawing about four percent in the first year, then adjusting for inflation, lasted at least thirty years in every period he tested. Four percent is one twenty-fifth. But it's a rule of thumb, not a guarantee. For a much longer retirement, many planners suggest closer to three and a half percent, which means about twenty-eight or twenty-nine times spending.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "STEP 3",
    "text": "The target",
    "pct": ""
   },
   {
    "at": "Twenty-five thousand times",
    "type": "bignum",
    "head": "$25,000 × 25",
    "num": "$625,000",
    "sub": "Alex's number"
   },
   {
    "at": "In 1994",
    "type": "lines",
    "head": "William Bengen, 1994",
    "lines": [
     [
      "Withdraw ~4% in year one"
     ],
     [
      "Raise it with inflation each year"
     ],
     [
      "Lasted 30+ years in every US period tested"
     ]
    ],
    "step": 3.0
   },
   {
    "at": "But it's a rule of thumb",
    "type": "bars",
    "head": "Longer retirement? Many planners suggest",
    "step": 1.5,
    "rows": [
     [
      "4% rule (about 30 years)",
      25,
      "× 25",
      [
       190,
       120,
       10
      ]
     ],
     [
      "~3.5% (longer retirement)",
      28.6,
      "× 28–29",
      [
       222,
       160,
       36
      ]
     ]
    ],
    "note": "A rule of thumb, not a guarantee"
   }
  ]
 },
 {
  "label": "Step 4: The timeline",
  "text": "Step four: how long will it take? Alex is starting from zero. If Alex invests eight hundred dollars a month, and it grows five percent a year after inflation, it takes about twenty-nine years to reach six hundred and twenty-five thousand. If Alex finds a way to invest twelve hundred a month, it takes about twenty-three years. Four hundred dollars a month buys about six years of Alex's life. These are simplified examples, but they show where the real lever is: not income, but the share of income Alex saves and invests. In a simple model, saving ten percent of your income takes about fifty-two years. Twenty percent, about thirty-seven. Thirty percent, about twenty-eight. Fifty percent, about seventeen.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "STEP 4",
    "text": "The timeline",
    "pct": ""
   },
   {
    "at": "If Alex invests eight hundred",
    "type": "bars",
    "head": "Time to reach $625,000 (5% a year after inflation)",
    "step": 2.5,
    "rows": [
     [
      "$800 a month",
      29,
      "~29 years",
      [
       222,
       160,
       36
      ]
     ],
     [
      "$1,200 a month",
      23,
      "~23 years",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "note": "Simplified example"
   },
   {
    "at": "Four hundred dollars a month buys",
    "type": "say",
    "text": "$400 a month = about 6 years of Alex's life.",
    "char": [
     "happy",
     420,
     640,
     "sam"
    ]
   },
   {
    "at": "In a simple model",
    "type": "bars",
    "head": "Years to retire from zero, by savings rate",
    "step": 1.3,
    "rows": [
     [
      "Save 10%",
      52,
      "~52 yrs",
      [
       206,
       64,
       60
      ]
     ],
     [
      "Save 20%",
      37,
      "~37 yrs",
      [
       222,
       160,
       36
      ]
     ],
     [
      "Save 30%",
      28,
      "~28 yrs",
      [
       52,
       104,
       214
      ]
     ],
     [
      "Save 50%",
      17,
      "~17 yrs",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "compact": True,
    "note": "Assumes 5% a year after inflation, target = 25× spending"
   }
  ]
 },
 {
  "label": "Step 5: Stress test",
  "text": "Step five: stress-test the plan. Inflation means Alex's spending number will grow over time. Alex might live longer than expected. Health costs often rise with age. And if markets fall sharply right when Alex retires, withdrawing the same amount can shrink savings fast. That's why many retirees keep a few years of spending in safer assets, like cash or bonds. And it's why Alex's employer match matters so much: free money from an employer is one of the easiest ways to move the date closer.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "STEP 5",
    "text": "Stress test",
    "pct": ""
   },
   {
    "at": "Inflation means",
    "type": "checklist",
    "head": "What could break the plan",
    "items": [
     "Inflation",
     "Living longer",
     "Health costs",
     "A crash right at retirement"
    ],
    "marks": [
     "Inflation means",
     "Alex might live",
     "Health costs",
     "And if markets fall"
    ]
   },
   {
    "at": "That's why many retirees",
    "type": "say",
    "text": "Keep a few years of spending in cash or bonds.",
    "char": [
     "think",
     420,
     640,
     "rose"
    ]
   },
   {
    "at": "And it's why Alex's employer match",
    "type": "say",
    "text": "Get the full employer match. It's free money.",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Alex's plan",
  "text": "So here's Alex's plan. Spend forty thousand. Pensions cover fifteen. Target, six hundred and twenty-five thousand. Invest around twelve hundred a month, get the full employer match, and raise the savings rate with every pay rise. And if part-time work in the early years feels good, that softer landing makes the numbers much easier. Your plan will have different numbers, but the same five steps. Next on the channel: high-yield savings accounts, the best place for money you'll need soon. See you there.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Alex's plan",
    "lines": [
     [
      "Spend $40,000 · pensions $15,000"
     ],
     [
      "Target $625,000"
     ],
     [
      "Invest ~$1,200 a month + full match"
     ]
    ],
    "step": 2.5
   },
   {
    "at": "Your plan will have",
    "type": "takeaway",
    "head": "Your turn",
    "text": "Different numbers. Same five steps."
   },
   {
    "at": "Next on the channel",
    "type": "subscribe",
    "next": "High-yield savings accounts",
    "next_sub": "the best place for money you'll need soon",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
