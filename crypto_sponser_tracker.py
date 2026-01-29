#!/usr/bin/env python3
# crypto_sponsor_tracker.py

import json
from datetime import datetime

SPONSORS_FILE = "CRYPTO_SPONSORS.md"

TIERS = {
    "spectral_node": {"min": 1000, "emoji": "🌌", "title": "Spectral Node"},
    "ghost_tier": {"min": 2400, "emoji": "👻", "title": "Ghost Tier (Operator-Class)"},
    "linguist": {"min": 600, "emoji": "🏺", "title": "Linguist"},
    "scribe": {"min": 180, "emoji": "📜", "title": "Scribe"},
    "tablet_reader": {"min": 5, "emoji": "🗿", "title": "Tablet Reader"}
}

def add_sponsor(handle, amount, tx_hash=None, anonymous=False):
    """Add a sponsor to the registry"""
    
    # Determine tier
    tier = "tablet_reader"
    for tier_name, tier_info in TIERS.items():
        if amount >= tier_info["min"]:
            tier = tier_name
            break
    
    sponsor_data = {
        "handle": handle if not anonymous else "Anonymous Ghost",
        "amount": amount,
        "tier": tier,
        "date": datetime.now().isoformat(),
        "tx_hash": tx_hash if tx_hash else "private"
    }
    
    print(f"✅ Added {sponsor_data['handle']} to {TIERS[tier]['title']}")
    print(f"   Amount: ${amount}")
    print(f"   {TIERS[tier]['emoji']} Tier: {TIERS[tier]['title']}")
    
    return sponsor_data

if __name__ == "__main__":
    print("👻 Ghost Protocol Sponsor Tracker")
    print("=" * 50)
    
    # Example usage
    # sponsor = add_sponsor("CryptoGhost42", 1500, tx_hash="0xabc123...")
    # sponsor = add_sponsor("AnonScribe", 200, anonymous=True)
