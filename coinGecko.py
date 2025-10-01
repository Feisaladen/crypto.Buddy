# Comprehensive crypto data
CRYPTO_PRICES = {
    "bitcoin": {
        "price": 48000,
        "change_24h": 2.5,
        "market_cap": "1.2T",
        "volume_24h": "28B",
        "high_24h": 48500,
        "low_24h": 47200,
        "supply": "19.5M",
        "max_supply": "21M",
        "description": "The first and largest cryptocurrency by market cap. Bitcoin uses proof-of-work consensus.",
        "use_cases": ["Store of Value", "Digital Gold", "Payment System"],
        "pros": ["Most secure network", "Widely adopted", "Limited supply"],
        "cons": ["Energy intensive", "Slower transactions", "High fees during congestion"],
        "technology": "Proof of Work (PoW)",
        "launch_date": "2009",
        "founder": "Satoshi Nakamoto"
    },
    "ethereum": {
        "price": 2800,
        "change_24h": 1.8,
        "market_cap": "320B",
        "volume_24h": "15B",
        "high_24h": 2850,
        "low_24h": 2750,
        "supply": "120M",
        "max_supply": "No limit",
        "description": "A decentralized platform for smart contracts and DApps. Recently switched to proof-of-stake.",
        "use_cases": ["Smart Contracts", "DeFi", "NFTs", "DAOs"],
        "pros": ["Smart contract platform", "Large developer community", "Many use cases"],
        "cons": ["Network congestion", "Gas fees can be high"],
        "technology": "Proof of Stake (PoS)",
        "launch_date": "2015",
        "founder": "Vitalik Buterin"
    },
    "dogecoin": {
        "price": 0.15,
        "change_24h": -1.2,
        "market_cap": "18B",
        "volume_24h": "900M",
        "high_24h": 0.16,
        "low_24h": 0.14,
        "supply": "140B",
        "max_supply": "No limit",
        "description": "Started as a meme coin, now a popular cryptocurrency for tips and payments.",
        "use_cases": ["Digital Payments", "Tipping", "Community Currency"],
        "pros": ["Fast transactions", "Low fees", "Strong community"],
        "cons": ["Infinite supply", "Limited development", "High volatility"],
        "technology": "Proof of Work (PoW)",
        "launch_date": "2013",
        "founder": "Billy Markus and Jackson Palmer"
    },
    "solana": {
        "price": 120,
        "change_24h": 5.2,
        "market_cap": "45B",
        "volume_24h": "2.5B",
        "high_24h": 122,
        "low_24h": 115,
        "supply": "450M",
        "max_supply": "No limit",
        "description": "High-performance blockchain platform known for fast transactions and low fees.",
        "use_cases": ["DeFi", "NFTs", "Web3 Apps", "Gaming"],
        "pros": ["Very fast", "Low fees", "Growing ecosystem"],
        "cons": ["Network outages", "More centralized", "Complex technology"],
        "technology": "Proof of Stake + Proof of History",
        "launch_date": "2020",
        "founder": "Anatoly Yakovenko"
    },
    "cardano": {
        "price": 0.85,
        "change_24h": 0.5,
        "market_cap": "28B",
        "volume_24h": "800M",
        "high_24h": 0.87,
        "low_24h": 0.83,
        "supply": "35B",
        "max_supply": "45B",
        "description": "Peer-reviewed blockchain platform focusing on sustainability and scalability.",
        "use_cases": ["Smart Contracts", "DeFi", "Identity Solutions", "Education"],
        "pros": ["Research-based", "Energy efficient", "Strong roadmap"],
        "cons": ["Slower development", "Less adoption", "Academic approach"],
        "technology": "Proof of Stake (PoS)",
        "launch_date": "2017",
        "founder": "Charles Hoskinson"
    }
}

# Market Overview Data
MARKET_DATA = {
    "total_market_cap": "2.1T",
    "total_volume_24h": "98B",
    "bitcoin_dominance": "42%",
    "total_cryptocurrencies": "12,000+",
    "total_exchanges": "500+",
    "market_sentiment": "Bullish",
    "fear_greed_index": 65,  # 0-100 scale
    "trending_coins": [
        {
            "name": "Bitcoin",
            "symbol": "BTC",
            "trend_reason": "ETF approval speculation",
            "price_change_24h": "+5.2%",
            "social_volume": "Very High"
        },
        {
            "name": "Solana",
            "symbol": "SOL",
            "trend_reason": "NFT market growth",
            "price_change_24h": "+12.8%",
            "social_volume": "High"
        },
        {
            "name": "Cardano",
            "symbol": "ADA",
            "trend_reason": "New DeFi protocol launch",
            "price_change_24h": "+8.3%",
            "social_volume": "Medium"
        },
        {
            "name": "Ethereum",
            "symbol": "ETH",
            "trend_reason": "Layer 2 adoption",
            "price_change_24h": "+3.7%",
            "social_volume": "High"
        }
    ]
}

# Educational Content
CRYPTO_EDUCATION = {
    "blockchain": "A decentralized, distributed ledger technology that records transactions across multiple computers securely.",
    "mining": "The process of validating and adding new transactions to a blockchain using computational power.",
    "wallet": "A tool that stores your private keys and allows you to interact with the blockchain to send and receive crypto.",
    "defi": "Decentralized Finance - financial services built on blockchain technology without traditional intermediaries.",
    "nft": "Non-Fungible Token - unique digital assets that represent ownership of specific items or content.",
    "smart_contract": "Self-executing contracts with terms directly written into code.",
    "pos": "Proof of Stake - consensus mechanism where validators stake tokens to secure the network.",
    "pow": "Proof of Work - consensus mechanism where miners solve complex puzzles to validate transactions.",
}

def get_price(crypt_name):
    crypt_name = crypt_name.lower()
    if crypt_name in CRYPTO_PRICES:
        data = CRYPTO_PRICES[crypt_name]
        return (
            f"📊 {crypt_name.upper()} Stats:\n"
            f"💰 Price: ${data['price']:,.2f}\n"
            f"📈 24h Change: {data['change_24h']}%\n"
            f"💎 Market Cap: ${data['market_cap']}\n"
            f"📊 24h Volume: ${data['volume_24h']}\n"
            f"⚡ 24h High/Low: ${data['high_24h']:,.2f} / ${data['low_24h']:,.2f}"
        )
    return "Sorry, I don't have data for that cryptocurrency. Try Bitcoin, Ethereum, Dogecoin, Solana, or Cardano."

def get_info(crypt_name):
    crypt_name = crypt_name.lower()
    if crypt_name in CRYPTO_PRICES:
        data = CRYPTO_PRICES[crypt_name]
        return (
            f"ℹ️ {crypt_name.upper()} Information:\n"
            f"📝 Description: {data['description']}\n"
            f"🚀 Use Cases: {', '.join(data['use_cases'])}\n"
            f"✅ Pros: {', '.join(data['pros'])}\n"
            f"⚠️ Cons: {', '.join(data['cons'])}\n"
            f"⚙️ Technology: {data['technology']}\n"
            f"📅 Launched: {data['launch_date']}\n"
            f"👤 Founder(s): {data['founder']}"
        )
    return "Sorry, I don't have detailed information for that cryptocurrency."

def get_market_overview():
    data = MARKET_DATA
    return (
        f"🌍 Global Crypto Market Overview:\n"
        f"💰 Total Market Cap: ${data['total_market_cap']}\n"
        f"📊 24h Volume: ${data['total_volume_24h']}\n"
        f"🏆 Bitcoin Dominance: {data['bitcoin_dominance']}\n"
        f"🔢 Total Cryptocurrencies: {data['total_cryptocurrencies']}\n"
        f"📈 Market Sentiment: {data['market_sentiment']}\n"
        f"😨 Fear & Greed Index: {data['fear_greed_index']}/100"
    )

def get_education_info(topic):
    topic = topic.lower()
    if topic in CRYPTO_EDUCATION:
        return f"📚 {topic.upper()}:\n{CRYPTO_EDUCATION[topic]}"
    return "Sorry, I don't have information about that topic. Try asking about: blockchain, mining, wallet, defi, nft, smart_contract, pos, or pow."

def get_trending_coins():
    """Get information about trending cryptocurrencies"""
    trending = MARKET_DATA["trending_coins"]
    response = "🔥 TRENDING CRYPTOCURRENCIES:\n\n"
    
    for coin in trending:
        response += f"📈 {coin['name']} ({coin['symbol']})\n"
        response += f"   • Price Change: {coin['price_change_24h']}\n"
        response += f"   • Trending due to: {coin['trend_reason']}\n"
        response += f"   • Social Activity: {coin['social_volume']}\n\n"
    
    response += get_disclaimer()
    return response

def get_disclaimer():
    """Get the standard financial disclaimer"""
    return """⚠️ IMPORTANT DISCLAIMER:
• This is not financial advice
• Cryptocurrencies are highly volatile
• Past performance doesn't guarantee future results
• Only invest what you can afford to lose
• Always do your own research (DYOR)
• Verify information from multiple sources
• Consider consulting a financial advisor"""

def get_price(crypt_name):
    crypt_name = crypt_name.lower()
    if crypt_name in CRYPTO_PRICES:
        data = CRYPTO_PRICES[crypt_name]
        return (
            f"📊 {crypt_name.upper()} Stats:\n"
            f"💰 Price: ${data['price']:,.2f}\n"
            f"📈 24h Change: {data['change_24h']}%\n"
            f"💎 Market Cap: ${data['market_cap']}"
        )
    else:
        return "Sorry, I don't have data for that cryptocurrency. Try Bitcoin, Ethereum, Dogecoin, Solana, or Cardano."