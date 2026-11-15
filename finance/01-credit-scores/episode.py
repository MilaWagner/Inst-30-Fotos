# Ролик «Credit Score Questions» (формат вопрос-ответ, тема sky)
THEME = "sky"
LOOK = "finn_casual"
SECTIONS = [
 {
  "label": "Two applicants",
  "text": "A low credit score can mean paying more interest on almost everything you borrow. In the next few minutes, you'll learn exactly what moves your score, and what to do this week to improve it. Here's how it plays out. Two people earn the same salary and apply for the same mortgage. One gets approved at a lower rate. The other pays more, or gets turned down. The difference is a three-digit number. So, no lecture today: just the eight questions people ask most about credit scores in the US, answered one by one. Quick note: this is for education only, not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "hook",
    "kicker": "Money Q&A",
    "text": "A low credit score makes almost everything you borrow cost more."
   },
   {
    "at": "In the next few minutes",
    "type": "hook",
    "kicker": "In this video",
    "text": "What moves your score, and what to do this week."
   },
   {
    "at": "Here's how it plays out",
    "type": "ident",
    "series": "Money Q&A",
    "title": "8 Credit Score Questions, Answered"
   },
   {
    "at": "Two people earn",
    "type": "people"
   },
   {
    "at": "One gets approved",
    "type": "people",
    "result": True
   },
   {
    "at": "The difference",
    "type": "gauge"
   },
   {
    "at": "So, no lecture today",
    "type": "say",
    "text": "8 questions people ask about credit scores.",
    "sub": "Answered one by one",
    "char": [
     "point_right",
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
  "label": "Question 1",
  "text": "Question one: what is a credit score, really? It's a number that tries to predict one thing: how likely you are to pay back what you borrow. The most widely used one, the FICO Score, runs from three hundred to eight hundred and fifty, and higher is better. It's calculated from your credit reports, the files kept by the three big bureaus: Equifax, Experian and TransUnion.",
  "beats": [
   {
    "at": "^",
    "type": "question",
    "tag": "Q1",
    "q": "What is a credit score, really?"
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
    "at": "It's calculated from",
    "type": "bureaus"
   }
  ]
 },
 {
  "label": "Question 2",
  "text": "Question two: why does my bank app show a different number than my lender? Because there isn't just one score. There are several FICO versions, and there's also VantageScore, built on reports from three different bureaus. So two numbers can both be right. They all look at the same kind of information, so the same habits move all of them.",
  "beats": [
   {
    "at": "^",
    "type": "question",
    "tag": "Q2",
    "q": "Why does my app show a different number?"
   },
   {
    "at": "Because there isn't",
    "type": "two_apps"
   },
   {
    "at": "They all look at",
    "type": "say",
    "text": "Same habits move every version.",
    "char": [
     "thumbs_up",
     420,
     640,
     "sam"
    ]
   }
  ]
 },
 {
  "label": "Question 3",
  "text": "Question three: what goes into the score? According to FICO, five things. Payment history counts for thirty-five percent. Amounts owed, thirty percent. Length of credit history, fifteen. New credit, ten. And credit mix, ten. The first two make up almost two thirds of the score, so that's where your effort pays off most.",
  "beats": [
   {
    "at": "^",
    "type": "question",
    "tag": "Q3",
    "q": "What goes into the score?"
   },
   {
    "at": "According to FICO",
    "type": "donut",
    "build": 8.0
   },
   {
    "at": "The first two make up",
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
  "label": "Question 4",
  "text": "Question four: how bad is one late payment? It can hurt, and a payment reported as late can stay on your credit report for up to seven years. Collections and bankruptcies weigh even more, and a Chapter 7 bankruptcy can be reported for up to ten years. The fix is boring, and it works: set up autopay for at least the minimum on every account. You can always pay more by hand.",
  "beats": [
   {
    "at": "^",
    "type": "question",
    "tag": "Q4",
    "q": "How bad is one late payment?"
   },
   {
    "at": "It can hurt",
    "type": "timeline"
   },
   {
    "at": "The fix is boring",
    "type": "toggle"
   }
  ]
 },
 {
  "label": "Question 5",
  "text": "Question five: I pay my card in full every month. Why is my score still low? Probably because of utilization: how much of your credit limit you're using. It's usually based on the balance your card company reports, which is often your statement balance. So a big balance on the statement date can show up, even if you pay it off right after. Say your limit is one thousand dollars and your statement shows three hundred. That's thirty percent. FICO says people with a perfect eight fifty use, on average, only about four percent. A simple trick: pay part of the balance before the statement closes.",
  "beats": [
   {
    "at": "^",
    "type": "question",
    "tag": "Q5",
    "q": "I pay in full. Why is my score still low?"
   },
   {
    "at": "It's usually based on",
    "type": "statement"
   },
   {
    "at": "Say your limit",
    "type": "util",
    "limit": 1000,
    "balance": 300
   },
   {
    "at": "FICO says people",
    "type": "bignum",
    "head": "People with a perfect 850 score",
    "num": "~4%",
    "sub": "average share of their available credit they use",
    "src": "Source: myFICO"
   },
   {
    "at": "A simple trick",
    "type": "say",
    "text": "Pay part of it before the statement closes.",
    "char": [
     "happy",
     420,
     640,
     "maya"
    ]
   }
  ]
 },
 {
  "label": "Question 6",
  "text": "Question six: does checking my own score hurt it? No. Checking your own credit is a soft inquiry, and it doesn't affect your FICO Score. What counts is a hard inquiry, when a lender pulls your credit after you apply. A hard inquiry can stay on your report for about two years, but FICO only counts those from the last twelve months, and one usually has a small effect. Several applications in a short time can add up.",
  "beats": [
   {
    "at": "^",
    "type": "question",
    "tag": "Q6",
    "q": "Does checking my own score hurt it?"
   },
   {
    "at": "Checking your own credit",
    "type": "soft"
   },
   {
    "at": "What counts is a hard inquiry",
    "type": "inquiry"
   }
  ]
 },
 {
  "label": "Question 7",
  "text": "Question seven: should I close my old credit cards? Think twice. An old card may be holding up both the length of your history and your total available credit. Close it, and your utilization can jump. And does a higher income help? No. FICO says your income is not part of your score at all. Neither is your job, your age, or where you live.",
  "beats": [
   {
    "at": "^",
    "type": "question",
    "tag": "Q7",
    "q": "Should I close my old cards?"
   },
   {
    "at": "An old card may be",
    "type": "keepcard"
   },
   {
    "at": "And does a higher income help",
    "type": "myth",
    "n": 1,
    "myth": "A higher income means a higher score",
    "fact": "Income, job, age and where you live are not part of your FICO Score.",
    "src": "Source: myFICO"
   }
  ]
 },
 {
  "label": "Question 8",
  "text": "Question eight: what can I do this week? Get your free credit reports from all three bureaus at AnnualCreditReport.com, the official site. Look for accounts you don't recognize or late payments that are wrong. Errors can be disputed with the credit bureau. Accurate negative information can't be removed early, but mistakes can be fixed. Then turn on autopay, and watch your balance before each statement date.",
  "beats": [
   {
    "at": "^",
    "type": "question",
    "tag": "Q8",
    "q": "What can I do this week?"
   },
   {
    "at": "Get your free credit reports",
    "type": "browser"
   },
   {
    "at": "Look for accounts",
    "type": "errors"
   },
   {
    "at": "Then turn on autopay",
    "type": "checklist",
    "head": "This week",
    "items": [
     "Get your free reports",
     "Check for mistakes",
     "Turn on autopay",
     "Watch your statement balance"
    ],
    "marks": [
     "Get your free",
     "Look for accounts",
     "Then turn on autopay",
     "watch your balance"
    ]
   }
  ]
 },
 {
  "label": "The answer",
  "text": "So, back to our two applicants with the same salary. The difference wasn't income. It was payment history, balances, and time. None of this is fast, but all of it is in your control. Next on the channel: how the stock market actually works, from what a share really is to why prices move. See you there.",
  "beats": [
   {
    "at": "^",
    "type": "reveal"
   },
   {
    "at": "None of this is fast",
    "type": "takeaway",
    "text": "Pay on time. Keep balances low. Give it time."
   },
   {
    "at": "Next on the channel",
    "type": "subscribe",
    "next": "The bakery that went public",
    "next_sub": "how the stock market really works",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
