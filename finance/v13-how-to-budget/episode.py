# Ролик «How to Budget Your Money»
SECTIONS = [
 {
  "label": "Intro",
  "text": "Where does all your money go? If you get to the end of the month and wonder that, you're not alone. A budget isn't about saying no to everything. It's about telling your money where to go, instead of wondering where it went. Today: a simple step-by-step way to build a budget, three popular methods, and the mistakes that make most budgets fail. This works whether you're in the US, the UK, Canada or Australia. This video is for education only, and is not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Where does all your money go?",
    "char": [
     "think",
     420,
     640
    ]
   },
   {
    "at": "A budget isn't about",
    "type": "say",
    "text": "Tell your money where to go.",
    "sub": "Instead of wondering where it went",
    "char": [
     "point_right",
     420,
     640
    ]
   },
   {
    "at": "Today:",
    "type": "checklist",
    "head": "Today",
    "items": [
     "A simple step-by-step budget",
     "Three popular methods",
     "Mistakes that make budgets fail"
    ],
    "marks": [
     "a simple step",
     "three popular",
     "the mistakes"
    ]
   },
   {
    "at": "This works whether",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "Step one",
  "text": "Step one: know your real income. Use your take-home pay, the amount that actually lands in your account after tax and deductions. If your income changes from month to month, use a low, realistic month as your starting point. Budgeting with money you don't reliably have is how plans fall apart.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Step 1: your real income",
    "lines": [
     [
      "Take-home pay"
     ],
     [
      "after tax and deductions"
     ]
    ],
    "step": 2.0
   },
   {
    "at": "If your income changes",
    "type": "say",
    "text": "Irregular income? Plan with a low month.",
    "char": [
     "think",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Step two",
  "text": "Step two: track where your money goes. Look at your bank and card statements for the last two or three months, and sort every expense into categories: housing, food, transport, bills, debt, subscriptions, fun. Most people are surprised. Small things, like takeout, delivery and forgotten subscriptions, often add up to hundreds a month.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Step 2: track 2–3 months",
    "items": [
     "Housing",
     "Food",
     "Transport",
     "Bills and debt",
     "Subscriptions and fun"
    ],
    "marks": [
     "housing",
     "food",
     "transport",
     "bills",
     "subscriptions"
    ]
   },
   {
    "at": "Most people are surprised",
    "type": "say",
    "text": "Small things add up to hundreds a month.",
    "sub": "Takeout, delivery, forgotten subscriptions",
    "char": [
     "worried",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Fixed and flexible",
  "text": "Next, split your spending into two groups. Fixed costs stay about the same every month: rent or mortgage, insurance, loan payments, phone. Flexible costs change: groceries, eating out, shopping, entertainment. Fixed costs are hard to change quickly, but they're where the big wins are. Flexible costs are where you can adjust every month.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Two kinds of spending",
    "step": 3.0,
    "cols": [
     [
      "Fixed",
      [
       "Rent or mortgage",
       "Insurance",
       "Loan payments, phone"
      ],
      [
       52,
       104,
       214
      ]
     ],
     [
      "Flexible",
      [
       "Groceries",
       "Eating out",
       "Shopping, entertainment"
      ],
      [
       222,
       160,
       36
      ]
     ]
    ]
   }
  ]
 },
 {
  "label": "The 50/30/20 rule",
  "text": "Now, a simple method to start with: the fifty thirty twenty rule, popularized by Elizabeth Warren and Amelia Warren Tyagi in their book All Your Worth. Fifty percent of your take-home pay goes to needs, like housing, food, transport and minimum debt payments. Thirty percent goes to wants. And twenty percent goes to saving, investing and paying off extra debt. On a take-home pay of four thousand a month, that's two thousand for needs, one thousand two hundred for wants, and eight hundred for your future.",
  "beats": [
   {
    "at": "^",
    "type": "donut",
    "head": "The 50/30/20 rule",
    "parts": [
     [
      50,
      "Needs"
     ],
     [
      30,
      "Wants"
     ],
     [
      20,
      "Saving & extra debt"
     ]
    ],
    "build": 6.0,
    "src": "From the book All Your Worth (Warren & Tyagi)"
   },
   {
    "at": "On a take-home pay",
    "type": "bars",
    "head": "Take-home pay: 4,000 a month",
    "step": 1.5,
    "rows": [
     [
      "Needs (50%)",
      2000,
      "2,000",
      [
       52,
       104,
       214
      ]
     ],
     [
      "Wants (30%)",
      1200,
      "1,200",
      [
       222,
       160,
       36
      ]
     ],
     [
      "Your future (20%)",
      800,
      "800",
      [
       36,
       156,
       92
      ]
     ]
    ],
    "note": "Example. Works the same in $, £, C$ or A$."
   }
  ]
 },
 {
  "label": "When it doesn't fit",
  "text": "In expensive cities, needs can easily take more than fifty percent, especially rent. That's okay. The rule is a starting point, not a test you pass or fail. If needs take sixty percent, you might do sixty, twenty, twenty. What matters most is that the saving part isn't zero.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Needs over 50%? That's okay.",
    "sub": "Expensive cities, high rent",
    "char": [
     "shrug",
     420,
     640
    ]
   },
   {
    "at": "If needs take sixty",
    "type": "bignum",
    "head": "Adjust it",
    "num": "60 / 20 / 20",
    "sub": "just don't let saving hit zero"
   }
  ]
 },
 {
  "label": "Zero-based budgeting",
  "text": "A second method is zero-based budgeting. Every dollar of income gets a job, until income minus everything you've planned equals zero. That doesn't mean spending everything. Savings and investments are jobs too. It takes more effort, but it gives you the most control, and it's great if you feel like money just disappears.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Zero-based budgeting",
    "lines": [
     [
      "Every dollar gets a job"
     ],
     [
      "Income − plan = 0"
     ]
    ],
    "step": 2.5
   },
   {
    "at": "That doesn't mean spending",
    "type": "say",
    "text": "Savings and investing are jobs too.",
    "sub": "Most effort, most control",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Pay yourself first",
  "text": "A third method is the simplest of all: pay yourself first. As soon as you get paid, an automatic transfer moves a set amount into savings or investments. Then you spend what's left, without tracking every coffee. It works because it removes willpower from the equation. You can't spend money you never see.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Pay yourself first",
    "lines": [
     [
      "Payday → automatic transfer to savings"
     ],
     [
      "Spend what's left"
     ]
    ],
    "step": 3.0
   },
   {
    "at": "It works because",
    "type": "say",
    "text": "You can't spend money you never see.",
    "char": [
     "happy",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Automate it",
  "text": "Whichever method you choose, automate as much as you can. Set up automatic transfers to savings on payday. Put fixed bills on autopay, so you never pay late fees. And if your employer offers a retirement plan with a match, contribute at least enough to get it.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Automate it",
    "items": [
     "Auto-transfer to savings on payday",
     "Fixed bills on autopay",
     "Get the full retirement match"
    ],
    "marks": [
     "Set up automatic",
     "Put fixed bills",
     "And if your employer"
    ]
   }
  ]
 },
 {
  "label": "Sinking funds",
  "text": "Here's a trick that saves many budgets: sinking funds. Some costs don't come every month, like car repairs, holidays, gifts, insurance renewals or annual subscriptions. Add them up for the year, divide by twelve, and set that amount aside every month. Then when the bill arrives, the money is already there, and it doesn't wreck your budget.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Sinking funds for",
    "items": [
     "Car repairs",
     "Holidays and gifts",
     "Insurance renewals",
     "Annual subscriptions"
    ],
    "marks": [
     "car repairs",
     "holidays",
     "insurance renewals",
     "annual subscriptions"
    ]
   },
   {
    "at": "Add them up",
    "type": "lines",
    "head": "Sinking fund",
    "lines": [
     [
      "Yearly total ÷ 12"
     ],
     [
      "set aside every month"
     ]
    ],
    "step": 2.0
   }
  ]
 },
 {
  "label": "Why budgets fail",
  "text": "Why do most budgets fail? They're too strict, with no room for fun, so people give up. They forget irregular costs. They don't get reviewed. And people quit after one bad month. A budget should have some fun money built in, and it should change as your life changes.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Why budgets fail",
    "items": [
     "Too strict, no fun",
     "Irregular costs forgotten",
     "Never reviewed",
     "Quitting after one bad month"
    ],
    "marks": [
     "They're too strict",
     "They forget",
     "They don't get",
     "And people quit"
    ]
   }
  ]
 },
 {
  "label": "Check in",
  "text": "So check in regularly. Once a week, take five minutes to look at your spending. Once a month, compare what you planned with what actually happened, and adjust. You don't need a perfect budget. You need one you'll actually stick to.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Check in",
    "step": 2.0,
    "cols": [
     [
      "Every week",
      [
       "5 minutes",
       "Look at spending"
      ],
      [
       52,
       104,
       214
      ]
     ],
     [
      "Every month",
      [
       "Plan vs reality",
       "Adjust"
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
    "at": "You don't need a perfect",
    "type": "say",
    "text": "Not perfect. One you'll stick to.",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. Start with your real take-home pay. Track where your money goes. Separate fixed and flexible costs. Pick a method: fifty thirty twenty, zero-based, or pay yourself first. Automate your savings and bills. Use sinking funds for irregular costs. And check in every week and every month. If this helped, subscribe. Next, we'll look at compound interest, and why starting early matters so much. See you there.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "items": [
     "Real take-home pay",
     "Track, then fixed vs flexible",
     "50/30/20, zero-based, or pay yourself first",
     "Automate, use sinking funds",
     "Check in weekly and monthly"
    ],
    "marks": [
     "Start with",
     "Track where",
     "Pick a method",
     "Automate",
     "And check in"
    ]
   },
   {
    "at": "If this helped",
    "type": "subscribe",
    "next": "Compound interest explained",
    "next_sub": "why starting early matters so much",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
