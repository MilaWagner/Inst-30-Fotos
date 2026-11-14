# Ролик «Rent vs Buy: The Real Math (US)»
SECTIONS = [
 {
  "label": "Intro",
  "text": "Is renting really throwing money away? It's one of the most common pieces of money advice, and it's only half True. Today we'll look at the real math of renting versus buying a home in the US: what a mortgage really costs, the costs people forget, a simple rule of thumb to compare, and when buying makes sense. This video uses US data, is for education only, and is not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Is renting really throwing money away?",
    "sub": "Only half True",
    "char": [
     "think",
     420,
     640
    ]
   },
   {
    "at": "Today we'll look",
    "type": "checklist",
    "head": "Today",
    "items": [
     "What a mortgage really costs",
     "The costs people forget",
     "A simple rule of thumb",
     "When buying makes sense"
    ],
    "marks": [
     "what a mortgage",
     "the costs people",
     "a simple rule",
     "when buying makes"
    ]
   },
   {
    "at": "This video uses US data",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "The numbers today",
  "text": "Let's start with today's numbers. According to the National Association of Realtors, the median price of an existing home sold in the US in September 2026 was about four hundred and seventeen thousand dollars. And according to Freddie Mac, the average thirty-year fixed mortgage rate in early November 2026 was about seven point two percent. Those two numbers shape everything that follows.",
  "beats": [
   {
    "at": "^",
    "type": "bignum",
    "head": "Median existing-home price, Sept 2026",
    "num": "$417,500",
    "sub": "US",
    "src": "Source: National Association of Realtors"
   },
   {
    "at": "And according to Freddie Mac",
    "type": "bignum",
    "head": "Average 30-year fixed mortgage rate",
    "num": "~7.2%",
    "sub": "early November 2026 (7.18%)",
    "src": "Source: Freddie Mac PMMS"
   }
  ]
 },
 {
  "label": "The mortgage",
  "text": "Say you buy that four hundred and seventeen thousand dollar home, put twenty percent down, about eighty-three thousand dollars, and borrow the rest, about three hundred and thirty-four thousand, at seven point two percent for thirty years. Your monthly payment for principal and interest is about two thousand two hundred and sixty dollars. But here's the part people miss. In the first month, about two thousand dollars of that is interest. Only around two hundred and sixty five dollars actually pays down your loan.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Example purchase",
    "lines": [
     [
      "Home: ~$417,000"
     ],
     [
      "20% down: ~$83,000"
     ],
     [
      "Loan: ~$334,000 at 7.2%, 30 years"
     ]
    ],
    "step": 3.0
   },
   {
    "at": "Your monthly payment",
    "type": "bignum",
    "head": "Principal + interest",
    "num": "~$2,260/mo",
    "sub": "before taxes, insurance and maintenance"
   },
   {
    "at": "In the first month",
    "type": "bars",
    "head": "First month's payment",
    "step": 2.0,
    "rows": [
     [
      "Interest",
      1998,
      "~$2,000",
      [
       206,
       64,
       60
      ]
     ],
     [
      "Pays down the loan",
      265,
      "~$265",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "note": "Example calculation"
   }
  ]
 },
 {
  "label": "Unrecoverable costs",
  "text": "That's the key idea: unrecoverable costs. When you rent, your rent is an unrecoverable cost. You pay it, and it's gone. But owning has unrecoverable costs too. Mortgage interest. Property taxes. Homeowners insurance. Maintenance and repairs. And the opportunity cost of your down payment, money that could have been invested elsewhere. Principal is different: that part builds your equity. So the fair comparison isn't rent versus your mortgage payment. It's rent versus the unrecoverable costs of owning.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "The key idea: unrecoverable costs.",
    "char": [
     "point_right",
     420,
     640
    ]
   },
   {
    "at": "But owning has",
    "type": "twocol",
    "head": "Unrecoverable costs",
    "step": 2.5,
    "cols": [
     [
      "Renting",
      [
       "Rent"
      ],
      [
       52,
       104,
       214
      ]
     ],
     [
      "Owning",
      [
       "Mortgage interest",
       "Property taxes",
       "Insurance",
       "Maintenance",
       "Opportunity cost"
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
    "at": "So the fair comparison",
    "type": "say",
    "text": "Compare rent with unrecoverable costs.",
    "sub": "Not with the full mortgage payment",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Maintenance",
  "text": "Maintenance is the cost people underestimate most. A common rule of thumb is to budget about one percent of your home's value every year for maintenance and repairs, and more for older homes. On a four hundred thousand dollar home, that's about four thousand dollars a year. Some years you'll spend less. Then the roof or the furnace needs replacing, and you'll spend much more.",
  "beats": [
   {
    "at": "^",
    "type": "bignum",
    "head": "Common rule of thumb",
    "num": "~1% a year",
    "sub": "of the home's value for maintenance and repairs"
   },
   {
    "at": "On a four hundred",
    "type": "bignum",
    "head": "$400,000 home",
    "num": "~$4,000/yr",
    "sub": "more for older homes"
   },
   {
    "at": "Then the roof",
    "type": "say",
    "text": "Then the roof needs replacing.",
    "char": [
     "worried",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Buying and selling",
  "text": "Then there are the costs of buying and selling. Closing costs when you buy are often around two to five percent of the loan amount, according to Freddie Mac. And when you sell, agent fees and other costs can take several percent of the sale price. That's why buying and selling a home within a few years often loses money, even if prices rise a little.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Costs of buying and selling",
    "items": [
     "Closing costs: ~2–5% of the loan amount",
     "Selling: agent fees and other costs, several %"
    ],
    "marks": [
     "Closing costs",
     "And when you sell"
    ]
   },
   {
    "at": "That's why buying",
    "type": "say",
    "text": "Buy and sell within a few years? Often a loss.",
    "char": [
     "worried",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "The five percent rule",
  "text": "Here's a simple rule of thumb to compare. It's often called the five percent rule. Multiply the home's price by five percent, and divide by twelve. That's a rough estimate of the monthly unrecoverable cost of owning: about one percent for property taxes, about one percent for maintenance, and about three percent for the cost of your money. For a four hundred and seventeen thousand dollar home, that's about one thousand seven hundred and forty dollars a month. If you can rent a similar home for less than that, renting may be the better deal financially. If rent is much higher, buying may win. It's a rough guide, not a precise answer, and with mortgage rates above seven percent, the True cost can be even higher.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "The 5% rule",
    "lines": [
     [
      "Home price × 5% ÷ 12"
     ]
    ],
    "step": 1
   },
   {
    "at": "about one percent",
    "type": "bars",
    "head": "Unrecoverable cost of owning (rule of thumb)",
    "step": 1.5,
    "rows": [
     [
      "Property taxes",
      1,
      "~1%",
      [
       222,
       160,
       36
      ]
     ],
     [
      "Maintenance",
      1,
      "~1%",
      [
       222,
       160,
       36
      ]
     ],
     [
      "Cost of your money",
      3,
      "~3%",
      [
       222,
       160,
       36
      ]
     ]
    ],
    "note": "Varies by state, home and interest rates"
   },
   {
    "at": "For a four hundred and seventeen",
    "type": "bignum",
    "head": "$417,000 × 5% ÷ 12",
    "num": "~$1,740/mo",
    "sub": "rent less than this? Renting may win financially"
   },
   {
    "at": "It's a rough guide",
    "type": "say",
    "text": "A rough guide, not a precise answer.",
    "sub": "With rates above 7%, the True cost can be higher",
    "char": [
     "shrug",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Renting the smart way",
  "text": "Renting only works out if you invest the difference. If owning would cost you more each month, a renter who invests that money, and the money that would have been the down payment, can build similar wealth over time. But if you rent and spend the difference, you'll likely end up with less. Owning forces you to save through your mortgage. Renting requires you to do it on purpose.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Renting works if you invest the difference.",
    "char": [
     "point_right",
     420,
     640
    ]
   },
   {
    "at": "Owning forces you",
    "type": "twocol",
    "head": "Saving",
    "step": 2.5,
    "cols": [
     [
      "Owning",
      [
       "Mortgage forces you to save"
      ],
      [
       222,
       160,
       36
      ]
     ],
     [
      "Renting",
      [
       "You must save on purpose"
      ],
      [
       52,
       104,
       214
      ]
     ]
    ]
   }
  ]
 },
 {
  "label": "When buying makes sense",
  "text": "So when does buying make sense? When you plan to stay at least five years or more, so the buying and selling costs are spread out. When your income is stable, and you have an emergency fund on top of your down payment. When the total monthly cost, including taxes, insurance and maintenance, fits comfortably in your budget. And when owning fits your life: stability, schools, and freedom to make the place your own.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Buying can make sense if",
    "items": [
     "You'll stay 5+ years",
     "Stable income + emergency fund",
     "Total cost fits your budget",
     "It fits your life"
    ],
    "marks": [
     "When you plan",
     "When your income",
     "When the total",
     "And when owning"
    ]
   }
  ]
 },
 {
  "label": "When renting makes sense",
  "text": "And when does renting make sense? When you might move for work in the next few years. When local prices are very high compared with rents. When you don't yet have a solid emergency fund. And when you value flexibility, and not having to deal with repairs. Renting isn't failure. It's a choice, and sometimes it's the smarter one.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Renting can make sense if",
    "items": [
     "You might move soon",
     "Prices are high vs rents",
     "No solid emergency fund yet",
     "You value flexibility"
    ],
    "marks": [
     "When you might",
     "When local prices",
     "When you don't",
     "And when you value"
    ]
   },
   {
    "at": "Renting isn't failure",
    "type": "say",
    "text": "Renting isn't failure. It's a choice.",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Three myths",
  "text": "Let's clear up three myths. Myth one: renting is throwing money away. Owning has unrecoverable costs too, especially interest. Myth two: a home is always a great investment. Over the long run, home prices have tended to rise, but not always, and not everywhere, and the costs eat into your return. Myth three: you need to buy as soon as possible. Buying before you're ready can cost far more than waiting.",
  "beats": [
   {
    "at": "^",
    "type": "myth",
    "n": 1,
    "myth": "Renting is throwing money away",
    "fact": "Owning has unrecoverable costs too, especially interest."
   },
   {
    "at": "Myth two",
    "type": "myth",
    "n": 2,
    "myth": "A home is always a great investment",
    "fact": "Prices have tended to rise, but not always, not everywhere."
   },
   {
    "at": "Myth three",
    "type": "myth",
    "n": 3,
    "myth": "Buy as soon as possible",
    "fact": "Buying before you're ready can cost far more than waiting."
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. Compare rent with the unrecoverable costs of owning, not with the full mortgage payment. Budget for taxes, insurance and maintenance. Remember the costs of buying and selling. Use the five percent rule as a quick check. And if you rent, invest the difference. If this helped, subscribe. See you in the next video.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "items": [
     "Rent vs unrecoverable costs",
     "Budget taxes, insurance, maintenance",
     "Buying and selling costs",
     "5% rule as a quick check",
     "Renting? Invest the difference"
    ],
    "marks": [
     "Compare rent",
     "Budget for",
     "Remember the costs",
     "Use the five",
     "And if you rent"
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
