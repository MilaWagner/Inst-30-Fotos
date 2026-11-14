# Сцены ролика 06 для finance/engine/explainer.py
SECTIONS = [
 {
  "label": "Intro",
  "text": "Imagine you owe five thousand dollars on a credit card. The interest rate is twenty-two percent — close to the average rate on US cards that carry a balance right now. And every month, you pay just the minimum. How long until you're debt-free? Two years? Five? With a common minimum-payment formula, it takes about nineteen years. And you pay around eight thousand dollars in interest. More than you borrowed. Today we'll take credit card interest apart, step by step, so it never surprises you again. Whether you pay in dollars, pounds or euros, the math works the same way. Quick note: this video is for education only, not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "debtcard",
    "char": [
     "worried",
     420,
     640
    ]
   },
   {
    "at": "How long until",
    "type": "lines",
    "head": "How long until you're debt-free?",
    "lines": [
     [
      "2 years?"
     ],
     [
      "5 years?"
     ]
    ],
    "step": 1.0
   },
   {
    "at": "With a common",
    "type": "bignum",
    "head": "Paying only the minimum",
    "num": "~19 years",
    "sub": "with a common minimum-payment formula",
    "src": "Example: $5,000 at 22% APR",
    "char": [
     "worried",
     300,
     560
    ]
   },
   {
    "at": "And you pay around",
    "type": "bignum",
    "head": "Total interest paid",
    "num": "~$8,100",
    "sub": "more than you borrowed",
    "src": "Example: $5,000 at 22% APR"
   },
   {
    "at": "Today we'll",
    "type": "say",
    "text": "Let's take credit card interest apart, step by step.",
    "sub": "Dollars, pounds or euros — same math",
    "char": [
     "wave",
     420,
     640
    ]
   },
   {
    "at": "Quick note",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "What APR means",
  "text": "Let's start with three letters: A, P, R. Annual percentage rate. It's the yearly price of borrowing on your card. If your card says twenty-two percent APR, that sounds like something that happens once a year. It doesn't. On most cards, interest is calculated every single day. Here's how. The card company divides your APR by the number of days in a year. That gives a daily rate. At twenty-four percent APR, the daily rate is about zero point zero six six percent. Tiny, right? Now multiply it by your balance. On a one thousand dollar balance, that's about sixty-six cents. Every day. Over a month, roughly twenty dollars — for doing nothing at all. And here's the part that makes it expensive: compounding. Interest that you don't pay off gets added to your balance. Then tomorrow, you pay interest on that interest. It's the same force that grows savings — just working against you.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "APR",
    "lines": [
     [
      "Annual Percentage Rate",
      72
     ],
     [
      "the yearly price of borrowing",
      48
     ]
    ],
    "step": 0.8
   },
   {
    "at": "It doesn't.",
    "type": "say",
    "text": "Interest is calculated every single day.",
    "sub": "On most cards",
    "char": [
     "point_right",
     420,
     640
    ]
   },
   {
    "at": "Here's how.",
    "type": "lines",
    "head": "Daily interest",
    "lines": [
     [
      "24% APR ÷ 365 ≈ 0.066% per day"
     ],
     [
      "$1,000 × 0.066% ≈ $0.66 a day"
     ],
     [
      "≈ $20 a month"
     ]
    ],
    "step": 3.0,
    "note": "Example numbers"
   },
   {
    "at": "And here's the part",
    "type": "compound"
   }
  ]
 },
 {
  "label": "The grace period",
  "text": "Now the good news. Most credit cards have something called a grace period. It's the time between the end of your billing cycle and your payment due date. If you pay your full statement balance by the due date, you usually pay no interest on purchases at all. Zero. That's the secret. A credit card can cost you nothing — if you pay it in full, every month. But the moment you leave even part of the balance unpaid, you can lose that grace period. Interest starts on the remaining balance, and often on new purchases too, until you've paid in full again. One important exception: cash advances. Taking cash from an ATM with your credit card usually has no grace period. Interest often starts the same day, frequently at a higher rate, and there's usually a fee on top.",
  "beats": [
   {
    "at": "^",
    "type": "grace"
   },
   {
    "at": "That's the secret",
    "type": "say",
    "text": "Pay in full every month and the card can cost you nothing.",
    "sub": "Leave a balance and you can lose the grace period",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   },
   {
    "at": "One important exception",
    "type": "atm"
   }
  ]
 },
 {
  "label": "Your statement",
  "text": "Before we go further, grab your latest statement, or open your card's app. Look for five numbers. One: your statement balance. That's what you owed when the billing cycle ended. Pay this in full by the due date, and on most cards you keep your grace period. Two: your current balance. It's often different, because it includes purchases you made after the statement closed. Three: the minimum payment due. Four: the payment due date. Miss it, and you can be charged a late fee, and on some cards your rate can go up. And five: the interest charged this period. That's the real cost of carrying a balance, in plain numbers. If that number isn't zero, keep watching. This video is for you.",
  "beats": [
   {
    "at": "^",
    "type": "statement5",
    "hi": -1
   },
   {
    "at": "One: your",
    "type": "statement5",
    "hi": 0
   },
   {
    "at": "Two: your",
    "type": "statement5",
    "hi": 1
   },
   {
    "at": "Three: the",
    "type": "statement5",
    "hi": 2
   },
   {
    "at": "Four: the",
    "type": "statement5",
    "hi": 3
   },
   {
    "at": "And five",
    "type": "statement5",
    "hi": 4
   }
  ]
 },
 {
  "label": "The minimum payment trap",
  "text": "Which brings us to the minimum payment. Your statement shows a small number you're required to pay. Pay at least that, on time, and your account stays in good standing. It feels responsible. But it's designed to be small. Formulas differ between banks and countries. A common one is one percent of your balance, plus that month's interest. Let's run our example. Five thousand dollars at twenty-two percent. Your first minimum payment is about one hundred and forty dollars. But almost ninety dollars of that is interest. Only about fifty dollars actually reduces your debt. And as your balance shrinks, the minimum shrinks too. So you pay a little less, and a little less, and the debt drags on. Following that formula all the way, it takes about two hundred and thirty months to pay off. That's over nineteen years. Total interest: about eight thousand one hundred dollars.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "The minimum payment: small on purpose.",
    "sub": "It keeps your account in good standing — that's all",
    "char": [
     "think",
     420,
     640
    ]
   },
   {
    "at": "Formulas differ",
    "type": "lines",
    "head": "A common formula",
    "lines": [
     [
      "Minimum ="
     ],
     [
      "1% of your balance"
     ],
     [
      "+ this month's interest"
     ]
    ],
    "step": 1.0,
    "note": "Formulas differ between banks and countries"
   },
   {
    "at": "Your first minimum",
    "type": "minsplit"
   },
   {
    "at": "And as your balance shrinks",
    "type": "payoff",
    "stage": 1
   }
  ]
 },
 {
  "label": "Fixed payments",
  "text": "Now watch what happens with one simple change. Instead of paying the shrinking minimum, you pay a fixed amount every month. Let's say a fixed one hundred and fifty dollars — about the same as your very first minimum. The debt is gone in about fifty-two months, and you pay around two thousand eight hundred dollars in interest. Bump it to two hundred dollars a month, and you're done in about thirty-four months, with roughly one thousand seven hundred and fifty dollars in interest. Same debt. Same rate. Nineteen years versus under three. The only difference is the payment you choose. These are simplified examples. Real numbers depend on your card's terms, fees, and new purchases. But the pattern is always the same: every extra dollar above the minimum goes straight to the debt itself.",
  "beats": [
   {
    "at": "^",
    "type": "payoff",
    "stage": 1
   },
   {
    "at": "Let's say a fixed",
    "type": "payoff",
    "stage": 2
   },
   {
    "at": "Bump it",
    "type": "payoff",
    "stage": 3
   },
   {
    "at": "These are simplified",
    "type": "say",
    "text": "Every dollar above the minimum goes straight to the debt.",
    "sub": "Same debt, same rate — your payment decides",
    "char": [
     "point_right",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Finding extra money",
  "text": "\"Sure,\" you might say, \"but where do I find an extra fifty dollars a month?\" Start small. Look at your last three months of card spending and circle anything you wouldn't buy again. A subscription you forgot about. Delivery fees. Things that seemed small at the time. Then make the extra payment automatic, right after payday, before you can spend it. And one more trick: while you're paying down a card, try to stop adding new purchases to it. Otherwise you're filling the bucket while you try to empty it.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "“Where do I find an extra $50 a month?”",
    "sub": "Start small",
    "char": [
     "shrug",
     420,
     640
    ]
   },
   {
    "at": "Look at your last",
    "type": "checklist",
    "head": "Find the money",
    "step": 2.5,
    "items": [
     "Review 3 months of card spending",
     "Cancel forgotten subscriptions",
     "Cut delivery fees and small extras",
     "Automate the extra payment after payday",
     "Stop adding new purchases to the card"
    ]
   }
  ]
 },
 {
  "label": "3 myths",
  "text": "Let's clear up three myths. Myth number one: carrying a balance helps your credit score. It doesn't. The US Consumer Financial Protection Bureau lists this as a myth. Paying in full is the best way to build or keep a good score, and you avoid the interest. Myth number two: the minimum payment is what you're supposed to pay. It's the least you can pay without a late payment. That's all. It is not a plan. Myth number three: a zero percent offer means it's free. Zero percent deals can be useful, but they end. Balance transfer offers usually charge a fee up front, and once the promo ends, the regular rate applies to whatever is left. Read the end date before you sign.",
  "beats": [
   {
    "at": "^",
    "type": "myth",
    "n": 1,
    "myth": "Carrying a balance helps your credit score",
    "fact": "It doesn't. Paying in full is the best way to build or keep a good score.",
    "src": "Source: CFPB"
   },
   {
    "at": "Myth number two",
    "type": "myth",
    "n": 2,
    "myth": "The minimum payment is what you're supposed to pay",
    "fact": "It's the least you can pay without a late payment. It is not a plan."
   },
   {
    "at": "Myth number three",
    "type": "myth",
    "n": 3,
    "myth": "0% means it's free",
    "fact": "Promos end. Transfers usually cost a fee, then the regular rate applies.",
    "src": "Source: CFPB"
   }
  ]
 },
 {
  "label": "Your action plan",
  "text": "So what can you do? First: if you can, pay your full statement balance every month. That's how you keep the grace period and pay zero interest. Second: if you already have a balance, stop paying the shrinking minimum. Pick a fixed amount you can afford, and pay it every month, even as the balance falls. Third: if you have several cards, put the extra money toward the highest interest rate first. That's called the avalanche method, and we'll compare it with the snowball method in the next video. Fourth: avoid cash advances. And fifth: call your card company and ask for a lower rate. It doesn't always work. But it's one phone call, and sometimes the answer is yes.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Your action plan",
    "step": 9.0,
    "items": [
     "Pay the full statement balance",
     "Already in debt? Pay a fixed amount",
     "Several cards? Highest rate first",
     "Avoid cash advances",
     "Call and ask for a lower rate"
    ]
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. Interest is charged daily and compounds. Pay in full and the grace period makes your card free. The minimum payment keeps you in debt for years. A fixed, higher payment can save you thousands. And every dollar above the minimum attacks the debt itself. If this helped, subscribe. Next, we'll compare the debt avalanche and the debt snowball, and find out which one gets you out of debt faster. See you there.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "step": 3.0,
    "items": [
     "Interest is daily and compounds",
     "Pay in full → grace period → $0",
     "The minimum keeps you in debt for years",
     "A fixed, higher payment saves thousands",
     "Every extra dollar attacks the debt"
    ]
   },
   {
    "at": "If this helped",
    "type": "subscribe",
    "next": "Debt avalanche vs debt snowball",
    "next_sub": "Which one gets you out of debt faster?",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
