<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Multi‑Agent Venture Team</title>
      <style>
          /* ---------- Global Styles ---------- */
          body {
              margin: 0;
              font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
              line-height: 1.6;
              color: #333;
              background: #f9fafb;
          }
          a { color: #2563eb; text-decoration: none; }
          a:hover { text-decoration: underline; }

          /* ---------- Layout ---------- */
          .container { max-width: 960px; margin: 0 auto; padding: 2rem; }

          header {
              text-align: center;
              padding: 3rem 0;
              background: linear-gradient(135deg, #4f46e5, #2563eb);
              color: #fff;
              border-radius: 0 0 1rem 1rem;
          }
          header h1 { margin: 0; font-size: 2.5rem; }
          header p { margin: 0.5rem 0 0; font-size: 1.2rem; }

          .badge-group { margin-top: 1rem; }
          .badge-group img { margin-right: 0.5rem; vertical-align: middle; }

          .hero {
              display: flex;
              flex-wrap: wrap;
              align-items: center;
              justify-content: space-between;
              margin: 4rem 0;
          }
          .hero img {
              max-width: 100%;
              border-radius: .5rem;
              box-shadow: 0 4px 12px rgba(0,0,0,.1);
          }
          .hero .text { flex: 1 1 45%; }
          .hero .text h2 { font-size: 2rem; margin-top: 0; }
          .hero .text p { margin: 1rem 0; }

          /* ---------- Sections ---------- */
          section { margin-bottom: 3rem; }
          section h2 {
              border-left: .4rem solid #2563eb;
              padding-left: .6rem;
              font-size: 1.6rem;
              color: #1e40af;
          }
          pre {
              background:#1e293b;
              color:#f8fafc;
              padding:1rem;
              overflow-x:auto;
              border-radius:.5rem;
          }

          /* ---------- Footer ---------- */
          footer {
              text-align: center;
              padding: 2rem 0;
              font-size: .9rem;
              color: #6b7280;
          }

          /* ---------- Responsive ---------- */
          @media (max-width: 768px) {
              .hero { flex-direction: column; text-align: center; }
              .hero .text { flex: none; }
          }
      </style>
  </head>
  <body>
      <header>
          <h1>🤖 Multi‑Agent Venture Team</h1>
          <p>An AI‑driven “virtual C‑suite” built with Python and OpenRouter’s OSS‑120B model</p>
          <div class="badge-group">
              <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python">
              <img src="https://img.shields.io/badge/OpenRouter-OSS%20120B-green?logo=openai" alt="OpenRouter">
              <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
              <img src="https://img.shields.io/github/stars/your‑username/your‑repo?style=social" alt="Stars">
          </div>
      </header>

      <div class="container">
          <!-- Hero Section -->
          <section class="hero">
              <div class="text">
                  <h2>What is it?</h2>
                  <p>
                      A lightweight Python framework that spins up a team of specialized agents
                      (

●                 <p>
                      A lightweight Python framework that spins up a team of specialized agents
                      (Marketing, CTO, CEO, Developer, HR, CFO) powered by OpenRouter’s OSS‑120B model.
                      Interact via a simple REPL, save/load conversation state, and extend with custom
                      roles or integrations.
                  </p>
                  <a href="https://github.com/your-username/multi-agent-venture-team"
  style="display:inline-block;margin-top:1rem;padding:.6rem
  1.2rem;background:#2563eb;color:#fff;border-radius:.4rem;">Explore the Repo →</a>
              </div>
              <img
  src="https://raw.githubusercontent.com/your-username/multi-agent-venture-team/main/docs/screenshot.png" alt="REPL
  screenshot" width="400">
          </section>

          <!-- Features -->
          <section id="features">
              <h2>✨ Features</h2>
              <ul>
                  <li>🔄 Role‑specific agents with custom system prompts.</li>
                  <li>💬 Interactive REPL supporting <code>ask</code>, <code>broadcast</code>, <code>save</code>,
  <code>load</code>, and <code>roles</code>.</li>
                  <li>🧩 Modular architecture – add new agents by dropping a Python file in <code>agents/</code>.</li>
                  <li>🔒 Secure handling of API keys via <code>.env</code> and <code>python‑dotenv</code>.</li>
                  <li>📦 Zero‑dependency deployment – just <code>pip install -r requirements.txt</code>.</li>
              </ul>
          </section>

          <!-- Quick Start -->
          <section id="quick-start">
              <h2>🚀 Quick Start</h2>
              <pre><code># Clone the repo
  git clone https://github.com/your-username/multi-agent-venture-team.git
  cd multi-agent-venture-team

  # Install dependencies
  pip install -r requirements.txt

  # Add your OpenRouter key
  echo 'OPENROUTER_API_KEY="YOUR_KEY_HERE"' &gt; .env

  # Launch the REPL
  python run.py
  </code></pre>
          </section>

          <!-- Usage -->
          <section id="usage">
              <h2>💡 Usage</h2>
              <p>Within the REPL you can type:</p>
              <pre><code># Ask a single role
  ask marketing "What channels should we focus on for a new e‑commerce launch?"

  # Broadcast a thought to all roles
  broadcast "We need a unified brand voice across marketing, product, and support."

  # Persist the conversation
  save

  # Load the last session
  load

  # List available roles
  roles
  </code></pre>
          </section>

          <!-- Architecture -->
          <section id="architecture">
              <h2>🛠️ Architecture Snapshot</h2>
              <pre><code>multi_agent_team/
  │   run.py                # REPL entry point
  │   router.py             # In‑memory message router
  │   base_agent.py         # Shared logic for all agents
  │   state.py              # Simple JSON persistence
  │   requirements.txt
  │   .env                  # API key
  │
  ├─ agents/
  │   ├─ marketing.py
  │   ├─ cto.py
  │   ├─ ceo.py
  │   ├─ developer.py
  │   ├─ hr.py
  │   └─ cfo.py
  │
  └─ prompts/
      ├─ marketing.json
      ├─ cto.json
      ├─ ceo.json
      ├─ developer.json
      ├─ hr.json
      └─ cfo.json
  </code></pre>
          </section>

          <!-- Contributing -->
          <section id="contributing">
              <h2>🤝 Contributing</h2>
              <p>
                  Contributions are welcome! Fork the repo, create a feature branch,
                  and submit a pull request. Please ensure your code follows the existing
                  style, includes type hints, and updates the relevant <code>prompts/*.json</code>
                  if you add a new role.
              </p>
          </section>

          <!-- License -->
          <section id="license">
              <h2>📄 License</h2>
              <p>MIT License – see the <a
  href="https://github.com/your-username/multi-agent-venture-team/blob/main/LICENSE">LICENSE</a> file.</p>
          </section>

● <footer>
      © 2026 Your Name • <a href="https://github.com/your-username/multi-agent-venture-team">GitHub Repository</a>
  </footer>
