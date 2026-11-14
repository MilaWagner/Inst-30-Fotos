# Ролик «Compound Interest Explained»
SECTIONS = [
 {
  "label": "Intro",
  "text": "Compound interest is often called the most powerful force in personal finance. It can quietly make you wealthy, or quietly keep you in debt. Today we'll see exactly how it works, why time matters more than almost anything else, and how it works against you when you borrow. This applies in the US, the UK, Canada and Australia. This video is for education only, and is not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "The most powerful force in personal finance?",
    "sub": "It can make you wealthy, or keep you in debt",
    "char": [
     "think",
     420,
     640
    ]
   },
   {
    "at": "Today we'll see",
    "type": "checklist",
    "head": "Today",
    "items": [
     "How compounding works",
     "Why time matters most",
     "How it works against you"
    ],
    "marks": [
     "exactly how it works",
     "why time matters",
     "how it works against"
    ]
   },
   {
    "at": "This applies in the US",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "Simple vs compound",
  "text": "Let's start with the difference. Simple interest is paid only on the money you put in. Compound interest is paid on your money, and on the interest you've already earned. Interest on interest. In the first year, the difference is tiny. But give it enough time, and it becomes enormous.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Simple vs compound",
    "step": 2.5,
    "cols": [
     [
      "Simple interest",
      [
       "Paid only on",
       "what you put in"
      ],
      [
       112,
       120,
       138
      ]
     ],
     [
      "Compound interest",
      [
       "Paid on your money",
       "and past interest"
      ],
      [
       36,
       156,
       92
      ]
     ]
    ]
   },
   {
    "at": "In the first year",
    "type": "say",
    "text": "Tiny at first. Enormous with time.",
    "char": [
     "point_right",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "An example",
  "text": "Say you invest ten thousand dollars, and it grows seven percent a year. After ten years, you'd have about nineteen thousand seven hundred. After twenty years, about thirty-eight thousand seven hundred. After thirty years, about seventy-six thousand. And after forty years, about one hundred and fifty thousand. With simple interest at the same rate, after forty years you'd have only thirty-eight thousand. Same money, same rate. The difference is compounding.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "$10,000 at 7% a year",
    "step": 2.2,
    "rows": [
     [
      "After 10 years",
      19672,
      "~$19,700",
      [
       52,
       104,
       214
      ]
     ],
     [
      "After 20 years",
      38697,
      "~$38,700",
      [
       52,
       104,
       214
      ]
     ],
     [
      "After 30 years",
      76123,
      "~$76,100",
      [
       52,
       104,
       214
      ]
     ],
     [
      "After 40 years",
      149745,
      "~$149,700",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "compact": True,
    "lw": 320,
    "note": "Compounded yearly. Example, not a promise."
   },
   {
    "at": "With simple interest",
    "type": "bars",
    "head": "40 years at 7%",
    "step": 1.5,
    "rows": [
     [
      "Simple interest",
      38000,
      "$38,000",
      [
       112,
       120,
       138
      ]
     ],
     [
      "Compound interest",
      149745,
      "~$149,700",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "note": "Same money, same rate"
   }
  ]
 },
 {
  "label": "The curve",
  "text": "Notice the pattern. In the first ten years, your money grew by under ten thousand. In the last ten years, by more than seventy thousand. That's the shape of compound growth: slow at first, then faster and faster. It's why so many people give up early. The best part happens at the end.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "Growth per decade ($10,000 at 7%)",
    "step": 2.0,
    "rows": [
     [
      "First 10 years",
      9672,
      "+$9,700",
      [
       112,
       120,
       138
      ]
     ],
     [
      "Last 10 years",
      73622,
      "+$73,600",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "note": "Slow at first, then faster and faster"
   },
   {
    "at": "It's why so many people",
    "type": "say",
    "text": "The best part happens at the end.",
    "sub": "Many people give up too early",
    "char": [
     "happy",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Rule of 72",
  "text": "Here's a quick way to estimate it: the rule of seventy-two. Divide seventy-two by your yearly return, and you get roughly how many years it takes your money to double. At seven percent, about ten years. At ten percent, about seven years. At two percent, about thirty-six years.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Rule of 72",
    "lines": [
     [
      "72 ÷ yearly return = years to double"
     ]
    ],
    "step": 1
   },
   {
    "at": "At seven percent",
    "type": "bars",
    "head": "Years for money to double",
    "step": 1.5,
    "rows": [
     [
      "At 10%",
      7.2,
      "~7 years",
      [
       36,
       156,
       92
      ]
     ],
     [
      "At 7%",
      10.3,
      "~10 years",
      [
       52,
       104,
       214
      ]
     ],
     [
      "At 2%",
      36,
      "~36 years",
      [
       112,
       120,
       138
      ]
     ]
    ],
    "note": "Rule of 72: an approximation"
   }
  ]
 },
 {
  "label": "Start early",
  "text": "Now let's see why starting early matters so much. Meet two investors. The first invests three hundred dollars a month from age twenty-five to thirty-five, then stops completely. That's thirty-six thousand dollars in total. The second waits, and invests three hundred dollars a month from thirty-five all the way to sixty-five. That's one hundred and eight thousand dollars, three times as much. Assume both earn seven percent a year. At sixty-five, the first investor has about four hundred and twenty-one thousand dollars. The second has about three hundred and sixty-six thousand. The early starter put in a third of the money, and still ends up with more.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Two investors · $300 a month · 7%",
    "step": 4.0,
    "cols": [
     [
      "Early starter",
      [
       "Age 25 to 35, then stops",
       "Puts in $36,000"
      ],
      [
       36,
       156,
       92
      ]
     ],
     [
      "Late starter",
      [
       "Age 35 to 65",
       "Puts in $108,000"
      ],
      [
       52,
       104,
       214
      ]
     ]
    ]
   },
   {
    "at": "At sixty-five",
    "type": "growth",
    "head": "$300 a month at 7% a year",
    "monthly": 300,
    "max": 450000,
    "lines": [
     [
      25,
      [
       36,
       156,
       92
      ],
      0.3,
      35
     ],
     [
      35,
      [
       52,
       104,
       214
      ],
      3.8
     ]
    ]
   },
   {
    "at": "The early starter put in",
    "type": "say",
    "text": "A third of the money. Still more at 65.",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Keep going",
  "text": "And if the first investor simply kept going, three hundred dollars a month from twenty-five all the way to sixty-five, they'd have about seven hundred and eighty-seven thousand dollars, from one hundred and forty-four thousand contributed. The rest is compounding.",
  "beats": [
   {
    "at": "^",
    "type": "growth",
    "head": "$300 a month at 7%, age 25 to 65",
    "monthly": 300,
    "max": 850000,
    "lines": [
     [
      25,
      [
       36,
       156,
       92
      ],
      0.3
     ]
    ],
    "contrib": 3.5,
    "contrib_v": 144000,
    "contrib_lab": "you put in $144k"
   }
  ]
 },
 {
  "label": "Three levers",
  "text": "So compounding has three levers. The amount you invest. The rate of return. And time. You can't control the market's returns, but you can control how much you invest, how much you pay in fees, and how early you start. And of the three, time is the one you can never get back.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Three levers",
    "items": [
     "How much you invest",
     "Rate of return",
     "Time"
    ],
    "marks": [
     "The amount",
     "The rate of return",
     "And time"
    ]
   },
   {
    "at": "And of the three",
    "type": "say",
    "text": "Time is the one you can never get back.",
    "char": [
     "point_right",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Fees compound too",
  "text": "That's why fees matter. A fee of one percent a year doesn't sound like much. But it's taken every year, from your whole balance, so it compounds against you. Over decades, a one percent difference in fees can cost you a large share of your final balance. Low-cost index funds keep more of the compounding for you.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "1% a year doesn't sound like much.",
    "sub": "But it's taken from your whole balance, every year",
    "char": [
     "worried",
     420,
     640
    ]
   },
   {
    "at": "Low-cost index funds",
    "type": "say",
    "text": "Low fees keep more compounding for you.",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Debt compounds too",
  "text": "Compounding also works against you. Credit card debt is the classic example. Interest is added to your balance, and then you pay interest on that interest. If you only make minimum payments on a high-rate card, the balance can take many years to pay off, and cost far more than you borrowed. That's why paying off high-interest debt is one of the best returns you can get.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Compounding works against you too.",
    "sub": "Credit card debt: interest on interest",
    "char": [
     "worried",
     420,
     640
    ]
   },
   {
    "at": "That's why paying off",
    "type": "bignum",
    "head": "Paying off high-interest debt",
    "num": "= a top return",
    "sub": "every dollar repaid stops compounding against you"
   }
  ]
 },
 {
  "label": "Make it work for you",
  "text": "So how do you make compounding work for you? Start as early as you can, even with small amounts. Invest regularly, automatically, every month. Reinvest your dividends and interest instead of spending them. Keep fees low. Pay off high-interest debt. And be patient. Don't interrupt the process by cashing out early.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Make it work for you",
    "items": [
     "Start early, even small",
     "Invest automatically every month",
     "Reinvest dividends and interest",
     "Keep fees low",
     "Pay off high-interest debt",
     "Be patient"
    ],
    "marks": [
     "Start as early",
     "Invest regularly",
     "Reinvest",
     "Keep fees",
     "Pay off",
     "And be patient"
    ]
   }
  ]
 },
 {
  "label": "Three myths",
  "text": "Let's clear up three myths. Myth one: you need a lot of money to start. You don't. Small amounts, invested early and regularly, can grow into large sums. Myth two: it's too late for me. The best time to start was years ago, the second best time is now. Myth three: compounding means guaranteed growth. Investment returns go up and down. Compounding works over long periods, not every single year.",
  "beats": [
   {
    "at": "^",
    "type": "myth",
    "n": 1,
    "myth": "You need a lot of money to start",
    "fact": "Small amounts, invested early and regularly, can grow large."
   },
   {
    "at": "Myth two",
    "type": "myth",
    "n": 2,
    "myth": "It's too late for me",
    "fact": "The second best time to start is now."
   },
   {
    "at": "Myth three",
    "type": "myth",
    "n": 3,
    "myth": "Compounding means guaranteed growth",
    "fact": "Returns go up and down. It works over long periods."
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. Compound interest is interest on interest. Growth is slow at first, then speeds up. The rule of seventy-two tells you roughly how fast money doubles. Starting early can beat investing more later. Fees and debt compound against you. So start early, invest regularly, keep fees low, and be patient. If this helped, subscribe. See you in the next video.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "items": [
     "Interest on interest",
     "Slow at first, then faster",
     "Rule of 72",
     "Starting early beats investing more later",
     "Fees and debt compound against you"
    ],
    "marks": [
     "Compound interest is",
     "Growth is slow",
     "The rule",
     "Starting early",
     "Fees and debt"
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
