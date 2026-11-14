# Ролик «How Tax Brackets Really Work (US)»
SECTIONS = [
 {
  "label": "Intro",
  "text": "Have you ever heard someone say: \"I don't want a raise, it'll push me into a higher tax bracket\"? It's one of the most common money myths, and it's wrong. Today we'll see how US federal income tax brackets really work, the difference between your marginal and your effective tax rate, and a simple example with real 2026 numbers. This video is about US federal income tax, is for education only, and is not tax advice.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "\"I don't want a raise. It'll push me into a higher bracket.\"",
    "char": [
     "worried",
     420,
     640
    ]
   },
   {
    "at": "It's one of the most common",
    "type": "say",
    "text": "One of the most common money myths.",
    "sub": "And it's wrong",
    "char": [
     "shrug",
     420,
     640
    ]
   },
   {
    "at": "Today we'll see",
    "type": "checklist",
    "head": "Today",
    "items": [
     "How brackets really work",
     "Marginal vs effective rate",
     "A real 2026 example"
    ],
    "marks": [
     "how US federal",
     "the difference",
     "a simple example"
    ]
   },
   {
    "at": "This video is about US",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "Progressive tax",
  "text": "The US federal income tax is progressive. That means higher slices of income are taxed at higher rates. There are seven rates: ten, twelve, twenty-two, twenty-four, thirty-two, thirty-five, and thirty-seven percent. Each rate applies only to the slice of income inside its bracket, not to all of your income.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Progressive tax",
    "lines": [
     [
      "Higher slices of income, higher rates"
     ]
    ],
    "step": 1
   },
   {
    "at": "There are seven rates",
    "type": "lines",
    "head": "7 federal rates",
    "lines": [
     [
      "10% · 12% · 22% · 24%"
     ],
     [
      "32% · 35% · 37%"
     ]
    ],
    "step": 1.5
   },
   {
    "at": "Each rate applies only",
    "type": "say",
    "text": "Each rate applies only to its own slice.",
    "sub": "Not to all of your income",
    "char": [
     "point_right",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Taxable income",
  "text": "First, an important step: brackets apply to your taxable income, not your salary. For most people, taxable income is your income minus the standard deduction. For 2026, the standard deduction is sixteen thousand one hundred dollars for a single filer, and thirty-two thousand two hundred for married couples filing jointly, according to the IRS.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Taxable income",
    "lines": [
     [
      "Income − standard deduction"
     ]
    ],
    "step": 1
   },
   {
    "at": "For 2026",
    "type": "bars",
    "head": "2026 standard deduction",
    "step": 1.5,
    "rows": [
     [
      "Single",
      16100,
      "$16,100",
      [
       52,
       104,
       214
      ]
     ],
     [
      "Married filing jointly",
      32200,
      "$32,200",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "note": "Source: IRS"
   }
  ]
 },
 {
  "label": "The brackets",
  "text": "Here are the first three brackets for a single filer in 2026. The first twelve thousand four hundred dollars of taxable income is taxed at ten percent. Income from there up to fifty thousand four hundred is taxed at twelve percent. And income from there up to one hundred and five thousand seven hundred is taxed at twenty-two percent. Higher brackets work the same way.",
  "beats": [
   {
    "at": "^",
    "type": "bars",
    "head": "2026 brackets, single filer (taxable income)",
    "step": 3.0,
    "rows": [
     [
      "10%",
      12400,
      "$0 – $12,400",
      [
       52,
       104,
       214
      ]
     ],
     [
      "12%",
      38000,
      "$12,400 – $50,400",
      [
       222,
       160,
       36
      ]
     ],
     [
      "22%",
      55300,
      "$50,400 – $105,700",
      [
       206,
       64,
       60
      ]
     ]
    ],
    "compact": True,
    "lw": 140,
    "note": "Source: IRS. Higher brackets: 24%, 32%, 35%, 37%."
   }
  ]
 },
 {
  "label": "An example",
  "text": "Let's work through an example. Say you're single and earn eighty thousand dollars. Subtract the standard deduction of sixteen thousand one hundred, and your taxable income is sixty-three thousand nine hundred. The first twelve thousand four hundred is taxed at ten percent: one thousand two hundred and forty dollars. The next thirty-eight thousand, up to fifty thousand four hundred, is taxed at twelve percent: four thousand five hundred and sixty dollars. And the last thirteen thousand five hundred is taxed at twenty-two percent: 2009 hundred and seventy dollars. Your total federal income tax is about eight thousand seven hundred and seventy dollars.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Single · earns $80,000",
    "lines": [
     [
      "$80,000 − $16,100 = $63,900 taxable"
     ]
    ],
    "step": 1
   },
   {
    "at": "The first twelve thousand",
    "type": "bars",
    "head": "Tax on $63,900 of taxable income",
    "step": 1.0,
    "rows": [
     [
      "$12,400 at 10%",
      1240,
      "$1,240",
      [
       52,
       104,
       214
      ]
     ],
     [
      "$38,000 at 12%",
      4560,
      "$4,560",
      [
       222,
       160,
       36
      ]
     ],
     [
      "$13,500 at 22%",
      2970,
      "$2,970",
      [
       206,
       64,
       60
      ]
     ]
    ],
    "compact": True,
    "lw": 360,
    "note": "2026 single brackets, standard deduction only"
   },
   {
    "at": "Your total federal income tax",
    "type": "bignum",
    "head": "Total federal income tax",
    "num": "~$8,770",
    "sub": "on $80,000 of income"
   }
  ]
 },
 {
  "label": "Marginal vs effective",
  "text": "Now the key idea. Your marginal tax rate is the rate on your last dollar of income. In this example, that's twenty-two percent. But your effective tax rate is your total tax divided by your income. Eight thousand seven hundred and seventy dollars on eighty thousand is about eleven percent. So even though you're \"in the twenty-two percent bracket\", you pay about eleven percent of your income in federal income tax.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Two different rates",
    "step": 2.5,
    "cols": [
     [
      "Marginal rate",
      [
       "Rate on your last dollar",
       "Here: 22%"
      ],
      [
       206,
       64,
       60
      ]
     ],
     [
      "Effective rate",
      [
       "Total tax ÷ income",
       "Here: ~11%"
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
    "at": "So even though",
    "type": "bignum",
    "head": "\"In the 22% bracket\"",
    "num": "~11%",
    "sub": "of income actually paid in federal income tax"
   }
  ]
 },
 {
  "label": "The raise myth",
  "text": "So, does a raise ever cost you money because of a higher bracket? No. If a raise pushes you into the next bracket, only the extra dollars above the line are taxed at the higher rate. Everything below stays taxed exactly as before. You always keep more money after a raise, not less. There are a few special cases where benefits or credits phase out with income, but the bracket system itself never makes a raise lose you money.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Can a raise cost you money? No.",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   },
   {
    "at": "If a raise pushes you",
    "type": "lines",
    "head": "Crossing into a new bracket",
    "lines": [
     [
      "Only the extra dollars pay the higher rate"
     ],
     [
      "Everything below stays the same"
     ]
    ],
    "step": 2.5
   },
   {
    "at": "There are a few special cases",
    "type": "say",
    "text": "Some benefits and credits phase out with income.",
    "sub": "But brackets alone never make a raise lose you money",
    "char": [
     "think",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Deductions and credits",
  "text": "Two more terms. A deduction lowers your taxable income. So a deduction is worth your marginal rate: a one thousand dollar deduction saves you two hundred and twenty dollars if you're in the twenty-two percent bracket. A tax credit is different. It reduces your tax bill dollar for dollar. A one thousand dollar credit saves you one thousand dollars. That's why credits are usually more valuable.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Deduction vs credit",
    "step": 3.0,
    "cols": [
     [
      "$1,000 deduction",
      [
       "Lowers taxable income",
       "Saves $220 at 22%"
      ],
      [
       52,
       104,
       214
      ]
     ],
     [
      "$1,000 credit",
      [
       "Lowers your tax bill",
       "Saves $1,000"
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
  "label": "Lower your taxable income",
  "text": "How can you legally lower your taxable income? Contributions to a traditional 401(k) or a traditional IRA, if you're eligible, are usually subtracted from your taxable income. So is money you put into a health savings account, if you have an eligible health plan. And because these come off the top, they save you tax at your marginal rate.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Lower your taxable income",
    "items": [
     "Traditional 401(k)",
     "Traditional IRA (if eligible)",
     "Health savings account (HSA)"
    ],
    "marks": [
     "traditional 401(k)",
     "traditional IRA",
     "health savings"
    ]
   },
   {
    "at": "And because these come off",
    "type": "say",
    "text": "They save tax at your marginal rate.",
    "char": [
     "happy",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Not the whole picture",
  "text": "Remember, federal income tax isn't the only tax. Most workers also pay Social Security and Medicare taxes on their wages, and many states and some cities have their own income taxes with different rules. So your total tax rate depends on where you live, too.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Other taxes",
    "items": [
     "Social Security tax",
     "Medicare tax",
     "State and some city income taxes"
    ],
    "marks": [
     "Social Security",
     "Medicare",
     "many states"
    ]
   }
  ]
 },
 {
  "label": "Three myths",
  "text": "Let's clear up three myths. Myth one: a raise can push you into a higher bracket and lower your take-home pay. It can't. Only the extra income is taxed at the higher rate. Myth two: your tax bracket is the percentage of your income you pay. That's your marginal rate. Your effective rate is usually much lower. Myth three: a big refund is a bonus. A refund is just your own money coming back, because too much was withheld during the year.",
  "beats": [
   {
    "at": "^",
    "type": "myth",
    "n": 1,
    "myth": "A raise can lower your take-home pay",
    "fact": "Only the extra income is taxed at the higher rate."
   },
   {
    "at": "Myth two",
    "type": "myth",
    "n": 2,
    "myth": "Your bracket is what you pay",
    "fact": "That's your marginal rate. Your effective rate is usually much lower."
   },
   {
    "at": "Myth three",
    "type": "myth",
    "n": 3,
    "myth": "A big refund is a bonus",
    "fact": "It's your own money, withheld too much during the year."
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. US federal income tax is progressive, with seven rates. Brackets apply to taxable income, after deductions. Each rate applies only to the slice of income in its bracket. Your marginal rate is the rate on your last dollar, your effective rate is what you really pay overall. And a raise always leaves you with more money. If this helped, subscribe. See you in the next video.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "items": [
     "Progressive, seven rates",
     "Brackets apply to taxable income",
     "Each rate only on its slice",
     "Marginal vs effective rate",
     "A raise always leaves you with more"
    ],
    "marks": [
     "US federal income tax is",
     "Brackets apply",
     "Each rate",
     "Your marginal",
     "And a raise"
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
