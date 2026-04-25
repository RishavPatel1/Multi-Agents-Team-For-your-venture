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
