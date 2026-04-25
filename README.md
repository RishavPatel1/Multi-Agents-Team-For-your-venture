<h1 align="center">🤖 Multi-Agent Venture Team</h1>

<p align="center">
  An AI-driven virtual C-suite built with Python and OpenRouter OSS-120B model.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenRouter-OSS%20120B-green" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

---

<h2>📌 Overview</h2>

<p>
Multi-Agent Venture Team is a lightweight Python-based AI framework that simulates a virtual startup leadership team.
It includes role-specific AI agents such as CEO, CTO, Marketing Head, Developer, HR, and CFO.
</p>

<p>
Each agent works with a dedicated system prompt and can respond individually or participate in a shared discussion using a simple command-line REPL interface.
</p>

---

<h2>✨ Features</h2>

<ul>
  <li>Role-specific AI agents with custom system prompts</li>
  <li>Interactive REPL interface</li>
  <li>Supports commands like <code>ask</code>, <code>broadcast</code>, <code>save</code>, <code>load</code>, and <code>roles</code></li>
  <li>Conversation state saving and loading</li>
  <li>Modular architecture for adding new agents easily</li>
  <li>Secure API key handling using <code>.env</code></li>
  <li>Powered by OpenRouter OSS-120B model</li>
</ul>

---

<h2>🧠 Agent Roles</h2>

<ul>
  <li><strong>CEO Agent:</strong> Handles strategy, vision, and business decisions</li>
  <li><strong>CTO Agent:</strong> Handles technical architecture and scalability</li>
  <li><strong>Marketing Agent:</strong> Handles growth, branding, and campaigns</li>
  <li><strong>Developer Agent:</strong> Handles implementation and coding-related planning</li>
  <li><strong>HR Agent:</strong> Handles hiring, team management, and people operations</li>
  <li><strong>CFO Agent:</strong> Handles finance, budgeting, and cost planning</li>
</ul>

---

<h2>🚀 Quick Start</h2>

<pre>
<code>
# Clone the repository
git clone https://github.com/your-username/multi-agent-venture-team.git

# Go inside the project folder
cd multi-agent-venture-team

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your OpenRouter API key
OPENROUTER_API_KEY="YOUR_KEY_HERE"

# Run the application
python run.py
</code>
</pre>

---

<h2>💡 Usage</h2>

<p>Once the REPL starts, you can use commands like:</p>

<pre>
<code>
# Ask one specific agent
ask marketing "What channels should we focus on for a new e-commerce launch?"

# Ask all agents together
broadcast "We need a product launch strategy for our new AI tool."

# Save current conversation
save

# Load previous conversation
load

# Show all available roles
roles
</code>
</pre>

---

<h2>🛠️ Project Structure</h2>

<pre>
<code>
multi_agent_team/
│
├── run.py                # Main REPL entry point
├── router.py             # Message routing logic
├── base_agent.py         # Base agent class
├── state.py              # Save/load conversation state
├── requirements.txt      # Python dependencies
├── .env                  # API key configuration
│
├── agents/
│   ├── ceo.py
│   ├── cto.py
│   ├── marketing.py
│   ├── developer.py
│   ├── hr.py
│   └── cfo.py
│
└── prompts/
    ├── ceo.json
    ├── cto.json
    ├── marketing.json
    ├── developer.json
    ├── hr.json
    └── cfo.json
</code>
</pre>

---

<h2>🔐 Environment Variables</h2>

<p>Create a <code>.env</code> file in the root directory:</p>

<pre>
<code>
OPENROUTER_API_KEY="your_openrouter_api_key_here"
</code>
</pre>

<p><strong>Important:</strong> Never push your <code>.env</code> file to GitHub.</p>

---

<h2>📦 Requirements</h2>

<ul>
  <li>Python 3.10+</li>
  <li>OpenRouter API Key</li>
  <li>python-dotenv</li>
  <li>requests or OpenAI-compatible SDK</li>
</ul>

---

<h2>🌱 Future Improvements</h2>

<ul>
  <li>Add web-based dashboard</li>
  <li>Add memory for each agent</li>
  <li>Add tool calling support</li>
  <li>Add database storage</li>
  <li>Add voice-based interaction</li>
  <li>Add multi-agent task delegation</li>
</ul>

---

<h2>🤝 Contributing</h2>

<p>
Contributions are welcome. You can fork this repository, create a new branch, make improvements, and submit a pull request.
</p>

---

<h2>📄 License</h2>

<p>
This project is licensed under the Apache License 2.0.
</p>

---

<h2>👨‍💻 Author</h2>

<p>
Built by <strong>Rishav Patel</strong>
</p>

<p>
GitHub: <a href="https://github.com/RishavPatel1">https://github.com/RishavPatel1</a>
</p>
