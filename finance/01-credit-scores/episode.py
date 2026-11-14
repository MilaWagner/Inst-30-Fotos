# Сцены ролика 01 для finance/engine/explainer.py
SECTIONS = [
 {
  "label": "Intro",
  "text": "Two people earn the same salary. They apply for the same mortgage. One gets approved with a lower rate. The other gets a higher rate, or gets turned down. The difference? A three-digit number most people have never had explained to them. Today we'll take your credit score apart, piece by piece, so you know exactly what moves it. Quick note before we start: this video is for education only. It's not financial advice, and your situation may be different.",
  "beats": [
   {
    "at": "^",
    "type": "people"
   },
   {
    "at": "One gets approved",
    "type": "people",
    "result": True
   },
   {
    "at": "The difference?",
    "type": "gauge"
   },
   {
    "at": "Today we",
    "type": "title",
    "kicker": "Explained",
    "text": "How credit scores actually work",
    "sub": "5 factors, piece by piece"
   },
   {
    "at": "Quick note",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "What is a credit score",
  "text": "A credit score is a number that tries to predict one thing: how likely you are to pay back what you borrow. Lenders use it to decide whether to lend to you, and at what interest rate. Landlords and some insurers may look at your credit too. The most widely used score is the FICO Score, and it runs from 300 to 850. Higher is better. The score is calculated from your credit reports — the files kept by the three big credit bureaus: Equifax, Experian and TransUnion. One important detail: you don't have just one score. There are different FICO versions, and there's also VantageScore. A lender may see a different number than the one in your banking app. But they all look at the same kind of information, so the habits we'll cover work across the board.",
  "beats": [
   {
    "at": "^",
    "type": "flow"
   },
   {
    "at": "The most widely used",
    "type": "gauge",
    "head": "FICO Score: 300 to 850",
    "sweep": [
     350,
     760
    ],
    "label": "Higher is better  ·  score bands shown are approximate"
   },
   {
    "at": "The score is calculated",
    "type": "bureaus"
   },
   {
    "at": "One important detail",
    "type": "two_apps"
   }
  ]
 },
 {
  "label": "The 5 factors",
  "text": "According to FICO, your score is built from five categories. Payment history: 35 percent. Amounts owed: 30 percent. Length of credit history: 15 percent. New credit: 10 percent. And credit mix: 10 percent. Notice something? The first two make up almost two thirds of the score. That's where we'll spend most of our time.",
  "beats": [
   {
    "at": "^",
    "type": "donut",
    "build": 9.0
   },
   {
    "at": "Notice something",
    "type": "donut",
    "hi": [
     0,
     1
    ],
    "head": "Two factors = almost two thirds"
   }
  ]
 },
 {
  "label": "1 · Payment history",
  "text": "Payment history is the biggest piece. It answers a simple question: do you pay on time? Every on-time payment adds to a positive record. A payment reported as late can hurt your score — and it can stay on your credit report for up to seven years. Bigger problems weigh even more. Accounts sent to collections, and bankruptcies, can stay for years. A Chapter 7 bankruptcy can be reported for up to ten years. The fix here isn't clever. It's boring, and it works: never miss a payment. The easiest way is autopay for at least the minimum amount on every account. You can always pay more by hand — autopay is just your safety net.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "FACTOR 1",
    "text": "Payment history",
    "pct": "35%"
   },
   {
    "at": "Every on-time",
    "type": "calendar"
   },
   {
    "at": "A payment reported",
    "type": "timeline"
   },
   {
    "at": "The fix here",
    "type": "toggle"
   }
  ]
 },
 {
  "label": "2 · Amounts owed",
  "text": "The second piece is amounts owed. The key idea here is something called credit utilization. It means: how much of your available credit card limit are you actually using? Here's a simple example. Say you have one credit card with a 1,000 dollar limit, and your statement shows a 300 dollar balance. Your utilization is 300 divided by 1,000 — that's 30 percent. Now say you have two cards with 5,000 dollars in total limits and 500 dollars in balances. That's 10 percent. Lower is generally better. How low? FICO's own data shows that people with a perfect 850 score use, on average, only about 4 percent of their available credit. You don't need to hit 4 percent. But it shows the direction: using less of your limit tends to help. And here's a detail many people miss: utilization is usually based on the balance your card company reports, which is often your statement balance. So even if you pay in full every month, a big balance on the statement date can still show up. One simple habit: pay part of your balance before the statement closes. The good news: utilization has no long memory in most scoring models. Pay the balance down, and your score can recover as soon as the lower balance is reported.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "FACTOR 2",
    "text": "Amounts owed",
    "pct": "30%"
   },
   {
    "at": "Here's a simple example",
    "type": "util",
    "limit": 1000,
    "balance": 300
   },
   {
    "at": "Now say you have two",
    "type": "util",
    "limit": 5000,
    "balance": 500,
    "label": "Total limits (2 cards)"
   },
   {
    "at": "How low?",
    "type": "bignum",
    "head": "People with a perfect 850 score",
    "num": "~4%",
    "sub": "average share of their available credit they use",
    "src": "Source: myFICO"
   },
   {
    "at": "And here's a detail",
    "type": "statement"
   },
   {
    "at": "The good news",
    "type": "recover"
   }
  ]
 },
 {
  "label": "3 · Length of history",
  "text": "Third: length of credit history. This looks at how long your accounts have been open — your oldest account, your newest one, and the average age of all of them. A longer track record gives the model more evidence. This is the one factor you can't rush. What you can do is avoid hurting it. Many people close their oldest credit card when they stop using it. But that card may be holding up both your history and your total available credit. Before you close an old no-fee card, think twice.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "FACTOR 3",
    "text": "Length of history",
    "pct": "15%"
   },
   {
    "at": "This looks at",
    "type": "accounts"
   },
   {
    "at": "Many people close",
    "type": "keepcard"
   }
  ]
 },
 {
  "label": "4 · New credit",
  "text": "Fourth: new credit. When you apply for a loan or a credit card, the lender usually pulls your credit. That's called a hard inquiry. A hard inquiry can stay on your report for about two years, but FICO Scores only count hard inquiries from the past twelve months. One inquiry usually has a small effect. Several new applications in a short time can add up. Checking your own credit is different. That's a soft inquiry, and it doesn't affect your score. So check as often as you like.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "FACTOR 4",
    "text": "New credit",
    "pct": "10%"
   },
   {
    "at": "When you apply",
    "type": "inquiry"
   },
   {
    "at": "Checking your own",
    "type": "soft"
   }
  ]
 },
 {
  "label": "5 · Credit mix",
  "text": "Fifth: credit mix. Scoring models like to see that you can handle different types of credit — for example, a credit card and an installment loan like a car loan. But this is the smallest factor. Never take out a loan you don't need just to improve your mix.",
  "beats": [
   {
    "at": "^",
    "type": "section",
    "n": "FACTOR 5",
    "text": "Credit mix",
    "pct": "10%"
   },
   {
    "at": "Scoring models like",
    "type": "mix"
   }
  ]
 },
 {
  "label": "3 myths",
  "text": "Before we get practical, let's clear up three myths that cost people real money. Myth number one: a high income means a high credit score. It doesn't. FICO says your income is not part of your FICO Score at all. Neither is your job title, your employer, your age, or where you live. A lender may ask about your income when you apply — but the score itself never sees your salary. That's why someone earning a modest salary can have a better score than a high earner who pays late. Myth number two: checking your own score will lower it. It won't. When you check your own credit, that's a soft inquiry, and soft inquiries are not part of your FICO Score. Avoiding your own credit report doesn't protect you — it just means you find problems later. Myth number three: there is one official credit score. As we saw, there are many versions, built on reports from three different bureaus. So don't panic if two apps show two different numbers. Focus on the habits that move all of them in the same direction. And remember our two people from the beginning, same salary, different rates? Now you know: the difference wasn't income. It was payment history, balances, and time.",
  "beats": [
   {
    "at": "^",
    "type": "title",
    "kicker": "Before we get practical",
    "text": "3 myths that cost people money"
   },
   {
    "at": "Myth number one",
    "type": "myth",
    "n": 1,
    "myth": "A high income means a high credit score",
    "fact": "Income, job, age and where you live are not part of your FICO Score.",
    "src": "Source: myFICO"
   },
   {
    "at": "Myth number two",
    "type": "myth",
    "n": 2,
    "myth": "Checking my own score will lower it",
    "fact": "Checking your own credit is a soft inquiry. It doesn't count."
   },
   {
    "at": "Myth number three",
    "type": "myth",
    "n": 3,
    "myth": "There is one official credit score",
    "fact": "There are many versions, built on reports from three bureaus."
   },
   {
    "at": "And remember our two",
    "type": "reveal"
   }
  ]
 },
 {
  "label": "Your action plan",
  "text": "So, what can you do this week? First: get your credit reports. In the US, you can get free weekly reports from all three bureaus at annualcreditreport.com. That's the official site. The reports don't include your score, but they show what your score is built from. Second: look for mistakes. Accounts you don't recognize, wrong late payments, wrong balances. If something is wrong, you have the right to dispute it with the credit bureau. Accurate negative information can't be removed early — but errors can be fixed. Third: set up autopay. Fourth: watch your utilization before statement dates. And fifth: think before you close old accounts or open several new ones at once.",
  "beats": [
   {
    "at": "^",
    "type": "title",
    "kicker": "Your action plan",
    "text": "What to do this week"
   },
   {
    "at": "First: get",
    "type": "browser"
   },
   {
    "at": "Second: look",
    "type": "errors"
   },
   {
    "at": "Third: set up",
    "type": "checklist",
    "head": "This week",
    "step": 1.4,
    "items": [
     "Get your free reports",
     "Check for mistakes",
     "Set up autopay",
     "Watch utilization before statement dates",
     "Think before closing or opening accounts"
    ]
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. Pay on time — that's 35 percent. Keep your balances low — that's 30. Let your history grow. Apply for new credit only when you need it. And don't chase credit mix. None of this is fast. But it's simple, and it compounds. If this helped, subscribe — next, we'll break down how credit card interest really works, and why the minimum payment is a trap. See you there.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "step": 1.7,
    "items": [
     "Pay on time  —  35%",
     "Keep balances low  —  30%",
     "Let your history grow",
     "New credit only when needed",
     "Don't chase credit mix"
    ]
   },
   {
    "at": "If this helped",
    "type": "subscribe"
   }
  ]
 }
]
