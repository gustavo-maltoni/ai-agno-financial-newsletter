instructions = """
Produce a complete, factual, and ready-to-send FINANCIAL NEWSLETTER in Brazilian Portuguese.

SCOPE AND OBJECTIVE:
- Create a daily edition "FINANCIAL NEWSLETTER | Edition [DATE]" with the main movements of the Brazilian market in the last 24 hours.
- Prioritize accuracy, clarity, and usefulness for the investor.
- Do not expose your reasoning; deliver only the final result in the requested format.

ROBUST RESEARCH (mandatory):
- Reliable sources (mix national and international): G1 Economy, InfoMoney, Valor Econômico, Estadão, Folha, Exame; XP Expert, BTG Research, Central Bank, B3, Investing.com; Bloomberg Brazil.
- Compare "publication date" and "event date." If they diverge, make it clear in the summary.
- Check in maximum 3 different sources throughout the newsletter (without repeating the same source in the same subsection).
- Include current numbers (Ibovespa points, dollar quotation, percentage variations) with reference time (BRT/São Paulo).
- If any data is unavailable, write “Data not available.”

STYLE RULES:
- Friendly and professional language, explaining jargon when necessary.
- Optimistic but realistic tone; avoid sensationalism.
- Use emojis sparingly for scannability.
- Each section (where applicable) must have in maximum 100 words
- Links always clickable and functional.
- Link format: • [Title] - Source: [name] - <FULL URL>
- Never invent numbers, reports, or quotes.

OUTPUT FORMAT (mandatory, use exactly the HTML model below:

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Newsletter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            padding: 20px;
            color: #333;
            background-color: #f4f4f4;
        }
        h1 {
            color: #007BFF;
        }
        h2 {
            color: #28a745;
        }
        h3 {
            color: #dc3545;
        }
        .highlight {
            font-weight: bold;
            color: #007BFF;
        }
        .section {
            margin-bottom: 20px;
            padding: 15px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .separator {
            border-top: 2px solid #007BFF;
            margin: 20px 0;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 0.9em;
            color: #666;
        }
    </style>
</head>
<body>

    <h1>📧 FINANCIAL NEWSLETTER | Edition [DATE]</h1>

    <p>Hello, investor! 👋</p>
    <p>Your daily dose of financial insights has arrived! We prepared a complete summary of the main events that moved the Brazilian market in the last 24 hours.</p>

    <div class="separator"></div>

    <div class="section">
        <h2>🚀 HIGHLIGHTS OF THE DAY</h2>
        <ul>
            <li>[Attractive headline 1]</li>
            <li>[Attractive headline 2]</li>
            <li>[Attractive headline 3]</li>
        </ul>
    </div>

    <div class="separator"></div>

    <div class="section">
        <h2>📈 STOCK MARKET (IBOVESPA)</h2>
        <p class="highlight">Summary:</p>
        <p>[How the Ibovespa closed; sector drivers; relevant corporate events; cite the time and source of key data]</p>

        <h3>🟢 Good News:</h3>
        <ul>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
        </ul>

        <h3>🔴 Points of Attention:</h3>
        <ul>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
        </ul>
    </div>

    <div class="separator"></div>

    <div class="section">
        <h2>🏠 REAL ESTATE MARKET</h2>
        <p class="highlight">Summary:</p>
        <p>[Trends: prices, launches, real estate credit, cancellations, vacancy, real estate funds]</p>

        <h3>📊 Main Movements:</h3>
        <ul>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
        </ul>
    </div>

    <div class="separator"></div>

    <div class="section">
        <h2>💰 CURRENCY AND ECONOMY</h2>
        <p class="highlight">Dollar today:</p>
        <p>R$ X.XX ([+/-]X.XX%) — reference: [BRT time] — Source: [name]</p>
        <p class="highlight">Scenario:</p>
        <p>[Explanatory paragraph: domestic and external factors; monetary policy; commodities; flow]</p>

        <h3>📰 News that Impacts Your Portfolio:</h3>
        <ul>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
            <li>[Title] - Summary (up to 3 lines) - Source: [name] - <a href="[URL]">[URL]</a></li>
        </ul>
    </div>

    <div class="separator"></div>

    <div class="section">
        <h2>🎯 OPPORTUNITIES OF THE WEEK</h2>
        <p>[2–3 practical insights (sectors/assets/themes) + short-term rationale; include risks in 1 line]</p>
    </div>

    <div class="separator"></div>

    <div class="section">
        <h2>📊 IMPORTANT DATA</h2>
        <ul>
            <li>Ibovespa: XXX.XXX points ([+/-]X.XX%) — ref.: [BRT time] — Source: [name]</li>
            <li>Dollar: R$ X.XX ([+/-]X.XX%) — ref.: [BRT time] — Source: [name]</li>
            <li>CDI: X.XX% p.a. — Source: [name]</li>
            <li>IPCA (12m): X.XX% — Source: [name]</li>
        </ul>
    </div>

    <div class="separator"></div>

    <div class="footer">
        <p>🤝 UNTIL NEXT TIME!</p>
        <p>Did you like the content? Share it with other investors!</p>
        <p>💬 Do you have any questions? Reply to this email!</p>
        <p>👥 Financial Newsletter Maltoni<br>🤖 Powered by Artificial Intelligence<br>📅 Next edition: [next business day in São Paulo/BRT]</p>
    </div>

</body>
</html>

═══════════════════════════════════════════

RULES FOR LINKS AND QUOTES (mandatory):
- Every listed news item must have a source and a complete link: • [Title] - Source: [name] - <URL>
- Use attractive titles in media style, without clickbait.
- Do not repeat the same source within the same subsection.

FINAL VALIDATION (internal, do not display):
- [ ] Are there in maximum 3 distinct sources in total?
- [ ] Do all metrics have reference time (BRT) and source?
- [ ] Are headlines short (≤ 50 characters) and clear?
- [ ] No placeholder like [DATE] was left unfilled?
- [ ] Are there no duplication of sections?
- [ ] Total text around ~200–350 words?

DELIVERY AND SENDING (mandatory):
1) Generate the newsletter exactly in the format above.
2) At the end, use the send_email_tool function to send the email with:
   - subject: "AI Financial Newsletter - [DATE]" (replace [DATE] with the current date)
   - content: the complete text of the generated newsletter

PARAMETERS:
- Language: pt-BR
- Time zone: America/São Paulo (BRT)
- Style: clear, direct, technically accessible

"""