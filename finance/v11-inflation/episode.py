# Ролик «How Inflation Works (US, UK, Canada, Australia)»
SECTIONS = [
 {
  "label": "Intro",
  "text": "Why does everything keep getting more expensive? Groceries, rent, gas, insurance. The answer is inflation. Today we'll look at what inflation really is, how it's measured, what causes it, why central banks actually want a little of it, and most importantly, how to protect your money from it, with examples from the US, the UK, Canada and Australia. This video is for education only, and is not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Why does everything keep getting more expensive?",
    "sub": "Groceries, rent, gas, insurance",
    "char": [
     "worried",
     420,
     640
    ]
   },
   {
    "at": "Today we'll look",
    "type": "checklist",
    "head": "Today",
    "items": [
     "What inflation really is",
     "How it's measured",
     "What causes it",
     "How to protect your money"
    ],
    "marks": [
     "what inflation really",
     "how it's measured",
     "what causes it",
     "how to protect"
    ]
   },
   {
    "at": "This video is for education",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "What inflation is",
  "text": "Inflation is the general rise in prices over time. When there's inflation, each dollar or pound buys a little less than before. That's why it's often described as a loss of purchasing power. A little inflation each year doesn't feel like much. But over many years, it adds up.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Inflation",
    "lines": [
     [
      "The general rise in prices over time"
     ]
    ],
    "step": 1
   },
   {
    "at": "When there's inflation",
    "type": "say",
    "text": "Each dollar or pound buys a little less.",
    "sub": "A loss of purchasing power",
    "char": [
     "point_right",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "How it's measured",
  "text": "Inflation is usually measured with the consumer price index, or CPI. Statisticians track the prices of a big basket of things people buy: food, housing, energy, transport, clothing, healthcare, and more. Then they compare the cost of that basket with a year earlier. In the US, it's published by the Bureau of Labor Statistics. In the UK, by the Office for National Statistics. In Canada, by Statistics Canada. And in Australia, by the Australian Bureau of Statistics.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Consumer Price Index (CPI)",
    "lines": [
     [
      "A basket of what people buy"
     ],
     [
      "food · housing · energy · transport"
     ],
     [
      "Cost now vs a year earlier"
     ]
    ],
    "step": 3.0
   },
   {
    "at": "In the US, it's published",
    "type": "countries",
    "head": "Who measures it",
    "rows": [
     [
      "United States",
      "Bureau of Labor Statistics"
     ],
     [
      "United Kingdom",
      "Office for National Statistics"
     ],
     [
      "Canada",
      "Statistics Canada"
     ],
     [
      "Australia",
      "Australian Bureau of Statistics"
     ]
    ],
    "marks": [
     "In the US",
     "In the UK",
     "In Canada",
     "And in Australia"
    ]
   }
  ]
 },
 {
  "label": "Recent numbers",
  "text": "Here's how big it can get. In 2022, inflation hit its highest levels in decades. In the US, CPI inflation peaked at nine point one percent in June 2022. In the UK, it reached eleven point one percent in October 2022. In Canada, eight point one percent in June 2022. And in Australia, seven point eight percent over the year to the December quarter of 2022. And it's not gone away. In the US, the Bureau of Labor Statistics reported inflation of three point seven percent over the twelve months to September 2026.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "2022 inflation peaks (CPI, year over year)",
    "step": 2.5,
    "rows": [
     [
      "United States · Jun 2022",
      9.1,
      "9.1%",
      [
       52,
       104,
       214
      ]
     ],
     [
      "United Kingdom · Oct 2022",
      11.1,
      "11.1%",
      [
       206,
       64,
       60
      ]
     ],
     [
      "Canada · Jun 2022",
      8.1,
      "8.1%",
      [
       222,
       160,
       36
      ]
     ],
     [
      "Australia · Dec qtr 2022",
      7.8,
      "7.8%",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "compact": True,
    "note": "Sources: BLS, ONS, Statistics Canada, ABS"
   },
   {
    "at": "And it's not gone away",
    "type": "bignum",
    "head": "US inflation, 12 months to Sept 2026",
    "num": "3.7%",
    "sub": "consumer price index, all items",
    "src": "Source: Bureau of Labor Statistics"
   }
  ]
 },
 {
  "label": "What causes it",
  "text": "So what causes inflation? There are two classic causes. First, demand-pull inflation: when people and businesses want to buy more than the economy can produce, prices rise. That can happen when money is cheap, or after big government spending. Second, cost-push inflation: when the cost of making things goes up, like energy, raw materials or wages, businesses pass those costs on. And there's a third force: expectations. If everyone expects prices to rise, workers ask for higher pay and businesses raise prices, which can keep inflation going.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Two classic causes",
    "step": 2.5,
    "cols": [
     [
      "Demand-pull",
      [
       "People want to buy more",
       "than the economy can make"
      ],
      [
       52,
       104,
       214
      ]
     ],
     [
      "Cost-push",
      [
       "Energy, materials, wages",
       "costs passed on"
      ],
      [
       222,
       160,
       36
      ]
     ]
    ]
   },
   {
    "at": "And there's a third force",
    "type": "say",
    "text": "Third force: expectations.",
    "sub": "Expect higher prices, and they can keep rising",
    "char": [
     "think",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "The target",
  "text": "Here's something surprising: central banks don't want zero inflation. They aim for a small, steady amount. The Federal Reserve targets two percent. The Bank of England targets two percent. The Bank of Canada targets two percent, the middle of a one to three percent range. And the Reserve Bank of Australia aims for two to three percent. A little inflation encourages spending and investment, and gives central banks room to cut rates in a downturn. Deflation, falling prices, can be much more dangerous, because people delay spending, and the economy can stall.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Central banks don't want zero inflation.",
    "char": [
     "shrug",
     420,
     640
    ]
   },
   {
    "at": "The Federal Reserve",
    "type": "countries",
    "head": "Inflation targets",
    "rows": [
     [
      "Federal Reserve",
      "2%"
     ],
     [
      "Bank of England",
      "2%"
     ],
     [
      "Bank of Canada",
      "2% (1–3% range)"
     ],
     [
      "Reserve Bank of Australia",
      "2–3%"
     ]
    ],
    "marks": [
     "The Federal Reserve",
     "The Bank of England",
     "The Bank of Canada",
     "And the Reserve Bank"
    ]
   },
   {
    "at": "Deflation",
    "type": "say",
    "text": "Deflation can be more dangerous.",
    "sub": "People delay spending, and the economy can stall",
    "char": [
     "worried",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Interest rates",
  "text": "When inflation runs too hot, central banks usually raise interest rates. Higher rates make borrowing more expensive, so people and businesses spend less, and that cools prices down. That's why mortgage rates and savings rates rose so much after 2022. When inflation falls back toward the target, central banks can cut rates again.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Inflation too hot?",
    "lines": [
     [
      "Central banks raise interest rates"
     ],
     [
      "Borrowing costs more"
     ],
     [
      "Spending cools, prices cool"
     ]
    ],
    "step": 3.0
   },
   {
    "at": "When inflation falls back",
    "type": "say",
    "text": "Inflation back near target? Rates can fall.",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "What it does to cash",
  "text": "Now, what does inflation do to your money? Let's take one hundred dollars. If prices rise three percent a year, after ten years that hundred dollars will buy only about what seventy-four dollars buys today. At four percent, about sixty-eight dollars. And here's a quick rule, the rule of seventy-two. Divide seventy-two by the inflation rate to see roughly how many years it takes for prices to double. At three percent, prices double in about twenty-four years.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "What $100 buys after 10 years",
    "step": 2.0,
    "rows": [
     [
      "No inflation",
      100,
      "$100",
      [
       112,
       120,
       138
      ]
     ],
     [
      "3% a year",
      74,
      "~$74",
      [
       222,
       160,
       36
      ]
     ],
     [
      "4% a year",
      68,
      "~$68",
      [
       206,
       64,
       60
      ]
     ]
    ],
    "note": "Example calculation, in today's money"
   },
   {
    "at": "And here's a quick rule",
    "type": "bignum",
    "head": "Rule of 72",
    "num": "72 ÷ 3 = 24",
    "sub": "years for prices to double at 3% inflation"
   }
  ]
 },
 {
  "label": "Winners and losers",
  "text": "Inflation has winners and losers. Savers with cash earning less than inflation lose purchasing power. People on fixed incomes can fall behind. But borrowers with fixed-rate debt, like a fixed mortgage, can benefit, because they repay with money that's worth less than when they borrowed it. And wages often lag behind prices at first, which is why high inflation feels so painful.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Winners and losers",
    "step": 2.5,
    "cols": [
     [
      "Can lose",
      [
       "Cash savers",
       "Fixed incomes",
       "Wages lagging prices"
      ],
      [
       206,
       64,
       60
      ]
     ],
     [
      "Can gain",
      [
       "Fixed-rate borrowers",
       "e.g. a fixed mortgage"
      ],
      [
       36,
       156,
       92
      ]
     ]
    ]
   }
  ]
 },
 {
  "label": "How to protect yourself",
  "text": "So how do you protect yourself? First, don't leave too much cash in an account that pays almost nothing. Keep an emergency fund in a high-yield savings account. Second, for long-term money, invest in diversified assets, like a low-cost index fund. Over long periods, stocks have historically grown faster than inflation, though not every year. Third, consider inflation-linked bonds, like TIPS in the US, or index-linked gilts in the UK. Fourth, invest in yourself: skills that raise your income are one of the best hedges. And fifth, avoid high-interest debt, especially when rates are rising.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Protect yourself",
    "items": [
     "Don't leave too much in low-rate cash",
     "Invest long-term money in index funds",
     "Inflation-linked bonds (TIPS, index-linked gilts)",
     "Invest in your skills and income",
     "Avoid high-interest debt"
    ],
    "marks": [
     "First, don't",
     "Second, for long",
     "Third, consider",
     "Fourth, invest",
     "And fifth"
    ]
   }
  ]
 },
 {
  "label": "Three myths",
  "text": "Let's clear up three myths. Myth one: inflation means prices will go back down. Usually they don't. Lower inflation means prices rise more slowly, not that they fall. Myth two: cash is always safe. It's safe from market swings, but not from inflation. Myth three: gold is the perfect inflation hedge. Gold has sometimes protected against inflation, but its price can swing a lot, and it pays no income.",
  "beats": [
   {
    "at": "^",
    "type": "myth",
    "n": 1,
    "myth": "Prices will go back down",
    "fact": "Lower inflation means prices rise more slowly, not that they fall."
   },
   {
    "at": "Myth two",
    "type": "myth",
    "n": 2,
    "myth": "Cash is always safe",
    "fact": "Safe from market swings, not from inflation."
   },
   {
    "at": "Myth three",
    "type": "myth",
    "n": 3,
    "myth": "Gold is the perfect inflation hedge",
    "fact": "Sometimes it helped, but it swings a lot and pays no income."
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. Inflation is the general rise in prices, measured with the consumer price index. It's caused by strong demand, rising costs, and expectations. Central banks aim for about two percent, and raise rates when it runs too hot. Over time, inflation quietly eats into cash. To protect yourself, keep only what you need in cash, invest for the long term, and grow your income. If this helped, subscribe. Next, we'll look at the 401(k), and how to get the most from it. See you there.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "items": [
     "Inflation = rising prices, measured by CPI",
     "Demand, costs, expectations",
     "Targets around 2%",
     "It quietly eats cash",
     "Invest long-term, grow your income"
    ],
    "marks": [
     "Inflation is the",
     "It's caused",
     "Central banks aim",
     "Over time",
     "To protect"
    ]
   },
   {
    "at": "If this helped",
    "type": "subscribe",
    "next": "The 401(k) explained",
    "next_sub": "how to get the most from it",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
