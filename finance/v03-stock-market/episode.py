# Ролик «How the Stock Market Actually Works»
SECTIONS = [
 {
  "label": "Intro",
  "text": "Every day, trillions of dollars move through the stock market. Prices jump, prices crash, and the news makes it sound like a casino. But underneath all that noise, the stock market is surprisingly simple. Today, we'll open it up: what a stock really is, why prices move, what an index is, why markets crash, and what all of this means for your money. This video is for education only. It's not financial advice.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "Trillions of dollars move through the stock market every day.",
    "sub": "It sounds like a casino. It isn't.",
    "char": [
     "think",
     420,
     640
    ]
   },
   {
    "at": "Today, we'll open it up",
    "type": "checklist",
    "head": "Today",
    "items": [
     "What a stock really is",
     "Why prices move",
     "What an index is",
     "Why markets crash"
    ],
    "marks": [
     "what a stock",
     "why prices",
     "what an index",
     "why markets crash"
    ]
   },
   {
    "at": "This video is for education",
    "type": "disclaimer"
   }
  ]
 },
 {
  "label": "What a stock is",
  "text": "Let's start with a business. Imagine a bakery that wants to open ten new shops. It needs money. It could borrow from a bank. Or it could sell small pieces of ownership to investors. Those pieces are called shares, or stocks. If you own a share, you own a tiny part of that business. When the business earns more, your piece can become more valuable. And some companies pay part of their profits to shareholders in cash. That's called a dividend. The first time a company sells its shares to the public is called an initial public offering, or IPO.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "A bakery wants to open ten new shops. It needs money.",
    "char": [
     "think",
     420,
     640
    ]
   },
   {
    "at": "It could borrow",
    "type": "twocol",
    "head": "Two ways to raise money",
    "step": 2.5,
    "cols": [
     [
      "Borrow",
      [
       "A loan from a bank",
       "Must be paid back",
       "With interest"
      ],
      [
       52,
       104,
       214
      ]
     ],
     [
      "Sell shares",
      [
       "Small pieces of ownership",
       "Investors become owners",
       "They share the profits"
      ],
      [
       16,
       122,
       96
      ]
     ]
    ]
   },
   {
    "at": "If you own a share",
    "type": "lines",
    "head": "Owning a share",
    "lines": [
     [
      "A tiny part of the business"
     ],
     [
      "Business earns more → piece can be worth more"
     ],
     [
      "Dividend = part of the profits paid in cash"
     ]
    ],
    "step": 3.0
   },
   {
    "at": "The first time a company",
    "type": "bignum",
    "head": "First sale of shares to the public",
    "num": "IPO",
    "sub": "initial public offering"
   }
  ]
 },
 {
  "label": "The exchange",
  "text": "After that, shares are bought and sold between investors on a stock exchange. Think of it as a giant marketplace that matches buyers and sellers. The New York Stock Exchange traces its roots back to 1792, when traders signed an agreement under a buttonwood tree in Manhattan. Today there's the New York Stock Exchange and the Nasdaq in the United States, the London Stock Exchange in the UK, the Toronto Stock Exchange in Canada, and the ASX in Australia. Most trading now happens electronically, in fractions of a second. And you don't go there yourself. You use a broker, usually an app, which sends your order to the market.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "After the IPO, investors trade shares on a stock exchange.",
    "sub": "A giant marketplace that matches buyers and sellers",
    "char": [
     "point_right",
     420,
     640
    ]
   },
   {
    "at": "The New York Stock Exchange traces",
    "type": "bignum",
    "head": "New York Stock Exchange",
    "num": "1792",
    "sub": "traders signed an agreement under a buttonwood tree"
   },
   {
    "at": "Today there's",
    "type": "checklist",
    "head": "Major exchanges",
    "items": [
     "US: New York Stock Exchange, Nasdaq",
     "UK: London Stock Exchange",
     "Canada: Toronto Stock Exchange",
     "Australia: ASX"
    ],
    "marks": [
     "Today there's",
     "the London",
     "the Toronto",
     "and the ASX"
    ]
   },
   {
    "at": "And you don't go there",
    "type": "say",
    "text": "You use a broker, usually an app.",
    "sub": "It sends your order to the market",
    "char": [
     "thumbs_up",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Why prices move",
  "text": "So why do prices move? In the short term, it's simple: supply and demand. If more people want to buy a stock than sell it, the price rises until enough sellers appear. If more want to sell, the price falls. But what makes people want to buy or sell? News. Earnings reports. Interest rates. Fear. Excitement. In the short term, prices can swing wildly for reasons that have little to do with the business itself.",
  "beats": [
   {
    "at": "^",
    "type": "twocol",
    "head": "Short term: supply and demand",
    "step": 4,
    "cols": [
     [
      "More buyers",
      [
       "Price rises",
       "until sellers appear"
      ],
      [
       36,
       156,
       92
      ]
     ],
     [
      "More sellers",
      [
       "Price falls",
       "until buyers appear"
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
    "at": "But what makes people",
    "type": "checklist",
    "head": "What moves prices short term",
    "items": [
     "News",
     "Earnings reports",
     "Interest rates",
     "Fear and excitement"
    ],
    "marks": [
     "News.",
     "Earnings",
     "Interest rates",
     "Fear."
    ]
   }
  ]
 },
 {
  "label": "Long term",
  "text": "In the long term, though, something different happens. Over many years, a company's share price tends to follow what the business actually earns. A company that grows its profits for decades usually sees its stock rise. A company that shrinks usually sees its stock fall. That's why investors often say: in the short run, the market is a voting machine, and in the long run, it's a weighing machine. The quote is credited to Benjamin Graham, Warren Buffett's teacher. Short term, it counts opinions. Long term, it weighs results.",
  "beats": [
   {
    "at": "^",
    "type": "growth",
    "head": "Long term: prices tend to follow profits",
    "lines": [
     [
      25,
      [
       16,
       122,
       96
      ],
      0.3
     ]
    ]
   },
   {
    "at": "That's why investors",
    "type": "twocol",
    "head": "Benjamin Graham's famous idea",
    "step": 2.5,
    "cols": [
     [
      "Short run",
      [
       "A voting machine",
       "It counts opinions"
      ],
      [
       222,
       160,
       36
      ]
     ],
     [
      "Long run",
      [
       "A weighing machine",
       "It weighs results"
      ],
      [
       16,
       122,
       96
      ]
     ]
    ]
   }
  ]
 },
 {
  "label": "Indexes",
  "text": "Now, when the news says the market is up today, what market do they mean? Usually an index. An index is a list of companies that represents a part of the market. The S&P 500 tracks five hundred large US companies, and bigger companies count for more in it. The Dow Jones tracks thirty big US companies. In the UK there's the FTSE 100, in Canada the S&P/TSX Composite, and in Australia the ASX 200. If the index is up one percent, those companies, on average, gained about one percent that day.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "“The market is up today.” Which market?",
    "sub": "Usually an index",
    "char": [
     "shrug",
     420,
     640
    ]
   },
   {
    "at": "An index is a list",
    "type": "lines",
    "head": "What is an index?",
    "lines": [
     [
      "A list of companies"
     ],
     [
      "that represents part of the market"
     ]
    ],
    "step": 1.5
   },
   {
    "at": "The S&P 500 tracks",
    "type": "checklist",
    "head": "Major indexes",
    "items": [
     "S&P 500: 500 large US companies",
     "Dow Jones: 30 big US companies",
     "UK: FTSE 100",
     "Canada: S&P/TSX Composite",
     "Australia: ASX 200"
    ],
    "marks": [
     "The S&P 500 tracks",
     "The Dow Jones",
     "In the UK",
     "in Canada",
     "and in Australia"
    ]
   }
  ]
 },
 {
  "label": "Returns",
  "text": "Here's what history shows. Since it launched in 1957, the S&P 500 has returned roughly ten percent a year on average, including dividends, before inflation. After inflation, it's closer to six or seven percent. But that average hides a lot of bumpy years. Some years the market gains thirty percent. Some years it loses twenty or more. The average only shows up if you stay invested through the bad years too. And past returns don't guarantee future ones.",
  "beats": [
   {
    "at": "^",
    "type": "bignum",
    "head": "S&P 500 since 1957, average per year",
    "num": "~10%",
    "sub": "including dividends, before inflation (~6–7% after inflation)",
    "src": "Past returns don't guarantee future returns"
   },
   {
    "at": "But that average hides",
    "type": "bars",
    "head": "Some years look very different",
    "step": 1.5,
    "rows": [
     [
      "A strong year (example)",
      30,
      "+30%",
      [
       36,
       156,
       92
      ]
     ],
     [
      "An average year",
      10,
      "+10%",
      [
       16,
       122,
       96
      ]
     ],
     [
      "A bad year (example)",
      20,
      "−20%",
      [
       206,
       64,
       60
      ]
     ]
    ],
    "note": "Illustration of how bumpy single years can be"
   }
  ]
 },
 {
  "label": "Crashes",
  "text": "So let's talk about crashes. A drop of ten percent from a recent high is usually called a correction. A drop of twenty percent or more is called a bear market. A rising market is called a bull market. Crashes happen more often than people expect. In the financial crisis, the S&P 500 fell about fifty-seven percent from its peak in 2007 to its low in 2009. In 2020, during the pandemic, it fell about thirty-four percent in roughly a month. Both times, it later recovered and went on to new highs. But recoveries can take years, and there's no guarantee of how long the next one will take.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Market words",
    "items": [
     "Correction: down ~10% from a high",
     "Bear market: down 20% or more",
     "Bull market: a rising market"
    ],
    "marks": [
     "A drop of ten",
     "A drop of twenty",
     "A rising market"
    ]
   },
   {
    "at": "In the financial crisis",
    "type": "bars",
    "head": "S&P 500 drops from peak to low",
    "step": 3.0,
    "rows": [
     [
      "Financial crisis, 2007–2009",
      57,
      "−57%",
      [
       206,
       64,
       60
      ]
     ],
     [
      "Pandemic, 2020 (about a month)",
      34,
      "−34%",
      [
       222,
       160,
       36
      ]
     ]
    ],
    "note": "Both times it later recovered to new highs. No guarantee next time."
   },
   {
    "at": "But recoveries can take years",
    "type": "say",
    "text": "Recoveries can take years.",
    "sub": "No one knows how long the next one will take",
    "char": [
     "worried",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "Why crashes happen",
  "text": "Why do crashes happen? Usually because expectations change fast. Investors suddenly expect lower profits, higher interest rates, or a recession, and everyone tries to sell at the same time. Prices fall faster than the businesses themselves change. For a long-term investor, that's the uncomfortable truth: the same crashes that feel terrifying are also the moments when shares go on sale. The investors who get hurt most are often the ones who panic and sell near the bottom.",
  "beats": [
   {
    "at": "^",
    "type": "lines",
    "head": "Why crashes happen",
    "lines": [
     [
      "Expectations change fast"
     ],
     [
      "Everyone tries to sell at once"
     ],
     [
      "Prices fall faster than businesses change"
     ]
    ],
    "step": 4.0
   },
   {
    "at": "For a long-term investor",
    "type": "say",
    "text": "Crashes are when shares go on sale.",
    "sub": "Panic-selling near the bottom hurts the most",
    "char": [
     "think",
     420,
     640
    ]
   }
  ]
 },
 {
  "label": "How to take part",
  "text": "So how do regular people actually take part? You don't need to pick the next big winner. Most beginners start with a fund that buys a whole index at once, like an S&P 500 fund or a global fund. You buy it through a regulated broker, ideally inside a tax-advantaged account, like an ISA in the UK, a TFSA in Canada, or a 401(k) or IRA in the US. In Australia, your superannuation is already invested in the market for you. Then you add money regularly, and you give it time. We covered the step-by-step setup in our investing for beginners video.",
  "beats": [
   {
    "at": "^",
    "type": "say",
    "text": "You don't need to pick the next big winner.",
    "char": [
     "point_right",
     420,
     640
    ]
   },
   {
    "at": "Most beginners start",
    "type": "checklist",
    "head": "How regular people take part",
    "items": [
     "A fund that buys a whole index",
     "Through a regulated broker",
     "In a tax-advantaged account",
     "Add money regularly, give it time"
    ],
    "marks": [
     "Most beginners",
     "You buy it through",
     "ideally inside",
     "Then you add"
    ]
   }
  ]
 },
 {
  "label": "Three myths",
  "text": "Let's clear up three myths. Myth one: the stock market is just gambling. In a casino, the odds are built against you. Owning shares means owning real businesses that produce real profits. It's risky, but it's not a casino. Myth two: you need to watch the market every day. Most long-term investors do better by checking less often, and sticking to a plan. Myth three: a falling price means a bad company. Sometimes the whole market falls, and good companies fall with it. Price and value are not the same thing.",
  "beats": [
   {
    "at": "^",
    "type": "myth",
    "n": 1,
    "myth": "The stock market is just gambling",
    "fact": "Shares are pieces of real businesses with real profits. Risky, but not a casino."
   },
   {
    "at": "Myth two",
    "type": "myth",
    "n": 2,
    "myth": "You need to watch the market every day",
    "fact": "Most long-term investors do better checking less often and sticking to a plan."
   },
   {
    "at": "Myth three",
    "type": "myth",
    "n": 3,
    "myth": "A falling price means a bad company",
    "fact": "Sometimes the whole market falls. Price and value are not the same thing."
   }
  ]
 },
 {
  "label": "Recap",
  "text": "Let's recap. A stock is a piece of a real business. Exchanges match buyers and sellers. In the short term, prices move on supply, demand and emotion. In the long term, they tend to follow profits. Indexes like the S&P 500 show how a big group of companies is doing. Crashes are normal, and staying calm matters more than predicting them. If this helped, subscribe. Next, we'll look at the psychology of money: why smart people make bad money decisions, and how to avoid them. See you there.",
  "beats": [
   {
    "at": "^",
    "type": "checklist",
    "head": "Recap",
    "items": [
     "A stock is a piece of a real business",
     "Exchanges match buyers and sellers",
     "Short term: emotion. Long term: profits",
     "Indexes show how groups of companies do",
     "Crashes are normal: stay calm"
    ],
    "marks": [
     "A stock is",
     "Exchanges",
     "In the short term",
     "Indexes like",
     "Crashes are normal"
    ]
   },
   {
    "at": "If this helped",
    "type": "subscribe",
    "next": "The psychology of money",
    "next_sub": "why smart people make bad money decisions",
    "char": [
     "wave",
     230,
     560
    ]
   }
  ]
 }
]
