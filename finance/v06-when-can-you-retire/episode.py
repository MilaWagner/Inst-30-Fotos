# Ролик «When Can You Actually Retire?»
SECTIONS = [
 {
  "label": "Intro",
  "text": "When can you actually retire? Most people answer with an age. Sixty-five. Sixty-seven. But the real answer isn't an age at all. It's a number. Once your savings and pensions can cover your spending for the rest of your life, you can retire, whether you're forty-five or seventy. Today, we'll work out how to find your number, what the famous four percent rule says, how state pensions fit in across the US, UK, Canada and Australia, and what you can do to get there sooner. This video is for education only. It's not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "When can you actually retire?",
    "sub": "Most people answer with an age",
    "char": [
     "think",
     420,
     640
    ]
   },
   {
    "at": "But the real answer",
    "type": "say",
    "text": "It's not an age. It's a number.",
    "sub": "When savings and pensions cover your spending for life",
    "char": [
     "point_right",
     420,
     640
    ]
   },
   {
    "at": "Today, we'll work out",
    "type": "checklist",
    "head": "Today",
    "items": [
     "Find your number",
     "The 4% rule",
     "State pensions in 4 countries",
     "How to get there sooner"
    ],
    "marks": [
     "how to find",
     "the famous four",
     "how state pensions",
     "what you can do"
    ]
   },
   {
    "at": "This video is for education",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "Your number",
  "text": "Let's start with your number. The simplest way to estimate it is this: take how much you expect to spend each year in retirement, and multiply it by twenty-five. If you plan to spend forty thousand dollars a year, that's about one million dollars. That sounds huge. But here's the good news: you probably won't need to cover all of it from savings. If a state pension covers fifteen thousand a year, your savings only need to cover twenty-five thousand. Twenty-five thousand times twenty-five is six hundred and twenty-five thousand dollars. Still a big number, but a lot more reachable.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Your retirement number",
    "lines": [
     [
      "Yearly spending × 25"
     ]
    ],
    "step": 1
   },
   {
    "at": "If you plan to spend",
    "type": "bignum",
    "head": "$40,000 a year × 25",
    "num": "$1,000,000",
    "sub": "if savings had to cover everything"
   },
   {
    "at": "But here's the good news",
    "type": "bars",
    "head": "If a pension covers $15,000 a year",
    "step": 2.0,
    "rows": [
     [
      "Savings cover everything",
      1000000,
      "$1,000,000",
      [
       112,
       120,
       138
      ]
     ],
     [
      "Savings cover $25,000 a year",
      625000,
      "$625,000",
      [
       16,
       122,
       96
      ]
     ]
    ],
    "note": "Example numbers"
   }
  ]
 },
 {
  "label": "The four percent rule",
  "text": "Where does twenty-five come from? It comes from the four percent rule. In 1994, a financial planner named William Bengen studied historical US stock and bond returns. He found that if retirees withdrew about four percent of their savings in the first year, and then adjusted that amount for inflation each year, their money lasted at least thirty years in every period he tested. Four percent is one twenty-fifth. So twenty-five times your spending is the same idea, turned around.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Where does 25 come from?",
    "sub": "The 4% rule",
    "char": [
     "think",
     420,
     640
    ]
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
    "step": 3.5
   },
   {
    "at": "Four percent is one",
    "type": "bignum",
    "head": "4% = 1/25",
    "num": "× 25",
    "sub": "the same rule, turned around"
   }
  ]
 },
 {
  "label": "Limits of the rule",
  "text": "But the four percent rule is a rule of thumb, not a guarantee. It was based on US history, and on retirements of about thirty years. If you retire early, say at forty-five, your money may need to last fifty years, and many planners suggest a lower rate, closer to three and a half percent. That means about twenty-eight or twenty-nine times your spending. And real life isn't a spreadsheet. Many retirees adjust their spending in bad years, which makes their plan much safer.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "A rule of thumb, not a guarantee.",
    "sub": "Based on US history and ~30-year retirements",
    "char": [
     "shrug",
     420,
     640
    ]
   },
   {
    "at": "If you retire early",
    "type": "bars",
    "head": "Retiring early? Many planners suggest",
    "step": 1.5,
    "rows": [
     [
      "4% rule (about 30 years)",
      25,
      "× 25",
      [
       16,
       122,
       96
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
    "note": "Many retirees also adjust spending in bad years"
   }
  ]
 },
 {
  "label": "Savings rate",
  "text": "So what decides how fast you get there? Not your income. Your savings rate: the share of your income you save and invest. Here's a simple model. Start from zero, assume investments grow five percent a year after inflation, and retire when you have twenty-five times your yearly spending. Save ten percent of your income, and it takes about fifty-two years. Save twenty percent, about thirty-seven years. Thirty percent, about twenty-eight years. And fifty percent, about seventeen years. Saving more helps twice: you invest more, and you get used to living on less.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "It's not your income. It's your savings rate.",
    "char": [
     "point_right",
     420,
     640
    ]
   },
   {
    "at": "Save ten percent",
    "type": "bars",
    "head": "Years to retire from zero (simple model)",
    "step": 1.2,
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
    "note": "Assumes 5% a year after inflation, target = 25× spending"
   },
   {
    "at": "Saving more helps twice",
    "type": "say",
    "text": "Saving more helps twice.",
    "sub": "You invest more, and you need less",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "State pensions",
  "text": "Now let's add state pensions, because they reduce how much you need to save. In the United States, Social Security's full retirement age is sixty-seven for anyone born in 1960 or later, and you can claim a reduced amount from sixty-two. In the United Kingdom, the State Pension age is rising from sixty-six to sixty-seven between 2020-six and 2020-eight. In Canada, the standard age for the Canada Pension Plan is sixty-five, but you can start anywhere from sixty to seventy. And in Australia, the Age Pension age is sixty-seven, while you can usually access your superannuation from sixty. Rules change, so check your official government estimate.",
  "beats": [
   {
    "at": "^",
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
   }
  ]
 },
 {
  "label": "Workplace pensions",
  "text": "On top of state pensions, there are workplace and personal accounts: 401(k) plans and IRAs in the US, workplace pensions and ISAs in the UK, RRSPs and TFSAs in Canada, and superannuation in Australia. If your employer adds money to your account, that's part of your pay. Contributing at least enough to get the full employer match is one of the easiest ways to move your retirement date closer.",
  "beats": [
   {
    "at": "^",
    "type": "countries",
    "marks": [
     "On top of state",
     "workplace pensions and",
     "RRSPs and TFSAs",
     "and superannuation"
    ]
   },
   {
    "at": "If your employer adds",
    "type": "say",
    "text": "Employer match is part of your pay.",
    "sub": "Contribute enough to get all of it",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "An example",
  "text": "Let's put it together with an example. Say you want to spend forty thousand dollars a year in retirement, and you expect pensions to cover fifteen thousand of it. Your savings need to cover twenty-five thousand a year, so your target is about six hundred and twenty-five thousand dollars. Starting from zero, if you invest eight hundred dollars a month and it grows five percent a year after inflation, you'd reach that target in about twenty-nine years. Raise that to twelve hundred dollars a month, and it takes about twenty-three years. Six years of your life, from four hundred dollars a month. These are simplified examples, but they show how much control you actually have.",
  "beats": [
   {
    "at": "^",
    "type": "bignum",
    "head": "Example target",
    "num": "$625,000",
    "sub": "$25,000 a year from savings × 25"
   },
   {
    "at": "Starting from zero",
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
    "at": "Six years of your life",
    "type": "say",
    "text": "$400 a month = about 6 years of your life.",
    "char": [
     "happy",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Risks",
  "text": "There are a few risks to plan for. Inflation: prices tend to rise over time, so your spending number grows too. Living longer than expected: many people underestimate how long their money needs to last. Health costs, which often rise with age. And bad timing: if markets fall sharply just as you retire and you keep withdrawing the same amount, your savings can shrink fast. That's why many retirees keep some money in safer assets, like cash or bonds, to cover a few years of spending.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Risks to plan for",
    "items": [
     "Inflation",
     "Living longer than expected",
     "Health costs",
     "Bad market timing at the start"
    ],
    "marks": [
     "Inflation:",
     "Living longer",
     "Health costs",
     "And bad timing"
    ]
   },
   {
    "at": "That's why many retirees",
    "type": "say",
    "text": "Keep a few years of spending in safer assets.",
    "sub": "Cash or bonds",
    "char": [
     "think",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Retire sooner",
  "text": "So how do you retire sooner? Raise your savings rate a little every year, especially when you get a raise. Keep your biggest fixed costs, like housing and cars, under control. Invest in low-cost, diversified funds instead of leaving savings in cash for decades. Use tax-advantaged accounts and employer matches. And consider a softer landing: many people move to part-time work or a lower-stress job before they stop completely, which makes the numbers much easier.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Retire sooner",
    "items": [
     "Raise your savings rate every year",
     "Control housing and car costs",
     "Invest in low-cost diversified funds",
     "Use tax-advantaged accounts and matches",
     "Consider a softer landing: part-time"
    ],
    "marks": [
     "Raise your savings",
     "Keep your biggest",
     "Invest in low-cost",
     "Use tax",
     "And consider"
    ]
   }
  ]
 },
 {
  "label": "Three myths",
  "text": "Let's clear up three myths. Myth one: everyone needs at least a million dollars. Your number depends on your spending and your pensions, not on a magic figure. Myth two: you'll automatically spend much less in retirement. Some costs go down, but travel, hobbies and health can push others up. Plan with real numbers. Myth three: retirement is all or nothing. Part-time work, flexible jobs, or a small business can bridge the gap and reduce how much you need to save.",
  "beats": [
   {
    "at": "^",
    "type": "myth",
    "n": 1,
    "myth": "Everyone needs at least a million",
    "fact": "Your number depends on your spending and pensions, not a magic figure."
   },
   {
    "at": "Myth two",
    "type": "myth",
    "n": 2,
    "myth": "You'll spend much less in retirement",
    "fact": "Some costs fall, but travel, hobbies and health can push others up."
   },
   {
    "at": "Myth three",
    "type": "myth",
    "n": 3,
    "myth": "Retirement is all or nothing",
    "fact": "Part-time work or a small business can bridge the gap."
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. Retirement is a number, not an age. Estimate your yearly spending and multiply by twenty-five, or about twenty-eight to twenty-nine if you retire early. Subtract what state and workplace pensions will cover. Your savings rate decides how fast you get there. Plan for inflation, a long life, and bad market timing. If this helped, subscribe. Next, we'll look at high-yield savings accounts: where to keep your emergency fund and short-term cash. See you there.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "items": [
     "Retirement is a number, not an age",
     "Spending × 25 (× 28–29 if early)",
     "Subtract pensions",
     "Savings rate decides the speed",
     "Plan for inflation, long life, timing"
    ],
    "marks": [
     "Retirement is a number",
     "Estimate your",
     "Subtract",
     "Your savings rate",
     "Plan for inflation"
    ]
   },
   {
    "at": "If this helped",
    "type": "subscribe",
    "next": "High-yield savings accounts",
    "next_sub": "where to keep your emergency fund",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
