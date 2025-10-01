from coinGecko import get_price, get_info, get_market_overview, get_education_info, get_trending_coins, get_disclaimer


# Basic responses for common questions
responses = {
    # Greetings with conversation starters
    "hi": """👋 Hello! I'm Crypto Buddy, your friendly crypto assistant! 
    
Would you like to:
1. Check today's trending coins? 🔥
2. Learn about a specific cryptocurrency? 📚
3. Get the latest market updates? 📊
4. Learn crypto basics? 🎓

Just let me know what interests you!""",

    "hello": """👋 Hey there! Exciting times in crypto today! 

I can tell you about:
• What's trending right now 🚀
• Latest price updates 💰
• Market insights 📈
• Beginner guides 📚

What would you like to explore?""",

    "help": """🤝 I'm here to be your crypto guide! Here's what we can chat about:

🎯 Quick Actions:
• "Show me what's trending"
• "How's Bitcoin doing?"
• "Tell me about Ethereum"
• "What's the market like today?"

📚 Learn About Crypto:
• "Explain blockchain simply"
• "How do I start investing?"
• "What are the risks?"
• "How do wallets work?"

💡 Pro Tips:
• "Give me investment tips"
• "How to stay safe in crypto"
• "Best practices for trading"

What would you like to know more about?""",
    
    # Trading and Investment
    "buy crypto": """� How to Buy Cryptocurrency:
1. Choose a reliable exchange (Binance, Coinbase, Kraken)
2. Complete KYC verification
3. Add funds via bank transfer or card
4. Place your order
⚠️ Remember: Always do your research and start small!""",
    
    "sell crypto": """📍 How to Sell Cryptocurrency:
1. Transfer to your exchange account
2. Place a sell order
3. Withdraw to your bank account
⚠️ Consider tax implications in your country.""",
    
    # Security and Safety
    "security": """🔒 Crypto Security Tips:
1. Use hardware wallets for large amounts
2. Enable 2FA on all accounts
3. Never share private keys
4. Beware of scams and phishing
5. Keep backup of recovery phrases""",
    
    "wallet": """👛 Types of Crypto Wallets:
1. Hardware (most secure): Ledger, Trezor
2. Software: MetaMask, Exodus
3. Mobile: Trust Wallet, Atomic
4. Exchange (least secure)
Choose based on your needs and amount!""",
    
    # Tips and Advice
    "tip": """💡 Crypto Investment Tips:
1. Never invest more than you can afford to lose
2. Do Your Own Research (DYOR)
3. Think long-term
4. Diversify your portfolio
5. Be wary of FOMO and FUD
6. Keep track of your trades""",
    
    "risks": """⚠️ Crypto Risks to Consider:
1. High volatility
2. Regulatory changes
3. Security risks
4. Market manipulation
5. Technical complexity
Always assess your risk tolerance!""",
    
    # Educational
    "blockchain": "🔗 Blockchain is a decentralized digital ledger that securely records all transactions across a network. Think of it as a chain of blocks, each containing transaction data, linked together cryptographically.",
    
    "mining": "⛏️ Crypto mining is the process of validating transactions and adding them to the blockchain using computational power. Miners are rewarded with new coins for their work.",
    
    "defi": "🏦 DeFi (Decentralized Finance) refers to financial services built on blockchain technology. It includes lending, borrowing, trading, and earning interest without traditional banks.",
}

# Mapping common names to standard IDs
crypto_ids = {
    "bitcoin": "bitcoin",
    "btc": "bitcoin",
    "ethereum": "ethereum",
    "eth": "ethereum",
    "dogecoin": "dogecoin",
    "doge": "dogecoin",
    "sol": "solana",
    "solana": "solana",
    "ada": "cardano",
    "cardano": "cardano"
}

# Educational topics
edu_topics = ["blockchain", "mining", "wallet", "defi", "nft", "smart_contract", "pos", "pow"]


def get_response(message):
    message = message.lower()
    
    # Personalized greeting with smart context detection
    if any(word in message for word in ["hi", "hello", "hey"]):
        greeting = "👋 Hey there! "
        
        if "price" in message or "market" in message:
            return f"{greeting}Perfect timing - let me help you with market insights!\n\n" \
                   f"What would you like to know?\n" \
                   f"• Current prices and trends 📊\n" \
                   f"• Market analysis and predictions 📈\n" \
                   f"• Investment opportunities 💡\n\n" \
                   f"Just ask about any coin or market trend you're curious about!"
        
        elif any(word in message for word in ["new", "start", "learn", "beginner"]):
            return f"{greeting}Welcome to the world of crypto! Let's start your journey.\n\n" \
                   f"What interests you most?\n" \
                   f"• Understanding crypto basics 📚\n" \
                   f"• Getting started safely 🛡️\n" \
                   f"• Popular cryptocurrencies 🌟\n\n" \
                   f"Don't worry - I'll explain everything in simple terms!"
        
        else:
            return f"{greeting}Great to see you! Let's explore crypto together.\n\n" \
                   f"I can help you with:\n" \
                   f"• Latest trends and prices 📊\n" \
                   f"• Crypto education and tips 💡\n" \
                   f"• Market insights 📈\n" \
                   f"• Security advice 🔒\n\n" \
                   f"What would you like to explore first?"
    
    if "help" in message:
        return "🤝 I'm here to make crypto simple and fun! Let's focus on what matters to you.\n\n" \
               "Quick Actions:\n" \
               "• Type 'trend' for hot coins right now 🔥\n" \
               "• Ask about any coin (e.g., 'How's Bitcoin?') 💰\n" \
               "• Say 'market' for the big picture 📊\n\n" \
               "Learning Corner:\n" \
               "• 'Explain [any crypto term]' 📚\n" \
               "• 'How to invest safely' 🛡️\n" \
               "• 'Give me tips' 💡\n\n" \
               "What would you like to know more about?"
    
    # Smart context detection for trending queries
    if any(word in message for word in ["trending", "hot", "popular", "momentum", "moving", "trend"]):
        base_response = get_trending_coins()
        
        # Customize follow-up based on message context
        if "price" in message or "value" in message:
            follow_up = "\n\n� Want to dig deeper?\n" \
                       "• Ask for price predictions\n" \
                       "• Compare with other coins\n" \
                       "• Check historical performance"
        elif "why" in message or "reason" in message:
            follow_up = "\n\n🔍 Want to understand more?\n" \
                       "• Ask why each coin is trending\n" \
                       "• Get news and updates\n" \
                       "• See market sentiment"
        else:
            follow_up = "\n\n🎯 What's your next move?\n" \
                       "• Get detailed analysis of any coin\n" \
                       "• Learn about investment strategies\n" \
                       "• Stay updated with alerts"
        
        return base_response + follow_up + "\n\nJust ask me anything you're curious about! 😊"
    
    # Interactive market overview with context
    if any(phrase in message for phrase in ["market", "overview", "global", "market cap"]):
        base_response = get_market_overview()
        
        # Tailor the follow-up based on user's likely interests
        if "bear" in message or "bull" in message:
            follow_up = "\n\n📈 Market Sentiment Check:\n" \
                       "• Want detailed trend analysis?\n" \
                       "• Looking for safe haven assets?\n" \
                       "• Need investment strategies for this market?"
        elif "invest" in message or "buy" in message:
            follow_up = "\n\n💰 Investment Opportunities:\n" \
                       "• Want to know the best entry points?\n" \
                       "• Need risk management tips?\n" \
                       "• Looking for promising projects?"
        else:
            follow_up = "\n\n🎯 Deep Dive Options:\n" \
                       "• Analyze specific sectors\n" \
                       "• Check market correlations\n" \
                       "• Get personalized insights"
        
        response = base_response + follow_up + "\n\nWhat aspect interests you most? 🤔"
        
        if "price" in message or "market" in message:
            response += "\n\n" + get_disclaimer()
        return response
    
    # Handle security and wallet related questions
    if "security" in message or "protect" in message or "safe" in message:
        return responses["security"]
    
    if "wallet" in message:
        return responses["wallet"]
    
    # Handle buying and selling questions
    if "buy" in message or "purchase" in message or "get" in message:
        return responses["buy crypto"] + "\n\n" + get_disclaimer()
    
    if "sell" in message or "selling" in message:
        return responses["sell crypto"] + "\n\n" + get_disclaimer()
    
    # Handle risk and tip related questions
    if "risk" in message or "danger" in message:
        return responses["risks"] + "\n\n" + get_disclaimer()
    
    if "tip" in message or "advice" in message:
        return responses["tip"] + "\n\n" + get_disclaimer()
    
    # Handle educational content
    if "what is" in message or "explain" in message or "tell me about" in message:
        # Check for educational topics
        for topic in edu_topics:
            if topic in message:
                return get_education_info(topic)
        
        # If it's about a specific crypto
        for key in crypto_ids:
            if key in message:
                response = get_info(crypto_ids[key])
                return response + "\n\n" + get_disclaimer()
    
    # Handle price queries
    if any(word in message for word in ["price", "cost", "worth", "value"]):
        for key in crypto_ids:
            if key in message:
                response = get_price(crypto_ids[key])
                return response + "\n\n" + get_disclaimer()
    
    # Handle info queries about specific cryptos
    for key in crypto_ids:
        if key in message:
            response = get_info(crypto_ids[key])
            return response + "\n\n" + get_disclaimer()
    
    # Check for direct keyword responses as fallback
    for key in responses:
        if key in message:
            return responses[key]
    
    # Default response with suggestions
    return """I'm not sure what you're asking. Try these:
1. "What's trending in crypto?"
2. "What's the Bitcoin price?"
3. "Tell me about Ethereum"
4. "How to buy crypto?"
5. "Show market overview"
6. "What is blockchain?"
7. Type "help" for more options"""