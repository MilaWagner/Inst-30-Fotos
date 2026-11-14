# Ролик «Average Net Worth by Age (US, Fed SCF 2025)»
SECTIONS = [
 {
  "label": "Intro",
  "text": "How does your net worth compare with people your age? Today we'll look at real numbers from the Federal Reserve's Survey of Consumer Finances, the most detailed survey of American household wealth. The latest edition, for 2025, was released in October 2026. We'll see the typical net worth for every age group, why the average is so misleading, and what actually moves your number. This video uses US data, is for education only, and is not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "How does your net worth compare?",
    "sub": "Real numbers from the Federal Reserve",
    "char": [
     "think",
     420,
     640
    ]
   },
   {
    "at": "The latest edition",
    "type": "bignum",
    "head": "Survey of Consumer Finances",
    "num": "2025",
    "sub": "released October 2026 · US households"
   },
   {
    "at": "We'll see the typical",
    "type": "checklist",
    "head": "Today",
    "items": [
     "Net worth for every age group",
     "Why the average misleads",
     "What moves your number"
    ],
    "marks": [
     "We'll see the typical",
     "why the average",
     "what actually moves"
    ]
   },
   {
    "at": "This video uses US data",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "What net worth is",
  "text": "First, what is net worth? It's simple: everything you own, minus everything you owe. Your savings, investments, retirement accounts, the value of your home and car. Minus your mortgage, student loans, car loans and credit card debt. If you owe more than you own, your net worth is negative, and that's very common early in life.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Net worth",
    "lines": [
     [
      "What you own − what you owe"
     ]
    ],
    "step": 1
   },
   {
    "at": "Your savings",
    "type": "twocol",
    "head": "Net worth",
    "step": 2.5,
    "cols": [
     [
      "What you own",
      [
       "Savings & investments",
       "Retirement accounts",
       "Home & car"
      ],
      [
       36,
       156,
       92
      ]
     ],
     [
      "What you owe",
      [
       "Mortgage",
       "Student & car loans",
       "Credit card debt"
      ],
      [
       206,
       64,
       60
      ]
     ]
    ]
   },
   {
    "at": "If you owe more",
    "type": "say",
    "text": "Negative net worth is common early in life.",
    "char": [
     "shrug",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Median vs average",
  "text": "Before we look at the numbers, one key idea: median versus average. The median is the household right in the middle: half have more, half have less. The average, or mean, adds up all the wealth and divides it equally. And because a small number of very wealthy households pull the average way up, the average is much higher than what a typical family has. For all US families in 2025, the median net worth was about two hundred and sixteen thousand dollars. The average was about one point two three million. That's more than five times higher. So when you compare yourself, use the median.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Median vs average",
    "step": 2.5,
    "cols": [
     [
      "Median",
      [
       "The household in the middle",
       "Half have more, half less"
      ],
      [
       52,
       104,
       214
      ]
     ],
     [
      "Average (mean)",
      [
       "Total wealth ÷ households",
       "Pulled up by the very rich"
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
    "at": "For all US families",
    "type": "bars",
    "head": "All US families, 2025",
    "step": 2.5,
    "rows": [
     [
      "Median",
      216,
      "$216K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "Average",
      1232,
      "$1.23M",
      [
       222,
       160,
       36
      ]
     ]
    ],
    "note": "Source: Federal Reserve, Survey of Consumer Finances 2025 (2025 dollars)"
   },
   {
    "at": "So when you compare",
    "type": "say",
    "text": "Compare yourself with the median.",
    "char": [
     "point_right",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Under 35",
  "text": "Let's go age by age, using median net worth. Families where the head of household is under thirty-five had a median net worth of about thirty-three thousand dollars. That's lower than in 2022, when it was about forty-three thousand in today's dollars. Many people at this age are paying off student loans, renting, and just starting to save. If you're here and your number is small or even negative, you're not behind. You're early.",
  "beats": [
   {
    "at": "^",
    "type": "bignum",
    "head": "Median net worth · under 35",
    "num": "$33,000",
    "sub": "2022: about $43,000 (in 2025 dollars)",
    "src": "Source: Federal Reserve, Survey of Consumer Finances 2025 (2025 dollars)"
   },
   {
    "at": "Many people at this age",
    "type": "say",
    "text": "Small or negative? You're not behind. You're early.",
    "sub": "Student loans, renting, just starting to save",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "35 to 44",
  "text": "From thirty-five to forty-four, the median jumps to about one hundred and fifty-six thousand dollars. This is when many people buy a home, earn more, and their retirement accounts start to grow. Home equity and retirement savings become the two biggest pieces of wealth for a typical family.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "Median net worth by age",
    "step": 1.0,
    "rows": [
     [
      "Under 35",
      33,
      "$33K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "35–44",
      156,
      "$156K",
      [
       52,
       104,
       214
      ]
     ]
    ],
    "shown": 1,
    "compact": True,
    "max": 505,
    "note": "Source: Federal Reserve, Survey of Consumer Finances 2025 (2025 dollars)"
   },
   {
    "at": "Home equity",
    "type": "say",
    "text": "Home equity + retirement savings",
    "sub": "the two biggest pieces of a typical family's wealth",
    "char": [
     "point_right",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "45 to 54",
  "text": "From forty-five to fifty-four, the median is about two hundred and fifty-five thousand dollars. Incomes are often at their peak, and years of compounding start to show. But this is also when college costs and supporting family can slow things down.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "Median net worth by age",
    "step": 1.0,
    "rows": [
     [
      "Under 35",
      33,
      "$33K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "35–44",
      156,
      "$156K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "45–54",
      255,
      "$255K",
      [
       52,
       104,
       214
      ]
     ]
    ],
    "shown": 2,
    "compact": True,
    "max": 505,
    "note": "Source: Federal Reserve, Survey of Consumer Finances 2025 (2025 dollars)"
   }
  ]
 },
 {
  "label": "55 to 64",
  "text": "From fifty-five to sixty-four, the median rises to about four hundred and eleven thousand dollars. This is the last stretch before retirement for many people, and it's when catch-up contributions to retirement accounts are allowed.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "Median net worth by age",
    "step": 1.0,
    "rows": [
     [
      "Under 35",
      33,
      "$33K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "35–44",
      156,
      "$156K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "45–54",
      255,
      "$255K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "55–64",
      411,
      "$411K",
      [
       52,
       104,
       214
      ]
     ]
    ],
    "shown": 3,
    "compact": True,
    "max": 505,
    "note": "Source: Federal Reserve, Survey of Consumer Finances 2025 (2025 dollars)"
   },
   {
    "at": "it's when catch-up",
    "type": "say",
    "text": "From 50: catch-up contributions.",
    "sub": "Extra room in retirement accounts",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "65 and older",
  "text": "From sixty-five to seventy-four, the median is about four hundred and thirty-two thousand dollars. And for seventy-five and older, about five hundred and five thousand. Many older households own their home outright, which is a big part of their net worth. But remember, this wealth has to last for the rest of their lives.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "Median net worth by age",
    "step": 5.0,
    "rows": [
     [
      "Under 35",
      33,
      "$33K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "35–44",
      156,
      "$156K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "45–54",
      255,
      "$255K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "55–64",
      411,
      "$411K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "65–74",
      432,
      "$432K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "75+",
      505,
      "$505K",
      [
       52,
       104,
       214
      ]
     ]
    ],
    "shown": 4,
    "compact": True,
    "max": 505,
    "note": "Source: Federal Reserve, Survey of Consumer Finances 2025 (2025 dollars)"
   },
   {
    "at": "But remember",
    "type": "say",
    "text": "This wealth has to last for life.",
    "char": [
     "think",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "The average by age",
  "text": "Now look at the averages by age, and you'll see the gap. Under thirty-five, the average is about one hundred and thirty-six thousand dollars, four times the median. From fifty-five to sixty-four, the average is about one point eight seven million, more than four times the median. If you've ever seen headlines saying the average American in their fifties has over a million dollars, this is why. It's the very top pulling the number up.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "Median vs average, 2025",
    "step": 2.0,
    "rows": [
     [
      "Under 35 · median",
      33,
      "$33K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "Under 35 · average",
      136,
      "$136K",
      [
       222,
       160,
       36
      ]
     ],
     [
      "55–64 · median",
      411,
      "$411K",
      [
       52,
       104,
       214
      ]
     ],
     [
      "55–64 · average",
      1871,
      "$1.87M",
      [
       222,
       160,
       36
      ]
     ]
    ],
    "note": "Source: Federal Reserve, Survey of Consumer Finances 2025 (2025 dollars)"
   },
   {
    "at": "If you've ever seen headlines",
    "type": "say",
    "text": "Millionaire averages? The very top pulls them up.",
    "char": [
     "shrug",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Owners vs renters",
  "text": "One of the biggest differences isn't age at all. It's housing. In 2025, the median net worth of homeowners was about four hundred and fifty-nine thousand dollars. For renters, it was about eleven thousand. Part of that is age and income, because older, higher-earning people are more likely to own. But a paid-down mortgage also works like forced saving, month after month.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "Median net worth, 2025",
    "step": 2.5,
    "rows": [
     [
      "Homeowners",
      459,
      "$459K",
      [
       36,
       156,
       92
      ]
     ],
     [
      "Renters",
      10.55,
      "$11K",
      [
       112,
       120,
       138
      ]
     ]
    ],
    "note": "Source: Federal Reserve, Survey of Consumer Finances 2025 (2025 dollars)"
   },
   {
    "at": "Part of that is age",
    "type": "say",
    "text": "A mortgage works like forced saving.",
    "sub": "Partly also age and income",
    "char": [
     "think",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "What moves your number",
  "text": "So what actually moves your net worth? Four things. Your savings rate: how much of your income you keep. Paying down high-interest debt, because every dollar of credit card debt you clear raises your net worth by a dollar. Investing consistently in low-cost, diversified funds, and using retirement accounts and employer matches. And time: the earlier you start, the more compounding can work for you.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "What moves your net worth",
    "items": [
     "Your savings rate",
     "Paying down high-interest debt",
     "Investing consistently, low-cost funds",
     "Time and compounding"
    ],
    "marks": [
     "Your savings rate",
     "Paying down",
     "Investing consistently",
     "And time"
    ]
   }
  ]
 },
 {
  "label": "How to track it",
  "text": "Tracking your own net worth is easy. Once or twice a year, list everything you own and everything you owe, and subtract. Don't worry about the exact value of your car or furniture. What matters is the trend. If your number goes up every year, you're moving in the right direction, whatever your age.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Track it once or twice a year",
    "items": [
     "List what you own",
     "List what you owe",
     "Subtract",
     "Watch the trend"
    ],
    "marks": [
     "list everything you own",
     "and everything you owe",
     "and subtract",
     "What matters is the trend"
    ]
   }
  ]
 },
 {
  "label": "Three myths",
  "text": "Let's clear up three myths. Myth one: the average tells you what's normal. It doesn't. The median does. Myth two: if you're below the median, you're failing. These are snapshots of different people, and everyone starts from a different place. Myth three: a high income means a high net worth. Not necessarily. What you keep and invest matters more than what you earn.",
  "beats": [
   {
    "at": "^",
    "type": "myth",
    "n": 1,
    "myth": "The average tells you what's normal",
    "fact": "It doesn't. The median does."
   },
   {
    "at": "Myth two",
    "type": "myth",
    "n": 2,
    "myth": "Below the median means you're failing",
    "fact": "Everyone starts from a different place."
   },
   {
    "at": "Myth three",
    "type": "myth",
    "n": 3,
    "myth": "High income means high net worth",
    "fact": "What you keep and invest matters more than what you earn."
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. Net worth is what you own minus what you owe. Use the median, not the average. In 2025, the median was about thirty-three thousand under thirty-five, one hundred and fifty-six thousand from thirty-five to forty-four, two hundred and fifty-five thousand from forty-five to fifty-four, and about four hundred and eleven thousand from fifty-five to sixty-four. Focus on your own trend, your savings rate, and your debt. If this helped, subscribe. See you in the next video.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "items": [
     "Own − owe = net worth",
     "Use the median, not the average",
     "Under 35: $33K · 35–44: $156K",
     "45–54: $255K · 55–64: $411K",
     "Focus on your own trend"
    ],
    "marks": [
     "Net worth is",
     "Use the median",
     "In 2025",
     "two hundred and fifty-five",
     "Focus on your own"
    ]
   },
   {
    "at": "If this helped",
    "type": "subscribe",
    "next": "More money explained",
    "next_sub": "new video every 3 days",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
